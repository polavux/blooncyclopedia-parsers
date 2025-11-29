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

aaaaa = "{0}"

fartifacts = dict()

def n(lang, z):
    for a in lang[0]:
        for b in a:
            if b.attrib['id'] == z: return b.text
            
def d(lang, z):
    for a in lang[0]:
        for b in a:
            if b.attrib['id'] == z: return b.text

for i in os.listdir('data'):

    

    f = open('data/'+i, 'r', encoding='utf-8')
    ft = json.load(f)
    #print(ft)
    fd = dict()
    #print(ft)

    if 'itemArtifactModel' in ft:
        fd = ft['itemArtifactModel']
    elif 'mapArtifactModel' in ft:
        fd = ft['mapArtifactModel']
    elif 'boostArtifactModel' in ft:
        fd = ft['boostArtifactModel']

    if fd['isQuestArtifact']: print(i)    
    if fd['baseId'] not in fartifacts: fartifacts[fd['baseId']] = {}
    if 'itemArtifactModel' in ft:
        fd = ft['itemArtifactModel']
        fartifacts[fd['baseId']]['type'] = 'Artifact'
    elif 'mapArtifactModel' in ft:
        fd = ft['mapArtifactModel']
        fartifacts[fd['baseId']]['type'] = 'Map'
    elif 'boostArtifactModel' in ft:
        fd = ft['boostArtifactModel']
        fartifacts[fd['baseId']]['type'] = 'Boost'

    fartifacts[fd['baseId']][fd['tier']] = {
        'name': fd['nameLocKey'],
        'description': fd['descriptionLocKey'],
        'descriptionParams': fd['descriptionParams']
    }

    if 'itemArtifactModel' in ft:
        fartifacts[fd['baseId']][fd['tier']]['instaTowerToGive'] = fd['instaTowerToGive']['baseId']
        fartifacts[fd['baseId']][fd['tier']]['instaTowerTiers'] = ''
        for zzz in fd['instaTowerToGive']['tiers']:
            fartifacts[fd['baseId']][fd['tier']]['instaTowerTiers'] += str(zzz)
            if fd['instaTowerToGive']['isFree']: print(fd['baseId'], fd['instaTowerToGive']['isFree'])

    else:
        fartifacts[fd['baseId']][fd['tier']]['instaTowerToGive'] = ''
        fartifacts[fd['baseId']][fd['tier']]['instaTowerTiers'] = ''

o = open("pywiki_BTD6_artifacts.txt", "w", encoding="utf-8")
for k, v in fartifacts.items():

    desc1 = "" if 0 not in v else n(en, v[0]['description'])
    for sbrjs in range(10):
        print("{" + str(sbrjs) + "}")
        if ("{" + str(sbrjs) + "}") in desc1:
            print('fsbzdzb')
            desc1 = desc1.replace('{' + str(sbrjs) + "}", v[0]['descriptionParams'][sbrjs])

    desc2 = "" if 1 not in v else n(en, v[1]['description'])
    for sbrjs in range(10):
        print("{" + str(sbrjs) + "}")
        if ("{" + str(sbrjs) + "}") in desc2:
            print('fsbzdzb')
            desc2 = desc2.replace('{' + str(sbrjs) + "}", v[1]['descriptionParams'][sbrjs])

    desc3 = "" if 2 not in v else n(en, v[2]['description'])
    for sbrjs in range(10):
        print("{" + str(sbrjs) + "}")
        if ("{" + str(sbrjs) + "}") in desc3:
            print('fsbzdzb')
            desc3 = desc3.replace('{' + str(sbrjs) + "}", v[2]['descriptionParams'][sbrjs])
    if 0 not in v: v[0] = v[1] if 1 in v else v[2]

    o.write(f"""{{{{-start-}}}}
{{{{stub}}}}
{{{{BTD6 artifact info
|id={k}
|type={v['type']}

|name ={n(en, v[0]['name']).replace(' '+aaaaa,'')}
|image=BTD6 Artifact{k}.png

|description common   ={desc1}
|description rare     ={desc2}
|description legendary={desc3}

|insta type common   ={"" if 0 not in v else v[0]['instaTowerToGive']}
|insta type rare     ={"" if 1 not in v else v[1]['instaTowerToGive']}
|insta type legendary={"" if 2 not in v else v[2]['instaTowerToGive']}

|insta tiers common   ={"" if 0 not in v else v[0]['instaTowerTiers']}
|insta tiers rare     ={"" if 1 not in v else v[1]['instaTowerTiers']}
|insta tiers legendary={"" if 2 not in v else v[2]['instaTowerTiers']}
|introduced=51.0
}}}}
'''{n(en, v[0]['name']).replace(' '+aaaaa,'')}''' is a type of [[Artifact]] in the ''[[Rogue Legends]]'' DLC for ''[[Bloons TD 6]]'', introduced in {{{{BTD6 version|51.0}}}}.

==In other languages==
{{{{langlist
|table=btd6_text
|key={v[0]['name'] if 0 in v else v[1]['name'] if 1 in v else v[2]['name']}
|ar   ={n(ar, v[0]['name']).replace(' '+aaaaa,'')}
|da   ={n(da, v[0]['name']).replace(' '+aaaaa,'')}
|de   ={n(de, v[0]['name']).replace(' '+aaaaa,'')}
|es   ={n(es, v[0]['name']).replace(' '+aaaaa,'')}
|es-la={n(esla, v[0]['name']).replace(' '+aaaaa,'')}
|fi   ={n(fi, v[0]['name']).replace(', '+aaaaa,'')}
|fr   ={n(fr, v[0]['name']).replace(' '+aaaaa,'')}
|it   ={n(it, v[0]['name']).replace(' - '+aaaaa,'')}
|ja   ={n(ja, v[0]['name']).replace('・'+aaaaa,'').replace(aaaaa,'')}
|ko   ={n(ko, v[0]['name']).replace(aaaaa+' ','')}
|nl   ={n(nl, v[0]['name']).replace('('+aaaaa+')','')}
|no   ={n(no, v[0]['name']).replace(' – '+aaaaa,'')}
|pl   ={n(pl, v[0]['name']).replace(' – '+aaaaa,'')}
|pt-br={n(ptbr,v[0]['name']).replace(' - '+aaaaa,'')}
|ru   ={n(ru, v[0]['name']).replace(' '+aaaaa,'')}
|sv   ={n(sv, v[0]['name']).replace(' '+aaaaa,'')}
|th   ={n(th, v[0]['name']).replace(' '+aaaaa,'')}
|tr   ={n(tr, v[0]['name']).replace(' - '+aaaaa,'')}
|zh-cn={n(zhcn, v[0]['name']).replace('（'+aaaaa+'）','')}
|zh-tw={n(zhtw, v[0]['name']).replace(aaaaa,'')}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BTD6 artifact nav}}}}
{{{{-stop-}}}}
""")
    #print(k)
    #print(v)

o.close()