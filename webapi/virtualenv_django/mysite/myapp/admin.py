from django.contrib import admin

# Register your models here.
from myapp.models import Topic, Entity

admin.site.register(Topic)
admin.site.register(Entity)