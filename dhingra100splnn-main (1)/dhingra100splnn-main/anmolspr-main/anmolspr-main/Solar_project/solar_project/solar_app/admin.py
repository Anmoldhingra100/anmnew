from django.contrib import admin
from .models import MySolarrr

class solarAdmin(admin.ModelAdmin):
    list_display = ['solar_generation','production','sales','revenue','invertor_power_conversion','temperature','faulty_panels','working_panels','performance','weather_prediction','temperature','humidity','efficiency','maintainance_cost','Profit_and_loss','UV_index','Irradiance','Rain_prediction','Energy_Distribution','date']  # Fields to display in the list view
     # Fields to display in the list view
  

admin.site.register(MySolarrr, solarAdmin)





