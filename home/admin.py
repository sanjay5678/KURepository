from django.contrib import admin

# Register your models here.
from home.models import Applications, Approved, Authenticate
admin.site.register(Applications)
admin.site.register(Approved)
admin.site.register(Authenticate)