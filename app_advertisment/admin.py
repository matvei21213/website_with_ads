from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'descriptoin', 'author', 'auction', 'price', 'created_date', 'update_date', 'photo' ]
    list_filter = ['author', 'title']
    actions = ['delete_description', 'make_auction_as_true']
    #date_hierarchy = 'created_at'
    #fieldsets = (
    #    ('Общие', { # блок 1 
    #        "fields": (
    #            'title','description', 'user' , 'image'    # поля блока
    #        ),
    #    }),
    #    ('Финансы', { # блок 2
    #        "fields": (
    #            'price','auction'    # поля блока
    #        ),
    #        'classes': ['collapse'] # скрыть/показать блок
    #    })
    #)
    
    @admin.action(description="Удалить описание выбранных объектов")
    def delete_description(self, request, queryset):
        queryset.update(text='')
        
    @admin.action(description="Включить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
    
admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
