from django.urls import path
from .import views

urlpatterns = [
    path('candidates/', views.CandidateListCreate.as_view(), name='candidates-view-create'),
]