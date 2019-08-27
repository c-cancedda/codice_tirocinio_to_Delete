from html.parser import HTMLParser
import urllib.request as HttpRequest
from urllib.error import URLError
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas as pd





# COSTRUZIONE DIZIONARIO PIL_PROVINCE
# regione,  pil_totale, pil_pro_capite
province_data = {"region" : [],
                "pil_total" : [],
                "pil_pro_capite" : []}

with open("pil.html") as fp:
    soup = BeautifulSoup(fp)

    tables = soup.find_all("table")
    for table in tables:
        t_body = table.tbody
        #print(type(t_body.contents))
        for t_row in t_body.contents:
            if isinstance(t_row, Tag):
                td_list = [ x  for x in t_row.contents if isinstance(x, Tag) ]
            #    province_data[td_list[0].string] = [float(td_list[1].string.replace(".", "")), float(td_list[2].string.replace(".", "")) ]

                region = td_list[0].string.strip().replace("-", " ")
                pil_total = float(td_list[1].string.replace(".", ""))
                pil_pro_capite = float(td_list[2].string.replace(".", ""))
                province_data["region"].append(region)
                province_data["pil_total"].append(pil_total)
                province_data["pil_pro_capite"].append( pil_pro_capite)

                #print(td_list[0].string, " : ", province_data[td_list[0].string])


def get_tags(contents, tagname=None):
    tag_list = []
    for x in contents:
         if isinstance(x, Tag):
            if tagname == None:
                tag_list.append(x)
            else:
                if x.name == tagname:
                    tag_list.append(x)
    return tag_list

# COSTRUZIONE DIZIONARIO DENOMINAZIONE PROVINCE
# province_id,  province_name, province_region
provinces_dict = {
                "province_id" : [],
                "province_name" : [],
                "province_region" : [] }



with open("province.html") as fp:
    soup = BeautifulSoup(fp)

    t_rows = soup.find_all("tr")
    for t_row in t_rows:
        tds = get_tags(t_row, "td")

                                                    # removed op .replace(" ", "").
        province_id = get_tags(tds[0], "p")[0].string.strip().replace("\n", "").replace("-",  " ")
        province_name = get_tags(tds[1], "p")[0].string.strip().replace("\n", "").replace("-", " ")
        province_region = get_tags(tds[2], "p")[0].string.strip().replace("\n", "").replace("-", " ")
        #provinces_dict[province_name] = [ province_id, province_region ]
        provinces_dict["province_id" ].append(province_id)
        provinces_dict["province_name" ].append(province_name)
        provinces_dict["province_region" ].append(province_region)
        #print(province_id, "\n" , province_name, "\n", province_region)


                #print(t_row.string)

            #print(isinstance(t_row, Tag) )
            #print()
            #print(t_row.contents)
            #print()

print(provinces_dict)

for k, v in provinces_dict.items():
    print(len(v))

province_names_df = pd.DataFrame( provinces_dict )
print(province_names_df.head())

province_names_df.to_csv("denom_province.csv", index=False)


provinces_pil_df = pd.DataFrame(province_data)
print(provinces_pil_df.head())
provinces_pil_df.to_csv("pil_province.csv", index=False)

provinces_pil_merged = province_names_df.merge(right=provinces_pil_df, how="inner", left_on="province_region", right_on="region" )
print(provinces_pil_merged)

# CHECK NOMI PROVINCE E NOMI REGIONI 
regions_df1_list = province_names_df["province_name"].unique()
regions_df2_list = provinces_pil_merged["province_name"].unique()


# il data cleaning è stato effettuato ripetendo piu volte le seguenti operazioni e modificando manualmente i pochi casi speciali che si sono presentati
print(regions_df1_list)
print(regions_df2_list)

set1 = set(regions_df1_list)
set2 = set(regions_df2_list)
print()
print(set1 - set2)
print()
print(set2 - set1)
