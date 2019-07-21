import csv
import json
import codecs
import requests
from contextlib import closing
import App
import UpdateGist

# All products from vinmonopolet in a CSV format
url = "https://www.vinmonopolet.no/medias/sys_master/products/products/hbc/hb0/8834253127710/produkter.csv"


with closing(requests.get(url, stream=True)) as f:
    #Creates a dictionary with all of the items, where ; is the delimiter (Separator)
    reader = csv.DictReader(codecs.iterdecode(f.iter_lines(), 'ISO-8859-1'), delimiter=";")

    items = []
    for row in reader:
        # If an item lacks either of these items, or it is not properly formatted, it will be not be used
        try:
            literpris = float(row["Literpris"].replace(",", "."))
            alkohol = float(row["Alkohol"].replace(",", "."))
            pris = float(row["Pris"].replace(",", "."))
            cl = float(row["Volum"].replace(",", ".")) * 100
        except:
            continue

        # Not interested in alcohol free products
        # They also yield a zero-division problem
        if alkohol == 0: continue

        # Price per litre of pure alcohol
        alkopris = int(literpris/(alkohol*0.01))

        #An item may have more than one types
        #Items are separated at "," and made into an array
        type = row["Varetype"].split(", ")
        for i in range(len(type)):
            type[i] = type[i].capitalize()

        #Some drinks are does not have all of its categories, so this helps add some
        typeL = type[0].lower()
        if("øl" in typeL or "pale ale" in typeL or typeL in ["lys lager", "brown ale"]): type.append("Øl")
        if("brennevin" in typeL and typeL != "brennevin"): type.append("Brennevin")
        if("champagne" in typeL and typeL != "champagne"): type.append("Champagne")


        item = {"name": row["Varenavn"], "price": pris, "litre_price": literpris, "alcohol": alkohol, "price_per_alco": alkopris, "cl": cl, "url": row["Vareurl"], "type": type, "land": row["Land"], "picture":  "https://bilder.vinmonopolet.no/cache/515x515-0/" + row["Varenummer"] + "-1.jpg"}
        items.append(item)

# Sort the list by price per alcohol
sortedItems = sorted(items, key=lambda i: i["price_per_alco"])


with codecs.open("WineCsvSorted.json", "w+", encoding="utf8") as f:
    json.dump(sortedItems, f, ensure_ascii=False)

# Top 100 for each category is made
App.start()
# The updated list with categories is pushed to the gist
UpdateGist.update()