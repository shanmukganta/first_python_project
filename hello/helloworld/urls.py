from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home),
    path('signup',views.home),
    path('submit',views.hi),

    
]
