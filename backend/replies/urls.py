from django.urls import path
from .views import get_all_replies, user_replies

urlpatterns = [
    path('', get_all_replies),
    path('<int:pk>/create/', user_replies),
    path('<int:pk>/view/', user_replies),
]
