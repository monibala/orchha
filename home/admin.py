from django.contrib import admin

# Register your models here.
from django.contrib import admin

from home.models import HomeSlider, Prescriptions

# Register your models here.
admin.site.register(Prescriptions)
admin.site.register(HomeSlider)