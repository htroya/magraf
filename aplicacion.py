import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import plotly.express as px

ticker='AAPL'
years_analysis=20

fecha_fin=date.today()
fecha_inicio = fecha_fin - relativedelta(years=years_analysis)

fecha_fin=fecha_fin.strftime("%Y-%m-%d")
fecha_inicio=fecha_inicio.strftime("%Y-%m-%d")

data = yf.download(ticker,
                   start=fecha_inicio,
                   end=fecha_fin,
                   progress=False)

print(data)
figure = px.line(data, x = data.index,
                 y = "Close",
                 title = "Analisis de precios de la empresa " + ticker)
figure.show()
