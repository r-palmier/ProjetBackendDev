from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Cree une instance du schema Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Recrutement API",
      default_version='v1',
      description="API pour gérer les candidatures et les vues recruteurs.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@recrutement.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('Applying/', views.CandidateApplying.as_view(), name='candidates-view-create'),
    path('candidates/<int:id>/', views.CandidateRetrieveUpdateDestroy.as_view(), name='candidates-update'),
    path('recruiters/', views.RecruteurViewSet.as_view({'get': 'list'}), name='recruteur-candidates-list'),
    path('swagger/', schema_view.as_view(), name='swagger-docs'),
]