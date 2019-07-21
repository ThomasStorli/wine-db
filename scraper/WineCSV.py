import csv
import json
import codecs
import requests
from contextlib import closing
import App
import UpdateGist

url = "https://www.vinmonopolet.no/medias/sys_master/products/products/hbc/hb0/8834253127710/produkter.csv"

with closing(requests.get(url, stream=True)) as f:

    reader = csv.DictReader(codecs.iterdecode(f.iter_lines(), 'ISO-8859-1'), delimiter=";")

    items = []
    for row in reader:
        try:
            literpris = float(row["Literpris"].replace(",", "."))
            alkohol = float(row["Alkohol"].replace(",", "."))
            pris = float(row["Pris"].replace(",", "."))
            cl = float(row["Volum"].replace(",", ".")) * 100
        except:
            continue

        if alkohol == 0: continue

        alkopris = int(literpris/(alkohol*0.01))

        type = row["Varetype"].split(", ")
        for i in range(len(type)):
            type[i] = type[i].capitalize()

        typeL = type[0].lower()
        if("øl" in typeL or "pale ale" in typeL or typeL in ["lys lager", "brown ale"]): type.append("Øl")
        if("brennevin" in typeL and typeL != "brennevin"): type.append("Brennevin")
        if("champagne" in typeL): type.append("Champagne" and typeL != "champagne")

        item = {"name": row["Varenavn"], "price": pris, "litre_price": literpris, "alcohol": alkohol, "price_per_alco": alkopris, "cl": cl, "url": row["Vareurl"], "type": type, "land": row["Land"], "picture":  "https://bilder.vinmonopolet.no/cache/515x515-0/" + row["Varenummer"] + "-1.jpg"}
        items.append(item)

sortedItems = sorted(items, key=lambda i: i["price_per_alco"])


with codecs.open("WineCsvSorted.json", "w+", encoding="utf8") as f:
    json.dump(sortedItems, f, ensure_ascii=False)

App.start()
UpdateGist.update()