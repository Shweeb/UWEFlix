from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Club)
admin.site.register(Representitive)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(UserPurchaseHistory)
admin.site.register(ClubPurchaseHistory)
