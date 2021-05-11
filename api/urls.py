from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.destination_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]