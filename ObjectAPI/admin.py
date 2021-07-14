from django.contrib import admin

from .models import *
admin.site.register(Person)
admin.site.register(Guest)
admin.site.register(Housemate)
admin.site.register(Residence)
admin.site.register(Room)
admin.site.register(Visit)
