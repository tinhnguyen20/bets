from django.contrib import admin

# Register your models here.
from core.models import Bet, BetOption, BetParticipant

class BetOptionInline(admin.TabularInline):
    model = BetOption
    extra = 1  # Number of empty forms to display for adding new BetOption instances

class BetAdmin(admin.ModelAdmin):
    inlines = [BetOptionInline]


from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Bet, BetAdmin)
admin.site.register(BetOption)
admin.site.register(BetParticipant)