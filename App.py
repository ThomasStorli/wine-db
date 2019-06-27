import json

def start(fileURL):
    with open(fileURL, 'r') as f:
        data = json.load(f)
        createObject(data)


def createObject(s):
    products = {}
    for p in s["wine"]:
        for k in p["type"]:
            if k in products:
                products[k].append(p)
            else:
                products[k] = [p]

    prodList = []
    for prod, v in products.items():
        prodList.append({prod:v})

    output = {"date": "27/06/19"}
    output["items"] = prodList

    with open("produtto.json", "w+") as g:
        json.dump(output, g)


start('C:/Users/Alexander/git/wine-db/src/assets/wine_3.json')