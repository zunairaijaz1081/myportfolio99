from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.email}"

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/')  # Make sure MEDIA settings are configured

    def __str__(self):
        return self.title


from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    content = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name




from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.name
