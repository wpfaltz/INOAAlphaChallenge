from django.contrib import admin
from .models import Portfolio
from .models import Watchlist

admin.site.register(Portfolio)
admin.site.register(Watchlist)