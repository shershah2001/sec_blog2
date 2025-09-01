from django.contrib import admin
from api.models import Author,Blog,Categories
# Register your models here.

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Categories)