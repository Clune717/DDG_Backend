from rest_framework import serializers 
from .models import Member 

class MemberSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Member # tell django which model to use
        fields = ('id', 'name', 'age', 'email',) # tell django which fields to include
