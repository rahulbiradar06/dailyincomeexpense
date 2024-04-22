from django.contrib import admin

# Register your models here.
from income.models import Income

class incomeadmin(admin.ModelAdmin):
    list_display=['income', 'income_type', 'income_date', 'description', 'user']


admin.site.register(Income , incomeadmin)