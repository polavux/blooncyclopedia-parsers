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
s = """{"coopChallenges": {
            "coop1": {
               "numberOfPlayers": 4,
               "coopDivisionType": "VERTICAL",
               "replaces": "standard",
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
               "map": "Spillway",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:150#InstaMonkey:TackShooter,203",
               "mode": "Standard",
               "id": 1,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": 860,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Teamwork makes the Dreamwork",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop2": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "standard",
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
                     "max": 4,
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
               "map": "KartsNDarts",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:120#InstaMonkey:EngineerMonkey,200",
               "mode": "Standard",
               "id": 2,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Tech Race",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop3": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "rewards": "MonkeyMoney:110#InstaMonkey:TackShooter,022",
               "mode": "Standard",
               "id": 3,
               "maxTowers": 16,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "Best Buddies for Life",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop4": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "ParkPath",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:125#InstaMonkey:SniperMonkey,202",
               "mode": "DoubleMoabHealth",
               "id": 4,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": 860,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "MOAB incoming",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop5": {
               "numberOfPlayers": 2,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
               "map": "SpiceIslands",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:IceMonkey,320",
               "mode": "MilitaryOnly",
               "id": 5,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 50
               },
               "name": "Spicy",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop6": {
               "numberOfPlayers": 2,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "Chutes",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:150#InstaMonkey:MonkeySub,300",
               "mode": "Standard",
               "id": 6,
               "maxTowers": 15,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Double Trouble",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop7": {
               "numberOfPlayers": 4,
               "coopDivisionType": "VERTICAL",
               "replaces": "advanced",
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
                     "max": 4,
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
               "map": "FourCircles",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#Power:EnergisingTotem",
               "mode": "Standard",
               "id": 7,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": 856,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 63
               },
               "name": "Working together",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop8": {
               "numberOfPlayers": 2,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
               "map": "EndOfTheRoad",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#InstaMonkey:BananaFarm,003",
               "mode": "Standard",
               "id": 8,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 70
               },
               "name": "Top or Tail?",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop9": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
                     "max": 1,
                     "isHero": false
                  },
                  {
                     "tower": "EngineerMonkey",
                     "max": 0,
                     "isHero": false
                  }
               ],
               "map": "MoonLanding",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:DartMonkey,320",
               "mode": "Standard",
               "id": 9,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Green Space ",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop10": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
                     "max": 2,
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
                     "max": 0,
                     "isHero": false
                  },
                  {
                     "tower": "EngineerMonkey",
                     "max": 2,
                     "isHero": false
                  }
               ],
               "map": "Rake",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#CollectionEvent:18",
               "mode": "Reverse",
               "id": 10,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": 860,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Split decisions",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop11": {
               "numberOfPlayers": 4,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
                     "max": 4,
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
                     "max": 4,
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
                     "max": 4,
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
               "rewards": "MonkeyMoney:130#CollectionEvent:20",
               "mode": "AlternateBloonsRounds",
               "id": 11,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": 11832,
                  "round": 34,
                  "maxLives": -1,
                  "endRound": 88
               },
               "name": "Atlantis57's Challenge",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop12": {
               "numberOfPlayers": 4,
               "coopDivisionType": "DIAGONAL_LR",
               "replaces": "advanced",
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
               "map": "Carved",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#CollectionEvent:20",
               "mode": "MilitaryOnly",
               "id": 12,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Trouble in paradice",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop13": {
               "numberOfPlayers": 2,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
               "map": "Cubism",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:IceMonkey,022",
               "mode": "Standard",
               "id": 13,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "Slow Time",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop14": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "FrozenOver",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#Power:TechBot",
               "mode": "Standard",
               "id": 14,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Ice C what the problem is",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop15": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
                     "max": 0,
                     "isHero": false
                  }
               ],
               "map": "Carved",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:WizardMonkey,302",
               "mode": "Standard",
               "id": 15,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Spooky Friends",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": true,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop16": {
               "numberOfPlayers": 2,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
               "map": "TownCentre",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:EngineerMonkey,230",
               "mode": "Standard",
               "id": 16,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "Support Hacks",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop17": {
               "numberOfPlayers": 3,
               "coopDivisionType": "DIAGONAL_RL",
               "replaces": "advanced",
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
                     "max": 3,
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
               "rewards": "MonkeyMoney:130#Power:GlueTrap",
               "mode": "PrimaryOnly",
               "id": 17,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "Primary Shots",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop18": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "SpringSpring",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:Alchemist,310",
               "mode": "Reverse",
               "id": 18,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Hot Springs",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop19": {
               "numberOfPlayers": 2,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "AlpineRun",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#Power:BananaFarmer",
               "mode": "Standard",
               "id": 19,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "Cold Points",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop20": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "Carved",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#Power:DartTime",
               "mode": "Standard",
               "id": 20,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": 860,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 63
               },
               "name": "Warm soup",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop21": {
               "numberOfPlayers": 3,
               "coopDivisionType": "DIAGONAL_RL",
               "replaces": "advanced",
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
               "map": "MoonLanding",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:EngineerMonkey,220",
               "mode": "Standard",
               "id": 21,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Slightly Chilled Craters",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop22": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
                     "max": 2,
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
                     "max": 2,
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
                     "max": 2,
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
                     "max": 2,
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
                     "max": 2,
                     "isHero": false
                  }
               ],
               "map": "SpiceIslands",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:Druid,300",
               "mode": "Standard",
               "id": 22,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 70
               },
               "name": "Tropic Lightning",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop23": {
               "numberOfPlayers": 2,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
               "map": "Streambed",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:TackShooter,023",
               "mode": "Standard",
               "id": 23,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "Magic Steam",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop24": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "Spillway",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#Power:Pontoon",
               "mode": "Standard",
               "id": 24,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 50
               },
               "name": "Splosh",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop25": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "rewards": "MonkeyMoney:130#InstaMonkey:NinjaMonkey,203",
               "mode": "MagicOnly",
               "id": 25,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "Frozen Magic",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop26": {
               "numberOfPlayers": 2,
               "coopDivisionType": "VERTICAL",
               "replaces": "advanced",
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
               "map": "TownCentre",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:WizardMonkey,302",
               "mode": "Standard",
               "id": 26,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 50
               },
               "name": "Magic Spikes",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop27": {
               "numberOfPlayers": 4,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
                     "max": -1,
                     "isHero": false
                  }
               ],
               "map": "FourCircles",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#CollectionEvent:25",
               "mode": "Standard",
               "id": 27,
               "maxTowers": 50,
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
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "halo challenge ~By Yourmom",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop28": {
               "numberOfPlayers": 2,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "TreeStump",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#CollectionEvent:50",
               "mode": "Standard",
               "id": 28,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Christmas Cheer",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop29": {
               "numberOfPlayers": 4,
               "coopDivisionType": "DIAGONAL_RL",
               "replaces": "advanced",
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
               "map": "FrozenOver",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#CollectionEvent:25",
               "mode": "Standard",
               "id": 29,
               "maxTowers": 50,
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
                  "lives": 100,
                  "cash": -1,
                  "round": 1,
                  "maxLives": 100,
                  "endRound": 60
               },
               "name": "Artic Mission:By LStracck ~By LStracck",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop30": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
                     "max": -1,
                     "isHero": false
                  },
                  {
                     "tower": "EngineerMonkey",
                     "max": 0,
                     "isHero": false
                  }
               ],
               "map": "SpringSpring",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#CollectionEvent:50",
               "mode": "Standard",
               "id": 30,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "New Years Day",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop31": {
               "numberOfPlayers": 2,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
                     "max": 3,
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
               "rewards": "MonkeyMoney:130#InstaMonkey:BombShooter,320",
               "mode": "Standard",
               "id": 31,
               "maxTowers": 50,
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
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "Bloons go boom ~By EyeOfThe",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop32": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "KartsNDarts",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#Power:CashDrop",
               "mode": "Standard",
               "id": 32,
               "maxTowers": 50,
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
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "Wheres my camo!? ~By Player",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop33": {
               "numberOfPlayers": 4,
               "coopDivisionType": "HORIZONTAL",
               "replaces": "advanced",
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
               "map": "AdorasTemple",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:BoomerangMonkey,032",
               "mode": "Standard",
               "id": 33,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Mother of Sun God",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop34": {
               "numberOfPlayers": 2,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "WinterPark",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:BananaFarm,023",
               "mode": "Standard",
               "id": 34,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "A stroll for two",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop35": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#Power:GlueTrap",
               "mode": "Standard",
               "id": 35,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Blue fire",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop36": {
               "numberOfPlayers": 4,
               "coopDivisionType": "DIAGONAL_RL",
               "replaces": "advanced",
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
               "map": "Cubism",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#Power:MoabMine",
               "mode": "Standard",
               "id": 36,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "Tanky",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop37": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "Cubism",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:HeliPilot,320",
               "mode": "DoubleMoabHealth",
               "id": 37,
               "maxTowers": 50,
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
                  "cash": 2129,
                  "round": 9,
                  "maxLives": -1,
                  "endRound": 61
               },
               "name": "KiwiFreezer101's Challenge",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            },
            "coop38": {
               "numberOfPlayers": 2,
               "coopDivisionType": "DIAGONAL_LR",
               "replaces": "advanced",
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
               "rewards": "MonkeyMoney:130#InstaMonkey:IceMonkey,302",
               "mode": "Standard",
               "id": 38,
               "maxTowers": 50,
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
                  "lives": 111,
                  "cash": -1,
                  "round": 1,
                  "maxLives": 153,
                  "endRound": 59
               },
               "name": "RedKahuna56482's Challenge",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            },
            "coop39": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "InTheLoop",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:MonkeyAce,032",
               "mode": "Standard",
               "id": 39,
               "maxTowers": 50,
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
                  "cash": 900,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": " ~By ThatGuyPaper",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            },
            "coop40": {
               "numberOfPlayers": 2,
               "coopDivisionType": "VERTICAL",
               "replaces": "advanced",
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
                     "max": -1,
                     "isHero": false
                  }
               ],
               "map": "Haunted",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#Power:RoadSpikes",
               "mode": "Standard",
               "id": 40,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Haunted Darts",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop41": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "EndOfTheRoad",
               "difficulty": "Medium",
               "rewards": "MonkeyMoney:130#InstaMonkey:TackShooter,230",
               "mode": "Standard",
               "id": 41,
               "maxTowers": 16,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 60
               },
               "name": "Warm Ending",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop42": {
               "numberOfPlayers": 4,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
                     "max": 4,
                     "isHero": false
                  },
                  {
                     "tower": "SniperMonkey",
                     "max": 4,
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
               "rewards": "MonkeyMoney:130#InstaMonkey:GlueGunner,320",
               "mode": "Standard",
               "id": 42,
               "maxTowers": 50,
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
                  "lives": -1,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "Water Park",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": false
            },
            "coop43": {
               "numberOfPlayers": 2,
               "coopDivisionType": "VERTICAL",
               "replaces": "advanced",
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
               "map": "Tutorial",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#Power:CashDrop",
               "mode": "Standard",
               "id": 43,
               "maxTowers": 50,
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
                  "lives": 100,
                  "cash": 400,
                  "round": 1,
                  "maxLives": 1000000,
                  "endRound": 50
               },
               "name": "Player's Challenge ~By Player",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            },
            "coop44": {
               "numberOfPlayers": 3,
               "coopDivisionType": "FREE_FOR_ALL",
               "replaces": "advanced",
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
               "map": "ParkPath",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#Power:TechBot",
               "mode": "DoubleMoabHealth",
               "id": 44,
               "maxTowers": 50,
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
                  "cash": 850,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 80
               },
               "name": "sharp shooter's ~By wkrwk",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            },
            "coop45": {
               "numberOfPlayers": 4,
               "coopDivisionType": "VERTICAL",
               "replaces": "advanced",
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
                     "max": 1,
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
               "map": "Carved",
               "difficulty": "Hard",
               "rewards": "MonkeyMoney:130#InstaMonkey:MonkeyVillage,230",
               "mode": "Standard",
               "id": 45,
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
                  "lives": 500,
                  "cash": -1,
                  "round": 3,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "DartMaster5531's Challenge ~By DartMaster5531",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            },
            "coop46": {
               "numberOfPlayers": 2,
               "coopDivisionType": "DIAGONAL_RL",
               "replaces": "advanced",
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
                     "max": 0,
                     "isHero": false
                  }
               ],
               "map": "Cubism",
               "difficulty": "Easy",
               "rewards": "MonkeyMoney:130#InstaMonkey:SpikeFactory,203",
               "mode": "Standard",
               "id": 46,
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
                  "round": 1,
                  "maxLives": -1,
                  "endRound": 40
               },
               "name": "dhud384's Challenge ~By dhud384",
               "displayIncludedTowers": true,
               "disableSelling": false,
               "disablePowers": false,
               "noContinues": false,
               "noInstaReward": true
            }
         }
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

dayz = 1

for i in range(22, 22+9):
    #j = open(str(i) + ".json", "r", encoding="utf-8")
    jd = s2["coopChallenges"][f"coop{i}"]
    #j.close()
    #print(i)

    dayz += 3
    if i % 2 == 1: dayz += 1

    out.write("===" + jd["name"] + "===\n")
    out.write("{{BTD6 challenge rules/new")
    out.write("\n|type=coopChallenge")
    out.write(f"\n|date={dayz} December 2019")
    out.write(parse(jd))
    out.write("\n}}\n")

out.close()