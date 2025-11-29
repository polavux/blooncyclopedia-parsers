f = open("maps lite.txt", "r")
import math

o = open('pywiki_BLP_levels.txt', 'w')

def abbr(num):
    if str(num)[-1] == '1' and str(num) != "11": return 'st'
    elif str(num)[-1] == '2' and str(num) != "12": return 'nd'
    elif str(num)[-1] == '3' and str(num) != "13": return 'rd'
    else: return 'th'

names = []

for i in range(1, 26):

    azz = f.readline()
    print("_" + azz + "_")
    while azz == "\n": azz = f.readline()


    #f.readline()
    num = int(f.readline())
    name = f.readline().replace('\n', '')
    target = f.readline().replace('\n', '')
    darts = f.readline().replace('\n', '')

    names.append(str(num) + ". [[" + name + "]]")

    blons = 0
    day = math.floor((num - 1) / 3) + 1

    dic = dict()

    x = f.readline()
    #print(x)

    blones = ['1', '2', '3', '5', '6', '8', '9', 'a', 'b', 'c', 'x']
    bloks = ['j', 'k', 'l', 'm', 'n']
    other = ['0', '4', ' ', '\n']

    dic = {
        'bloon L': 0,
        'tack L': 0,
        'bonus dart L': 0,
        'bomb L': 0,
        'ice L': 0,
        'boomerang L': 0,
        'triple shot L': 0,
        'spikey L': 0,
        'light sabre L': 0,
        'helium L': 0,
        'chomper L': 0,

        'breakable L': 0,
        'solid L': 0,
        'rubber L' : 0,
        'angled rubber L': 0,
    }

    for i in x:
        match i:
            case '0': None
            case '1': dic['bloon L'] += 1
            case '2': dic['tack L'] += 1
            case '3': dic['bonus dart L'] += 1
            case '4': None
            case '5': dic['bomb L'] += 1
            case '6': dic['ice L'] += 1
            case '8': dic['boomerang L'] += 1
            case '9': dic['triple shot L'] += 1
            case 'a': dic['spikey L'] += 1
            case 'b': dic['light sabre L'] += 1
            case 'c': dic['helium L'] += 1
            case 'x': dic['chomper L'] += 1

            case 'j': dic['breakable L'] += 1
            case 'k': dic['solid L'] += 1
            case 'l': dic['rubber L'] += 1
            case 'm' | 'n': dic['angled rubber L'] += 1

            case ' ' | '\n': None
            case _: print('???', name, i)

        if i in blones: blons += 1

    print(num, name, dic)

    dic2 = []

    for k,v in dic.items():
        if v != 0: dic2.append(f'|{k}={v}')

    dic2 = ''.join(dic2)

    o.write(f'''{{{{-start-}}}}
\'\'\'{name}\'\'\'
{{{{bot generated}}}}
{{{{B1 level info
|name L ={name}
|image L=BL {name}.png

|level L ={num}
|darts L ={darts}
|target L={target}
|total L ={blons}

{dic2}
}}}}
\'\'\'{name}\'\'\' is the {num}{abbr(num)} level in ''[[Bloons (iOS)|Bloons Lite]]''.

==Solution==
{{{{empty}}}}
{{{{clear|right}}}}
==Navigation==
{{{{B1M level nav}}}}
{{{{-stop-}}}}
''')

o.close()
f.close()

print("{{*}}".join(names))