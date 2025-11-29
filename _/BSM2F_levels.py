import zlib, base64, os

threshs = {
    "MonkeyLane1": [600,1500,2000,2380],
    "MonkeyLane2": [800,1500,2000,2208],
    "MonkeyLane3": [1500,4500,7500,7763],
    "MonkeyLane4": [1800,4000,5400,5846],
    "MonkeyLane5": [3000,7200,14200,14842],
    "BloonDunes1": [4500,8400,12900,13857],
    "BloonDunes2": [6000,11000,15200,16148],
    "BloonDunes3": [6100,15500,24900,25846],
    "BloonDunes4": [13000,19200,28800,29742],
    "BloonDunes5": [10000,18400,35000,35997],
    "DeepBloonSea1": [10000,18000,23900,34845],
    "DeepBloonSea2": [11500,32500,41900,42925],
    "DeepBloonSea3": [13000,36500,57400,58335],
    "DeepBloonSea4": [15000,32500,41000,43126],
    "DeepBloonSea5": [20000,50000,83900,84956],
    "MountMagma1": [15000,26000,30600,31192],
    "MountMagma2": [20000,33000,38800,39243],
    "MountMagma3": [26000,38000,44100,44734],
    "MountMagma4": [16000,22000,27500,28072],
    "MountMagma5": [15000,47000,59400,59981],
    "Altitude1": [700,1200,1500,2000],
    "Altitude2": [700,1200,1500,2000],
    "Altitude3": [700,1200,1500,2000],
    "Altitude4": [700,1200,1500,2000],
    "Altitude5": [700,1200,1500,2000]
}

blones = {
    0: "red",
	1: "blue",
    2: "green",
    3: "yellow",
    4: "pink",
    5: "black",
    6: "white",
    7: "lead",
    8: "zebra",
    9: "rainbow",
    10: "ceramic",
    11: "tack",
    12: "glass",
    13: "bomb",
    14: "gold",
    15: "ufo",
    16: "coco",
    17: "moab",
    18: "minimoab",
    19: "bfb",
    20: "powerup",
    21: "superufo",
    22: "squid",
    23: "robo",
    
    30: "sred",
	31: "sblue",
    32: "sgreen",
    33: "syellow",
    34: "spink",
    35: "sblack",
    36: "swhite",
    37: "slead",
    38: "szebra",
    39: "srainbow",
    40: "sceramic",
    41: "stack",
    42: "sglass",
    43: "sbomb",
    44: "sgold",
    45: "sufo",
    46: "scoco",
    47: "smoab",
    48: "sminimoab",
    49: "sbfb",
    50: "spowerup",
    51: "ssuperufo",
    52: "ssquid",
    53: "srobo",
}



behavs = []
behavs2 = []

f = open("MonkeyLane1.txt", "rb")
v = (zlib.decompress(base64.b64decode(f.read()))).decode()
#print(v)
zz = open("output_for_science.txt", "w")
zz.write(v)
zz.close
#print(v)
for j in v.split("\n"):
            for k in j.split("|"):
                for l in k.split(","):
                    if "::" in l and l not in behavs:
                        behavs.append(l)
                        behavs2.append(k)
behavs2.sort()
#print(behavs2)

blons_reg = set()
blons_phase = set()

for j in v.split("\n"):
    to_add = []
    to_add_phase = []
    for k in j.split("|"):
        pars = k.split(",")
        if len(pars) > 2:
            match pars[1]:
                case "behaviours::AddBloon":
                    #print(k)
                    to_add.append(int(pars[4]))
                case "behaviours::CreateCircle":
                    #print(k)
                    if pars[3] != "0": to_add.append(int(pars[4]))
                case "behaviours::CreateRing":
                    #print(k)
                    to_add.append(int(pars[2]))
                case "behaviours::CreateBlock":
                    #print(k)
                    if pars[2] != "0" and pars[3] != "0": to_add.append(int(pars[6]))
                case "behaviours::SetTypeByBand":
                    for m in pars[6:]:
                        to_add.append(int(m))
                case "behaviours::SetTypeBySector":
                    for m in pars[5:]:
                        to_add.append(int(m))
                case "behaviours::AddShields":
                    for m in range(len(to_add)):
                        if to_add[m] < 30 and to_add[m] > -1: to_add[m] += 30
                case "behaviours::RadialPhase" | "behaviours::FadeOut":
                    to_add_phase += to_add
                    to_add = []
                case _:
                    to_add.append(-1)
            

    for k in to_add:
        if k in blones: blons_reg.add(k)
    for k in to_add_phase:
        if k in blones: blons_phase.add(k)

blons_reg2 = set()
for i in blons_reg: blons_reg2.add(blones[i])
print(blons_reg2)
print(blons_phase)

bees = []
bees2 = []

for i in os.listdir():
    break
    if 'txt' in i:
        f = open(i, "rb")
        v = (zlib.decompress(base64.b64decode(f.read()))).decode()

        print(i)
        print(threshs[i[:-4]])

        for j in v.split("\n"):
            for k in j.split("|"):
                for l in k.split(","):
                    if "behaviours::" in l and l not in bees:
                        l2 = l.replace("behaviours::", "")
                        bees.append(l)
                        bees2.append(l2)

        f.close()
        #break
                
#bees2.sort()
#print(bees2)

# ['AddBloon', 'AddShields', 'BossBehaviourW2', 'BossBehaviourW3', 'BossBehaviourW4', 'CreateBlock', 'CreateCircle', 'CreateFromBitmap', 'CreateRing', 'CreateTrain', 'EndChild', 'EnterBySector',
# 'ExitBySector', 'FadeOut', 'Fall', 'FollowBezier', 'FollowPath', 'Geostatic', 'MoabBossBehaviour', 'MoveAtVelocity', 'Offset', 'OscillateOnX', 'OscillateOnY', 'Pulse', 'PulseRotate', 'RadialPhase',
# 'RemoveAtAge', 'RemoveAtBottom', 'RemoveIfGreaterThanX', 'Rock', 'Rotate', 'RotateAroundPoint', 'RotateWithVelocity', 'Scale', 'ScaleOnX', 'ScaleOnY', 'SetPosition', 'SetTypeByBand', 'SetTypeBySector',
# 'SmoothMove', 'StartChild', 'TiltWithX', 'Wave', 'Wobble']