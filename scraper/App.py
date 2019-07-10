import json
import codecs
from datetime import date

def start():
    with codecs.open('wine_sorted.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        createObject(data)

types = ["Rødvin", "Cognac", "Hvitvin", "Rosévin", "Sterkvin", "Musserende vin", "Brennevin", "Vodka", "Gin", "Sake", "Øl", "Perlende vin", "Tequila", "Bitter", "Rom", "Likør", "Whisky", "Akevitt", "India pale ale"]
def createObject(s):
    prodList = []
    prodList.append({"name": "top", "products": []})

    for p in s:
        if p not in prodList[0]["products"] and len(prodList[0]["products"])< 100:
            prodList[0]["products"].append(p)
            
        for t in p["type"]:
            t = t.lower()
            t = t.capitalize()
            if t not in types:
                continue

            e = typeInList(prodList, t)

            if (e == -1):
                prodList.append({"name": t, "products": [p]})
                continue
            elif p not in prodList[e]["products"] and len(prodList[e]["products"])< 100:
                prodList[e]["products"].append(p)

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    output = {"date": f"{d1}"}
    output["items"] = prodList

    with codecs.open("output.json", "w+", encoding='utf8') as g:
        json.dump(output, g, ensure_ascii=False)

def typeInList(l, t):
    for e, x in enumerate(l):
        if x["name"] == t:
            return e
    return -1

start()