from django.contrib import admin

from .models import Cup, Using

admin.site.register(Cup)
# register the new Feeding Model 
admin.site.register(Using)
