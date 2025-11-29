import xml.etree.ElementTree as ET
import json

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

o = open("pywiki_BMC_special_items_3.txt", "w", encoding="utf-8")

fd = json.load(open('12077_ninjakiwi.monkeyTown.data.RemoteDataManager_JsonData.json'))
md = json.load(open('SpecialItems.json'))


vi = 0
for k, i in fd['specialItems'].items():

    o.write(f'''{{{{-start-}}}}
\'\'\'{i['name']}\'\'\'
{{{{bot generated}}}}
{{{{BMC special item info
|id={k}

|name F       ={i['name']}
|image F      =
|description F={i["gameDescription"]}

|rarity={i['rarity']}
}}}}
The \'\'\'{i['name']}\'\'\' is a [[Special Item]] in the {{{{flash version of|Bloons Monkey City}}}}.

{{{{clear|right}}}}
==Navigation==
{{{{BMC special item nav}}}}
{{{{-stop-}}}}
''')
        
o.close()