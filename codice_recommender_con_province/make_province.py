import pandas as pd


def generate_province_data():
    names = pd.read_csv("denom_province.csv", index_col="nome_provincia")
    incidenti_provincia = pd.read_csv("incidenti_provincia.csv",  index_col="provincia")
    km_carreggiata = pd.read_csv("km_carreggiata.csv",  index_col="provincia")
    pil_regioni = pd.read_csv("pil_regioni.csv",  index_col="regione")
    prov_pop_auto = pd.read_csv("prov_pop_auto.csv",  index_col="provincia")

    '''
    merge1 = names.merge(incidenti_provincia, how="inner", left_on="nome_provincia", right_on="provincia")
    print(merge1.head())
    merge2 = merge1.merge(km_carreggiata, how="left", left_on="nome_provincia", right_on="provincia", copy=False, suffix=)
    print(merge2.head())
    '''


    result = names.join( [incidenti_provincia, km_carreggiata, prov_pop_auto] )
    #result["provincia"] = result.index
    #print(result)
    result = result.merge(pil_regioni, how="left", left_on="regione", right_on="regione" )

    #print(result)
    return result


'''
nome_prov = set(merge2["nome_provincia"].values)
nome_prov_x = set(merge2["provincia_x"].values)
nome_prov_y = set(merge2["provincia_y"].values)

print(nome_prov - nome_prov_x)
print(nome_prov_x - nome_prov)

print(
)
print(nome_prov_x - nome_prov_y)
print(nome_prov_y - nome_prov_x)
print()
print(nome_prov - nome_prov_y)
print(nome_prov_y - nome_prov)
'''
