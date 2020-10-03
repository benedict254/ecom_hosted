from django.contrib import admin
from .models import *

class ItemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}
	list_display = [
		'title',
		'price',
		'discount_price'
	]


admin.site.register(Item,ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(slider)
admin.site.register(about)
admin.site.register(about1)
admin.site.register(addition_info)

