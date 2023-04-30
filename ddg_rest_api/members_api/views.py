from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import MemberSerializer
from .models import Member

class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = MemberSerializer # tell django what serializer to use

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all().order_by('id')
    serializer_class = MemberSerializer