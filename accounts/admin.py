from django.contrib import admin
from .models import Role, CustomUser,License

admin.site.register(Role)
admin.site.register(License)
admin.site.register(CustomUser)
