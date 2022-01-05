from django.urls import path
from . views import *

urlpatterns = [
    path('projects/', ProjectList.as_view()),
    path('projects/<slug:pk>/', ProjectDetail.as_view()),
    path('task/', TaskList.as_view()),
    path('task/<int:pk>', TaskDetail.as_view()),

]
