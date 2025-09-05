from django.contrib import admin
from django.urls import path
from api.views import home_view,contact_view,category_view,create_view,signup_view,login_view,detail_view,profile_view,logout_view,edit_view,delete_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',home_view,name='home'),
   path('contact/',contact_view,name='contact'),
   path('category/<slug:slug>/',category_view,name='category'),
   path('profile/',profile_view,name="profile"),
   path('detail/<slug:slug>/',detail_view,name='detail'),
   path('create/',create_view,name='create'),
   path('signup/',signup_view,name='signup'),
   path('edit/<slug:slug>/',edit_view,name="edit"),
   path('delete/<slug:slug>/',delete_view,name='delete'),
   path('login/',login_view,name='login'),
   path('logout/',logout_view,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
