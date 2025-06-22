from django.contrib import admin
from common import models

class OrderWorkerInline(admin.TabularInline):
    model = models.OrderWorker
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderWorkerInline]
    list_display = ('name', 'deadline', 'price', 'status', 'customer')
    list_filter = ('status', 'deadline')
    search_fields = ('name', 'information')

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Worker)
admin.site.register(models.Customer)
admin.site.register(models.RawMaterial)

class FinishedProductAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "order":
            kwargs["queryset"] = models.Order.objects.filter(status='Tayyor')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(models.FinishedProduct, FinishedProductAdmin)
admin.site.register(models.OrderWorker)
