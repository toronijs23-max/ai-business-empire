
import os
from html import escape

from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    rezultats = ""

    if request.method == "POST":
        ideja = request.form.get("ideja", "").strip()

        if not ideja:
            rezultats = "<p>Lūdzu, ievadi biznesa ideju.</p>"
        elif not os.getenv("OPENAI_API_KEY"):
            rezultats = "<p>Nav iestatīta OpenAI API atslēga.</p>"
        else:
            try:
                client = OpenAI()

                response = client.responses.create(
                    model="gpt-5.6",
                    input=f"""
Tu esi biznesa ideju analīzes aģents.

Analizē šo biznesa ideju:
{ideja}

Izvērtē:
1. Tirgus potenciālu
2. Mērķa klientus
3. Iespējas pelnīt
4. Galvenos riskus
5. Vērtējumu no 0 līdz 100
6. Gala verdiktu: GO, UZLABOT vai NO-GO

Atbildi latviešu valodā, konkrēti un praktiski.
"""
                )

                rezultats = (
                    "<h3>AI ANALĪZE</h3><pre>"
                    + escape(response.output_text)
                    + "</pre>"
                )

            except Exception:
                app.logger.exception("AI analīzes kļūda")
                rezultats = (
                    "<p>Analīzi pašlaik neizdevās veikt. "
                    "Pārbaudi API atslēgu un savienojumu.</p>"
                )

    return f"""
    <!doctype html>
    <html lang="lv">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>AI BUSINESS EMPIRE</title>
    </head>
    <body>
        <h1>AI BUSINESS EMPIRE</h1>
        <h2>AI Ideju Platforma</h2>
        <p>Iesniedz biznesa ideju un saņem AI analīzi.</p>

        <form method="POST">
            <textarea name="ideja" rows="6" cols="60"
                placeholder="Ieraksti biznesa ideju..."
                required></textarea>
            <br><br>
            <button type="submit">Analizēt ideju</button>
        </form>

        {rezultats}
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=False)
