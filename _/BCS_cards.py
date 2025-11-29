import xml.etree.ElementTree as ET
import json
import os

id = 0
iddd = ""

vers = "6.0"

indexofcardtype = 1

def g(lang):
    #if lang != en: return ""
    for i in lang[0][indexofcardtype]:
        if i.attrib["id"] == (iddd + ".Name"):
            if i.text == None: return ""
            return i.text

    print(iddd + ".Name")

def d(lang):
    #if lang != en: return ""
    for i in lang[0][indexofcardtype]:
        if i.attrib["id"] == (iddd + ".Description"):
            if i.text == None: return ""
            return i.text

def f(lang):
    #if lang != en: return ""
    for i in lang[0][indexofcardtype]:
        if i.attrib["id"] == (iddd + ".Flavor"):
            if i.text == None: return ""
            return i.text

en = ET.parse('../bcslang/English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('../bcslang/Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('../bcslang/German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
esla = ET.parse('../bcslang/Latin American Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('../bcslang/French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('../bcslang/Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('../bcslang/Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('../bcslang/Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('../bcslang/Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('../bcslang/Brazilian Portuguese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
pl = ET.parse('../bcslang/Polish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('../bcslang/Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('../bcslang/Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhtw = ET.parse('../bcslang/Traditional Chinese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

#a = []

rarity = open("bank_purchasable_items4.json", "r", encoding="utf-8")
rarityd = json.load(rarity)

def getr(idx):
    id = idx
    if id == "MOABConstructionFacility": id = "MOABConstrFacility"
    if id == "TotalTransformationMonkey": id = "TotalTransformMonkey"
    if id == "Arbitr": id = "ARBITR"
    if ("Card_" + id) not in rarityd["items"]: return None
    for k, v in (rarityd["items"]["Card_" + id]["costs"][0]["cost"]).items():
        match v:
            case 300: return "Common"
            case 800: return "Uncommon"
            case 1500: return "Rare"
            case 3500: return "Super Rare"
            case 4500: return "Super Rare"
            case 15000: return "Ultra Rare"

def getc(idx):
    id = idx
    if id == "MOABConstructionFacility": id = "MOABConstrFacility"
    if id == "TotalTransformationMonkey": id = "TotalTransformMonkey"
    if id == "Arbitr": id = "ARBITR"
    if ("Card_" + id) not in rarityd["items"]: return None
    for k, v in (rarityd["items"]["Card_" + id]["costs"][0]["cost"]).items():
        match k:
            case "PrimaryToken": return "Primary"
            case "MilitaryToken": return "Military"
            case "MagicToken": return "Magic"
            case "SupportToken": return "Support"
            case "BasicBloonToken": return "Basic"
            case "AdvancedBloonToken": return "Advanced"
            case "LargeBloonToken": return "Large"
            case "BasicPowerToken": return "Basic"
            case "AdvancedPowerToken": return "Advanced"
            case "ExoticPowerToken": return "Exotic"    


o = open("py_monkey.txt", "w", encoding="utf-8")

            
for k, v in (rarityd["items"]).items():
    doo = True
    if "Card_" in k and not "CraftCard_" in k:
        for i in en[0][0]:
            if i.attrib["id"].split(".")[0] == k.split("_")[1]:
                doo = False
                break
        for i in en[0][1]:
            if i.attrib["id"].split(".")[0] == k.split("_")[1]:
                doo = False
                break
        for i in en[0][2]:
            if i.attrib["id"].split(".")[0] == k.split("_")[1]:
                doo = False
                break

        #if doo: print(k)

include = ["Druid of Peace","Dart Arts Wizard","Bloon Impact","Extra Range Tack Shooter","Fireball Wizard","Distraction Ninja","Shinobi Tactics Ninja",
           "Grand Saboteur","Night Vision Sniper","Radar Scanner Village","Extra-Super Monkey","Even More Tacks","Ninja Monkey"]

for i in range(len(en[0][indexofcardtype])):
    id = i
    iddd = en[0][indexofcardtype][i].attrib["id"].split(".")[0]
    if g(en) not in include or ".Name" not in en[0][indexofcardtype][i].attrib["id"]: continue
    idd = en[0][indexofcardtype][i].attrib["id"].split(".")[1]
    o.write(f"""{{{{-start-}}}}
'''{g(en)}'''
{{{{bot generated}}}}
{{{{BCS monkey info
|id={iddd}
|numeric id=

|name       ={g(en)}
|image      =BCS {iddd} CardArt.png
|description={d(en)}
|flavor     ={f(en)}

|pack      ={"None" if {getr(iddd)} == None else "Lead Storm"}
|class     ={getc(iddd)}
|rarity    ={getr(iddd)}
|keywords  =
|exclusive =
|introduced={vers}

|cost   =
|charges=
|type   =
|ammo   =
|power  =
|reload =
}}}}
The '''{g(en)}''' is a [[{getc(iddd)}]] [[Monkey (BCS)|Monkey]] [[card]] in ''[[Bloons Card Storm]]'', introduced in {{{{BCS version|{vers}}}}}.
<!-- When uncommenting these, make sure not to create more than one blank line between visible and non-visible text, otherwise it makes the empty space visible
==Tips==
{{{{BCS last updated|{vers}|section=y}}}}-->
<!--
==Update history==
{{{{BCS change list by name|{g(en)}}}}}-->

==Gallery==
{{{{screenshot needed}}}}
<gallery>
BCS {iddd} Icon.png|Icon
</gallery>

==In other languages==
{{{{BCS last updated|{vers}|section=y}}}}
{{{{langlist
|label=Name
|key={iddd}.Name
|da   ={g(da)}
|de   ={g(de)}
|es-la={g(esla)}
|fr   ={g(fr)}
|it   ={g(it)}
|ja   ={g(ja)}
|ko   ={g(ko)}
|no   ={g(no)}
|pl   ={g(pl)}
|pt-br={g(ptbr)}
|ru   ={g(ru)}
|sv   ={g(sv)}
|zh-tw={g(zhtw)}
}}}}
{{{{langlist
|label=Flavor
|key={iddd}.Flavor
|da   ={f(da)}
|de   ={f(de)}
|es-la={f(esla)}
|fr   ={f(fr)}
|it   ={f(it)}
|ja   ={f(ja)}
|ko   ={f(ko)}
|no   ={f(no)}
|pl   ={f(pl)}
|pt-br={f(ptbr)}
|ru   ={f(ru)}
|sv   ={f(sv)}
|zh-tw={f(zhtw)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BCS monkey nav}}}}
{{{{-stop-}}}}
""")

indexofcardtype = 0
    
o.close()
o = open("py_bloon.txt", "w", encoding="utf-8")

include = ["Life Drain Bloon", "Spooky Bloon","Golden Blimp","Shielded MOAB","Spirit Bloon","Soulstealer Bloon","Life Drain Bloon","Camo Blue Bloon","Camo Green Bloon","DDT","Camo Regrow Ceramic Bloon",
           "Regrow Yellow Bloon","The Regenerator","Fortified Regrow Camo Red Bloon","Camo Regrow Rainbow Bloon","Camo Lead Bloon","Zombie Blue Bloon","Zombie MOAB","Zombie Rainbow Bloon"]

for i in range(len(en[0][indexofcardtype])):
    id = i
    iddd = en[0][indexofcardtype][i].attrib["id"].split(".")[0]
    if g(en) not in include or ".Name" not in en[0][indexofcardtype][i].attrib["id"]: continue
    idd = en[0][indexofcardtype][i].attrib["id"].split(".")[1]
    o.write(f"""{{{{-start-}}}}
'''{g(en)}'''
{{{{bot generated}}}}
{{{{BCS bloon info
|id={iddd}
|numeric id=

|name       ={g(en)}
|image      =BCS {iddd} CardArt.png
|description={d(en)}
|flavor     ={f(en)}

|pack      ={"None" if {getr(iddd)} == None else "Lead Storm"}
|class     ={getc(iddd)}
|rarity    ={getr(iddd)}
|keywords  =
|exclusive =
|introduced={vers}

|cost   =
|charges=
|health =
|delay  =
}}}}
The '''{g(en)}''' is a{"n" if getc(iddd) == "Advanced" else ""} [[Bloon (BCS)|{getc(iddd)} Bloon]] [[card]] in ''[[Bloons Card Storm]]'', introduced in {{{{BCS version|{vers}}}}}.
<!-- When uncommenting these, make sure not to create more than one blank line between visible and non-visible text, otherwise it makes the empty space visible
==Tips==
{{{{BCS last updated|{vers}|section=y}}}}-->
<!--
==Update history==
{{{{BCS change list by name|{g(en)}}}}}-->

==Gallery==
{{{{screenshot needed}}}}
<gallery>
BCS {iddd} Icon.png|Icon
</gallery>

==In other languages==
{{{{BCS last updated|{vers}|section=y}}}}
{{{{langlist
|label=Name
|key={iddd}.Name
|da   ={g(da)}
|de   ={g(de)}
|es-la={g(esla)}
|fr   ={g(fr)}
|it   ={g(it)}
|ja   ={g(ja)}
|ko   ={g(ko)}
|no   ={g(no)}
|pl   ={g(pl)}
|pt-br={g(ptbr)}
|ru   ={g(ru)}
|sv   ={g(sv)}
|zh-tw={g(zhtw)}
}}}}
{{{{langlist
|label=Flavor
|key={iddd}.Flavor
|da   ={f(da)}
|de   ={f(de)}
|es-la={f(esla)}
|fr   ={f(fr)}
|it   ={f(it)}
|ja   ={f(ja)}
|ko   ={f(ko)}
|no   ={f(no)}
|pl   ={f(pl)}
|pt-br={f(ptbr)}
|ru   ={f(ru)}
|sv   ={f(sv)}
|zh-tw={f(zhtw)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BCS bloon nav}}}}
{{{{-stop-}}}}
""")

indexofcardtype = 2
    
o.close()
o = open("py_power.txt", "w", encoding="utf-8")

include = ["Bloon Amalgam"] # "Target Locked" cut

for i in range(len(en[0][indexofcardtype])):
    id = i
    iddd = en[0][indexofcardtype][i].attrib["id"].split(".")[0]
    if g(en) not in include or ".Name" not in en[0][indexofcardtype][i].attrib["id"]: continue
    idd = en[0][indexofcardtype][i].attrib["id"].split(".")[1]
    o.write(f"""{{{{-start-}}}}
'''{g(en)}'''
{{{{bot generated}}}}
{{{{BCS power info
|id={iddd}
|numeric id=

|name       ={g(en)}
|image      =BCS {iddd} CardArt.png
|description={d(en)}
|flavor     ={f(en)}

|pack      ={"None" if {getr(iddd)} == None else "Lead Storm"}
|class     ={getc(iddd)}
|rarity    ={getr(iddd)}
|keywords  =
|exclusive =
|introduced={vers}

|cost   =
|charges=
}}}}
'''{g(en)}''' is a{"" if getc(iddd) == "Basic" else "n"} [[Power (BCS)|{getc(iddd)} Power]] [[card]] in ''[[Bloons Card Storm]]'', introduced in {{{{BCS version|{vers}}}}}.
<!-- When uncommenting these, make sure not to create more than one blank line between visible and non-visible text, otherwise it makes the empty space visible
==Tips==
{{{{BCS last updated|{vers}|section=y}}}}-->
<!--
==Update history==
{{{{BCS change list by name|{g(en)}}}}}-->

==Gallery==
<gallery>
BCS {iddd} Icon.png|Icon
</gallery>

==In other languages==
{{{{BCS last updated|{vers}|section=y}}}}
{{{{langlist
|label=Name
|key={iddd}.Name
|da   ={g(da)}
|de   ={g(de)}
|es-la={g(esla)}
|fr   ={g(fr)}
|it   ={g(it)}
|ja   ={g(ja)}
|ko   ={g(ko)}
|no   ={g(no)}
|pl   ={g(pl)}
|pt-br={g(ptbr)}
|ru   ={g(ru)}
|sv   ={g(sv)}
|zh-tw={g(zhtw)}
}}}}
{{{{langlist
|label=Flavor
|key={iddd}.Flavor
|da   ={f(da)}
|de   ={f(de)}
|es-la={f(esla)}
|fr   ={f(fr)}
|it   ={f(it)}
|ja   ={f(ja)}
|ko   ={f(ko)}
|no   ={f(no)}
|pl   ={f(pl)}
|pt-br={f(ptbr)}
|ru   ={f(ru)}
|sv   ={f(sv)}
|zh-tw={f(zhtw)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BCS power nav}}}}
{{{{-stop-}}}}
""")
    
o.close()
rarity.close()