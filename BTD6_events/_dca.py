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

s = """{"rotationAdvanced": [
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
                        "max": 3,
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
                  "map": "Streambed",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:100#Power:TechBot",
                  "mode": "Clicks",
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": -1,
                     "round": 6,
                     "maxLives": 1,
                     "endRound": 63
                  },
                  "name": "Clara's Challenge ~By Clara",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "Logs",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:70#Power:GlueTrap",
                  "mode": "Reverse",
                  "id": 478,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 0.65,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 50000,
                     "round": 76,
                     "maxLives": 1,
                     "endRound": 76
                  },
                  "name": "SpringTR's Challenge ~By SpringTR",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FourCircles",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:100#InstaMonkey:Druid,300",
                  "mode": "Apopalypse",
                  "id": 479,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.31,
                     "moabSpeedMultiplier": 4,
                     "healthMultipliers": {
                        "bloons": 5,
                        "moabs": 0.1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 5000,
                     "round": 38,
                     "maxLives": 1,
                     "endRound": 90
                  },
                  "name": "Role reversal! ...And vines! ~By Fun Cat",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "Cracked",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:110#InstaMonkey:SpikeFactory,023",
                  "mode": "Standard",
                  "id": 480,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 5,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 2000,
                     "round": 1,
                     "maxLives": -1,
                     "endRound": 14
                  },
                  "name": "impossible?",
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
                        "max": -1,
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
                  "rewards": "MonkeyMoney:80#Power:MoabMine",
                  "mode": "Deflation",
                  "id": 481,
                  "maxTowers": 1,
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 1555,
                     "round": 25,
                     "maxLives": 1,
                     "endRound": 28
                  },
                  "name": "Purples and Leads  ~By AKE1223",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 1,
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
                        "max": 1,
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
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:110#InstaMonkey:GlueGunner,130",
                  "mode": "Standard",
                  "id": 482,
                  "maxTowers": -1,
                  "seed": 0,
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
                     "lives": 100,
                     "cash": -1,
                     "round": 3,
                     "maxLives": -1,
                     "endRound": 80
                  },
                  "name": "Just the basics ~By Plantyby",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 1,
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
                  "map": "Cubism",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:80#Power:GlueTrap",
                  "mode": "Deflation",
                  "id": 483,
                  "maxTowers": 3,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.05,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 1
                     },
                     "allCamo": true,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 53334,
                     "round": 163,
                     "maxLives": 1,
                     "endRound": 163
                  },
                  "name": "When round 63 isnt your only problem ~By Fiire",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "Logs",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:300#InstaMonkey:TackShooter,203",
                  "mode": "Clicks",
                  "id": 484,
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 2225,
                     "round": 17,
                     "maxLives": 1,
                     "endRound": 19
                  },
                  "name": "Hall of Fame: Friday Stinger; 'nothing gets past my bow'",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:180#CollectionEvent:25",
                  "mode": "Standard",
                  "id": 485,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.01,
                     "moabSpeedMultiplier": 1.01,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 1.01
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 2000,
                     "cash": 26800,
                     "round": 76,
                     "maxLives": 9999999,
                     "endRound": 77
                  },
                  "name": "HOF: godvilla ~By Player1985992",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 5,
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
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:180#Power:MonkeyBoost",
                  "mode": "Impoppable",
                  "id": 486,
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
                     "round": 6,
                     "maxLives": -1,
                     "endRound": 100
                  },
                  "name": "EmanoNXD's Challenge ~By EmanoNXD",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": false,
                  "noContinues": true,
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
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "FourCircles",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:100#CollectionEvent:30",
                  "mode": "Apopalypse",
                  "id": 487,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.31,
                     "moabSpeedMultiplier": 4,
                     "healthMultipliers": {
                        "bloons": 5,
                        "moabs": 0.1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 5000,
                     "round": 38,
                     "maxLives": 1,
                     "endRound": 90
                  },
                  "name": "HOF: Role reversal! ...And vines! ~By Fun Cat",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "TreeStump",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:95#InstaMonkey:MonkeyBuccaneer,220",
                  "mode": "Clicks",
                  "id": 488,
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
                     "lives": 1,
                     "cash": 7000,
                     "round": 40,
                     "maxLives": 1,
                     "endRound": 42
                  },
                  "name": "HOF: Evelot YT's Challenge ~By Evelot YT",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 1,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Hedge",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:150#InstaMonkey:TackShooter,032",
                  "mode": "Apopalypse",
                  "id": 489,
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
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 999,
                     "round": 1,
                     "maxLives": 250,
                     "endRound": 90
                  },
                  "name": "Impossible challenge 1",
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
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "MoonLanding",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:300#Power:CamoTrap",
                  "mode": "AlternateBloonsRounds",
                  "id": 490,
                  "maxTowers": 4,
                  "seed": 0,
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 1776,
                     "round": 9,
                     "maxLives": -1,
                     "endRound": 43
                  },
                  "name": "HOF: Happy 4th of July!",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
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
                  "rewards": "MonkeyMoney:300#CollectionEvent:45",
                  "mode": "Standard",
                  "id": 491,
                  "maxTowers": 1,
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 12345,
                     "round": 59,
                     "maxLives": -1,
                     "endRound": 59
                  },
                  "name": "HOF: Friday Stinger; aaaaaaaaaaa ~By Pheonixcv",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Hedge",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:90#Power:Thrive",
                  "mode": "Standard",
                  "id": 492,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.25,
                     "moabSpeedMultiplier": 0.05,
                     "healthMultipliers": {
                        "bloons": 3.5,
                        "moabs": 0.05
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 5,
                     "cash": 22000,
                     "round": 3,
                     "maxLives": 5,
                     "endRound": 80
                  },
                  "name": "HOF: Brain dead easy ~By Slimcrazed",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "ParkPath",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:120#InstaMonkey:SpikeFactory,103",
                  "mode": "Standard",
                  "id": 493,
                  "maxTowers": 10,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.1,
                     "moabSpeedMultiplier": 2.5,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1.5
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 8946,
                     "round": 18,
                     "maxLives": 1,
                     "endRound": 51
                  },
                  "name": "sub to me boiz",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": true,
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
                  "map": "BloodyPuddles",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:95#Power:BananaFarmer",
                  "mode": "Standard",
                  "id": 494,
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
                     "lives": 1,
                     "cash": 550,
                     "round": 1,
                     "maxLives": -1,
                     "endRound": 15
                  },
                  "name": "sad man moments ~By Kakashi",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 5,
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
                        "max": 2,
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
                        "max": 3,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:110#CollectionEvent:35",
                  "mode": "Standard",
                  "id": 495,
                  "maxTowers": 6,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.19,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1.25
                     },
                     "allCamo": true,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 5187,
                     "round": 13,
                     "maxLives": 1,
                     "endRound": 62
                  },
                  "name": "Pro poper's Challenge ~By Pro poper",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "map": "SpiceIslands",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:95#Power:GlueTrap",
                  "mode": "Deflation",
                  "id": 496,
                  "maxTowers": 3,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 2.47,
                     "moabSpeedMultiplier": 1.75,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 0.05
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 45770,
                     "round": 68,
                     "maxLives": 1,
                     "endRound": 73
                  },
                  "name": "Mathias868's Challenge ~By Mathias868",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "TownCentre",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:100#InstaMonkey:IceMonkey,023",
                  "mode": "Impoppable",
                  "id": 497,
                  "maxTowers": 2,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 2,
                     "moabSpeedMultiplier": 4,
                     "healthMultipliers": {
                        "bloons": 19.99,
                        "moabs": 3
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 22222,
                     "round": 55,
                     "maxLives": -1,
                     "endRound": 55
                  },
                  "name": "the ceramic health is not maxed ~By Aug bro",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "map": "SpringSpring",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:90#InstaMonkey:SniperMonkey,220",
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
                     "lives": 1,
                     "cash": 550,
                     "round": 1,
                     "maxLives": 1,
                     "endRound": 40
                  },
                  "name": "Friday Stinger; Firewolf3670's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 3,
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
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:120#Power:DartTime",
                  "mode": "AlternateBloonsRounds",
                  "id": 499,
                  "maxTowers": 6,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 5,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 0.84,
                        "moabs": 0.84
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 9666,
                     "cash": 9999999,
                     "round": 79,
                     "maxLives": 9666,
                     "endRound": 79
                  },
                  "name": "EVERSON'S INPOPPABLE NOT CHALLENGE!!!!!!",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "Downstream",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:90#Power:CashDrop",
                  "mode": "Standard",
                  "id": 500,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 5,
                     "moabSpeedMultiplier": 3,
                     "healthMultipliers": {
                        "bloons": 0.25,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 150,
                     "cash": 3500,
                     "round": 3,
                     "maxLives": 150,
                     "endRound": 50
                  },
                  "name": "Gamer Challenge ~By Jadon Lovett",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": 5,
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
                        "max": 2,
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
                  "map": "Downstream",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:115#InstaMonkey:SniperMonkey,023",
                  "mode": "Clicks",
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
                     "lives": 10,
                     "cash": 12996,
                     "round": 36,
                     "maxLives": 87,
                     "endRound": 71
                  },
                  "name": "Ninjutsu god's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "map": "Streambed",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:100#InstaMonkey:WizardMonkey,302",
                  "mode": "Reverse",
                  "id": 502,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.21,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 1.02,
                        "moabs": 0.61
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 15,
                     "cash": 200,
                     "round": 1,
                     "maxLives": 15,
                     "endRound": 10
                  },
                  "name": "Neal S's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                        "max": 1,
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
                  "map": "Cracked",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:125#Power:MoabMine",
                  "mode": "Reverse",
                  "id": 503,
                  "maxTowers": 4,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.4,
                     "moabSpeedMultiplier": 2,
                     "healthMultipliers": {
                        "bloons": 2,
                        "moabs": 2.5
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 60,
                     "cash": 425,
                     "round": 10,
                     "maxLives": 60,
                     "endRound": 63
                  },
                  "name": "Don't Underestimate The Sniper(S) ~By IcyPepperPro",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": -1,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Underground",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:90#InstaMonkey:BoomerangMonkey,230",
                  "mode": "Standard",
                  "id": 504,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 5,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 20
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 63000,
                     "round": 63,
                     "maxLives": 1,
                     "endRound": 63
                  },
                  "name": "Meandyoi's Challenge ~By Meandyoi",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 2,
                        "isHero": false
                     }
                  ],
                  "map": "HighFinance",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:180#InstaMonkey:HeliPilot,203",
                  "mode": "Reverse",
                  "id": 505,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 2.19,
                        "moabs": 1.2
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 50,
                     "cash": 2000,
                     "round": 13,
                     "maxLives": 50,
                     "endRound": 63
                  },
                  "name": "Friday Stinger; We have business to discuss Ep. 2a ~By agla88",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
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
                  "map": "Logs",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:75#Power:SuperMonkeyStorm",
                  "mode": "Deflation",
                  "id": 506,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.18,
                     "moabSpeedMultiplier": 0.24,
                     "healthMultipliers": {
                        "bloons": 0.3,
                        "moabs": 0.29
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 100,
                     "cash": 400,
                     "round": 40,
                     "maxLives": 100,
                     "endRound": 40
                  },
                  "name": "moab ~By Matthew",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
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
                  "rewards": "MonkeyMoney:95#InstaMonkey:TackShooter,101",
                  "mode": "Impoppable",
                  "id": 507,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.25,
                     "moabSpeedMultiplier": 1.25,
                     "healthMultipliers": {
                        "bloons": 1.5,
                        "moabs": 2
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 3750,
                     "round": 31,
                     "maxLives": 1,
                     "endRound": 85
                  },
                  "name": "Just like ol' times! ~By David_The Superior",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 1,
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
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:90#InstaMonkey:IceMonkey,230",
                  "mode": "Standard",
                  "id": 508,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1.1
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 180000,
                     "round": 93,
                     "maxLives": 1,
                     "endRound": 93
                  },
                  "name": "Dracoblues's Challenge ~By Dracoblues",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                        "max": 1,
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
                  "map": "Hedge",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:95#Power:DartTime",
                  "mode": "Deflation",
                  "id": 509,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1.5,
                        "moabs": 0.8
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 7500,
                     "round": 40,
                     "maxLives": 50,
                     "endRound": 40
                  },
                  "name": "TVOJA MAMA ~By MINECRAFTPRO",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
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
                        "max": 1,
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
                        "max": 1,
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
                  "map": "Cracked",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:105#InstaMonkey:WizardMonkey,220",
                  "mode": "Standard",
                  "id": 510,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 0.5,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 0.8
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 10000,
                     "round": 3,
                     "maxLives": 1,
                     "endRound": 80
                  },
                  "name": "Vasnas's Challenge ~By Vasnas",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "TreeStump",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:80#InstaMonkey:Alchemist,320",
                  "mode": "Standard",
                  "id": 477,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.9,
                     "moabSpeedMultiplier": 1.15,
                     "healthMultipliers": {
                        "bloons": 1.7,
                        "moabs": 1.8
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 2,
                     "cash": 2800,
                     "round": 3,
                     "maxLives": 2,
                     "endRound": 80
                  },
                  "name": "What a beatiful map ~By Player3872692",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 1,
                        "isHero": false
                     }
                  ],
                  "map": "Logs",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:175#InstaMonkey:TackShooter,204",
                  "mode": "Clicks",
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
                     "cash": 37575,
                     "round": 50,
                     "maxLives": -1,
                     "endRound": 100
                  },
                  "name": "Friday Stinger; 4TC",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "map": "MuddyPuddles",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:MonkeyVillage,203",
                  "mode": "Deflation",
                  "id": 513,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 20
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": 35450,
                     "round": 40,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "Blue ~By Cheeky",
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
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:100#Power:CamoTrap",
                  "mode": "Standard",
                  "id": 514,
                  "maxTowers": 2,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 10,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 21000,
                     "round": 63,
                     "maxLives": 1,
                     "endRound": 63
                  },
                  "name": "the serious ceramics ~By OrigamiArk",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Logs",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:EngineerMonkey,320",
                  "mode": "Deflation",
                  "id": 515,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 0.1,
                        "moabs": 20
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 250,
                     "cash": 8000,
                     "round": 63,
                     "maxLives": -1,
                     "endRound": 63
                  },
                  "name": ":) ~By oioio",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "Ezili",
                        "max": 1,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "#ouch",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:80#InstaMonkey:DartMonkey,000",
                  "mode": "Clicks",
                  "id": 516,
                  "maxTowers": 99,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 2,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 0.3
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 80000,
                     "round": 100,
                     "maxLives": 1,
                     "endRound": 100
                  },
                  "name": "dart monkey is key",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": false,
                  "noInstaReward": true
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
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "AnotherBrick",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:115#Power:EnergisingTotem",
                  "mode": "Deflation",
                  "id": 517,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.5,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 2375,
                     "round": 4,
                     "maxLives": 1,
                     "endRound": 7
                  },
                  "name": "Hmmmmm ~By Higuy",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 3,
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
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 1,
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
                        "max": 4,
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
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "SpiceIslands",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:85#InstaMonkey:IceMonkey,103",
                  "mode": "Standard",
                  "id": 518,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.05,
                     "moabSpeedMultiplier": 0.05,
                     "healthMultipliers": {
                        "bloons": 0.1,
                        "moabs": 0.05
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 61234,
                     "round": 241,
                     "maxLives": 1,
                     "endRound": 241
                  },
                  "name": "BattleFrog79's Challenge ~By BattleFrog79",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "rewards": "MonkeyMoney:150#InstaMonkey:Druid,230",
                  "mode": "AlternateBloonsRounds",
                  "id": 519,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1.01,
                        "moabs": 1
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 37473,
                     "cash": 20502,
                     "round": 39,
                     "maxLives": 37473,
                     "endRound": 60
                  },
                  "name": "Friday Stinger; Spibo's Challenge",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 2,
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
                        "max": 3,
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
                        "max": 1,
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
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:150#Power:SuperMonkeyStorm",
                  "mode": "Standard",
                  "id": 520,
                  "maxTowers": 5,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 2,
                     "moabSpeedMultiplier": 1.5,
                     "healthMultipliers": {
                        "bloons": 1.5,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 3927,
                     "round": 25,
                     "maxLives": 1,
                     "endRound": 85
                  },
                  "name": "hmmmmmmm",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 6,
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
                  "map": "Logs",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:175#InstaMonkey:Druid,014",
                  "mode": "Clicks",
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": -1,
                     "round": 6,
                     "maxLives": 1,
                     "endRound": 100
                  },
                  "name": "First CHIMPS (402 Ninja + 015 Druid) ~By RandyZ524",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "EndOfTheRoad",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:85#InstaMonkey:SuperMonkey,013",
                  "mode": "AlternateBloonsRounds",
                  "id": 522,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 3.99,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 40100,
                     "round": 59,
                     "maxLives": 1,
                     "endRound": 60
                  },
                  "name": "Olive's Challenge ~By Olive",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": 2,
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
                        "max": 2,
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
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 2,
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
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 2,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 2,
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
                        "max": 2,
                        "isHero": false
                     }
                  ],
                  "map": "Cubism",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:80#InstaMonkey:BoomerangMonkey,022",
                  "mode": "Standard",
                  "id": 523,
                  "maxTowers": 2,
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 60,
                     "cash": 650,
                     "round": 36,
                     "maxLives": 65,
                     "endRound": 36
                  },
                  "name": "Budget Defense ~By The Line",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "Tutorial",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:90#Power:CashDrop",
                  "mode": "Deflation",
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 11000,
                     "round": 63,
                     "maxLives": 1,
                     "endRound": 63
                  },
                  "name": "found 63 ~By Matthew",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": 3,
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
                        "max": 1,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 3,
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
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 3,
                        "isHero": false
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:110#InstaMonkey:EngineerMonkey,120",
                  "mode": "Impoppable",
                  "id": 525,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.25,
                     "moabSpeedMultiplier": 1.11,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1.88
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 1500,
                     "round": 6,
                     "maxLives": 1,
                     "endRound": 100
                  },
                  "name": "Impoppable Plus by Ricky",
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Haunted",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:150#InstaMonkey:Alchemist,320",
                  "mode": "Standard",
                  "id": 526,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 5,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 20
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 100,
                     "cash": 44244,
                     "round": 63,
                     "maxLives": 100,
                     "endRound": 63
                  },
                  "name": "Friday Stinger; its time to make it shine ~By Matthew",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "map": "Haunted",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:80#Power:GlueTrap",
                  "mode": "Deflation",
                  "id": 527,
                  "maxTowers": 2,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.25,
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
                     "lives": 100,
                     "cash": 18000,
                     "round": 69,
                     "maxLives": 100,
                     "endRound": 69
                  },
                  "name": "Unnaturally good ~By FireMonkey250",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                        "max": 1,
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
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:120#InstaMonkey:BananaFarm,220",
                  "mode": "Reverse",
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 2,
                     "cash": 176543,
                     "round": 22,
                     "maxLives": 222,
                     "endRound": 33
                  },
                  "name": "Visionary ~By zuckers",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
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
                  "map": "Workshop",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:90#Power:MoabMine",
                  "mode": "Standard",
                  "id": 529,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.28,
                     "moabSpeedMultiplier": 1.25,
                     "healthMultipliers": {
                        "bloons": 1.4,
                        "moabs": 1.36
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 100,
                     "cash": 37698,
                     "round": 57,
                     "maxLives": -1,
                     "endRound": 64
                  },
                  "name": "Tronix's Challenge ~By Tronix",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                  "map": "FrozenOver",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:85#InstaMonkey:GlueGunner,210",
                  "mode": "Deflation",
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
                     "lives": 1,
                     "cash": 1000000,
                     "round": 144,
                     "maxLives": 1,
                     "endRound": 144
                  },
                  "name": "Jerry Ez Challenge ~By jerry",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": true,
                  "noInstaReward": true
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
                  "map": "Cornfield",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:80#InstaMonkey:IceMonkey,003",
                  "mode": "DoubleMoabHealth",
                  "id": 531,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.05,
                     "moabSpeedMultiplier": 0.3,
                     "healthMultipliers": {
                        "bloons": 0.1,
                        "moabs": 20
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 2,
                     "cash": 200000,
                     "round": 40,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "whooops camos huh ~By IM2SLICK4U",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": true,
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
                  "map": "Underground",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:100#InstaMonkey:Druid,011",
                  "mode": "Apopalypse",
                  "id": 532,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.1,
                     "moabSpeedMultiplier": 1.1,
                     "healthMultipliers": {
                        "bloons": 1.1,
                        "moabs": 1.1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 250,
                     "cash": 4100,
                     "round": 10,
                     "maxLives": 250,
                     "endRound": 65
                  },
                  "name": "Underground Mayhem by john321",
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
                        "max": 8,
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
                        "max": 1,
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
                        "max": 3,
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
                        "max": 3,
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
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 8,
                        "isHero": false
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "TackShooter",
                        "max": 1,
                        "isHero": false
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 3,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 5,
                        "isHero": false
                     }
                  ],
                  "map": "Rake",
                  "difficulty": "Easy",
                  "rewards": "MonkeyMoney:100#Power:MonkeyBoost",
                  "mode": "Deflation",
                  "id": 533,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.5,
                     "moabSpeedMultiplier": 5,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 20
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 100000,
                     "round": 95,
                     "maxLives": 1,
                     "endRound": 95
                  },
                  "name": "Friday Stinger; Dont try Challenge if You're Dablooon ~By SupremeAvocado",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": true
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
                        "max": 13,
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
                        "max": 6,
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
                        "max": 5,
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
                        "max": 2,
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
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:95#InstaMonkey:DartMonkey,201",
                  "mode": "Reverse",
                  "id": 534,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 0.8,
                     "moabSpeedMultiplier": 1.1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1.1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 100,
                     "cash": 2000,
                     "round": 10,
                     "maxLives": 100,
                     "endRound": 85
                  },
                  "name": "Off the coast ambush -by dartguy",
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
                  "map": "Logs",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:120#InstaMonkey:SniperMonkey,230",
                  "mode": "Clicks",
                  "id": 535,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 2
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 7,
                     "cash": -1,
                     "round": 6,
                     "maxLives": 7,
                     "endRound": 64
                  },
                  "name": "Sniper's skills ~By VSDlive",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 3,
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
                        "max": 4,
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
                        "max": 3,
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
                  "rewards": "MonkeyMoney:105#Power:MoabMine",
                  "mode": "Deflation",
                  "id": 536,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 2.5,
                     "moabSpeedMultiplier": 2.49,
                     "healthMultipliers": {
                        "bloons": 0.1,
                        "moabs": 0.05
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 1000000,
                     "round": 200,
                     "maxLives": 1,
                     "endRound": 200
                  },
                  "name": "really fast boi ~By Hugobaby",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 4,
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
                        "max": 4,
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
                        "max": 2,
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
                        "max": 2,
                        "isHero": false
                     }
                  ],
                  "map": "Streambed",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:110#InstaMonkey:BombShooter,021",
                  "mode": "AlternateBloonsRounds",
                  "id": 537,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.45,
                     "moabSpeedMultiplier": 1.3,
                     "healthMultipliers": {
                        "bloons": 3,
                        "moabs": 2.3
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 500,
                     "cash": 45000,
                     "round": 60,
                     "maxLives": 500,
                     "endRound": 80
                  },
                  "name": "Alt Modes call for Alt Strategies by Player556897",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
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
                        "max": 7,
                        "isHero": false
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "Druid",
                        "max": 4,
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
                        "max": 6,
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
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 5,
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
                        "max": 9,
                        "isHero": false
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 7,
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
                        "max": 5,
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
                  "map": "Streambed",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:110#InstaMonkey:DartMonkey,310",
                  "mode": "Standard",
                  "id": 538,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1.8,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 123,
                     "cash": 7866,
                     "round": 23,
                     "maxLives": 148,
                     "endRound": 76
                  },
                  "name": "Player2131625's Challenge ~By Player2131625",
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
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "EndOfTheRoad",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:85#InstaMonkey:WizardMonkey,110",
                  "mode": "Reverse",
                  "id": 539,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.5,
                     "moabSpeedMultiplier": 2,
                     "healthMultipliers": {
                        "bloons": 0.7,
                        "moabs": 0.75
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 50,
                     "cash": 1000,
                     "round": 6,
                     "maxLives": 50,
                     "endRound": 65
                  },
                  "name": "Glass Cannon MOABs by George",
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
                        "max": 2,
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
                        "max": 1,
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
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:150#Power:CashDrop",
                  "mode": "Standard",
                  "id": 540,
                  "maxTowers": 6,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.2,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 0.95,
                        "moabs": 1.2
                     },
                     "allCamo": false,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 2,
                     "cash": 123456,
                     "round": 98,
                     "maxLives": -1,
                     "endRound": 99
                  },
                  "name": "Friday Stinger; those are bad towers(exept vil and snip) ~By Philcrumbs ",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "rewards": "MonkeyMoney:95#InstaMonkey:BoomerangMonkey,202",
                  "mode": "Standard",
                  "id": 541,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 2.95,
                     "moabSpeedMultiplier": 2,
                     "healthMultipliers": {
                        "bloons": 8,
                        "moabs": 4
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 25000,
                     "round": 20,
                     "maxLives": 1,
                     "endRound": 80
                  },
                  "name": "Target Acquired, by Darby123",
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
                  "map": "FrozenOver",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:100#InstaMonkey:WizardMonkey,320",
                  "mode": "Standard",
                  "id": 542,
                  "maxTowers": 10,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 3,
                     "healthMultipliers": {
                        "bloons": 1,
                        "moabs": 1.5
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 25,
                     "cash": 850,
                     "round": 10,
                     "maxLives": 25,
                     "endRound": 50
                  },
                  "name": "Fire&ICe ~By PikachuVictini",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
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
                  "map": "AnotherBrick",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:115#InstaMonkey:SpikeFactory,210",
                  "mode": "Impoppable",
                  "id": 543,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.25,
                     "moabSpeedMultiplier": 1.25,
                     "healthMultipliers": {
                        "bloons": 1.1,
                        "moabs": 1.6
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 1900,
                     "round": 8,
                     "maxLives": 1,
                     "endRound": 60
                  },
                  "name": "Bricks Ahoy- By Tommy",
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Carved",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:80",
                  "mode": "Impoppable",
                  "id": 544,
                  "maxTowers": 10,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.2,
                     "moabSpeedMultiplier": 1.2,
                     "healthMultipliers": {
                        "bloons": 1.7,
                        "moabs": 2.2
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 460,
                     "round": 10,
                     "maxLives": 1,
                     "endRound": 60
                  },
                  "name": "IMPOSSIBLE ~By Player3480291",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": false,
                  "noInstaReward": true
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
                  "map": "ParkPath",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:250#InstaMonkey:BombShooter,204",
                  "mode": "Deflation",
                  "id": 545,
                  "maxTowers": 4,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 0.5,
                     "healthMultipliers": {
                        "bloons": 4.5,
                        "moabs": 4
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 1,
                     "cash": 30000,
                     "round": 60,
                     "maxLives": -1,
                     "endRound": 63
                  },
                  "name": "Tough Bois ~By Player3149254",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                  "map": "Cracked",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:130#InstaMonkey:HeliPilot,210",
                  "mode": "Reverse",
                  "id": 546,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 0.75,
                     "moabSpeedMultiplier": 2.5,
                     "healthMultipliers": {
                        "bloons": 7,
                        "moabs": 1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 100,
                     "cash": 2000,
                     "round": 20,
                     "maxLives": 100,
                     "endRound": 80
                  },
                  "name": "Slow and Heavy, by bloonguy322",
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
                        "max": 5,
                        "isHero": false
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 6,
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
                        "max": 1,
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
                        "max": 0,
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
                        "max": 0,
                        "isHero": false
                     }
                  ],
                  "map": "AdorasTemple",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:150#InstaMonkey:MonkeyBuccaneer,220",
                  "mode": "Impoppable",
                  "id": 547,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.1,
                     "moabSpeedMultiplier": 1.1,
                     "healthMultipliers": {
                        "bloons": 2.5,
                        "moabs": 2.1
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 650,
                     "round": 6,
                     "maxLives": 1,
                     "endRound": 80
                  },
                  "name": "Friday Stinger; Adoras Castle Defense, by Player435665",
                  "displayIncludedTowers": true,
                  "disableSelling": true,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": 4,
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
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:110#Power:Thrive",
                  "mode": "Standard",
                  "id": 548,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 1.52,
                        "moabs": 1.57
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": -1,
                     "cash": -1,
                     "round": 1,
                     "maxLives": -1,
                     "endRound": 60
                  },
                  "name": "Pirat party ~By Sivert Nistad",
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
                  "map": "Cargo",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:80#Power:MonkeyBoost",
                  "mode": "Standard",
                  "id": 549,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.19,
                     "moabSpeedMultiplier": 1.59,
                     "healthMultipliers": {
                        "bloons": 1.28,
                        "moabs": 2.91
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 20000,
                     "round": 39,
                     "maxLives": 1,
                     "endRound": 41
                  },
                  "name": "unknown ~By Colby Bong",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
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
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "Downstream",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:120#InstaMonkey:MonkeySub,021",
                  "mode": "AlternateBloonsRounds",
                  "id": 550,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.55,
                     "moabSpeedMultiplier": 0.7,
                     "healthMultipliers": {
                        "bloons": 0.8,
                        "moabs": 1.8
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 350,
                     "cash": 1750,
                     "round": 10,
                     "maxLives": 350,
                     "endRound": 70
                  },
                  "name": "How it all goes down - by John Doe",
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
                        "max": -1,
                        "isHero": false
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false
                     }
                  ],
                  "map": "FrozenOver",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:150#InstaMonkey:MonkeyVillage,023",
                  "mode": "Reverse",
                  "id": 551,
                  "maxTowers": 5,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.1,
                     "moabSpeedMultiplier": 1.1,
                     "healthMultipliers": {
                        "bloons": 1.1,
                        "moabs": 1.1
                     },
                     "allCamo": true,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 125,
                     "cash": 2185,
                     "round": 5,
                     "maxLives": 200,
                     "endRound": 90
                  },
                  "name": "can you see me? ~By Adenvinh01",
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
                  "map": "ParkPath",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:125#InstaMonkey:GlueGunner,230",
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
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 25000,
                     "round": 71,
                     "maxLives": 1,
                     "endRound": 95
                  },
                  "name": "Much Love, From Bloons ~By GachaBless",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
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
                        "max": -1,
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
                  "rewards": "MonkeyMoney:110#Power:DartTime",
                  "mode": "Standard",
                  "id": 553,
                  "maxTowers": 1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.82,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 0.1,
                        "moabs": 2
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 10,
                     "cash": 20000,
                     "round": 40,
                     "maxLives": 10,
                     "endRound": 63
                  },
                  "name": "DuowinSemin's Challenge ~By DuowinSemin",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 2,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     }
                  ],
                  "map": "Cracked",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:140#Power:Pontoon",
                  "mode": "Standard",
                  "id": 554,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.6,
                     "moabSpeedMultiplier": 0.42,
                     "healthMultipliers": {
                        "bloons": 2.71,
                        "moabs": 0.05
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 3640,
                     "cash": 6500,
                     "round": 55,
                     "maxLives": 4100,
                     "endRound": 61
                  },
                  "name": "Friday Stinger; icy glue pt1 ~By fam :o)",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": true,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 1,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeySub",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "TackShooter",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     }
                  ],
                  "map": "Logs",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:115#InstaMonkey:IceMonkey,101",
                  "mode": "Standard",
                  "id": 555,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1,
                     "moabSpeedMultiplier": 1,
                     "healthMultipliers": {
                        "bloons": 20,
                        "moabs": 1.08
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 163,
                     "cash": 18000,
                     "round": 63,
                     "maxLives": 163,
                     "endRound": 63
                  },
                  "name": "Jona Vajen's Challenge ~By Jona Vajen",
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
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Benjamin",
                        "max": 1,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "TackShooter",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     }
                  ],
                  "map": "OffTheCoast",
                  "difficulty": "Medium",
                  "rewards": "MonkeyMoney:120#InstaMonkey:BananaFarm,220",
                  "mode": "Reverse",
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
                  "disableMK": true,
                  "startRules": {
                     "lives": 2,
                     "cash": 176543,
                     "round": 22,
                     "maxLives": 222,
                     "endRound": 33
                  },
                  "name": "Visionary ~By zuckers",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": true,
                  "noContinues": false,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 1,
                        "path2NumBlockedTiers": 3,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": -1,
                        "path3NumBlockedTiers": -1
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 2,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 1,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 3,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 2,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "TackShooter",
                        "max": 2,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 3,
                        "path3NumBlockedTiers": 1
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 3,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 2,
                        "path3NumBlockedTiers": 1
                     }
                  ],
                  "map": "Haunted",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:120#InstaMonkey:TackShooter,202",
                  "mode": "Impoppable",
                  "id": 557,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 1.9,
                     "moabSpeedMultiplier": 2.1,
                     "healthMultipliers": {
                        "bloons": 0.5,
                        "moabs": 0.45
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 12500,
                     "round": 33,
                     "maxLives": 1,
                     "endRound": 62
                  },
                  "name": "Scary Front - By Mike",
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
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 1,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": -1,
                        "path2NumBlockedTiers": 3,
                        "path3NumBlockedTiers": 1
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 2,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 2,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 1,
                        "path2NumBlockedTiers": -1,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 2,
                        "path2NumBlockedTiers": -1,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": -1,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     }
                  ],
                  "map": "Cracked",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:115#InstaMonkey:SpikeFactory,210",
                  "mode": "Reverse",
                  "id": 558,
                  "maxTowers": -1,
                  "seed": 0,
                  "bloonModifiers": {
                     "speedMultiplier": 3.5,
                     "moabSpeedMultiplier": 2.8,
                     "healthMultipliers": {
                        "bloons": 3.5,
                        "moabs": 3.5
                     },
                     "allCamo": true,
                     "allRegen": true
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 155000,
                     "round": 85,
                     "maxLives": 1,
                     "endRound": 90
                  },
                  "name": "Stall Team, Unite! By bloony223",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": false,
                  "noInstaReward": true
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     }
                  ],
                  "map": "Cornfield",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:110#InstaMonkey:IceMonkey,003",
                  "mode": "DoubleMoabHealth",
                  "id": 559,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 0.05,
                     "moabSpeedMultiplier": 0.3,
                     "healthMultipliers": {
                        "bloons": 0.1,
                        "moabs": 20
                     },
                     "allCamo": true,
                     "allRegen": false
                  },
                  "disableMK": false,
                  "startRules": {
                     "lives": 2,
                     "cash": 200000,
                     "round": 40,
                     "maxLives": -1,
                     "endRound": 40
                  },
                  "name": "whooops camos huh ~By IM2SLICK4U",
                  "displayIncludedTowers": true,
                  "disableSelling": false,
                  "disablePowers": false,
                  "noContinues": true,
                  "noInstaReward": false
               },
               {
                  "towers": [
                     {
                        "tower": "Alchemist",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ChosenPrimaryHero",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BananaFarm",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 3,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 3
                     },
                     {
                        "tower": "Quincy",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BombShooter",
                        "max": -1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Gwendolin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "BoomerangMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "StrikerJones",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "DartMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "ObynGreenfoot",
                        "max": 1,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Druid",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "CaptainChurchill",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "GlueGunner",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Benjamin",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "HeliPilot",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Ezili",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "IceMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "PatFusty",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyAce",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "Adora",
                        "max": 0,
                        "isHero": true,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyBuccaneer",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeySub",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "MonkeyVillage",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "NinjaMonkey",
                        "max": 2,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SniperMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SpikeFactory",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "SuperMonkey",
                        "max": 1,
                        "isHero": false,
                        "path1NumBlockedTiers": 1,
                        "path2NumBlockedTiers": 1,
                        "path3NumBlockedTiers": 1
                     },
                     {
                        "tower": "TackShooter",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "WizardMonkey",
                        "max": 2,
                        "isHero": false,
                        "path1NumBlockedTiers": 2,
                        "path2NumBlockedTiers": 2,
                        "path3NumBlockedTiers": 2
                     },
                     {
                        "tower": "MortarMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     },
                     {
                        "tower": "EngineerMonkey",
                        "max": 0,
                        "isHero": false,
                        "path1NumBlockedTiers": 0,
                        "path2NumBlockedTiers": 0,
                        "path3NumBlockedTiers": 0
                     }
                  ],
                  "map": "Tutorial",
                  "difficulty": "Hard",
                  "rewards": "MonkeyMoney:100#InstaMonkey:WizardMonkey,022",
                  "mode": "Standard",
                  "id": 560,
                  "maxTowers": -1,
                  "seed": 1,
                  "bloonModifiers": {
                     "speedMultiplier": 1.2,
                     "moabSpeedMultiplier": 1.15,
                     "healthMultipliers": {
                        "bloons": 0.8,
                        "moabs": 0.55
                     },
                     "allCamo": false,
                     "allRegen": false
                  },
                  "disableMK": true,
                  "startRules": {
                     "lives": 1,
                     "cash": 7650,
                     "round": 40,
                     "maxLives": 1,
                     "endRound": 50
                  },
                  "name": "Ultratoxic183's hard ~By Ultratoxic183",
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
    #jd = json.load(j)
    jd = s2["rotationAdvanced"][i]
    #j.close()
    #print(i)

    out.write("===" + jd["name"] + "===\n")
    out.write("{{BTD6 challenge rules/new")
    out.write("\n|type=advancedChallenge")
    out.write(f"\n|date={i+13} December 2019")
    out.write(parse(jd))
    out.write("\n}}\n")

out.close()