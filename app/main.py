from fastapi import FastAPI
import app.db as db
import math

app = FastAPI()

# Configurações da primeira base de dados (money transactions)
IG_DATABASE = "indicate_to_win"
IG_HOST = "db.upsports.app"
IG_PASSWORD = "Upb3t!2025"
IG_PORT = 5432
IG_USER = "upbet_tech"

# Configurações da segunda base de dados (afiliados)
ST_DATABASE = "sporting_tech"
ST_HOST = "sportingtech.upsports.app"
ST_PASSWORD = "Upb3t!2024"
ST_PORT = 5434
ST_USER = "upbet_tech"

@app.get("/afiliados")
async def get_money_transactions():
    print('Entrou na GET - /afiliados - upbetTiago')
    conn = db.get_db_connection(IG_DATABASE, IG_USER, IG_PASSWORD, IG_HOST, IG_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers LIMIT 10000;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    print('Saiu na GET - /afiliados - upbetTiago')
    return results

@app.get("/moneytrans")
async def get_customers():
    print('Entrou na GET - /moneytran - upbetTiago')
    conn = db.get_db_connection(ST_DATABASE, ST_USER, ST_PASSWORD, ST_HOST, ST_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM money_transactions LIMIT 1000;")
    results = cur.fetchall()
    cur.close()
    conn.close()
    print('Saiu na GET - /moneytran - upbetTiago')
    return results

@app.get("/teste")
async def get_teste():
    print('Entrou na GET - /teste - Calculando')
    
    # Exemplo de cálculo matemático complexo
    x = 15
    y = 10
    z = 5
    
    # Equação mais complexa envolvendo exponenciais, logaritmos e raízes
    resultado = (math.exp(x) * math.log(y + z) / (x ** 2 + y ** 2)) + math.sqrt(x * y) - (math.sin(z) * math.cos(x - z)) + (y ** z)

    print(f"Resultado do cálculo complexo: {resultado}")
    return {"resultado": resultado}
