import json
import codecs
from datetime import date
import operator

def start():
    with codecs.open('WineCsvSorted.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        createObject(data)

types = ["Rødvin", "Cognac", "Hvitvin", "Rosévin", "Sterkvin", "Musserende vin", "Brennevin", "Vodka", "Gin", "Sake", "Øl", "Perlende vin", "Tequila", "Bitter", "Rom", "Likør", "Whisky", "Akevitt", "Sider", "Surøl", "Portvin", "Rosévin"]


def createObject(s):
    prodList = []
    prodList.append({"name": "top", "products": []})

    for p in s:
        if p not in prodList[0]["products"] and len(prodList[0]["products"]) < 100:
            prodList[0]["products"].append(p)

        for t in p["type"]:
            if not isinstance(t, str): continue
            t = t.lower()
            t = t.capitalize()
            if t not in types:
                continue

            e = typeInList(prodList, t)

            if (e == -1):
                prodList.append({"name": t, "products": [p]})
                continue
            elif p not in prodList[e]["products"] and len(prodList[e]["products"]) < 100:
                prodList[e]["products"].append(p)

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    output = {"date": f"{d1}"}
    output["items"] = prodList

    with codecs.open("output.json", "w+", encoding='utf8') as g:
        json.dump(output, g, ensure_ascii=False)
        g.close()


def typeInList(l, t):
    for e, x in enumerate(l):
        if x["name"] == t:
            return e
    return -1


#start()

def counter():
    with codecs.open('WineCsvSorted.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    typer = {}
    for i in data:
        for j in i["type"]:
            if j in typer:
                typer[j] = typer[j] + 1
            else:
                typer[j] = 1
    print(sorted(typer.items(), key=operator.itemgetter(1)))

#counter()