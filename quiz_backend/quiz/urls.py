from django.urls import path, include
from .views import helloAPI
from .views import randomQuiz

urlpatterns = [
    path('hello/', helloAPI),
    path('<int:id>/', randomQuiz),
]   