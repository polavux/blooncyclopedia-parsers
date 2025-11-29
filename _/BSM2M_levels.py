import json, os

from datetime import datetime

o = open('pywiki_BSM2M_levels.txt', "w", encoding="utf-8")

totalpops = [24289,36604,28987,26771,18636,43538,32963,35202,39389,21632,52524,41169,35816,34191,43803,32342,24616,16671,59278,52610,49973,31446,59787,73901,43833,55115,71312,44926,69707,93188,63375,24725,31090,34658,31803,45125,37642,26299,32980,44478,55602,43859,28073,24837,35345,20928,36732,38269,42348,17064]

m = json.load(open("levels.json", "r"))

for i in os.listdir("hh"):
    x = open(f"hh/{i}", "r", encoding="utf-8")
    f = json.load(x)

    reg = []
    shield = []
    phase = []
    shield_phase = []

    for j in f["nodes"]:
        if 'bloon' in j:
            if "bloon_flag_array" in j:
                if "shield" in j["bloon_flag_array"] and "phase" in j["bloon_flag_array"] and j['bloon'] not in shield_phase: shield_phase.append(j['bloon'])
                elif "shield" in j["bloon_flag_array"] and j['bloon'] not in shield: shield.append(j['bloon'])
                elif "phase" in j["bloon_flag_array"] and j['bloon'] not in phase: phase.append(j['bloon'])
                elif j['bloon'] not in reg: reg.append(j['bloon'])
            elif j['bloon'] not in reg: reg.append(j['bloon'])


    for j in f["spawners"]:
        if 'spawn' in j:
            if "bloon_flag_array" in j:
                if "shield" in j["bloon_flag_array"] and "phase" in j["bloon_flag_array"] and j['spawn'] not in shield_phase: shield_phase.append(j['spawn'])
                elif "shield" in j["bloon_flag_array"] and j['spawn'] not in shield: shield.append(j['spawn'])
                elif "phase" in j["bloon_flag_array"] and j['spawn'] not in phase: phase.append(j['spawn'])
                elif j['spawn'] not in reg: reg.append(j['spawn'])
            elif j['spawn'] not in reg: reg.append(j['spawn'])

    for k in reg:
        if 'bfb' in k: print(i, k)

    levelnum = int(i[:-5]) + 50
    clevelnum = (levelnum - 50 if levelnum < 56 else levelnum - 55 if levelnum < 61 else levelnum - 60 if levelnum < 69 else levelnum - 68 if levelnum < 76 else levelnum - 75 if levelnum < 83 else levelnum-82 if levelnum < 89 else levelnum-88 if levelnum<95 else levelnum-94)

    uh = ''
    print(i, reg, phase, shield)

    for k in m["worlds"][1]["medal_gates"]:
        if k["level_index"] == levelnum - 26:
            uh = f' This level requires {k["req_gold"]} [[Medal (BSM series)|gold medal]]s to unlock.'

    uh2 = ''
    for k in reg:
        if 'ghost' in k: uh2 = ' The boss of this level is the [[Ghost]].'
        if 'radadactyl' in k: uh2 = ' The boss of this level is the [[Radadactyl (boss)|Radadactyl]].'
        if 'dreadbloon' in k: uh2 = ' The boss of this level is [[Dreadbloon (BSM2)|Dreadbloon]].'
        if 'zomg' in k: uh2 = ' The boss of this level is the [[ZOMG (BSM2)|ZOMG]].'
        if 'tutankhabloon' in k: uh2 = ' The boss of this level is [[Tutankhabloon]].'
        if 'bloonarius' in k: uh2 = ' The boss of this level is [[Bloonarius (BSM2)|Bloonarius]].'
        if 'blastapopoulos' in k: uh2 = ' The boss of this level is [[Blastapopoulos (BSM2)|Blastapopoulos]].'

    if "timestamp" in f: print((datetime.utcfromtimestamp((f["timestamp"]) / 1000.0)).strftime('%Y-%m-%dT%H:%M:%SZ'))

    if "total_blops" not in f: print(i)

    o.write(f'''{{{{-start-}}}}
\'\'\'Level {levelnum} (BSM2 mobile)\'\'\'
{{{{bot generated}}}}
{{{{BSM2M level info
|number ={levelnum}
|world  =[[Helium Heights]]
|chapter={'Feeling the Heat' if levelnum < 56 else 'Bump in the Night' if levelnum < 61 else 'Fossil Hunting' if levelnum < 69 else 'Digging Deep' if levelnum < 76 else "Getting Scrappy" if levelnum < 83 else "Pyramid Popping" if levelnum < 89 else "Prison Break" if levelnum < 95 else "Fires of Mount Bloon"} 

|bronze ={int(round((totalpops[levelnum-51]*f["rbe_targets"][0]) / 100.0)*100)}
|silver ={int(round((totalpops[levelnum-51]*f["rbe_targets"][1]) / 100.0)*100)}
|gold   ={int(round((totalpops[levelnum-51]*f["rbe_targets"][2]) / 100.0)*100)}
|diamond={totalpops[levelnum-51]}
|blops  ={f["total_blops"] if "total_rbe" in f else ''}

|regular     ={','.join(reg)}
|shield      ={','.join(shield)}
|phase       ={','.join(phase)}
|shield phase={','.join(shield_phase)}
}}}}
\'\'\'Level {levelnum}\'\'\' is the {'first' if clevelnum == 1 else 'second' if clevelnum == 2 else 'third' if clevelnum == 3 else 'fourth' if clevelnum == 4 else 'fifth' if clevelnum == 5 else 'sixth' if clevelnum == 6 else 'seventh' if clevelnum == 7 else 'eighth'} level of {'"Feeling the Heat"' if levelnum < 56 else '"Bump in the Night"' if levelnum < 61 else '"Fossil Hunting"' if levelnum < 69 else '"Digging Deep"' if levelnum < 76 else '"Getting Scrappy"' if levelnum < 83 else '"Pyramid Popping"' if levelnum < 89 else '"Prison Break"' if levelnum < 95 else '"Fires of Mount Bloon"'} in the {{{{mobile version of|Bloons Supermonkey 2}}}}.{uh}{uh2}

==Layout==
{{{{empty}}}}

==Golden Bloon and Mystery Bloon locations==
{{{{empty}}}}

==Strategy==
===First time===
{{{{strategy needed}}}}

===Diamond medal===
{{{{strategy needed}}}}

==Navigation==
{{{{BSM2M level nav}}}}
{{{{-stop-}}}}
''')

o.close()