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
s = """{"rotation": [
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "TownCentre",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:65#Power:PortableLake",
                  "mode": "Standard",
                  "id": 531,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Heroed UP ~By DrakonicPickles",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "FourCircles",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#Power:DartTime",
                  "mode": "Standard",
                  "id": 496,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Israel030506's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#InstaMonkey:SpikeFactory,120",
                  "mode": "Standard",
                  "id": 497,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Player's Challenge ~By Player",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Carved",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#Power:EnergisingTotem",
                  "mode": "Standard",
                  "id": 498,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Darts, Nails, and Bombs ~By FriendlyMonkey",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:85#CollectionEvent:25",
                  "mode": "Standard",
                  "id": 499,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Player4544765's Challenge ~By Player4544765",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:IceMonkey,200",
                  "mode": "Standard",
                  "id": 500,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "cookieb039's Challenge ~By cookieb039",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Hedge",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#CollectionEvent:25",
                  "mode": "Standard",
                  "id": 501,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "SNipers/Benjamin Only ~By DemoKat",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Hedge",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#Power:BananaFarmer",
                  "mode": "Standard",
                  "id": 502,
                  "maxTowers": 17,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "360dab21's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#CollectionEvent:25",
                  "mode": "Standard",
                  "id": 503,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "the no shooting challange ~By TopElite8214",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:100#CollectionEvent:50",
                  "mode": "Standard",
                  "id": 504,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Have a Very Merry Christmas",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "TownCentre",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:100#Power:CashDrop",
                  "mode": "Standard",
                  "id": 505,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Boxing Day Sale",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#CollectionEvent:25",
                  "mode": "Standard",
                  "id": 506,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 50
                  },
                  "name": "jadenman98's Challenge ~By jadenman98",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FrozenOver",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#InstaMonkey:DartMonkey,202",
                  "mode": "Standard",
                  "id": 507,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "looks easy hm 2 ~By Howdoiplay",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "PatsPond",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#CollectionEvent:25",
                  "mode": "Standard",
                  "id": 508,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 50
                  },
                  "name": "your great ~By Player2",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 4,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FiringRange",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#InstaMonkey:TackShooter,210",
                  "mode": "Standard",
                  "id": 509,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 45
                  },
                  "name": "Shooting Gallery ~By Jimmy Owens",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "AlpineRun",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:60#CollectionEvent:50",
                  "mode": "Standard",
                  "id": 510,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 80
                  },
                  "name": "New Years Celebration",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "AdorasTemple",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#Power:MoabMine",
                  "mode": "Standard",
                  "id": 511,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Happy New Years!",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 8,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 4,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 8,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "ParkPath",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#InstaMonkey:Alchemist,020",
                  "mode": "Standard",
                  "id": 512,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 80
                  },
                  "name": "2 of a kind ~By Soggycosplayer",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#Power:BananaFarmer",
                  "mode": "Standard",
                  "id": 513,
                  "maxTowers": 60,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 80
                  },
                  "name": "Penguin_'s Challenge ~By Penguin_",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "EndOfTheRoad",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:MortarMonkey,220",
                  "mode": "Standard",
                  "id": 514,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 63
                  },
                  "name": "the best of the cheapest ~By Stycore",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:85#InstaMonkey:MonkeyAce,022",
                  "mode": "Reverse",
                  "id": 515,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Kiwimaster :) ~By KiwiTower7024",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "SpringSpring",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#Power:CashDrop",
                  "mode": "Standard",
                  "id": 516,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Teebeutl's Challenge ~By Teebeutl",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:65#Power:RoadSpikes",
                  "mode": "Reverse",
                  "id": 517,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Churchill meets Magic ~By DariusKai",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FourCircles",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:MonkeyVillage,202",
                  "mode": "Standard",
                  "id": 518,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "ninja monkey only ~By Doggo69boi420",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:Alchemist,011",
                  "mode": "Standard",
                  "id": 519,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 50
                  },
                  "name": "Chumik8's Challenge ~By Chumik8",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FrozenOver",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#Power:BananaFarmer",
                  "mode": "Standard",
                  "id": 520,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "amindwars10's Challenge ~By amindwars10",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#Power:CamoTrap",
                  "mode": "Standard",
                  "id": 521,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": " try orange and super monkey ~By BloonPhoenix06",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "TreeStump",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#Power:CashDrop",
                  "mode": "Standard",
                  "id": 522,
                  "maxTowers": 99,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 52
                  },
                  "name": "John Wick challenge ~By John Wick",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 1,
                        "isHero": false
                     }
                  ],
                  "map": "ParkPath",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:BananaFarm,220",
                  "mode": "Standard",
                  "id": 523,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "There can only be one",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "MoonLanding",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:65#InstaMonkey:BombShooter,210",
                  "mode": "Reverse",
                  "id": 524,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Houston we have a problem ~By LStracck",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:70#Power:GlueTrap",
                  "mode": "Standard",
                  "id": 525,
                  "maxTowers": 20,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Katie Wenger's Challenge ~By Katie Wenger",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:75#InstaMonkey:BoomerangMonkey,120",
                  "mode": "Standard",
                  "id": 526,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Two heros vs Bloons ~By Idkisreal",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 4,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:80#InstaMonkey:DartMonkey,012",
                  "mode": "Standard",
                  "id": 527,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "BloonPopper748's Challenge ~By BloonPopper748",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "TownCentre",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:85#InstaMonkey:Druid,022",
                  "mode": "Standard",
                  "id": 528,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 50
                  },
                  "name": "Defender's Of Monkville ~By JakeTheFieryFox",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "DarkCastle",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:60#Power:MoabMine",
                  "mode": "Standard",
                  "id": 529,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 80
                  },
                  "name": "New Player Boom-tics ~By JieFengChin",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "EndOfTheRoad",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#Power:MonkeyBoost",
                  "mode": "Standard",
                  "id": 530,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Glue road ~By Josh Sucks",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "TownCentre",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:65#Power:PortableLake",
                  "mode": "Standard",
                  "id": 495,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Heroed UP ~By DrakonicPickles",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FiringRange",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:BombShooter,101",
                  "mode": "Standard",
                  "id": 532,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "KiwiPhoenix476's Challenge ~By KiwiPhoenix476",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "FourCircles",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:85#InstaMonkey:DartMonkey,020",
                  "mode": "Standard",
                  "id": 533,
                  "maxTowers": 35,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "The utility xp challenge ~By MaxaM368",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "SpringSpring",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:90#InstaMonkey:TackShooter,021",
                  "mode": "Standard",
                  "id": 534,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 80
                  },
                  "name": "domanator's Challenge ~By domanator",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:85#Power:GlueTrap",
                  "mode": "Standard",
                  "id": 535,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "MonkeyPopper36's Challenge ~By MonkeyPopper36",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 4,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "SpiceIslands",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:75#InstaMonkey:SniperMonkey,220",
                  "mode": "Reverse",
                  "id": 536,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 37
                  },
                  "name": "Pro poper's Challenge ~By Pro poper",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FrozenOver",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:95#InstaMonkey:IceMonkey,220",
                  "mode": "Standard",
                  "id": 537,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 75
                  },
                  "name": "Too Fast! ~By MakAttack",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#Power:DartTime",
                  "mode": "Standard",
                  "id": 538,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 43
                  },
                  "name": "I SEE SAYS THE BLIND MAN ~By Gooseyboi",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "MoonLanding",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#Power:RoadSpikes",
                  "mode": "Standard",
                  "id": 539,
                  "maxTowers": 17,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "LeafyDex's Challenge ~By LeafyDex",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 4,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "TownCentre",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#InstaMonkey:MonkeyAce,202",
                  "mode": "Standard",
                  "id": 540,
                  "maxTowers": 11,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "for ssundee",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:MonkeyBuccaneer,022",
                  "mode": "Standard",
                  "id": 541,
                  "maxTowers": 3,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Takenpanda1492's Challenge ~By Takenpanda1492",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Logs",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#Power:Pontoon",
                  "mode": "Standard",
                  "id": 542,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Mattrosa's fortnite challenge ~By Mattrosa",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#Power:EnergisingTotem",
                  "mode": "Standard",
                  "id": 543,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "the primary",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "TownCentre",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:85#InstaMonkey:MonkeySub,201",
                  "mode": "Standard",
                  "id": 544,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "PopElite5854's Challenge ~By PopElite5854",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 3,
                        "isHero": false
                     }
                  ],
                  "map": "Carved",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#Power:PortableLake",
                  "mode": "Standard",
                  "id": 545,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Infinate-Troll's Challenge ~By Infinate-Troll",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "ParkPath",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#Power:Thrive",
                  "mode": "Standard",
                  "id": 546,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Support challenge ~By Lucas",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:MonkeyVillage,012",
                  "mode": "Reverse",
                  "id": 547,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Wooden Nightmare ~By Player3970522",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:55#InstaMonkey:EngineerMonkey,102",
                  "mode": "Standard",
                  "id": 548,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 50
                  },
                  "name": "1 of every attacking tower ~By Baloonbuster6",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:70#Power:CashDrop",
                  "mode": "Standard",
                  "id": 549,
                  "maxTowers": 5,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "CONFUSION ~By Mega Ninja",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "InTheLoop",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#Power:GlueTrap",
                  "mode": "Standard",
                  "id": 550,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 53
                  },
                  "name": "OpalArchon1411's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "EndOfTheRoad",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:60#InstaMonkey:MortarMonkey,202",
                  "mode": "Standard",
                  "id": 551,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 63
                  },
                  "name": "epicmonkey900's challenge ~By EpicMonkey900",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "ParkPath",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:75#InstaMonkey:WizardMonkey,220",
                  "mode": "Standard",
                  "id": 552,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 56
                  },
                  "name": "10 waves of suffering (nerfed) ~By Lol u suck",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:55#Power:BananaFarmer",
                  "mode": "Standard",
                  "id": 553,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "rockaces96's Challenge ~By rockaces96",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FourCircles",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#Power:RoadSpikes",
                  "mode": "Standard",
                  "id": 554,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Lapin_13's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "AlpineRun",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:75#InstaMonkey:TackShooter,000",
                  "mode": "Standard",
                  "id": 555,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Jessen's Challenge ~By Jessen",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FrozenOver",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:SuperMonkey,000",
                  "mode": "Standard",
                  "id": 556,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "my liked towers ~By SpecialCough",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "MoonLanding",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#InstaMonkey:Druid,000",
                  "mode": "Standard",
                  "id": 557,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Stach_10's Challenge ~By Stach_10",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "SpiceIslands",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:80#Power:SuperMonkeyStorm",
                  "mode": "Standard",
                  "id": 558,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "hikoru6's Challenge ~By hikoru6",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:55#Power:MonkeyBoost",
                  "mode": "Standard",
                  "id": 559,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "purple path only with buffs ~By datboifall",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#InstaMonkey:GlueGunner,202",
                  "mode": "Standard",
                  "id": 560,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "One sniper ~By Player7348195",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "ParkPath",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:HeliPilot,220",
                  "mode": "Standard",
                  "id": 561,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "JoshGotEm's Challenge ~By JoshGotEm",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 10,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 10,
                        "isHero": false
                     }
                  ],
                  "map": "Cracked",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#Power:Pontoon",
                  "mode": "Standard",
                  "id": 562,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "rocky road ~By Slash",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "MoonLanding",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#Power:PortableLake",
                  "mode": "Standard",
                  "id": 563,
                  "maxTowers": 99,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 59
                  },
                  "name": "RedKahuna56482's Challenge ~By RedKahuna56482",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:70#Power:GlueTrap",
                  "mode": "Reverse",
                  "id": 564,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "BloonMaster760's Challenge ~By BloonMaster760",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "TreeStump",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:55#InstaMonkey:IceMonkey,103",
                  "mode": "Standard",
                  "id": 565,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Orpacking's Challenge ~By Orpacking",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FrozenOver",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:70#InstaMonkey:NinjaMonkey,201",
                  "mode": "Standard",
                  "id": 566,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "water challenge ~By Me",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FiringRange",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:85#InstaMonkey:MonkeyAce,012",
                  "mode": "Standard",
                  "id": 567,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Sniping Grounds ~By Targetings",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:70#Power:DartTime",
                  "mode": "Standard",
                  "id": 568,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 50
                  },
                  "name": "DIETER05's Challenge ~By DIETER05",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Cracked",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#Power:Thrive",
                  "mode": "Standard",
                  "id": 569,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Down to bussiness ~By - XxDanxX -",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "OffTheCoast",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:MonkeySub,220",
                  "mode": "Standard",
                  "id": 570,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Aquaman Challenge. ~By Ben Phelps",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "InTheLoop",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:65#Power:MoabMine",
                  "mode": "Standard",
                  "id": 571,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Clogged Up ~By KillerGriller",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "WinterPark",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:60#InstaMonkey:SniperMonkey,202",
                  "mode": "Standard",
                  "id": 572,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Blazingecho's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Downstream",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:55#InstaMonkey:DartMonkey,022",
                  "mode": "Standard",
                  "id": 573,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "brian2k420's Challenge ~By brian2k420",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Benjamin",
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 1,
                        "isHero": false
                     }
                  ],
                  "map": "FiringRange",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:85#Power:CashDrop",
                  "mode": "Standard",
                  "id": 574,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": -1,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "0-0-0 dart monkey ~By killercillian",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": false
               }
            ]
}"""

def parse(dat):
    o = ""
    for k, v in dat.items():
        if k == "map":
            o += "\n|" + k + "=" + mapkeys[v]
        elif k == "mode":
            o += "\n|" + k + "=" + modekeys[v]
        elif type(v) != list and type(v) != dict:
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

    return o

s2 = json.loads(s)

for i in range(0, 0+31):
    #j = open(str(i) + ".json", "r", encoding="utf-8")
    jd = s2["rotation"][i]
    #j.close()
    #print(i)

    out.write("===" + jd["name"] + "===\n")
    out.write("{{BTD6 challenge rules/new")
    out.write("\n|type=dailyChallenge")
    out.write(f"\n|date={i+16} December 2019")
    out.write(parse(jd))
    out.write("\n}}\n")

out.close()