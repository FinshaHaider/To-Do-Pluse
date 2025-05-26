
from django.urls import path
from django.contrib.auth import views as auth_views 

from todo_app import views

urlpatterns = [

    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('task',views.task,name='task'),
    path('add_todo/',views.add_todo,name='add_todo'),
    path('delete/<pkey>',views.delete_todo,name='delete_todo'),
    path('personal',views.personal,name='personal'),
    path('notes',views.notes,name='notes'),
    path('add_note/',views.add_note,name='add_note'),
    path('delete_note/<pkey>',views.delete_note,name='delete_note'),
    path('accounts/login/',views.user_login,name='login'),
    path('accounts/logout/',views.user_logout,name='logout'),
    path('conform/',views.user_conform,name='conform'),
    path('accounts/signup/',views.user_signup,name='signup'),

]
    # path('task_details',views.task_details,name='task_details'),
    # path('addtask/', views.addtask, name='addtask'),
    # path('delete_task/<pkey>/', views.delete_task, name='delete_task'),
    # path('complete_todo/<int:todo_id>',views.complete_todo,name='complete_todo')

    # path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    
