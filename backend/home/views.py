from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class PublicBlogView(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all().order_by("?")
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination   
    pagination_class.page_size = 2

    def get_queryset(self):
        blogs = self.queryset

        search = self.request.GET.get("search")
        if search:
            blogs = blogs.filter(Q(title__icontains=search) | Q(blog_text__icontains=search))

        return blogs


class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            data=request.data
            data['user'] = request.user.id
            serializer = BlogSerializer(data= data)

            if not serializer.is_valid():
                return Response(
                    {
                        "data": serializer.errors,
                        "message": "something went wrong"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        
            serializer.save()
            
            return Response({
                "data": serializer.data,
                "message": "Blog Created Successfully"
            }, status=status.HTTP_201_CREATED)

        
        except Exception as e:
            return Response(
                {
                    "data": {},
                    "message": f"Something went wrong: {str(e)}"
                }, status=status.HTTP_400_BAD_REQUEST
            )
    
    
    def get(self, request):
        try:
            blogs = Blog.objects.filter(user = request.user)

            if request.GET.get("search"):
                search = request.GET.get('search')
                blogs =blogs.filter(Q(title__icontains= search) | Q(blog_text__icontains = search))
            
            serializer = BlogSerializer(blogs,many = True)
            
            return Response({
                "data": serializer.data,
                "message": "Blog Fetched Successfully"
            }, status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response(
                {
                    "data": {},
                    "message": f"Something went wrong: {str(e)}"
                }, status=status.HTTP_400_BAD_REQUEST
            )
    
    
    def patch(self,request):
        try:
            data = request.data
            blog = Blog.objects.filter(id = data.get("id"))
            
            if not blog.exists():
                return Response(
                {
                    "data": {},
                    "message": "Invalid Blog id"
                }, status=status.HTTP_400_BAD_REQUEST
            )

            if request.user != blog[0].user:
                return Response(
                {
                    "data": {},
                    "message": "You are not Authorised"
                }, status=status.HTTP_403_FORBIDDEN
            )

            serializer = BlogSerializer(blog[0],data=data , partial = True)

            if not serializer.is_valid():
                return Response(
                    {
                        "data": serializer.errors,
                        "message": "something went wrong"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "Blog Updated Successfully"
            }, status=status.HTTP_201_CREATED)


        except Exception as e:
            return Response(
                {
                    "data": {},
                    "message": f"Something went wrong: {str(e)}"
                }, status=status.HTTP_400_BAD_REQUEST
            )
    
    
    def delete(self,request):
        try:
            data = request.data
            blog = Blog.objects.filter(id = data.get("id"))
            
            if not blog.exists():
                return Response(
                {
                    "data": {},
                    "message": "Invalid Blog id"
                }, status=status.HTTP_400_BAD_REQUEST
            )

            if request.user != blog[0].user:
                return Response(
                {
                    "data": {},
                    "message": "You are not Authorised"
                }, status=status.HTTP_403_FORBIDDEN
            )
            
            blog[0].delete()
            return Response({
                "data": {},
                "message": "Blog Deleted Successfully"
            }, status=status.HTTP_201_CREATED)


        except Exception as e:
            return Response(
                {
                    "data": {},
                    "message": f"Something went wrong: {str(e)}"
                }, status=status.HTTP_400_BAD_REQUEST
            )
