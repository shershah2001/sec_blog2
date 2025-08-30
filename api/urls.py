from django.contrib import admin
from django.urls import path
from api.views import home_view,contact_view,category_view,create_view,signup_view,login_view
urlpatterns = [
   path('',home_view,name='home'),
   path('contact/',contact_view,name='contact'),
   path('category/',category_view,name='category'),
   path('create/',create_view,name='create'),
   path('signup/',signup_view,name='signup'),
   path('login/',login_view,name='login'),
]
