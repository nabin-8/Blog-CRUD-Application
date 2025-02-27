# Step 1: Use an official Python image as the base
FROM python:3.10

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy project files into the container
COPY . /app

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port Django runs on
EXPOSE 8000

# Step 6: Run migrations and start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
