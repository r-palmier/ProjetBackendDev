from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Candidate
from .serializers import CandidateSerializer
  

class CandidateApplying(generics.CreateAPIView):
    serializer_class = CandidateSerializer
    
class CandidateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all() 
    serializer_class = CandidateSerializer
    lookup_field = 'id'
    

class RecruteurViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer