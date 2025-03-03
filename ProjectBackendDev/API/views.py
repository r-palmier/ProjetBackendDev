from django.shortcuts import render
from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateListCreate(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
from django.db import connection

def test_db_connection():
    try:
        connection.ensure_connection()
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

