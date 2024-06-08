from django.urls import path
from studentapp.views import studentcreate,studentalldetail

urlpatterns=[
    path('Api/student/',studentcreate.as_view(),name='studentcreate'),
    path('Api/student/<int:pk>/',studentalldetail.as_view(),name='studentalldetail'),

]