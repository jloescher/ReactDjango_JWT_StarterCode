from django.urls import path
from comments.views import get_all_comments, user_comments, video_comments

urlpatterns = [
    path('', get_all_comments),
    path('create/', user_comments),
    path('user/', user_comments),
    path('<str:video_id>/', video_comments)
]
