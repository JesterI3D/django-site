# Register your models here.

from django.contrib import admin

from .models import mainApp, Author

admin.site.register(mainApp)
admin.site.register(Author)