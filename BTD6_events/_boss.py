import json, os

out = open("result.txt", "w", encoding="utf-8")

def str2(value):
    if value == None: return ""
    ret = str(value)
    if ret == "True": return "1"
    elif ret == "False": return ""
    return ret

rd = dict()
startdates = []
startdate_to_rd = dict()

towerkeys = ["ChosenPrimaryHero", "Quincy", "Gwendolin", "StrikerJones", "ObynGreenfoot", "CaptainChurchill", "Benjamin", "Ezili", "PatFusty",
            "Adora", "AdmiralBrickell", "Etienne", "Sauda", "Psi", "Geraldo", "Corvus", "Rosalia", "Silas",
            "DartMonkey", "BoomerangMonkey", "BombShooter", "TackShooter", "IceMonkey", "GlueGunner", "Desperado",
            "SniperMonkey", "MonkeySub", "MonkeyBuccaneer", "MonkeyAce", "HeliPilot", "MortarMonkey", "DartlingGunner",
            "WizardMonkey", "SuperMonkey", "NinjaMonkey", "Alchemist", "Druid", "Mermonkey",
            "BananaFarm", "SpikeFactory", "MonkeyVillage", "EngineerMonkey", "BeastHandler"]

mapkeys = {
   "#ouch": "#Ouch",
   "AdorasTemple": "Adora's Temple",
   "AlpineRun": "Alpine Run",
   "AncientPortal": "Ancient Portal",
   "AnotherBrick": "Another Brick",
   "Balance": "Balance",
   "Bazaar": "Bazaar",
   "Blons": "Blons",
   "BloodyPuddles": "Bloody Puddles",
   "BloonariusPrime": "Bloonarius Prime",
   "CandyFalls": "Candy Falls",
   "Cargo": "Cargo",
   "Carved": "Carved",
   "CastleRevenge": "Castle Revenge",
   "Chutes": "Chutes",
   "Cornfield": "Cornfield",
   "CoveredGarden": "Covered Garden",
   "Cracked": "Cracked",
   "Cubism": "Cubism",
   "DarkCastle": "Dark Castle",
   "DarkDungeons": "Dark Dungeons",
   "DarkPath": "Dark Path",
   "Downstream": "Downstream",
   "EnchantedGlade": "Enchanted Glade",
   "Encrypted": "Encrypted",
   "EndOfTheRoad": "End Of The Road",
   "Erosion": "Erosion",
   "FiringRange": "Firing Range",
   "FloodedValley": "Flooded Valley",
   "FourCircles": "Four Circles",
   "FrozenOver": "Frozen Over",
   "Geared": "Geared",
   "GlacialTrail": "Glacial Trail",
   "Haunted": "Haunted",
   "Hedge": "Hedge",
   "HighFinance": "High Finance",
   "Infernal": "Infernal",
   "InTheLoop": "In The Loop",
   "KartsNDarts": "KartsNDarts",
   "LastResort": "Last Resort",
   "Logs": "Logs",
   "LostCrevasse": "Lost Crevasse",
   "LotusIsland": "Lotus Island",
   "LuminousCove": "Luminous Cove",
   "Mesa": "Mesa",
   "MiddleOfTheRoad": "Middle of the Road",
   "MidnightMansion": "Midnight Mansion",
   "MoonLanding": "Moon Landing",
   "MuddyPuddles": "Muddy Puddles",
   "OffTheCoast": "Off The Coast",
   "OneTwoTree": "One Two Tree",
   "ParkPath": "Park Path",
   "PatsPond": "Pat's Pond",
   "Peninsula": "Peninsula",
   "Polyphemus": "Polyphemus",
   "ProtectTheYacht": "Protect The Yacht",
   "Quad": "Quad",
   "Quarry": "Quarry",
   "QuietStreet": "Quiet Street",
   "Rake": "Rake",
   "Ravine": "Ravine",
   "Resort": "Resort",
   "Sanctuary": "Sanctuary",
   "Scrapyard": "Scrapyard",
   "Skates": "Skates",
   "SpiceIslands": "Spice Islands",
   "Spillway": "Spillway",
   "SpringSpring": "Spring Spring",
   "Streambed": "Streambed",
   "SulfurSprings": "Sulfur Springs",
   "SunkenColumns": "Sunken Columns",
   "SunsetGulch": "Sunset Gulch",
   "TheCabin": "The Cabin",
   "Tinkerton": "Tinkerton",
   "TownCentre": "Town Center",
   "TreeStump": "Tree Stump",
   "Tutorial": "Monkey Meadow",
   "Underground": "Underground",
   "WaterPark": "Water Park",
   "WinterPark": "Winter Park",
   "Workshop": "Workshop",
   "XFactor": "X Factor"
}

modekeys = {
   "AlternateBloonsRounds": "Alternate Bloons Rounds",
   "Impoppable": "Impoppable",
   "Standard": "Standard",
   "HalfCash": "Half Cash",
   "DoubleMoabHealth": "Double HP MOABs",
   "Reverse": "Reverse",
   "PrimaryOnly": "Primary Only",
   "MilitaryOnly": "Military Only",
   "Clicks": "CHIMPS",
   "Deflation": "Deflation",
   "MagicOnly": "Magic Monkeys Only",
   "Apopalypse": "Apopalypse"
}

def parse(dat):
   o = "{{BTD6 challenge rules/new\n|type=bossBloon"
   for k, v in dat.items():
      if k == "map":
         o += "\n|" + k + "=" + mapkeys[v]
      elif k == "mode":
         o += "\n|" + k + "=" + modekeys[v]
      elif type(v) != list and type(v) != dict and k != "name":
         o += "\n|" + k + "=" + str2(v)

      elif k == "towers":
         o += "\n|_towers="

         towerids = dict()

         for vv in v:
               if vv["max"] != 0:
                  o2 = "{{BTD6 tower restrictions"
                  for kkk, vvv in vv.items():
                     o2 += "|" + kkk + "=" + str2(vvv)

                  o2 += "}}"
                  towerids[vv["tower"]] = o2

         for i in towerkeys:
               if i in towerids: o += towerids[i]

      elif k == "startRules":
         o += "\n|lives=" + str2(v["lives"])
         o += "\n|maxLives=" + str2(v["maxLives"])
         o += "\n|startingCash=" + str2(v["cash"])
         o += "\n|startRound=" + str2(v["round"])
         o += "\n|endRound=" + str2(v["endRound"])
         if "revives" in v: o += "\n|revives=" + str2(v["revives"])

         
      elif k == "bloonModifiers":
         o += "\n|speedMultiplier=" + str2(v["speedMultiplier"])
         if "moabSpeedMultiplier" in v: o += "\n|moabSpeedMultiplier=" + str2(v["moabSpeedMultiplier"])
         if "bossSpeedMultiplier" in v: o += "\n|bossSpeedMultiplier=" + str2(v["bossSpeedMultiplier"])
         if "regrowRateMultiplier" in v: o += "\n|regrowRateMultiplier=" + str2(v["regrowRateMultiplier"])
         o += "\n|bloonHealthMultiplier=" + str2(v["healthMultipliers"]["bloons"])
         o += "\n|moabHealthMultiplier=" + str2(v["healthMultipliers"]["moabs"])
         if "boss" in v["healthMultipliers"]: o += "\n|bossHealthMultiplier=" + str2(v["healthMultipliers"]["boss"])

      elif k == "roundSets":
         if v != []: o += "\n|customRounds=" + ", ".join(v)
         else: o += "\n|customRounds="

   return o + "\n}}"

loaded = dict()

starts = []

for i in os.listdir():
   if ".json" not in i: continue
   j = open(i, "r", encoding="utf-8")
   jd = json.load(j)
   j.close()
   #print(i)

   if jd["SKU"]["start"] in loaded: print(i)
   else:
      loaded[jd["SKU"]["start"]] = jd
      starts.append(jd["SKU"]["start"])


for i in sorted(starts):
   jd = loaded[i]
   datuh = json.loads(jd["Data"])

   #out.write("===" + jd["name"] + "===\n")
   out.write("{{BTD6 boss event rules")
   out.write("\n|boss=" + ((datuh["bossType"]).capitalize() if "type" not in jd["SKU"]["metadata"] else jd["SKU"]["metadata"]["type"]))
   out.write('\n|start=' + str(jd["SKU"]["start"])[:-3])
   out.write('\n|end=' + str(jd["SKU"]["end"])[:-3])
   #out.write("\n|rewards=" + ",".join(jd["SKU"]["rewards"]))
   out.write("\n|normal rules=" + parse(datuh["normalDcm"]))
   out.write("\n|elite rules=" + parse(datuh["eliteDcm"]))
   out.write("\n}}\n")

out.close()