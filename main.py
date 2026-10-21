from dataclasses import dataclass
from openai import OpenAI

client = OpenAI()


@dataclass
class Agent:
    name: str
    role: str


AGENTS = [
    Agent("Internet Research Agent", "Mekle aktualu informaciju interneta"),
    Agent("Market Agent", "Analize tirgu, klientus un konkurentus"),
    Agent("Finance Agent", "Analize izmaksas, ienakumus un finansu riskus"),
    Agent("Quality Agent", "Parbauda riskus un idejas kvalitati"),
    Agent("CEO Agent", "Apkopo visu un pienem gala lemumu"),
]


def show_team():
    print("\n=== AI BUSINESS EMPIRE ===")
    print("AI agentu komanda:")
    for agent in AGENTS:
        print(f"- {agent.name}: {agent.role}")


show_team()

idea = input("\nIevadi savu biznesa ideju: ")


# 1. INTERNET RESEARCH AGENT

research_response = client.responses.create(
    model="gpt-5.6",
    tools=[{"type": "web_search"}],
    input=f"""Tu esi biznesa interneta izpetes agents.

Biznesa ideja:
{idea}

Izmanto interneta meklesanu un atrodi aktualu informaciju.

Izpeti:
1. Vai sada veida bizness jau eksiste
2. Galvenos konkurentus
3. Tirgus tendences
4. Tirgus iespejas
5. Galvenos riskus
6. Dod vertejumu no 0 lidz 100

Neizdoma faktus. Balsties uz atrasto informaciju."""
)

print("\n=== INTERNET RESEARCH AGENT ===")
print(research_response.output_text)


# 2. MARKET AGENT

market_response = client.responses.create(
    model="gpt-5.6",
    input=f"""Tu esi biznesa tirgus analitikis.

Biznesa ideja:
{idea}

Aktuala interneta izpete:
{research_response.output_text}

Izanalize:
1. Tirgus potencialu
2. Galvenos klientus
3. Konkurentus
4. Izaugsmes iespejas
5. Dod tirgus vertejumu no 0 lidz 100

Atbildi isi, konkreti un realistiski."""
)

print("\n=== MARKET AGENT ===")
print(market_response.output_text)


# 3. FINANCE AGENT

finance_response = client.responses.create(
    model="gpt-5.6",
    input=f"""Tu esi biznesa finansu analitikis.

Biznesa ideja:
{idea}

Tirgus analize:
{market_response.output_text}

Izanalize:
1. Sakuma izmaksas
2. Ienakumu avotus
3. Pelnas potencialu
4. Finansu riskus
5. Monetizacijas iespejas
6. Dod finansu vertejumu no 0 lidz 100

Atbildi isi un realistiski."""
)

print("\n=== FINANCE AGENT ===")
print(finance_response.output_text)


# 4. QUALITY AGENT

quality_response = client.responses.create(
    model="gpt-5.6",
    input=f"""Tu esi stingrs biznesa kvalitates un riska analitikis.

Biznesa ideja:
{idea}

Interneta izpete:
{research_response.output_text}

Tirgus analize:
{market_response.output_text}

Finansu analize:
{finance_response.output_text}

Parbaudi:
1. Galvenos riskus
2. Vajakos punktus
3. Vai secinajumi ir realistiski
4. Ko vajag parbaudit pirms ieguldit naudu
5. Dod kvalitates un riska vertejumu no 0 lidz 100

Atbildi isi un kritiski."""
)

print("\n=== QUALITY AGENT ===")
print(quality_response.output_text)


# 5. CEO AGENT

ceo_response = client.responses.create(
    model="gpt-5.6",
    input=f"""Tu esi AI BUSINESS EMPIRE galvenais CEO agents.

Biznesa ideja:
{idea}

INTERNET RESEARCH:
{research_response.output_text}

MARKET:
{market_response.output_text}

FINANCE:
{finance_response.output_text}

QUALITY:
{quality_response.output_text}

Izverte visu informaciju un pienem gala lemumu.

Dod tiesi sadu strukturu:

TIRGUS: X/100
FINANSES: X/100
KVALITATE/RISKS: X/100
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

Esi stingrs un realistisks. Neizdoma faktus."""
)

print("\n================================")
print("=== CEO GALA VERDIKTS ===")
print("================================")
print(ceo_response.output_text)

print("\n================================")
print("=== AI IDEJU PLATFORMA ===")
print("================================")

author = input("Ievadi idejas autora vardu: ")
idea_title = input("Ievadi idejas nosaukumu: ")

print("\nIdeja sagatavota publicesanai!")
print("Autors:", author)
print("Nosaukums:", idea_title)
print("AI analize ir pabeigta.")
with open("idejas.txt", "a", encoding="utf-8") as fails:
    fails.write(f"Autors: {author}\n")
    fails.write(f"Ideja: {idea_title}\n")
    fails.write(f"Apraksts: {idea}\n")
    fails.write("--------------------\n")

print("Ideja saglabata faila idejas.txt!")

rating = input("Noverte ideju no 1 lidz 5 zvaigznem: ")

print("Tavs vertejums:", rating, "/5")
with open("idejas.txt", "a", encoding="utf-8") as fails:
    fails.write(f"Vertejums: {rating}/5\n")
    fails.write("====================\n")

print("Vertejums saglabats!")
print("\n=== TOP IDEJU SISTEMA ===")
print("Ideja:", idea_title)
print("Autors:", author)
print("Vertejums:", rating, "/5")

print("\n=== IDEJU TOPS ===")
print("Nakamas versijas funkcija: lietotaju ideju tops un balsosana.")
