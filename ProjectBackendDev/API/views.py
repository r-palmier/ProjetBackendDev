from django.shortcuts import render
from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
