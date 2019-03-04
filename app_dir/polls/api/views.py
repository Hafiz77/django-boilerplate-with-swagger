from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView,
    RetrieveAPIView, DestroyAPIView, ListCreateAPIView,
)
from rest_framework.response import Response
from rest_framework import pagination
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
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(email__icontains=query) |
                Q(username__icontains=query)
            )

        return queryset_list.order_by('-id')


class PollRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PoolSerializer
    queryset = Choice.objects.all()
