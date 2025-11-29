import xml.etree.ElementTree as ET
import json
import os
import sys
import pyperclip

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ar = ET.parse('Arabic_pres.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fi = ET.parse('Finnish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('BrazilianPortuguese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

k = sys.argv[1]

def n(l):
    for i in l[0]:
            if i.attrib["id"] == k: return i.text
            
x = (f"""{{{{langlist
|label={sys.argv[2] if len(sys.argv) > 2 else ""}
|key={k}
|ar   ={n(ar)}
|da   ={n(da)}
|de   ={n(de)}
|es   ={n(es)}
|fi   ={n(fr)}
|fr   ={n(fr)}
|it   ={n(it)}
|ja   ={n(ja)}
|ko   ={n(ko)}
|no   ={n(no)}
|pt-br={n(ptbr)}
|ru   ={n(ru)}
|sv   ={n(sv)}
|tr   ={n(tr)}
}}}}""")
print()
print(x)
pyperclip.copy(x)