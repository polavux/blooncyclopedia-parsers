import xml.etree.ElementTree as ET
import json, os

ptbr = ET.parse('Brazilian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

o = open("pywiki_BATTD_characters.txt", "w", encoding="utf-8")

ids = ['Max','Finn','Jake','IceKing','FlamePrincess','Marceline','Bubblegum','C4Charlie','Sam','Sai','SuperMonkey','CaptainCassie','MarcelineTheVampireHunter','SerenadingJake','WarmasterBubblegum','CommanderCassie','WarriorFinn','JuggernautMax']

id = ""

def n(lang):
    for i in lang[0][5][1]:
        if i.attrib["id"] == id:
            return i.text

def ld(lang):
    for i in lang[0][5][3]:
        if i.attrib["id"] == id + "_desc":
            return i.text

def pd(lang):
    for i in lang[0][5][3]:
        if i.attrib["id"] == id + "_pro":
            return i.text

def cd(lang):
    for i in lang[0][5][3]:
        if i.attrib["id"] == id + "_con":
            return i.text

def d(lang):
    for i in lang[0][5][4]:
        if i.attrib["id"] == id + "_ShortDesc":
            return i.text

for i in ids:
    id = i
    o.write(f'''{{{{-start-}}}}
\'\'\'{n(en)} (BATTD)\'\'\'
{{{{for|{n(en)} in general|{n(en)}}}}}
{{{{bot generated}}}}
{{{{BATTD character info
|id={i}

|name       ={n(en)}
|image      =
|description={d(en)}
           
|cost         =
|weapon type  =
|resource type=

|bio description={ld(en)}
|bio strengths  ={pd(en)}
|bio weaknesses ={cd(en)}
}}}}
\'\'\'{n(en)}\'\'\' is a [[Character (BATTD)|character]] in ''[[Bloons Adventure Time TD]]''.
{{{{TOC}}}}
{{{{clear|right}}}}
==Upgrades==
{{{{BATTD upgrade list by tower|{n(en)}}}}}

==Strategy==
{{{{main strategy}}}}
{{{{strategy needed}}}}

==Gallery==
{{{{screenshot needed}}}}

==In other languages==
{{{{langlist
|label=Name
|key={i}
|da   ={n(da)}
|de   ={n(de)}
|es   ={n(es)}
|fr   ={n(fr)}
|it   ={n(it)}
|ja   ={n(ja)}
|ko   ={n(ko)}
|nl   ={n(nl)}
|no   ={n(no)}
|pt-br={n(ptbr)}
|ru   ={n(ru)}
|sv   ={n(sv)}
|tr   ={n(tr)}
}}}}
{{{{langlist
|label=Description
|key={i}_ShortDesc
|da   ={d(da)}
|de   ={d(de)}
|es   ={d(es)}
|fr   ={d(fr)}
|it   ={d(it)}
|ja   ={d(ja)}
|ko   ={d(ko)}
|nl   ={d(nl)}
|no   ={d(no)}
|pt-br={d(ptbr)}
|ru   ={d(ru)}
|sv   ={d(sv)}
|tr   ={d(tr)}
}}}}
{{{{langlist
|label=Profile description
|key={i}_Desc
|da   ={ld(da)}
|de   ={ld(de)}
|es   ={ld(es)}
|fr   ={ld(fr)}
|it   ={ld(it)}
|ja   ={ld(ja)}
|ko   ={ld(ko)}
|nl   ={ld(nl)}
|no   ={ld(no)}
|pt-br={ld(ptbr)}
|ru   ={ld(ru)}
|sv   ={ld(sv)}
|tr   ={ld(tr)}
}}}}

==Navigation==
{{{{BATTD character nav}}}}
{{{{-stop-}}}}
''')
o.close()