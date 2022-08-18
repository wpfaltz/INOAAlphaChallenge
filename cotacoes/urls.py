from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name = "home"),
	path('about', views.about, name = "about"),
	path('portfolio', views.portfolio, name = "portfolio"),
	path('watchlist', views.watchlist, name = "watchlist"),
	path('delete_from_portfolio/<portfolio_id>', views.delete_from_portfolio, name="delete_from_portfolio"),
	path('delete_from_watchlist/<watchlist_id>', views.delete_from_watchlist, name="delete_from_watchlist"),
	
]