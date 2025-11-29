import os

s = "maps.txt"

f = open(s, "r", encoding='utf-8')
lines = f.read().split("levelnum")

names = []
names2 = dict()

o = open("out_" + s, "w", encoding="utf-8")

for i in lines[1:]:
    if i[0] == "=":
        text = i[1:i.find('"')]

        for j in text.split("&"):
            #print(j)
            if "=" not in j:
                num = j
            else:
                before = j.split("=")[0]
                after = j.split("=")[1]
                if before == "title":
                    name = after
                    if name in names2:
                        names2[name] += 1
                    else:
                        names2[name] = 1

f.close()

br = "\n"

num = "?"
name = "?"
target = "?"
darts = "?"
creator = "?"
regular = 0
tack = 0
extra_dart = 0
bomb = 0
ice = 0
chomper = 0
boomer = 0
trip = 0
spike = 0
breakable = 0
solid = 0
rubber = 0
total = 0

def abbr(num):
    if str(num)[-1] == '1' and str(num) != "11": return 'st'
    elif str(num)[-1] == '2' and str(num) != "12": return 'nd'
    elif str(num)[-1] == '3' and str(num) != "13": return 'rd'
    else: return 'th'

ugh = set()

f = open(s, "r", encoding='utf-8')
lines = f.read().split("levelnum")

names = []

o = open("out_" + s, "w", encoding="utf-8")

for i in lines[1:]:
    if i[0] == "=":
        text = i[1:i.find('"')]
        #print(text)
        #print(text)
        regular = 0
        tack = 0
        extra_dart = 0
        bomb = 0
        ice = 0
        chomper = 0
        boomer = 0
        trip = 0
        spike = 0
        breakable = 0
        solid = 0
        rubber = 0
        angled_rubber = 0
        lightsabre = 0
        helium = 0
        total = 0

        #num = text[0]

        for j in text.split("&"):
            #print(j)
            if "=" not in j:
                num = j
            else:
                before = j.split("=")[0]
                after = j.split("=")[1]
                if before == "title":
                    name = after
                    namex = name
                    if names2[name] > 1: namex += " (level " + num + ")"
                    names.append(num + ". [[" + namex + ("|" if "(level" in namex else "") + "]]")
                elif before == "target": target = after
                elif before == "darts": darts = after
                elif before == "creator": creator = after
                else:
                    for k in after:
                        #print(k)
                        match k:
                            case '0': None
                            case '1':
                                regular += 1
                                total += 1
                            case '2':
                                tack += 1
                                total += 1
                            case '3':
                                extra_dart += 1
                                total += 1
                            case '4': None
                            case '5':
                                bomb += 1
                                total += 1
                            case '6':
                                ice += 1
                                total += 1
                            case '7':
                                chomper += 1
                                total += 1
                            case '8':
                                boomer += 1
                                total += 1
                            case '9':
                                trip += 1
                                total += 1
                            case 'a':
                                spike += 1
                                total += 1
                            case 'b':
                                lightsabre += 1
                                total += 1
                            case 'c':
                                helium += 1
                                total += 1

                            case 'j': breakable += 1
                            case 'k': solid += 1
                            case 'l': rubber += 1
                            case 'm' | 'n': angled_rubber += 1
                            case _:
                                print(num, k)
                                ugh.add(k)
        o.write(f"""{{{{-start-}}}}
'''{namex}'''{br + "{{DISPLAYTITLE:" + namex + "}}" if namex[0].islower() else ""}
{{{{bot generated}}}}
{{{{B1 level info
|name F   ={name}
|image F  =BIP {name}.png
|level PIP={num}
|darts F  ={darts}
|target F ={target}
|total F  ={total}
|creator  ={creator}

{("|bloon F=" + str(regular)) if regular != 0 else ""}{("|tack F=" + str(tack)) if tack != 0 else ""}{"|bonus dart F=" + str(extra_dart) if extra_dart > 0 else ""}{"|bomb F=" + str(bomb) if bomb > 0 else ""}{"|ice F=" + str(ice) if ice > 0 else ""}{"|chomper F=" + str(chomper) if chomper > 0 else ""}{"|boomerang F=" + str(boomer) if boomer > 0 else ""}{"|triple shot F=" + str(trip) if trip > 0 else ""}{"|spikey F=" + str(spike) if spike > 0 else ""}{"|light sabre F=" + str(lightsabre) if lightsabre > 0 else ""}{"|helium F=" + str(helium) if helium > 0 else ""}{"|breakable F=" + str(breakable) if breakable > 0 else ""}{"|solid F=" + str(solid) if solid > 0 else ""}{"|rubber F=" + str(rubber) if rubber > 0 else ""}{"|angled rubber F=" + str(angled_rubber) if angled_rubber > 0 else ""}
}}}}
'''{name}''' is the {num}{abbr(num)} level in ''[[Bloons Insanity Pack]]''.

==Solution==
{{{{empty}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BIP level nav}}}}
{{{{-stop-}}}}
""")

print(ugh)
print("{{*}}".join(names))