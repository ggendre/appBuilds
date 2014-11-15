from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(App)
admin.site.register(Build)
admin.site.register(Os)
