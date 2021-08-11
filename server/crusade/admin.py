from django.contrib import admin

from .models import OrderOfBattle, Unit, UnitUpgrade

admin.site.register(OrderOfBattle)
admin.site.register(Unit)
admin.site.register(UnitUpgrade)
