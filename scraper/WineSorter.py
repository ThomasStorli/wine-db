import json
import codecs

with open("wine_2.json", "r", encoding="utf8") as g:
    data1 = json.load(g)["wine"]
    g.close()

with open("wine_3.json", "r", encoding='utf8') as f:
    data = json.load(f)["wine"]
    f.close()

data.extend(data1)

newData = []
for i in data:
  if i not in newData:
    newData.append(i)

data = sorted(newData, key=lambda i:i["price_per_alco"])

with codecs.open("wine_sorted.json", "w+", encoding="utf8") as h:
    json.dump(data, h, ensure_ascii=False)