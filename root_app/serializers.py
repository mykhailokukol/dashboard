from rest_framework import serializers

from . import models


class LabelSerializer(serializers.ModelSerializer):
    """  """
    
    class Meta:
        model = models.Label
        field = (
            'id',
            'name',
        )
        

class UserSerializerCreate(serializers.ModelSerializer):
    """  """
    
    class Meta:
        model = models.User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'about',
            'github_username', 
            
            'is_active',
            'is_staff',
            'is_superuser',
        )
        
        
class DeskSerializerCreate(serializers.ModelSerializer):
    """  """
    
    class Meta:
        model = models.Desk
        fields = (
            'name',
            'owner'
        )
        

class TaskSerializerCreate(serializers.ModelSerializer):
    """  """
    
    class Meta:
        model = models.Task
        fields = (
            'title',
            'description',
            'status',
            'story_points',
            
            'labels',
            'assignees',
            'reviewers',
        )


class UserSerializerGet(serializers.ModelSerializer):
    """  """
    
    desks = DeskSerializerCreate(many=True, required=False)
    tasks = TaskSerializerCreate(many=True, required=False)
    
    class Meta:
        model = models.User
        fields = (
            'id', 
            'first_name',
            'last_name',
            'email',
            'phone', 
            'about',
            'github_username',
            
            'is_active',
            'is_staff',
            'is_superuser',
            
            'date_joined',
            
            'tasks',
            'desks',
        )
        
        
class DeskSerializerGet(serializers.ModelSerializer):
    """  """
    
    owner = UserSerializerCreate(required=False)
    tasks = TaskSerializerCreate(many=True, required=False)
    
    class Meta:
        model = models.Desk
        fields = (
            'id',
            'name',
            
            'owner',
            'tasks',
        )
        

class TaskSerializerGet(serializers.ModelSerializer):
    """  """
    
    labels = LabelSerializer(many=True, required=False)
    assignees = UserSerializerCreate(many=True, required=False)
    reviewers = UserSerializerCreate(many=True, required=False)
    
    class Meta:
        model = models.Task
        fields = (
            'id',
            'title',
            'description',
            'status',
            'story_points',

            'labels',
            'assignees',
            'reviewers',

            'date_opened',
            'date_updated',
            'date_assigned',
        )
    