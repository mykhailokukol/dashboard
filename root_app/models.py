from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


class UserManager(BaseUserManager):
    """ Overrided manager for User model """
    
    def create_user(self, email=None, password=None, **extra_fields):
        if not email or not password:
            raise ValueError('email and/or password must be provided')
        if email:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    


class User(AbstractBaseUser):
    """  """
    
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    github_username = models.CharField(max_length=256, unique=True, db_index=True)
    email = models.CharField(max_length=256, unique=True, db_index=True)
    phone = models.CharField(max_length=17, blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    
    is_active = models.BooleanField(default=False, db_index=True)
    is_staff = models.BooleanField(default=False, db_index=True)
    is_superuser = models.BooleanField(default=False, db_index=True)
    
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Label(models.Model):
    """  """
    
    name = models.CharField(max_length=128)


class Desk(models.Model):
    """  """
    
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='desk_owner')
    
class Task(models.Model):
    """  """
    
    STATUSES = (
        ('todo', 'todo'),
        ('in progress', 'in progress'),
        ('in testing', 'in testing'),
        ('done', 'done'),
        ('blocked', 'blocked'),
    )
    
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=16, default='todo')
    story_points = models.PositiveSmallIntegerField(default=1)
    
    labels = models.ManyToManyField(Label, related_name='task_labels')
    assignees = models.ManyToManyField(User, related_name='task_assignees')
    reviewers = models.ManyToManyField(User, related_name='task_reviewers')
    
    date_opened = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_assigned = models.DateTimeField(null=True, blank=True)
