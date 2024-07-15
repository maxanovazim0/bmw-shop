from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (biz_haqmizda_ga,bizning_asosiy_qoydlar,mashin_shop,
                    modeli,model_a,Comment,User,car,car_details,
                    VehicleImage,mashin_yuish_uchun,Address,CreditCard)
# Register your models here.



class biz_haqmizdaAdmin(admin.ModelAdmin):

    list_display = ("id", "name")

class bizning_asosiy_qoydlarmizAdmin(admin.ModelAdmin):

    list_display = ("id", "name","img_oldi")

class mashin_shopAdmin(admin.ModelAdmin):

    list_display = ('id','name')

class carAdmin(admin.ModelAdmin):

    list_display = ('id','name')

class car_detailsAdmin(admin.ModelAdmin):

    list_display = ('id','model')

#<=====================================================================================================>

admin.site.register(biz_haqmizda_ga, biz_haqmizdaAdmin)
admin.site.register(bizning_asosiy_qoydlar, biz_haqmizdaAdmin)
admin.site.register(mashin_shop,mashin_shopAdmin)
admin.site.register(modeli)
admin.site.register(model_a)
admin.site.register(Comment)
admin.site.register(car_details,car_detailsAdmin)
admin.site.register(car,carAdmin)
admin.site.register(VehicleImage)
admin.site.register(mashin_yuish_uchun)
admin.site.register(Address)
admin.site.register(CreditCard)




class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('image',)}),
    )

admin.site.register(User, CustomUserAdmin)