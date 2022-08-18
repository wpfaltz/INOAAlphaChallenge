#forms.py

from django import forms
from .models import Portfolio, Watchlist

#Criar um form para inserir uma ação ao portfolio
class PortfolioForm(forms.ModelForm):
	class Meta:
		model = Portfolio
		fields = ('ticker', 'quantity', 'bought_price', 'price_alert')
		
		labels = {
			'ticker': 'Insira o ticker da ação',
			'quantity': 'Quantidade de ações',
			'bought_price': 'Preço comprado',
			'price_alert': 'Alerta de preço',
		}
		widgets = {
			'ticker': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ticker'}),
			'quantity': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantidade'}),
			'bought_price': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Preço de compra'}),
			'price_alert': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Preço min de venda'}),

		}

class WatchlistForm(forms.ModelForm):
	class Meta:
		model = Watchlist
		fields = ('cod_acao', 'price_watch')
		
		labels = {
			'cod_acao' : 'Insira o ticker da ação',
			'price_watch':'Preço máx que gostaria de comprar',
		}
		widgets = {
			'cod_acao': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ticker'}),
			'price_watch': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Preço de compra'}),
		}