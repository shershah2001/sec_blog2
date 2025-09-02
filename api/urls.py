from django.contrib import admin
from django.urls import path
from api.views import home_view,contact_view,category_view,create_view,signup_view,login_view,detail_view
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',home_view,name='home'),
   path('contact/',contact_view,name='contact'),
   path('category/<slug:slug>/',category_view,name='category'),
   path('create/',create_view,name='create'),
   path('signup/',signup_view,name='signup'),
   path('login/',login_view,name='login'),
   path('detail/',detail_view,name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
