from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoApi, TodoAllDel

router = DefaultRouter()
router.register("todo", TodoApi, basename="todo")

urlpatterns = [
    path('api/todo/del/', TodoAllDel.as_view(), name="all_destroy")

]
urlpatterns += router.urls