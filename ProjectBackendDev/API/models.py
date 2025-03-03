from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    experience = models.IntegerField()
    degree = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
