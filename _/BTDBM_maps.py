import xml.etree.ElementTree as ET
import json
import os
import math

nl = '\n'

o = open("pywiki_BTDBM_maps.txt", "w", encoding="utf-8")
    
tl = open("tracklist.json", "r", encoding="utf-8")
dtl = json.load(tl)

skip = ["circuit_board"]
#skip = []

pathsl = dict()
pathsr = dict()

sendl = dict()
sendr = dict()

for j in os.listdir("LevelDefinitions"):
    p = open(f"LevelDefinitions/{j}/{j}_left.path", "r", encoding="utf-8")
    pd = json.load(p)

    paths = []

    for k in pd["Nodes"]:
        paths.append(0)
        xl = k["Points"][0][0]
        yl = k["Points"][0][1]
        for m in k["Points"]:
            paths[-1] += math.sqrt(((m[0] - xl) ** 2) + (((m[1] - yl) ** 2)))
            xl = m[0]
            yl = m[1]

    pathsl[j] = paths

    p.close()
    
    p = open(f"LevelDefinitions/{j}/{j}_left.map", "r", encoding="utf-8")
    pd = json.load(p)

    sendl[j] = pd["BloonSendPath"]

    p.close()

for j in os.listdir("LevelDefinitions"):
    p = open(f"LevelDefinitions/{j}/{j}_right.path", "r", encoding="utf-8")
    pd = json.load(p)

    paths = []

    for k in pd["Nodes"]:
        paths.append(0)
        xl = k["Points"][0][0]
        yl = k["Points"][0][1]
        for m in k["Points"]:
            paths[-1] += math.sqrt(((m[0] - xl) ** 2) + (((m[1] - yl) ** 2)))
            xl = m[0]
            yl = m[1]

    pathsr[j] = paths

    p.close()
    
    p = open(f"LevelDefinitions/{j}/{j}_right.map", "r", encoding="utf-8")
    pd = json.load(p)

    sendr[j] = pd["BloonSendPath"]

    p.close()

for i in dtl["Tracks"]:
    if i[1] in skip:
        lens = []
        labels = []
        if len(pathsl[i[1]]) > 1:
            for j in range(len(pathsl[i[1]])):
                
                if round(pathsl[i[1]][j],2) != round(pathsr[i[1]][j],2):
                    lens.append(str(round(pathsl[i[1]][j],2)))
                    labels.append('Left ' + ('send' if sendl[i[1]] == j else 'natural'))
                    lens.append(str(round(pathsr[i[1]][j],2)))
                    labels.append('Right ' + ('send' if sendr[i[1]] == j else 'natural'))
                else:
                    lens.append(str(round(pathsl[i[1]][j],2)))
                    labels.append('Send' if sendr[i[1]] == j else 'Natural')

        else:
            if round(pathsl[i[1]][0],2) != round(pathsr[i[1]][0],2):
                lens.append(str(round(pathsl[i[1]][0],2)))
                labels.append('Left')
                lens.append(str(round(pathsr[i[1]][0],2)))
                labels.append('Right')
            else:
                lens.append(str(round(pathsl[i[1]][0],2)))



        o.write(f'''{{{{-start-}}}}
\'\'\'{i[2]}\'\'\'
{{{{stub}}}}
{{{{BTDB map info
|id F=
|id M={i[1]}

|name F ={i[2]}
|name M ={i[2]}
|image F=BTDBF {i[2]}.png
|image M=BTDBM {i[1]} thumb.png

|availability=All [[Arena]]s
|introduced F=
|introduced M=

|symmetry =Lateral
|entrances={'2 (1 natural / 1 send)' if len(labels) > 1 else '1'}
|exits    ={'2 (1 natural / 1 send)' if len(labels) > 1 else '1'}
|junctions=0
|tunnels  =0
|water    ={"Yes" if i[5] else "No"}

|path labels   ={','.join(labels)}
|path lengths F=
|path lengths M={','.join(lens)}
}}}}
\'\'\'{i[2]}\'\'\' is a [[map]] in ''[[Bloons TD Battles]]''.

==Layout==
{{{{empty}}}}

==Strategy==
{{{{strategy needed}}}}
{{{{clear|right}}}}
==Navigation==
{{{{BTDBF map nav}}}}
{{{{BTDBM map nav}}}}
{{{{-stop-}}}}
''')

o.close()
tl.close()