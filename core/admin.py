from django.contrib import admin
from .models import *
# Register your models here.

class SubstanceAdmin(admin.ModelAdmin):
    fields = ['name', 'density']



admin.site.register(Substance, SubstanceAdmin)
