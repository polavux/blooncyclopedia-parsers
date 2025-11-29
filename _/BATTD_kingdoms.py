import xml.etree.ElementTree as ET
import os
import json

nn = "\n"

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

slop = 0

a = open("pywiki_BATTD_kds.txt", "w",encoding="utf-8")

zzzs = ["ZoneTitle_Grasslands", "ZoneTitle_Candy", "ZoneTitle_Ice", "ZoneTitle_Badlands", "ZoneTitle_FireKingdom", "ZoneTitle_Lemongrab", "ZoneTitle_UnderwaterCity", "ZoneTitle_Swamp", "ZoneTitle_LumpySpace"]


for t in zzzs:
    def n(l):
        for i in l[0]:
            if "id" in i.attrib and t== i.attrib['id']: return i.text
            if len(i) > 0:
                for j in i:
                    if "id" in j.attrib and t==j.attrib['id']: return j.text
                    if len(j) > 0:
                        for k in j:
                            if "id" in k.attrib and t== k.attrib['id']: return k.text
                            if len(k) > 0:
                                for l in k:
                                    if "id" in l.attrib and t== l.attrib['id']: return l.text


    a.write(f'''{{{{-start-}}}}
\'\'\'{n(en)}\'\'\'
{{{{bot generated}}}}
\'\'\'{n(en)}\'\'\' is a kingdom in the [[Land of Ooo]] in ''[[Bloons Adventure Time TD]]''.

==Adventures==
{{{{BATTD adventure list by kingdom|{n(en)}}}}}

==Gallery==
{{{{screenshot needed}}}}

==In other languages==
{{{{BATTD langs
|da name   ={n(da)}
|de name   ={n(de)}
|es name   ={n(es)}
|fr name   ={n(fr)}
|it name   ={n(it)}
|ja name   ={n(ja)}
|ko name   ={n(ko)}
|nl name   ={n(nl)}
|no name   ={n(no)}
|pt-br name={n(ptbr)}
|ru name   ={n(ru)}
|sv name   ={n(sv)}
|tr name   ={n(tr)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BATTD nav}}}}
[[Category:Kingdoms in BATTD]]
{{{{-stop-}}}}
''')

a.close()
        