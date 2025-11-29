import xml.etree.ElementTree as ET
import json
import os
import struct

numread = 0

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ar = ET.parse('Arabic.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhcn = ET.parse('ChineseSimplified.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
zhtw = ET.parse('ChineseTraditional.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
esla = ET.parse('Spanish (LATAM).xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fi = ET.parse('Finnish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
nl = ET.parse('Dutch.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
pl = ET.parse('Polish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('Portuguese (Brazil).xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
th = ET.parse('Thai.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()

sm = open("TextAsset/sim_model.bytes", "rb")

els = dict()
numread = 0

def add_int_array():
    global numread

    length = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length):
        els[len(els)] = int.from_bytes(sm.read(4), 'little')
        numread += 4

    print(length, numread, len(els))
def add_nested_int_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            arr.append(int.from_bytes(sm.read(4), 'little', signed=True))
            numread += 4

        els[len(els)] = arr

    print(length_o, numread, len(els))
def add_nested_string_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            strlen = int.from_bytes(sm.read(2), 'big', signed=True)
            arr.append(sm.read(strlen).decode("utf-8"))

            numread += 2 + strlen

        els[len(els)] = arr

    print(length_o, numread, len(els))
class TargetType:
    def __init__(self, vars):
        self.id = vars[0]
        self.actionOnCreate = vars[1]
def add_tt_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            strlen = int.from_bytes(sm.read(1), 'big', signed=True)

            data = [sm.read(strlen).decode("utf-8"), int.from_bytes(sm.read(1), 'little', signed=True)]
            arr.append(TargetType(data))

            numread += 2 + strlen

        els[len(els)] = arr

    print(length_o, numread, len(els))
def add_nested_curve_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            arr2 = [struct.unpack('f',sm.read(4))[0], struct.unpack('f',sm.read(4))[0], struct.unpack('f',sm.read(4))[0]]
            arr.append(arr2)
            #sm.read(12)

            numread += 12

        els[len(els)] = arr

    print(length_o, numread, len(els))
def add_nested_assetref_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            strlen = int.from_bytes(sm.read(1), 'little', signed=True)
            arr.append(sm.read(strlen).decode("utf-8"))

            numread += 1 + strlen

        els[len(els)] = arr

    print(length_o, numread, len(els))
def add_nested_something_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            strlen = int.from_bytes(sm.read(1), 'little', signed=True)
            arr.append(sm.read(strlen).decode("utf-8"))
            sm.read(4)
            numread += 5 + strlen

        els[len(els)] = arr

    print(length_o, numread, len(els))
def add_nested_thing2_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):
            strlen = int.from_bytes(sm.read(2), 'big', signed=True)
            arr.append(sm.read(strlen).decode("utf-8"))
            arr.append(struct.unpack('f',sm.read(4))[0])
            numread += 6 + strlen

        els[len(els)] = arr
    print(length_o, numread, len(els))
def add_nested_int_pair_array():
    global numread

    length_o = int.from_bytes(sm.read(4), 'little')
    numread += 4

    for i in range(length_o):
        length_i = int.from_bytes(sm.read(4), 'little')
        numread += 4

        arr = []

        for j in range(length_i):

            arr.append([int.from_bytes(sm.read(4), 'little'), int.from_bytes(sm.read(4), 'little')])

            numread += 8

        els[len(els)] = arr

    print(length_o, numread, len(els))

sm.read(4)
els[0] = int.from_bytes(sm.read(4), 'little')
els[1] = int.from_bytes(sm.read(4), 'little')
els[2] = int.from_bytes(sm.read(4), 'little')
els[3] = int.from_bytes(sm.read(4), 'little')
els[4] = int.from_bytes(sm.read(4), 'little')

#sm.read(4)

numread += 24

add_nested_int_array()      # 7460 83916 7465
add_nested_int_array()      # 2245 101768 9710
add_int_array()             # 2232 110700 11942
add_int_array()             # 12116 159168 24058
add_int_array()             # 3962 175020 28020
add_int_array()             # 12323 224316 40343
add_int_array()             # 2146 232904 42489
add_nested_string_array()   # 4821 444088 47310

def add_model_array(cl, atts):
    global numread, mods
    models = []

    base = int.from_bytes(sm.read(4), 'little')
    amt = int.from_bytes(sm.read(4), "little")
    
    numread += 8
    

    parms = [[] for i in range(amt)]

    for i in atts:
        for j in range(amt):
            data = []
            for k in i:
                #print(j, numread, amt)
                match k:
                    case "string":
                        length = int.from_bytes(sm.read(1), "little")
                        numread += 1
                        
                        # if starts with 1, string is empty
                        if length == 1:
                            data.append("")
                        else:
                            length = int.from_bytes(sm.read(1), "little")
                            ret = sm.read(length)
                            if b'\x01' in ret:
                                data.append(ret.decode("utf-8") + (sm.read(1)).decode("utf-8"))
                                numread += 2 + length
                            elif b'\x02' in ret:
                                data.append(ret.decode("utf-8") + (sm.read(129)).decode("utf-8"))
                                numread += 130 + length
                            else:
                                data.append(ret.decode("utf-8"))
                                numread += 1 + length
                    
                    case "int[]" | "string[]" | "AreaType[]" | "List<string>" | "TowerSet[]":
                        data.append(els[int.from_bytes(sm.read(4), "little")])
                        numread += 4

                    case "PrefabReference" | "SpriteReference" | "AudioSourceReference":
                        length = int.from_bytes(sm.read(1), "little")
                        
                        data.append(sm.read(length))
                        numread += 1 + length

                    case "TargetType":
                        length = int.from_bytes(sm.read(1), "little")
                        data.append(sm.read(length).decode("utf-8"))
                        numread += 1 + length

                    case ("List<Model>" | "int" | "ApplyModModel[]" | "Model[]" | "TowerSet" | "FootprintModel" | "UpgradePathModel[]" | "TargetType[]" | "UpgradePathModel" | "TargetSupplierModel" | "WeaponModel[]"
                          | "EmissionModel" | 'ProjectileModel' | 'WeaponBehaviorModel[]' | 'EmissionBehaviorModel[]' | "FilterModel[]" | 'BloonProperties' | "SoundModel"):
                        data.append(int.from_bytes(sm.read(4), "little"))
                        #print(data[:-1])
                        numread += 4

                    case "Vector2":
                        data.append(struct.unpack('f',sm.read(4))[0])
                        numread += 4
                        data.append(struct.unpack('f',sm.read(4))[0])
                        numread += 4

                    case "Vector3":
                        data.append(struct.unpack('f',sm.read(4))[0])
                        numread += 4
                        data.append(struct.unpack('f',sm.read(4))[0])
                        numread += 4
                        data.append(struct.unpack('f',sm.read(4))[0])
                        numread += 4

                    case "float":
                        data.append(struct.unpack('f',sm.read(4))[0])
                        numread += 4

                    case "bool":
                        data.append(int.from_bytes(sm.read(1), "little"))
                        numread += 1

                    case _:
                        data.append(int.from_bytes(sm.read(4), "little"))
                        numread += 4

                #print(k, data[-1])
            #print(data)
            parms[j] += data

    #print()
    #print()
    #print()
    for i in parms:
        models.append(cl(i))

    print(f"{cl.__name__:<100} {base:<20} {amt:<20} {numread:<20}")
    return models


sm.read(11717666)

a = open('pywiki_BTD6_mk.txt', 'w', encoding='utf-8')

class KnowledgeModel:
        def __init__(self, vars):
            self.name = vars[0]
            self.childDependants = vars[1]
            self.idx = vars[2]
            self.category = vars[3]
            self.investmentRequired = vars[4]
            self.monkeyMoneyCost = vars[5]
            self.prerequisiteIds = vars[6]
            self.mod = vars[7]
knowledge = add_model_array(KnowledgeModel, [['string', 'List<Model>'], ['int', 'KnowledgeCategory', 'int', 'int', 'string[]', 'ModModel']])

for i in knowledge:

    nid1 = 0
    nid2 = 0
    did1 = 0
    did2 = 0

    def n(lang):
        return lang[0][nid1][nid2].text
    def d(lang):
        return lang[0][did1][did2].text
    
    for j in range(len(en[0])):
        for k in range(len(en[0][j])):
            #if 'id' in en[0][j][k].attrib: print(en[0][j][k].attrib)
            if 'id' in en[0][j][k].attrib and en[0][j][k].attrib['id'] == i.name:
                nid1 = j
                nid2 = k

            if 'id' in en[0][j][k].attrib and en[0][j][k].attrib['id'] == f"{i.name}Description":
                did1 = j
                did2 = k

    prereq = []

    for z in i.prerequisiteIds:
    
        for j in range(len(en[0])):
            for k in range(len(en[0][j])):
                #if 'id' in en[0][j][k].attrib: print(en[0][j][k].attrib)
                if 'id' in en[0][j][k].attrib and en[0][j][k].attrib['id'] == z:
                    prereq.append(en[0][j][k].text)

    prereq2 = ','.join(prereq)

    a.write(f'''{{{{-start-}}}}
\'\'\'{n(en)}\'\'\'
{{{{bot generated}}}}
{{{{BTD6 mk info
|id={i.name}

|name       ={n(en)}
|image      =BTD6 mk {i.name}Icon.png
|description={d(en)}

|introduced  =
|introduced C=

|category       ={"Primary" if i.category == 0 else "Military" if i.category == 1 else "Magic" if i.category == 2 else "Support" if i.category == 3 else "Heroes" if i.category == 4 else "Powers" if i.category == 5 else "???"}
|cost           ={i.monkeyMoneyCost}
|points required={i.investmentRequired}
|prerequisites  ={prereq2}
}}}}
\'\'\'{n(en)}\'\'\' is a {"[[Primary]]" if i.category == 0 else "[[Military]]" if i.category == 1 else "[[Magic]]" if i.category == 2 else "[[Support]]" if i.category == 3 else "[[Hero]]es" if i.category == 4 else "[[Power]]s" if i.category == 5 else "???"} [[Monkey Knowledge (BTD6)|Monkey Knowledge]] upgrade in ''[[Bloons TD 6]]''.

==In other languages==
{{{{BTD6 langs
|ar name          ={n(ar)}
|ar description   ={d(ar)}
|da name          ={n(da)}
|da description   ={d(da)}
|de name          ={n(de)}
|de description   ={d(de)}
|es name          ={n(es)}
|es description   ={d(es)}
|es-la name       ={n(esla)}
|es-la description={d(esla)}
|fi name          ={n(fi)}
|fi description   ={d(fi)}
|fr name          ={n(fr)}
|fr description   ={d(fr)}
|it name          ={n(it)}
|it description   ={d(it)}
|ja name          ={n(ja)}
|ja description   ={d(ja)}
|ko name          ={n(ko)}
|ko description   ={d(ko)}
|nl name          ={n(nl)}
|nl description   ={d(nl)}
|no name          ={n(no)}
|no description   ={d(no)}
|pl name          ={n(pl)}
|pl description   ={d(pl)}
|pt-br name       ={n(ptbr)}
|pt-br description={d(ptbr)}
|ru name          ={n(ru)}
|ru description   ={d(ru)}
|sv name          ={n(sv)}
|sv description   ={d(sv)}
|th name          ={n(th)}
|th description   ={d(th)}
|tr name          ={n(tr)}
|tr description   ={d(tr)}
|zh-cn name       ={n(zhcn)}
|zh-cn description={d(zhcn)}
|zh-tw name       ={n(zhtw)}
|zh-tw description={d(zhtw)}

|last updated=43.2
}}}}

==Navigation==
{{{{BTD6 mk nav}}}}
{{{{-stop-}}}}
''')



a.close()