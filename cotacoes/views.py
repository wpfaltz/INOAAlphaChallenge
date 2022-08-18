#views.py


#Bibliotecas utilizadas
import requests
import json
import pandas as pd
from pandas_datareader import data as web
import time
import datetime

#Informações no framework
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import PortfolioForm, WatchlistForm
from .models import Portfolio, Watchlist

def about(request):
	return render(request, 'about.html', {})

def delete_from_portfolio(request, portfolio_id):
	item = Portfolio.objects.get(pk=portfolio_id)
	item.delete()
	messages.success(request, ("Ação removida do portfolio!"))
	return redirect('portfolio')

def delete_from_watchlist(request, watchlist_id):
	item = Watchlist.objects.get(pk=watchlist_id)
	item.delete()
	messages.success(request, ("Ação removida da lista de observação!"))
	return redirect('watchlist')

def home(request):
	#Alpha Vantage key: N0E8B0KGYQ978XE3

	if request.method == 'POST':
		ticker = request.POST['ticker_symbol']
		
		api_request = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + ticker +"&apikey=N0E8B0KGYQ978XE3")
		api_request_2 = requests.get("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + ticker + "&apikey=N0E8B0KGYQ978XE3")
		try:
			api_raw = json.loads(api_request.content)
			api_raw_2 = json.loads(api_request_2.content)
			company_name = api_raw_2["bestMatches"][0]["2. name"]
			currency = api_raw_2["bestMatches"][0]["8. currency"]
			company_code = ticker

			#Agora vem a parte que é importada do Yahoo Finance
			today = datetime.date.today()
			cod_empresa = ticker
			if '.SAO' in ticker:
				cod_empresa = ticker[:-1]
			else:
				cod_empresa = ticker
			latest_quotes = web.DataReader(f'{cod_empresa}', data_source = 'yahoo', start = today, end = today)
			current_quote = round(latest_quotes["Close"][-1], 2) #Pegar da API Yahoo Finance
			previous_close = round(float(api_raw["Global Quote"]["05. price"]),2) #Pegar da API Yahoo Finance
			change = round(current_quote - previous_close, 2)			#Esse aqui deve ser calculado dinamicamente através da diferença de fechamento entre o close do dia anterior e a cotação atual
			change_percent = ('{:6%}'.format(change/previous_close))	#Esse aqui é a variação percentual do valor acima
			api_raw = {"company" : company_name, "companycode" : company_code, "currency" : currency, "latest" : current_quote, "previousday" : previous_close, "change" : change, "changepercent" : change_percent}
		except Exception as e:
			api_raw = "Error"
		return render(request, 'home.html', {'api': api_raw })

	else:
		return render(request, 'home.html', {'ticker': "Insira o ticker da ação desejada no campo de busca" })


def portfolio(request):
	if request.method == "POST":
		form = PortfolioForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, ("Ação adicionada ao portfolio!"))
			return redirect('portfolio')
	else:
		form = PortfolioForm
		porttab = Portfolio.objects.all() 

		output = []
		for ticker_item in porttab:
			ticker = str(ticker_item)
			quantidade = Portfolio.objects.values_list('quantity')
			preco_compra = Portfolio.objects.values_list('bought_price')
			alerta_preco = Portfolio.objects.values_list('price_alert')
			api_request = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + ticker +"&apikey=N0E8B0KGYQ978XE3")
			api_request_2 = requests.get("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + ticker + "&apikey=N0E8B0KGYQ978XE3")
			try:
				api_raw = json.loads(api_request.content)
				api_raw_2 = json.loads(api_request_2.content)
				company_name = api_raw_2["bestMatches"][0]["2. name"]
				currency = api_raw_2["bestMatches"][0]["8. currency"]
				company_code = ticker

				#Agora vem a parte que é importada do Yahoo Finance
				today = datetime.date.today()
				cod_empresa = ticker
				if '.SAO' in ticker:
					cod_empresa = ticker[:-1]
				else:
					cod_empresa = ticker
				latest_quotes = web.DataReader(f'{cod_empresa}', data_source = 'yahoo', start = today, end = today)
				current_quote = round(latest_quotes["Close"][-1], 2) #Pegar da API Yahoo Finance
				previous_close = round(float(api_raw["Global Quote"]["05. price"]),2) #Pegar da API Yahoo Finance
				change = round(current_quote - previous_close, 2)			#Esse aqui deve ser calculado dinamicamente através da diferença de fechamento entre o close do dia anterior e a cotação atual
				change_percent = ('{:6%}'.format(change/previous_close))	#Esse aqui é a variação percentual do valor acima
				api_raw = {"company" : company_name, "companycode" : company_code, "currency" : currency, "latest" : current_quote, "previousday" : previous_close, "change" : change, "changepercent" : change_percent, "quantity" : quantidade, "bought_price":preco_compra, "price_alert":alerta_preco }
				output.append(api_raw)
			except Exception as e:
				api_raw = "Error"		
		return render(request, 'portfolio.html', {'form':form, 'porttab' : porttab, 'output' : output })

def watchlist(request):
	if request.method == "POST":
		bform = WatchlistForm(request.POST)
		if bform.is_valid():
			bform.save()
			messages.success(request, ("Ação adicionada à lista de observação!"))
			return redirect('watchlist')
	else:
		bform = WatchlistForm
		table = Watchlist.objects.all() 

		output = []
		for ticker_item in table:
			ticker = str(ticker_item)
			api_request = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + ticker +"&apikey=N0E8B0KGYQ978XE3")
			api_request_2 = requests.get("https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + ticker + "&apikey=N0E8B0KGYQ978XE3")
			try:
				api_raw = json.loads(api_request.content)
				api_raw_2 = json.loads(api_request_2.content)
				company_name = api_raw_2["bestMatches"][0]["2. name"]
				currency = api_raw_2["bestMatches"][0]["8. currency"]
				company_code = ticker

				#Agora vem a parte que é importada do Yahoo Finance
				today = datetime.date.today()
				cod_empresa = ticker
				if '.SAO' in ticker:
					cod_empresa = ticker[:-1]
				else:
					cod_empresa = ticker
				latest_quotes = web.DataReader(f'{cod_empresa}', data_source = 'yahoo', start = today, end = today)
				current_quote = round(latest_quotes["Close"][-1], 2) #Pegar da API Yahoo Finance
				previous_close = round(float(api_raw["Global Quote"]["05. price"]),2) #Pegar da API Yahoo Finance
				change = round(current_quote - previous_close, 2)			#Esse aqui deve ser calculado dinamicamente através da diferença de fechamento entre o close do dia anterior e a cotação atual
				change_percent = ('{:6%}'.format(change/previous_close))	#Esse aqui é a variação percentual do valor acima
				api_raw = {"company" : company_name, "companycode" : company_code, "currency" : currency, "latest" : current_quote, "previousday" : previous_close, "change" : change, "changepercent" : change_percent}
				output.append(api_raw)
			except Exception as e:
				api_raw = "Error"

		return render(request, 'watchlist.html', {'form':bform, 'table' : table, 'output' : output })