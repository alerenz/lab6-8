from django.contrib import admin
from .models import Bank, Clients, Sotrudnik, Credit, Dolzhnost, Count

# Register your models here.
admin.site.register(Bank)
admin.site.register(Clients)
admin.site.register(Sotrudnik)
admin.site.register(Credit)
admin.site.register(Count)
admin.site.register(Dolzhnost)
