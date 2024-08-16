from flask import Flask, render_template, request
import yfinance as yf
import plotly.express as px
import pandas as pd

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal para la aplicación
@app.route("/", methods=["GET", "POST"])
def index():
    graph_html = None  # Inicializa la variable para almacenar el gráfico HTML
    if request.method == "POST":  # Si se envía un formulario (método POST)
        # Descarga datos históricos del ticker proporcionado
        data = yf.download(request.form["ticker"], start=pd.Timestamp.today() - pd.DateOffset(years=20), progress=False)
        # Crea un gráfico de líneas con los datos descargados
        graph_html = px.line(data, x=data.index, y="Close").to_html(full_html=False)
    # Renderiza la plantilla HTML y pasa el gráfico como parámetro
    return render_template("index.html", graph_html=graph_html)

# Ejecuta la aplicación en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)
