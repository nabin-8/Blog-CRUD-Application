from django.db import models
from django.contrib.auth.models import User

import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=500)
    content = models.TextField()
    main_image = models.ImageField(upload_to="blogs")
    
    def __str__(self):
        return self.title
    
    
