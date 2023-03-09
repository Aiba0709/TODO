from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters
from rest_framework.response import Response

from .permissions import  TodoPermissions
from .serializer import TodoSerializer,Todo
# Create your views here.

class TodoApi(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    quaryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (TodoPermissions, )

    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'descriptions')

class TodoAllDel(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (TodoPermissions, )

    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.filter(user = request.user)
        todo = [i for i in todo.delete()]

        return  Response({'delete': "Все таски удалил"})  
