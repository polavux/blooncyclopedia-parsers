import json, os
import xml.etree.ElementTree as ET
en = ET.parse('../btd6lang/English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
xn = ET.parse('../btd6lang/ChineseSimplifiedxd.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

items = {}
itemIds = []

o = open("wt.txt", "w", encoding="utf-8")

def bol(a):
    return "y" if a else ""

def n():
    #for a in en[0]:
    #    for b in a:
    #        if b.attrib['id'] == (aj['m_Name']): return b.text
    for a in xn[0]:
        for b in a:
            if b.attrib['id'] == (aj['m_Name']): return b.text
            
def d(x):
    for a in xn[0]:
        for b in a:
            if b.attrib['id'] == (x + ' Description'): return b.text

for i in os.listdir("cn"):
    a = open(f"cn/{i}", "r", encoding="utf-8")

    aj = json.load(a)
    if aj["m_Script"]["m_PathID"] == -8469736156695596375:
        items[aj["productID"]] = aj

    a.close()

counter = 1
for i in range(len(en[0])):
    for j in range(len(en[0][i])):
        x = en[0][i][j].attrib["id"]
        if x in items:

            o.write(f"""
|item {counter} id={items[x]["productID"]}
|item {counter} batch id={items[x]["batchId"]}
|item {counter} name={en[0][i][j].text}
|item {counter} image=BTD6 {(en[0][i][j].text).replace(" ", "")}Shop.png
|item {counter} description={d(x)}
|item {counter} type={"Limited time" if items[x]["productType"] == 1 else "Sale" if items[x]["productType"] == 2 else "Regular"}
|item {counter} loot={items[x]["loot"]}
|item {counter} viewable in store={bol(items[x]["viewableInStore"])}
|item {counter} available in game={bol(items[x]["availableInGame"])}
|item {counter} viewable in heroes={bol(items[x]["viewableInHeroes"])}
|item {counter} associated heroes={items[x]["associatedHeroes"]}
|item {counter} not available if rank over={items[x]["notAvailableIfRankOver"]}
|item {counter} only available if rank over={items[x]["onlyAvailableIfRankOver"]}
|item {counter} show timer={bol(items[x]["showTimer"])}
|item {counter} monkey money cost={items[x]["monkeyMoneyCost"]}
|item {counter} consumable={bol(items[x]["consumable"])}
|item {counter} is one time consumable={bol(items[x]["isOneTimeConsumable"])}
|item {counter} introduced=
""")
            counter += 1
            
o.close()


