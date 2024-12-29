from django.urls import path
from . import views
urlpatterns =[
  path('',views.apply_for_job, name='apply_for_job'),
  path('developer',views.view_applications,name='view_applications'),
 ]