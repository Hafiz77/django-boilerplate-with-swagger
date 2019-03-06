from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView,
    RetrieveAPIView, DestroyAPIView, ListCreateAPIView, GenericAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination, status
from django.db.models import Q

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAuthenticated)
from app_dir.polls.models import Choice
from .serializers import PoolSerializer
from ...core.pagination import PostLimitOffsetPagination


class PollListCreate(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PoolSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Choice.objects.all()
        page_size = 'page_size'
        if self.request.GET.get(page_size):
            pagination.PageNumberPagination.page_size = self.request.GET.get(
                page_size)
        else:
            pagination.PageNumberPagination.page_size = 10
        return queryset_list.order_by('-id')


class PollRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PoolSerializer
    queryset = Choice.objects.all()


class ChoiceListCreate(GenericAPIView):
    """
    List all Choice.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PoolSerializer
    pagination_class = PostLimitOffsetPagination
    
    def get(self, request, format=None, *args, **kwargs):
        queryset_list = Choice.objects.all()
        serializer = self.serializer_class(queryset_list, many=True, context={'request': request})
        data = {'result': serializer.data}
        return Response(data)
        
    # """
    # Create Choice.
    # """
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
