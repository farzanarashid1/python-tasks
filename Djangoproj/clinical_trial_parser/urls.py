
#
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('task/',views.task,name="Task" ),
#
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name='task'),
]
