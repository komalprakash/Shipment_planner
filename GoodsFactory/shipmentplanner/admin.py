from django.contrib import admin
from .models import Shipments
from .models import DPA
from .models import DPB
# Register your models here.
admin.site.register(Shipments)
admin.site.register(DPA)
admin.site.register(DPB)
