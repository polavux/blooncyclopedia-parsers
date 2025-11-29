import xml.etree.ElementTree as ET

def tx(obj, x):
    return obj[0][3][x].text

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
id = ET.parse('Indonesian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('BrazilianPortuguese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhcn = ET.parse('Simplified Chinese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhtw = ET.parse('Traditional Chinese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()


f = open("pywiki_BSM2M_powerups.txt", "w", encoding="utf-8")
num = 0
for i in range(len(en[0][3])):
    if "LOC_POWERUPS_NAME_powerup" in en[0][3][i].attrib["id"] or "LOC_POWERUPS_NAME_superup" in en[0][3][i].attrib["id"]:


        r1 = ""
        r2 = ""
        r3 = ""
        r4 = ""

        for j in range(len(en[0][3])):
            if "LOC_POWERUPS_DESC_powerup" in en[0][3][j].attrib["id"] or "LOC_POWERUPS_DESC_superup" in en[0][3][j].attrib["id"]:
                j += (4 * num)
                r1 = en[0][3][j].text
                r2 = en[0][3][j+1].text
                r3 = en[0][3][j+2].text
                r4 = en[0][3][j+3].text
                break
                #print(r1)

        print(tx(en,i))
        num += 1



        str = '''{{{{-start-}}}}
{{{{BSM2M powerup infobox
|id=

|name ={0}
|image={}

|unlock level=
|type        =Constant
|rarity      =1

|rank 1={1}
|rank 2={2}
|rank 3={3}
|rank 4={4}
}}}}
\'\'\'{0}\'\'\' is a constant 1-star [[Powerup (BSM2 mobile)|powerup]] in the [[Bloons Supermonkey 2 (mobile)|mobile version of ''Bloons Supermonkey 2'']].

==Effects==
{{{{incomplete}}}}

==Strategy==
{{{{strategy needed}}}}

==In other languages==
{{{{BSM2M langs
|da   ={5}
|de   ={6}
|es   ={7}
|fr   ={8}
|id   ={9}
|it   ={10}
|ja   ={11}
|ko   ={12}
|nl   ={13}
|no   ={14}
|pt-br={15}
|ru   ={16}
|sv   ={17}
|tr   ={18}
|zh-cn={19}
|zh-tw={20}
}}}}

==Navigation==
{{{{BSM2M powerup navbox}}}}
{{{{-stop-}}}}
'''.format(tx(en,i), r1, r2, r3, r4, tx(da,i), tx(de,i), tx(es,i),tx(fr,i), tx(id,i), tx(it,i),tx(ja,i),tx(ko,i),tx(nl,i),tx(no,i),tx(ptbr,i),tx(ru,i),tx(sv,i),tx(tr,i),tx(zhcn,i),tx(zhtw,i))
        f.write(str)
f.close()