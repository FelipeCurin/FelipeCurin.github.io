from django.urls import path
from .views import home , terminos

urlpatterns = [
    path('', home, name="home"),  
    path('terminos/', terminos, name="terminos"), 
]

