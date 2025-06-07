from .views import calculator_view
from django.urls import path

urlpatterns = [
    path('calc/',calculator_view)
]