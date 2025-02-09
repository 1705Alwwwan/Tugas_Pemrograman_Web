from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name=''), 
   path ('cretae-mahasiswa/', views.crete_mahasiswa, name='create-mahasiswa'), 
   
   path ('update-mahasiswa/<str:pk>', views.update_mahasiswa, name='update-mahasiswa'),
   path ('delete-mahasiswa/<str:pk>', views.delete_mahasiswa, name='delete-mahasiswa'), 
    
    
]