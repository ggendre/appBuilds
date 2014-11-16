from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(Team)
admin.site.register(App)
admin.site.register(Build)
admin.site.register(Os)

admin.site.register(Profile,
    search_fields = ('user__username','team__name',),
    filter_horizontal = ("apps",),
)