import xml.etree.ElementTree as ET
import json
import os

en = ET.parse('../btd6lang/English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ar = ET.parse('../btd6lang/Arabic.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhcn = ET.parse('../btd6lang/ChineseSimplified.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhtw = ET.parse('../btd6lang/ChineseTraditional.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('../btd6lang/Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('../btd6lang/German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('../btd6lang/Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
esla = ET.parse('../btd6lang/Spanish (LATAM).xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fi = ET.parse('../btd6lang/Finnish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('../btd6lang/French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('../btd6lang/Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('../btd6lang/Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('../btd6lang/Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('../btd6lang/Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('../btd6lang/Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
pl = ET.parse('../btd6lang/Polish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('../btd6lang/Portuguese (Brazil).xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('../btd6lang/Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('../btd6lang/Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
th = ET.parse('../btd6lang/Thai.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('../btd6lang/Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

md = json.load(open("MapDetails.json", "r", encoding="utf-8"))
mi = json.load(open("maps.json", "r", encoding="utf-8"))

o = open("pywiki_BTD6_maps.txt", "w", encoding="utf-8")
xxx = ""
def gn(id):
    for i in range(len(en[0])):
        for j in range(len(en[0][i])):
            if 'id' in en[0][i][j].attrib and en[0][i][j].attrib['id'] == id:
                #print(en[0][i][j].attrib['id'])
                return [i, j]
    return [0, 0]


for i in range(len(md["Maps"]["items"])):
    #if md["Maps"]["items"][i]["id"] != "LuminousCove": continue

    a = gn(md["Maps"]["items"][i]["id"])[0]
    b = gn(md["Maps"]["items"][i]["id"])[1] + 1

    
    def n(l):
        for vv in l[0]:
            for j in vv:
                if j.attrib["id"] == md["Maps"]["items"][i]["id"]: return j.text

    o.write(f"""
{{{{BTD6 last updated|48.1|section=y}}}}
{{{{langlist
|key={md["Maps"]["items"][i]["id"]}
|ar   ={n(ar)}
|da   ={n(da)}
|de   ={n(de)}
|es   ={n(es)}
|es-la={n(esla)}
|fi   ={n(fi)}
|fr   ={n(fr)}
|it   ={n(it)}
|ja   ={n(ja)}
|ko   ={n(ko)}
|nl   ={n(nl)}
|no   ={n(no)}
|pl   ={n(pl)}
|pt-br={n(ptbr)}
|ru   ={n(ru)}
|sv   ={n(sv)}
|th   ={n(th)}
|tr   ={n(tr)}
|zh-cn={n(zhcn)}
|zh-tw={n(zhtw)}
}}}}""")

    '''
    v = mi[md["Maps"]["items"][i]["id"]]["v"] if mi[md["Maps"]["items"][i]["id"]]["v"] != 1.0 else ''
    if v != '':
        vt = f', introduced in [[Bloons TD 6 v{v}|version {v}]].'
    else:
        vt = '.'

    lens = []
    lenls = []

    if hasattr(mi[md["Maps"]["items"][i]["id"]]["l"], "__len__"):
        for j in range(len(mi[md["Maps"]["items"][i]["id"]]["l"])):
            if j % 2 == 1:
                lens.append(str(mi[md["Maps"]["items"][i]["id"]]["l"][j]))
            else:
                lenls.append(str(mi[md["Maps"]["items"][i]["id"]]["l"][j]))

        lens = ",".join(lens)
        lenls = ",".join(lenls)
    else:
        lens = mi[md["Maps"]["items"][i]["id"]]["l"]
        lenls = ""

    rcs = []
    rls = []
    ras = []
    
    if "r" in mi[md["Maps"]["items"][i]["id"]]:
        for j in range(len(mi[md["Maps"]["items"][i]["id"]]["r"])):
            if j % 3 == 1:
                rcs.append(str(mi[md["Maps"]["items"][i]["id"]]["r"][j]))
            elif j % 3 == 2:
                rls.append(str(mi[md["Maps"]["items"][i]["id"]]["r"][j]))
            else:
                ras.append(str(mi[md["Maps"]["items"][i]["id"]]["r"][j]))

        rcs = ",".join(rcs)
        rls = ",".join(rls)
        ras = ",".join(ras)
    else:
        rcs = ""
        rls = ""
        ras = ""

    m = "Winter Nights" if (md["Maps"]["items"][i]["mapMusic"] == "MusicCoopA"
        ) else 'Fiesta Flamenco' if (md["Maps"]["items"][i]["mapMusic"] == "MusicUpbeat1A"
        ) else "Sunshine Serenade" if (md["Maps"]["items"][i]["mapMusic"] == "MusicUpbeat2A"
        ) else 'Sunset Samba' if (md["Maps"]["items"][i]["mapMusic"] == "MusicUpbeat3A"
        ) else 'Tribes & Tribulations' if (md["Maps"]["items"][i]["mapMusic"] == "MusicDarkA"
        ) else 'Tropical Carnival' if (md["Maps"]["items"][i]["mapMusic"] == "MusicCityA"
        ) else "Jazz Theme" if (md["Maps"]["items"][i]["mapMusic"] == "MusicBTD5JazzA"
        ) else "Sails Again" if (md["Maps"]["items"][i]["mapMusic"] == "MusicSailsAgain"
        ) else '???'
    
    d = "Beginner" if md["Maps"]["items"][i]["difficulty"] == 0 else "Intermediate" if md["Maps"]["items"][i]["difficulty"] == 1 else "Advanced" if md["Maps"]["items"][i]["difficulty"] == 2 else "Expert"
    '''
    #xxx += f'BTD6 MapSelect{md["Maps"]["items"][i]["id"]}Button.png|link={en[0][a][b].text}|[[{en[0][a][b].text}]]\n'
    #continue
    
o.close()
#print(xxx)