import os, json


def replace_ids(fr, finder, finder2):
    out = fr
    xes = []

    x = 0
    while True:
        st = fr.find(finder, x)
        #print(st, fr)
        if st == -1: break

        st2 = fr.find(finder2, st+len(finder))
        ssub = fr[st+len(finder):st2]
        #print(ssub, finder, finder2)
        if "-" in ssub: xes.append(ssub)
        x = st2

    if x != 0:
        for i in xes:
            g = open("MonoBehaviour/"+i+".json", "r", encoding="utf-8")
            gd = g.read()

            if '\"Id\": \"' in gd: gd = replace_ids(gd, '\"Id\": \"', '\"')

            out = out.replace(i, gd.replace('"', '\\"'))

            g.close()

    return out



for i in os.listdir("MonoBehaviour"):
    if i[0].isalpha() and i[0].isupper():
        f = open("MonoBehaviour/"+i, "r", encoding="utf-8")
        fr = f.read()
        fd = json.loads(fr)
        f.close()
        if fd["m_Script"]["m_PathID"] == 8211594766679199408:
            print(i)
            out = replace_ids(fr, '\\"Id\\":\\"', '\\"')

            fo = open("out/"+i, "w", encoding="utf-8")
            fo.write(out)
            fo.close()

        f.close()