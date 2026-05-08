import pandas as pd
import datetime

data = {
    "cliente": ["angelica", "maria", "caique", "erro"],
    "valor": [100, 200, 300, 400],
    "data": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"]
}
df = pd.DataFrame(data)

df = df.dropna(subset=['valor'])
df = df[df["cliente"] != "erro"] 

resumo = f"Relatorio - {datetime.date.today()}\n"
resumo += f"Total valor: {df['valor'].sum()}\n"
resumo += f"cliente atendidos: {len(df)}"

with open("relatorio.json", "w") as arquivo:
    arquivo.write(resumo)
    
    print("dados processado")
    