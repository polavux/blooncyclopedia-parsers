import zlib, base64
import B2F_level_data

objects_by_numeric_id = ["Monkey", "BasicBloon", "BloomingBloon", "IceBloon", "BirdBloon", "TackBloon", "BombBloon", "BallBloon", "GravityBloon", "CamoBloon",
                         "MonkeyAceBloon", "TwoSkinnedBloon", "ThreeSkinnedBloon", "BonusDartBloon", "TripleDartBloon", "BoomerangBloon", "SolidBlock", "AngledBlockNE", "AngledBlockSE", "AngledBlockSW",
                         "AngledBlockNW", "DestructableBlock", "AngledDestructableBlockNE", "AngledDestructableBlockSE", "AngledDestructableBlockSW", "AngledDestructableBlockNW", "ReinforcedDestructableBlock", "AngledReinforcedDestructableBlockNE", "AngledReinforcedDestructableBlockSE", "AngledReinforcedDestructableBlockSW",
                         "AngledReinforcedDestructableBlockNW", "RubberBlock", "AngledRubberBlockNE", "AngledRubberBlockSE", "AngledRubberBlockSW", "AngledRubberBlockNW", "PerishedRubberBlock", "AngledPerishedRubberBlockNE", "AngledPerishedRubberBlockSE", "AngledPerishedRubberBlockSW",
                         "AngledPerishedRubberBlockNW", "UpFan", "DownFan", "LeftFan", "RightFan"]
zone_names = ["Popping Fields", "Bloon Dunes", "Frosty Fun", "Sneak Peeks", "Rubber Jungle", "The Temple of Bloon", "Crazy Coast", "Mount Magma", "Secret Zone"]
zone_links = ["[[Popping Fields]]", "[[Bloon Dunes (Bloons 2)|Bloon Dunes]]", "[[Frosty Fun]]", "[[Sneak Peeks]]", "[[Rubber Jungle]]", "[[Temple Of Bloon|The Temple of Bloon]]", "[[Crazy Coast]]", "[[Mount Magma (Bloons 2)|Mount Magma]]", "[[Pirate Cove (Bloons 2)|Secret Zone]]"]

def get_ordinal(num):
    if num > 10 and num < 20: return f"{num}th"

    match num % 10:
        case 1: return f"{num}st"
        case 2: return f"{num}nd"
        case 3: return f"{num}rd"
        case _: return f"{num}th"

# is there a better way to do this? probably. does it matter? no lol
def get_object_counts_output_formatted(entities):
    return (
        # bloons
        ("|bloon F="+str(entities['BasicBloon']) if str(entities['BasicBloon']) != "0" else "")
        + ("|tack F="+str(entities['TackBloon']) if str(entities['TackBloon']) != "0" else "")
        + ("|nested3 F="+str(entities['ThreeSkinnedBloon']) if str(entities['ThreeSkinnedBloon']) != "0" else "")
        + ("|nested2 F="+str(entities['TwoSkinnedBloon']) if str(entities['TwoSkinnedBloon']) != "0" else "")
        + ("|extra dart F="+str(entities['BonusDartBloon']) if str(entities['BonusDartBloon']) != "0" else "")
        + ("|triple shot F="+str(entities['TripleDartBloon']) if str(entities['TripleDartBloon']) != "0" else "")
        + ("|bee F="+str(entities['BirdBloon']) if str(entities['BirdBloon']) != "0" else "")
        + ("|spikey ball F="+str(entities['BallBloon']) if str(entities['BallBloon']) != "0" else "")
        + ("|blooming F="+str(entities['BloomingBloon']) if str(entities['BloomingBloon']) != "0" else "")
        + ("|bomb F="+str(entities['BombBloon']) if str(entities['BombBloon']) != "0" else "")
        + ("|ace F="+str(entities['MonkeyAceBloon']) if str(entities['MonkeyAceBloon']) != "0" else "")
        + ("|camo F="+str(entities['CamoBloon']) if str(entities['CamoBloon']) != "0" else "")
        + ("|boomerang F="+str(entities['BoomerangBloon']) if str(entities['BoomerangBloon']) != "0" else "")
        + ("|ice F="+str(entities['IceBloon']) if str(entities['IceBloon']) != "0" else "")
        + ("|reverse gravity F="+str(entities['GravityBloon']) if str(entities['GravityBloon']) != "0" else "")
        
        # blocks (count all variants of angled blocks as a single block)
        + ("|solid F="+str(entities['SolidBlock']) if str(entities['SolidBlock']) != "0" else "")
        + ("|angled solid F="+str(entities['AngledBlockNE']+entities['AngledBlockSE']+entities['AngledBlockSW']+entities['AngledBlockNW']) if str(entities['AngledBlockNE']+entities['AngledBlockSE']+entities['AngledBlockSW']+entities['AngledBlockNW']) != "0" else "")
        + ("|breakable F="+str(entities['DestructableBlock']) if str(entities['DestructableBlock']) != "0" else "")
        + ("|angled breakable F="+str(entities['AngledDestructableBlockNE']+entities['AngledDestructableBlockSE']+entities['AngledDestructableBlockSW']+entities['AngledDestructableBlockNW']) if str(entities['AngledDestructableBlockNE']+entities['AngledDestructableBlockSE']+entities['AngledDestructableBlockSW']+entities['AngledDestructableBlockNW']) != "0" else "")
        + ("|rubber F="+str(entities['RubberBlock']) if str(entities['RubberBlock']) != "0" else "")
        + ("|angled rubber F="+str(entities['AngledRubberBlockNE']+entities['AngledRubberBlockSE']+entities['AngledRubberBlockSW']+entities['AngledRubberBlockNW']) if str(entities['AngledRubberBlockNE']+entities['AngledRubberBlockSE']+entities['AngledRubberBlockSW']+entities['AngledRubberBlockNW']) != "0" else "")
        + ("|strong breakable F="+str(entities['ReinforcedDestructableBlock']) if str(entities['ReinforcedDestructableBlock']) != "0" else "")
        + ("|angled strong breakable F="+str(entities['AngledReinforcedDestructableBlockNE']+entities['AngledReinforcedDestructableBlockSE']+entities['AngledReinforcedDestructableBlockSW']+entities['AngledReinforcedDestructableBlockNW']) if str(entities['AngledReinforcedDestructableBlockNE']+entities['AngledReinforcedDestructableBlockSE']+entities['AngledReinforcedDestructableBlockSW']+entities['AngledReinforcedDestructableBlockNW']) != "0" else "")
        + ("|breakable rubber F="+str(entities['PerishedRubberBlock']) if str(entities['PerishedRubberBlock']) != "0" else "")
        + ("|angled breakable rubber F="+str(entities['AngledPerishedRubberBlockNE']+entities['AngledPerishedRubberBlockSE']+entities['AngledPerishedRubberBlockSW']+entities['AngledPerishedRubberBlockNW']) if str(entities['AngledPerishedRubberBlockNE']+entities['AngledPerishedRubberBlockSE']+entities['AngledPerishedRubberBlockSW']+entities['AngledPerishedRubberBlockNW']) != "0" else ""))

level_number = 0
zone_number = 0

try:
    with open("result.txt", "w", encoding="utf-8") as outfile:
        print("result.txt opened, beginning output")

        for zone in B2F_level_data.zones:
            zone_number += 1

            for level_data in zone:
                level_number += 1
                
                entities = {
                    'Monkey':0,
                    'BasicBloon':0,
                    'BloomingBloon':0,
                    'IceBloon':0,
                    'BirdBloon':0,
                    'TackBloon':0,
                    'BombBloon':0,
                    'BallBloon':0,
                    'GravityBloon':0,
                    'CamoBloon':0,
                    'MonkeyAceBloon':0,
                    'TwoSkinnedBloon':0,
                    'ThreeSkinnedBloon':0,
                    'BonusDartBloon':0,
                    'TripleDartBloon':0,
                    'BoomerangBloon':0,
                    'SolidBlock':0,
                    'AngledBlockNE':0,
                    'AngledBlockSE':0,
                    'AngledBlockSW':0,
                    'AngledBlockNW':0,
                    'DestructableBlock':0,
                    'AngledDestructableBlockNE':0,
                    'AngledDestructableBlockSE':0,
                    'AngledDestructableBlockSW':0,
                    'AngledDestructableBlockNW':0,
                    'ReinforcedDestructableBlock':0,
                    'AngledReinforcedDestructableBlockNE':0,
                    'AngledReinforcedDestructableBlockSE':0,
                    'AngledReinforcedDestructableBlockSW':0,
                    'AngledReinforcedDestructableBlockNW':0,
                    'RubberBlock':0,
                    'AngledRubberBlockNE':0,
                    'AngledRubberBlockSE':0,
                    'AngledRubberBlockSW':0,
                    'AngledRubberBlockNW':0,
                    'PerishedRubberBlock':0,
                    'AngledPerishedRubberBlockNE':0,
                    'AngledPerishedRubberBlockSE':0,
                    'AngledPerishedRubberBlockSW':0,
                    'AngledPerishedRubberBlockNW':0
                }

                # the level format stored in game is compressed with zlib and encoded in base64
                # this step does the decoding and decompressing
                decoded_bytes = zlib.decompress(base64.b64decode(level_data[1]))

                version = int.from_bytes(decoded_bytes[0:4], byteorder="big", signed=False)     # version           unsigned int (always 1)
                darts   = int.from_bytes(decoded_bytes[4:8], byteorder="big", signed=False)     # dartCount         unsigned int
                target  = int.from_bytes(decoded_bytes[8:12], byteorder="big", signed=False)    # targetCount       unsigned int
                background = decoded_bytes[13]                                                  # backgroundIndex   signed byte (unused, backgrounds are hardcoded, probably used in level builder)

                # everything else is an unsigned byte
                for obj in decoded_bytes[13:]:
                    # increment count of objects
                    object_id = objects_by_numeric_id[(obj % 50) - 1]
                    entities[object_id] = entities.get(object_id, 0) + 1

                total_bloons_in_level = 0
                + entities['BasicBloon']
                + entities['BloomingBloon'] * 8         # spawns 7 bloons when popped
                + entities['IceBloon']
                + entities['BirdBloon']
                + entities['TackBloon']
                + entities['BombBloon']
                + entities['BallBloon']
                + entities['GravityBloon']
                + entities['CamoBloon']
                + entities['MonkeyAceBloon']
                + entities['TwoSkinnedBloon'] * 2       # 2 layers
                + entities['ThreeSkinnedBloon'] * 3     # 3 layers
                + entities['BonusDartBloon']
                + entities['TripleDartBloon']
                + entities['BoomerangBloon']

                # this formats the data into a page ready for pymonkibot
                outfile.write(f"""{{{{-start-}}}}
    '''{level_data[0]}'''
    {{{{bot generated}}}}
    {{{{B2 level info
    |name F ={level_data[0]}
    |image F=B2F {level_data[0]}.png

    |level F={level_number}
    |zone_F ={zone_names[zone_number - 1]}

    |darts F ={darts}
    |target F={target}
    |total F ={total_bloons_in_level}

    {get_object_counts_output_formatted(entities)}
    }}}}
    '''{level_data[0]}''' is the {get_ordinal((level_number - 1) % 12 + 1)} level of {zone_links[zone_number - 1]} in the {{{{Flash version of|Bloons 2}}}}.

    ==Solution==
    {{{{empty}}}}
    {{{{clear|right}}}}
    ==Navigation==
    {{{{B2F level nav}}}}
    {{{{-stop-}}}}
    """)
                print(f"{level_number} - {level_data[0]}")
    print("Finished")

except Exception as e:

    print(f"An unexpected error occurred: {e}")
