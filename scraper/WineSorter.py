import json
import codecs

with open("wine_3.json", "r", encoding='utf8') as f:
    data = json.load(f)["wine"]
    f.close()

with open("wine_2.json", "r", encoding="utf8") as g:
    data1 = json.load(g)["wine"]
    g.close()

data.extend(data1)
data = sorted(data, key=lambda i:i["price_per_alco"])

with codecs.open("wine_sorted.json", "w+", encoding="utf8") as h:
    json.dump(data, h, ensure_ascii=False)