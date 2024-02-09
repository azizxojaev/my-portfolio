from django.db import models


class MainText(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=75)
    description = models.TextField()
    what_i_do = models.TextField()
    why_choose_me = models.TextField()
    my_works = models.TextField()
    blogs = models.TextField()
    contact = models.TextField()

class MainPhoto(models.Model):
    main_image = models.ImageField(upload_to='avatar/')
    avatar = models.ImageField(upload_to='avatar/')

class ProjectCounter(models.Model):
    happy_clients = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    awards_won = models.PositiveIntegerField(default=0)

class Skill(models.Model):
    percent = models.PositiveIntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()

class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=50)
    text = models.TextField()

class Contact(models.Model):
    location = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
