import pandas as pd


def get_name(str):
    index = -1
    for i in range(len(str)):
        c = str[i]
        #c = int(c)
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            index = i
            break
    return str[index:].strip().replace("-", " ")

def to_num(str):
    return str.strip().replace(",", "").replace(".", "")

'''
incidenti_df = pd.read_excel("incidenti_province.xlsx")
print(incidenti_df.head())
incidenti_df["provincia"] = incidenti_df["provincia"].apply(get_name)
incidenti_df.to_csv("indicenti_provincia.csv", index=False)
'''
'''
provincia_pop_auto = pd.read_excel( "provincia_popolazione_parco_auto.xlsx" )
print(provincia_pop_auto.head())
pop_auto_new = pd.DataFrame()
print( provincia_pop_auto["popolazione_residente"])
pop_auto_new["provincia"] = provincia_pop_auto["provincia"].apply(get_name)
pop_auto_new["parco_veicolare"] = provincia_pop_auto["parco_veicolare"]
pop_auto_new["popolazione_residente"] = provincia_pop_auto["popolazione_residente"]
pop_auto_new.to_csv("prov_pop_auto.csv", index=False)
'''

'''
km_carreggiata_df  = pd.read_excel("km_carreggiata_province.xlsx")


df = pd.DataFrame()

df["provincia"] = km_carreggiata_df["Province/Localizzazione strada"].apply(get_name)
df["km_totali"] = km_carreggiata_df["Totale complessivo"]
df["km_autostrada"] = km_carreggiata_df["Autostrade e Raccordi (7)"]
df["km_urbani"] = km_carreggiata_df["Strade urbane (1)"]
print(df)

df.to_csv("km_carreggiata.csv", index=False)
'''

'''
# CLEANING PROVINCE_NAMES
denom_prov = pd.read_csv("denom_province.csv")


km_carreggiata_df = pd.read_csv("prov_pop_auto.csv")

nomi_true = set(denom_prov["province_name"].values)
print(len(nomi_true))
print(nomi_true)

nomi_carr = set(km_carreggiata_df["provincia"].values)


print("NOMI_TRUE - NOMI_CARR")
print(nomi_true - nomi_carr)
print()
print("NOMI_CARR - NOMI_TRUE")
print(nomi_carr - nomi_true)
print()
'''




#print(km_carreggiata_df.head())
