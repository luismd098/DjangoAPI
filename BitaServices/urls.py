from django.urls import re_path
from BitaServices import views

urlpatterns = [
    re_path(r'^login$',views.loginApi),    
    re_path(r'^login/([0-9]+)$',views.loginApi),    
]
