from django.contrib import admin
from .models import Example
from .models import Dialect
from .models import SensorData
# from .models import ModelName

# Register your models here.
admin.site.register(Example)
admin.site.register(Dialect)
admin.site.register(SensorData)
# admin.site.register(ModelName)
