from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment, Reply
from .serializers import ReplySerializer

# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_replies(request):
    """
    api/replies/ GET
    """
    if request.method == 'GET':
        replies = Reply.objects.all()
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_replies(request, pk):
    """
    api/replies/1/create/ POST | create a reply related to a comment
    api/replies/1/view/ GET | view replies related to comment
    """
    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        comment = get_object_or_404(Comment, pk=pk)
        if serializer.is_valid():
            serializer.save(user=request.user, comment=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        replies = Reply.objects.filter(comment=pk)
        serializer = ReplySerializer(replies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
