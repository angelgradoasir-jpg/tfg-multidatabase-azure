from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>TFG Azure Flask</title>
        </head>

        <body style="font-family: Arial; text-align:center; margin-top:100px; background-color:#f4f4f4;">

            <h1>🚀 Aplicación Web TFG</h1>

            <p>Despliegue realizado correctamente en Azure App Service</p>

            <h2>Proyecto desarrollado con Flask y Azure</h2>

            <button style="
                padding:10px 20px;
                font-size:18px;
                border:none;
                border-radius:8px;
                background-color:#0078D4;
                color:white;
                cursor:pointer;
            ">
                Aplicación activa
            </button>

        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
