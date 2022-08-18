#models.py


from django.db import models

class Portfolio(models.Model):
	ticker = models.CharField(max_length=12)
	quantity = models.PositiveSmallIntegerField()
	bought_price = models.FloatField()
	price_alert = models.FloatField()

	def __str__(self):
		return self.ticker

class Watchlist(models.Model):
	cod_acao = models.CharField(max_length=12)
	price_watch = models.FloatField()

	def __str__(self):
		return self.cod_acao