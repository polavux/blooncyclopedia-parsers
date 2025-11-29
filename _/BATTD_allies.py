import xml.etree.ElementTree as ET
import json, os, sys
import pyperclip

da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('Brazilian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

k = sys.argv[1]

def n(l):
    for i in l:
        if i.tag == "T":
            if i.attrib["id"] == k: return i.text
        else:
            if n(i) != -1: return n(i)

    return -1
        

x = (f"""{{{{langlist
|label={sys.argv[2] if len(sys.argv) > 2 else ""}
|key={k}
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
}}}}""")
print()
print(x)
pyperclip.copy(x)