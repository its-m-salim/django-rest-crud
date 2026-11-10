from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('table/', get_tables, name="table"),
    path('create/<int:t_id>/', create, name="create"),
    path('read/', read, name="read"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]
