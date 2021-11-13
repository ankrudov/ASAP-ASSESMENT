from rest_framework import serializers
from .models import Member
import uuid

class MemberSerializer(serializers.ModelSerializer):
    member_id = serializers.UUIDField()
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    date_of_birth = serializers.DateField()
    country = serializers.CharField(max_length=60)
    
    class Meta:
        model = Member
        fields = ('__all__')