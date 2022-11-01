
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('',views.demo,name="demo"),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    # path('details',views.details,name='details')
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdteview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),

]
