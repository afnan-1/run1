from django.contrib import admin
from .models import CustomUser,Team,Sports,Challenge
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Challenge)
admin.site.register(Sports)