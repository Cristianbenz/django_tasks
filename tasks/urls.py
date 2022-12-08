from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('tasks/', views.render_tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_tasks')
]