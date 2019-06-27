import json
from datetime import date

def start(fileURL):
    with open(fileURL, 'r') as f:
        data = json.load(f)
        createObject(data)


def createObject(s):
    prodList = []

    for p in s["wine"]:
        for k in p["type"]:
            e = typeInList(prodList, k)
            if (e == -1):   
                prodList.append({"name": k, "products": [p]})
                continue
            else:
                prodList[e]["products"].append(p)


    
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    output = {"date": f"{d1}"}
    output["items"] = prodList

    with open("produtto1234.json", "w+") as g:
        json.dump(output, g)

def typeInList(l, t):
    for e, x in enumerate(l):
        if x["name"] == t:
            return e
    return -1



start('C:\\Projects\\wine-db\\wine_3.json')