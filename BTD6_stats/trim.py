import json
from trim_common import *
from trim_tower import *

tower = 'Sauda'
tower2 = ''
last_updated = '51.0'

# p = paragon
# h = hero
# s = single
# s2 = single with tower2
# any = tower
mode="h"

def mkdif(a, b):
    difs = dict()
    order = []

    for k, v in b.items():
        if k not in a:
            difs[k] = v

        elif k == '_order':
            None

        elif type(v) == dict:
            sub = mkdif(a[k], b[k])
            if sub != {}: difs[k] = sub

        elif a[k] != v:
            difs[k] = v

    for k, v in a.items():
        if k not in b and type(v) == bool:
            difs[k] = not v

    if "_order" in b:
        for i in b["_order"]:
            if i in difs:
                order.append(i)

    difs2 = {}

    if order != []:
        difs2["_order"] = order

    difs2.update(difs)

    return difs2

def single_tower(model):
    l = {"subtowers": {}}
    parse_tow(l, model)
    if len(l['subtowers']) > 2:
        l2 = l["subtowers"][model["name"]]
        del l["subtowers"][model["name"]]
        if 'subtowers' not in l2: l2['subtowers'] = dict()
        l2['subtowers'].update(l["subtowers"])
        l2['subtowers']['_order'].remove(model["name"])
        return l2
    else:
        return l["subtowers"][model["name"]]

chart = {
    "-100": [["-110"], ["-101"]],
    "-010": [["-110"], ["-011"]],
    "-001": [["-101"], ["-011"]],
    "-200": [["-210", "-220"], ["-201", "-202"]],
    "-020": [["-120", "-220"], ["-021", "-022"]],
    "-002": [["-102", "-202"], ["-012", "-022"]],
    "-300": [["-310", "-320"], ["-301", "-302"]],
    "-400": [["-410", "-420"], ["-401", "-402"]],
    "-500": [["-510", "-520"], ["-501", "-502"]],
    "-030": [["-130", "-230"], ["-031", "-032"]],
    "-040": [["-140", "-240"], ["-041", "-042"]],
    "-050": [["-150", "-250"], ["-051", "-052"]],
    "-003": [["-103", "-203"], ["-013", "-023"]],
    "-004": [["-104", "-204"], ["-014", "-024"]],
    "-005": [["-105", "-205"], ["-015", "-025"]],
}




if mode =="s" or mode =="p":
    mdl = open(f'TowerModels/{tower}/{tower}-Paragon.json', 'r', encoding='utf-8') if mode == "p" else open(f'TowerModels/{tower}/{tower}.json', 'r', encoding='utf-8')
    tow = single_tower(json.load(mdl))
    tow['_last_updated'] = last_updated

    o = open(f'Trims/{tower}/{tower}-Paragon.json', 'w', encoding='utf-8') if mode == "p" else open(f'Trims/{tower}/{tower}.json', 'w', encoding='utf-8')
    json.dump(tow, o, indent=4)
    o.close()


if mode =="s2":
    mdl = open(f'TowerModels/{tower}/{tower2}.json', 'r', encoding='utf-8')
    tow = single_tower(json.load(mdl))
    tow['_last_updated'] = last_updated

    o = open(f'Trims/{tower}/{tower2}.json', 'w', encoding='utf-8')
    json.dump(tow, o, indent=4)
    o.close()

elif mode=="h":
    for i in ['', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20']:

        mdl = open(f'TowerModels/{tower}/{tower}{i}.json', 'r', encoding='utf-8')
        tow = single_tower(json.load(mdl))

        o = open(f"Trims/{tower}/{tower}{i}.json", "w", encoding='utf-8')
        json.dump(tow, o, indent=4)
        o.close()

    o = open(f"Trims/{tower}/{tower}.json", "r", encoding='utf-8')
    f = json.load(o)
    o.close()

    out = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')

    prev = f

    for i in [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20']:
        mdl = open(f'Trims/{tower}/{tower}{i}.json', 'r', encoding='utf-8')
        io = json.load(mdl)

        f["_"+i[1:]] = mkdif(prev, io)

        prev = io

        mdl.close()
        
    f['_last_updated'] = last_updated

    o = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')
    json.dump(f, o, indent=4)
    o.close()

else:
    for i in ["", "-100", "-200", "-300", "-400", "-500",
              "-010", "-020", "-030", "-040", "-050",
              "-001", "-002", "-003", "-004", "-005",
              '-110', '-101', '-011',
              '-210', '-201', '-120',
              '-021', '-102', '-012',
              '-220', '-202', '-022',
              '-310', '-320', '-301', '-302',
              '-130', '-230', '-031', '-032',
              '-103', '-203', '-013', '-023',
              '-410', '-420', '-401', '-402',
              '-140', '-240', '-041', '-042',
              '-104', '-204', '-014', '-024',
              '-510', '-520', '-501', '-502',
              '-150', '-250', '-051', '-052',
              '-105', '-205', '-015', '-025']:

        mdl = open(f'TowerModels/{tower}/{tower}{i}.json', 'r', encoding='utf-8')
        tow = single_tower(json.load(mdl))

        o = open(f"Trims/{tower}/{tower}{i}.json", "w", encoding='utf-8')
        json.dump(tow, o, indent=4)
        o.close()
    
    o = open(f"Trims/{tower}/{tower}.json", "r", encoding='utf-8')
    f = {"_000": json.load(o)}
    o.close()

    out = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')

    

    for i in [["-100", "-200", "-300", "-400", "-500"], ["-010", "-020", "-030", "-040", "-050"], ["-001", "-002", "-003", "-004", "-005"]]:
        prev = f
        for j in i:
            mdl = open(f'Trims/{tower}/{tower}{j}.json', 'r', encoding='utf-8')
            io = json.load(mdl)

            f["_" + j[1:]] = io

            prev = io

            mdl.close()


    if tower != "BeastHandler":
        for i in [["-100", "-200", "-300", "-400", "-500"], ["-010", "-020", "-030", "-040", "-050"], ["-001", "-002", "-003", "-004", "-005"]]:
            for j in i:
                for k in chart[j]:
                    prev = f["_" + j[1:]]
                    for l in k:
                        cpmdl = open(f'Trims/{tower}/{tower}{l}.json', 'r', encoding='utf-8')
                        io = json.load(cpmdl)

                        f["_" + j[1:]]["_" + l[1:]] = mkdif(prev, io)

                        prev = io

                        cpmdl.close()

    f['_last_updated'] = last_updated

    o = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')
    output = json.dumps(f, indent=4)
    o.write(output)
    o.close()



"""

eggs = {
    "-100": [["-110", "-120", "-130", "-140", "-150"], ["-101", "-102", "-103", "-104", "-105"]],
    "-010": [["-110", "-210", "-310", "-410", "-510"], ["-011", "-012", "-013", "-014", "-015"]],
    "-001": [["-101", "-201", "-301", "-401", "-501"], ["-011", "-021", "-031", "-041", "-051"]],
    "-200": [["-210", "-220", "-230", "-240", "-250"], ["-201", "-202", "-203", "-204", "-205"]],
    "-020": [["-120", "-220", "-320", "-420", "-520"], ["-021", "-022", "-023", "-024", "-025"]],
    "-002": [["-102", "-202", "-302", "-402", "-502"], ["-012", "-022", "-032", "-042", "-052"]],
}

eggs3 = {
    "-100": [["-010", "-020", "-030", "-040", "-050"], ["-001", "-002", "-003", "-004", "-005"]],
    "-010": [["-100", "-200", "-300", "-400", "-500"], ["-001", "-002", "-003", "-004", "-005"]],
    "-001": [["-100", "-200", "-300", "-400", "-500"], ["-010", "-020", "-030", "-040", "-050"]],
    "-200": [["-010", "-020", "-030", "-040", "-050"], ["-001", "-002", "-003", "-004", "-005"]],
    "-020": [["-100", "-200", "-300", "-400", "-500"], ["-001", "-002", "-003", "-004", "-005"]],
    "-002": [["-100", "-200", "-300", "-400", "-500"], ["-010", "-020", "-030", "-040", "-050"]],
}

eggs2 = {
    "-300": [["-310", "-320"], ["-301", "-302"]],
    "-400": [["-410", "-420"], ["-401", "-402"]],
    "-500": [["-510", "-520"], ["-501", "-502"]],
    "-030": [["-130", "-230"], ["-031", "-032"]],
    "-040": [["-140", "-240"], ["-041", "-042"]],
    "-050": [["-150", "-250"], ["-051", "-052"]],
    "-003": [["-103", "-203"], ["-013", "-023"]],
    "-004": [["-104", "-204"], ["-014", "-024"]],
    "-005": [["-105", "-205"], ["-015", "-025"]],
}

if paragon:
    mdl = open(f'TowerModels/{tower}/{tower}-Paragon.json', 'r', encoding='utf-8') if tower != 'BattleCat' else open(f'TowerModels/{tower}/{tower}.json', 'r', encoding='utf-8')
    tow = parse_tow(json.load(mdl))
    tow['subtowers'].update(subtowers)
    tow['_last_updated'] = lup

    o = open(f"Trims/{tower}/{tower}-Paragon.json", "w", encoding='utf-8')
    output = json.dumps(tow, indent=4)
    o.write(output.replace(" Weapon", ""))
    o.close()

elif not hero:
    for i in ["", "-100", "-200", "-300", "-400", "-500",
              "-010", "-020", "-030", "-040", "-050",
              "-001", "-002", "-003", "-004", "-005",
              '-110', '-101', '-011',
              '-210', '-201', '-120',
              '-021', '-102', '-012',
              '-220', '-202', '-022',
              '-310', '-320', '-301', '-302',
              '-130', '-230', '-031', '-032',
              '-103', '-203', '-013', '-023',
              '-410', '-420', '-401', '-402',
              '-140', '-240', '-041', '-042',
              '-104', '-204', '-014', '-024',
              '-510', '-520', '-501', '-502',
              '-150', '-250', '-051', '-052',
              '-105', '-205', '-015', '-025']:

        mdl = open(f'TowerModels/{tower}/{tower}{i}.json', 'r', encoding='utf-8')
        tow = parse_tow(json.load(mdl))
        tow['subtowers'].update(subtowers)
        
        subtowers = dict()

        o = open(f"Trims/{tower}/{tower}{i}.json", "w", encoding='utf-8')
        output = json.dumps(tow, indent=4)
        o.write(output.replace(" Weapon", ""))
        o.close()



    o = open(f"Trims/{tower}/{tower}.json", "r", encoding='utf-8')
    f = {"_000": json.load(o)}
    o.close()

    out = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')

    for i in [["-100", "-200", "-300", "-400", "-500"], ["-010", "-020", "-030", "-040", "-050"], ["-001", "-002", "-003", "-004", "-005"]]:
        prev = f
        for j in i:
            mdl = open(f'Trims/{tower}/{tower}{j}.json', 'r', encoding='utf-8')
            io = json.load(mdl)

            f[j] = io

            prev = io

            mdl.close()

    for i in [["-100", "-200"], ["-010", "-020"], ["-001", "-002"]]:
        for j in i:
            for a,k in enumerate(eggs[j]):
                prev = f[j]
                for b,l in enumerate(k):
                    cpmdl = open(f'Trims/{tower}/{tower}{l}.json', 'r', encoding='utf-8')
                    io = json.load(cpmdl)
                    zcpmdl = open(f'Trims/{tower}/{tower}{eggs3[j][a][b]}.json', 'r', encoding='utf-8')
                    zio = json.load(zcpmdl)
                    z = mkdif(zio, io)

                    #print(l, eggs3[j][a][b],z)

                    #if mkdif(prev, z):
                        #f[j][l] = mkdif(prev, z)

                    prev = io

                    cpmdl.close()

    for i in [["-300", "-400", "-500"], ["-030", "-040", "-050"], ["-003", "-004", "-005"]]:
        for j in i:
            for k in eggs2[j]:
                prev = f[j]
                for l in k:
                    cpmdl = open(f'Trims/{tower}/{tower}{l}.json', 'r', encoding='utf-8')
                    io = json.load(cpmdl)

                    f[j][l] = mkdif(prev, io)

                    prev = io

                    cpmdl.close()
            '''
            for k in range(len(o2[i[j]])):
                for l in range(len(o2[i[j]][k])):
                    print(j, i[j], o2[i[j]][k][l],o3[i[j]][k][l])
                    # crosspath model
                    cpmdl = open(f'Trims/{tower}/{tower}{o2[i[j]][k][l]}.json', 'r', encoding='utf-8')
                    cpio = json.load(cpmdl)


                    # same path model
                    spmdl = open(f'Trims/{tower}/{tower}{i[j]}.json', 'r', encoding='utf-8')
                    spio = json.load(spmdl)

                    # find differences between 500 and 510
                    g = mkdif(spio, cpio)

                    # find differences between that and 010
                    h = mkdif(f[o3[i[j]][k][l]], g)

                    f[o2[i[j]][k][l]] = h


                    spmdl.close()
                    cpmdl.close()'''

    f['_last_updated'] = lup

    o = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')
    output = json.dumps(f, indent=4)
    output = output.replace(" Weapon", "")
    o.write(output)
    o.close()











else:
    for i in ['', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20']:

        mdl = open(f'TowerModels/{tower}/{tower}{i}.json', 'r', encoding='utf-8')
        tow = parse_tow(json.load(mdl))
        tow['subtowers'].update(subtowers)
        
        subtowers = dict()

        o = open(f"Trims/{tower}/{tower}{i}.json", "w", encoding='utf-8')
        output = json.dumps(tow, indent=4)
        o.write(output.replace(" Weapon", ""))
        o.close()

    o = open(f"Trims/{tower}/{tower}.json", "r", encoding='utf-8')
    f = json.load(o)
    o.close()

    out = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')

    prev = f

    for i in [' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20']:
        mdl = open(f'Trims/{tower}/{tower}{i}.json', 'r', encoding='utf-8')
        io = json.load(mdl)

        f["_"+i[1:]] = mkdif(prev, io)

        prev = io

        mdl.close()
        
    f['_last_updated'] = lup

    o = open(f"Trims/{tower}/{tower}_C.json", "w", encoding='utf-8')
    json.dump(f, o, indent=4)
    o.close()"""