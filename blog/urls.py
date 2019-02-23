from django.urls import path
from . import views #getting all of views from the blog application

urlpatterns= [
    path('',views.post_list,name="post_list"), #assigning the view called post_list to the root url. "" signify the root url
    path('post/<int:pk>/',views.post_detail,name='post_detail')
]