from django.urls import path 
from views import RegisterView 

urlpatterns = [
    path('register/', RegisterViewas_view())
    path('login/', LoginView.as_view()),
]