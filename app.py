
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
Tu esi AI BUSINESS EMPIRE galvenais CEO agents.

Biznesa ideja:
{ideja}

Izverte ideju no 4 skatpunktiem:

1. TIRGUS AGENTS
- klienti
- pieprasijums
- konkurence
- izaugsmes potencials

2. FINANSU AGENTS
- ienakumu avoti
- izmaksas
- pelnas potencials
- monetizacija

3. RISKU AGENTS
- galvenie riski
- vajie punkti
- ko obligati parbaudit

4. KLIENTU AGENTS
- kam produktu pardot
- kapec vini maksatu
- ka iegut pirmos klientus

Pec tam dod CEO gala rezultatu:

TIRGUS: X/100
FINANSES: X/100
RISKS: X/100
KLIENTI: X/100
KOPEJAIS VERTEJUMS: X/100

VERDIKTS: GO / UZLABOT / NO-GO

3 GALVENIE IEMESLI:
1.
2.
3.

3 NAKAMIE SOLI:
1.
2.
3.

Atbildi latviesu valoda. Esi kritisks un realistisks. Neizdoma faktus.
"""




                )

                rezultats = (
                    "<h3>AI ANALĪZE</h3><pre>"
                    + escape(response.output_text)
                    + "</pre>"
                )
                with open("web_idejas.txt", "a", encoding="utf-8") as fails:
                    fails.write("IDEJA: " + ideja + "\n")
                    fails.write("AI ANALIZE:\n" + response.output_text + "\n")
                    fails.write("====================\n")
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
