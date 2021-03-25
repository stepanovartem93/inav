from django.contrib import admin
from .models import TypeOfMeasurment, MeasuringInstrument

# Register your models here.
# admin.site.register(TypeOfMeasurment)
# admin.site.register(MeasuringInstrument)

@admin.register(MeasuringInstrument)
class MeasuringInstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'typeofmeasurment', 'state_register_number', 'year', 'invertarian_number', 
    'factory_number', 'owner', 'status')
    list_filter = ('typeofmeasurment', 'state_register_number', 'year', 'owner', 'status')
    # search_fileds = ('name','state_register_number')
    ordering = ('state_register_number', 'year', 'status', 'owner')
    list_editable = ('status',)


@admin.register(TypeOfMeasurment)
class TypeOfMeasurmentAdmin(admin.ModelAdmin):
    list_display = ('measurment', )