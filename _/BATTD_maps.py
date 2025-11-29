import xml.etree.ElementTree as ET
import json
import os

nn = '\n'

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
esla = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
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

s = [dict(), dict(), dict(), dict()]

for i in os.listdir():
    #print(i)
    if ".json" in i:
        f = json.load(open(i, "r", encoding="utf-8"))
        if f["m_Script"]["m_PathID"] == 2054827106835398978:
            for j in f["difficultyBounds"]:
                #if j["speedMultiplier"] != 1: s.append(f'{j["speedMultiplier"]} {j["difficulty"]} {i:<30}')
                if "m_Name" not in s[j['difficulty']]:
                    s[j['difficulty']][f["m_Name"]] = set()

                if j["speedMultiplier"] != 1.0:  s[j['difficulty']][f["m_Name"]].add('speed=' + str(j["speedMultiplier"]))

                for k in j["difficultyModifiers"]:
                    
                    #if k["regenSpeedMultiplier"] != 0: print(j["difficulty"], i)
                    #s.append(f'{i:<30} {j["difficulty"]:<5} {k["ghostMoabChance"]:<5} {k["startRound"]:<5} {k["endRound"]:<5}')
                    if k['fortifyRoundChance'] != 0: s[j['difficulty']][f["m_Name"]].add('fortified=y')
                    if k['camoRoundChance'] != 0: s[j['difficulty']][f["m_Name"]].add('camo=y')
                    if k['regenRoundChance'] != 0: s[j['difficulty']][f["m_Name"]].add('regrow=y')
                    if k['regenSpeedMultiplier'] != 0:s[j['difficulty']][f["m_Name"]].add('regrow speed=' + str(k['regenSpeedMultiplier']))
                    if k['promoteBloonsChance'] != 0: s[j['difficulty']][f["m_Name"]].add('promote=y')
                    if k['zombieBloonChance'] != 0: s[j['difficulty']][f["m_Name"]].add('zombie=y')
                    if k['ghostBloonChance'] != 0: s[j['difficulty']][f["m_Name"]].add('ghost=y')
                    if k['shieldBloonChance'] != 0: s[j['difficulty']][f["m_Name"]].add('shield=y')

for i in s: print(i)
    #return lang[0][6][2][itemtype][id].text


o = open("_pywiki_BATTD_maps.txt", "w", encoding="utf-8")


avsav = dict()


for i in os.listdir():
    if '.json' in i:
        f = json.load(open(i, "r", encoding="utf-8"))
        if f["m_Script"]["m_PathID"] == 3885764064146622363:
            zzzzz = 0
            for j in f["mapData"]:
                zzzzz += 1
                for k in os.listdir("rs"):
                    if k == str(j["roundSet"]["m_PathID"]) + ".json":
                        f2 = json.load(open("rs/" + k, "r", encoding="utf-8"))
                        
                        xxxx = j["mapPath"].split("/")[4].split(".")[0]
                        #print(xxxx)
                        def g(lang):
                            for i in lang[0]:
                                for j in i:
                                    if "id" in j.attrib and j.attrib["id"] == xxxx: return j.text

                                    
                        def dg(lang):
                            for i in lang[0]:
                                for j in i:
                                    if "id" in j.attrib and j.attrib["id"] == f["m_Name"] + "_Title": return j.text

                        easy = []
                        medium = []
                        hard = []
                        impop = []

                        for a in s[0][f2["m_Name"]]: easy.append('\n|easy ' + a)
                        if xxxx != "map_Bloons_TreeExterior":
                            for a in s[1][f2["m_Name"]]: medium.append('\n|medium ' + a)
                            for a in s[2][f2["m_Name"]]: hard.append('\n|hard ' + a)
                            for a in s[3][f2["m_Name"]]: impop.append('\n|impoppable ' + a)

                        if dg(en) not in avsav: avsav[dg(en)] = []
                        avsav[dg(en)].append("[[" + g(en) + "]]")
        

                        o.write(f'''{{{{-start-}}}}
\'\'\'{g(en)}\'\'\'
{{{{bot generated}}}}
{{{{BATTD map info
|id={f2["m_Name"]}

|name ={g(en)}
|image=BATTD thumb {f["m_Name"]} {f2["m_Name"]}.png
{''.join(easy)}{''.join(medium)}{''.join(hard)}{''.join(impop)}

|difficulty={j["difficultySkulls"]}
|entrances =
|exits     =
|junctions =
|water     =
}}}}
\'\'\'{g(en)}\'\'\' is the {zzzzz}{"st" if zzzzz == 1 else "nd" if zzzzz==2 else "rd" if zzzzz==3 else "th"} [[map]] of [[{dg(en)}]] in ''[[Bloons Adventure Time TD]]''.

==Layout==
{{{{empty}}}}

==In other languages==
{{{{BATTD langs
|da name   ={g(da)}
|de name   ={g(de)}
|es-la name={g(esla)}
|fr name   ={g(fr)}
|it name   ={g(it)}
|ja name   ={g(ja)}
|ko name   ={g(ko)}
|nl name   ={g(nl)}
|no name   ={g(no)}
|pt-br name={g(ptbr)}
|ru name   ={g(ru)}
|sv name   ={g(sv)}
|tr name   ={g(tr)}
}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BATTD adventure nav}}}}
{{{{-stop-}}}}
''')
                        
o.close()

for i, v in avsav.items(): print(f"![[{i}]]\n|{'{{*}}'.join(v)}\n|-")