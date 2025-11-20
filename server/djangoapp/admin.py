from django.contrib import admin
from .models import CarMake, CarModel


# Inline: show CarModel entries inside CarMake admin page
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # how many empty forms to display
    fields = ('name', 'type', 'year')  # matches your model fields
    show_change_link = True  # adds a link to edit each model


# Custom admin for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('type', 'year', 'car_make')
    search_fields = ('name',)
    ordering = ('car_make', 'name')


# Custom admin for CarMake with inline CarModels
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]


# Register models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
