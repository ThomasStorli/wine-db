import json
import codecs
from datetime import date

def start(fileURL):
    with codecs.open(fileURL, 'r', encoding='utf8') as f:
        data = json.load(f)
        createObject(data)


def createObject(s):
    prodList = []

    for p in s["wine"]:
        for k in p["type"]:
            k = k.lower()
            k = k.capitalize()
            if k not in ["Rødvin", "Hvitvin", "Rosévin", "Sterkvin", "Musserende vin", "Brennevin", "Vodka", "Gin", "Sake", "Øl", "Perlende vin", "Tequila", "Bitter", "Rom", "Likør", "Whisky", "Akevitt", "India pale ale"]:
                continue

            e = typeInList(prodList, k)
            if (e == -1):
                prodList.append({"name": k, "products": [p]})
                continue
            elif len(prodList[e]["products"])< 100:
                prodList[e]["products"].append(p)



    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    output = {"date": f"{d1}"}
    output["items"] = prodList

    with codecs.open("produtto12345.json", "w+", encoding='utf8') as g:
        json.dump(output, g, ensure_ascii=False)

def typeInList(l, t):
    for e, x in enumerate(l):
        if x["name"] == t:
            return e
    return -1



start('C:/Users/Alexander/PycharmProjects/WineScraper/wine_sorted.json')