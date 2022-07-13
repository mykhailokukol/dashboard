from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from . import serializers
from . import models


class UserViewSet(viewsets.ModelViewSet):
    """  """
    
    queryset = models.User.objects.exclude(is_active=False)
    serializer_class = serializers.UserSerializerGet
    
    def get_serializer_class(self):
        if self.action == 'create':
            self.serializer_class = serializers.UserSerializerGet
        if self.action == 'update':
            self.serializer_class = serializers.UserSerializerCreate
        if self.action == 'partial_update':
            self.serializer_class = serializers.UserSerializerCreate
        return super().get_serializer_class()
