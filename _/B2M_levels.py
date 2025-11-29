import xml.etree.ElementTree as ET

zone_names = ["Popping Fields", "Bloon Dunes", "Frosty Fun", "Sneak Peeks", "Rubber Jungle", "Temple Of Bloon", "Crazy Coast", "Mount Magma", "Pirate Cove"]

zone_links = {
    '0': "[[Popping Fields]]",
    '1': "[[Bloon Dunes (Bloons 2)|Bloon Dunes]]",
    '2': "[[Frosty Fun]]",
    '3': "[[Sneak Peaks]]",
    '4': "[[Rubber Jungle]]",
    '5': "[[Temple Of Bloon]]",
    '6': "[[Crazy Coast]]",
    '7': "[[Mount Magma (Bloons 2)|Mount Magma]]",
    '8': "[[Pirate Cove (Bloons 2)|Pirate Cove]]"
}

def get_ordinal(num):
	if num > 10 and num < 20: return f"{num}th"

	match num % 10:
		case 1: return f"{num}st"
		case 2: return f"{num}nd"
		case 3: return f"{num}rd"
		case _: return f"{num}th"

f = open("pywiki_B2M_levels.txt", "w")

# levels 1-108
for i in range(1,109):
    with ET.parse(f'{i:03d}.xml').getroot() as level_data:

        entities = {
            'Monkey':0,
            'Bloon':0,
            'Blooming':0,
            'Ice':0,
            'Bee':0,
            'Tack':0,
            'Bomb':0,
            'SpikeyBall':0,
            'ReverseGravity':0,
            'Camo':0,
            'MonkeyAceBloon':0,
            'Layered2':0,
            'Layered3':0,
            'ExtraDart':0,
            'TripleShot':0,
            'Boomerang':0,
            'SolidBlock':0,
            'AngledSolidBlock':0,
            'BreakableBlock':0,
            'AngledBreakableBlock':0,
            'StrongBreakableBlock':0,
            'AngledStrongBreakableBlock':0,
            'RubberBlock':0,
            'AngledRubberBlock':0,
            'BreakableRubberBlock':0,
            'AngledBreakableRubberBlock':0
        }

        for j in level_data[1]:
            if j.attrib['type'] == "Layered":
                if j.attrib['Lives'] == '3':
                    entities["Layered3"] += 1
                    total_bloons_in_level += 3 # 3 layers
                elif j.attrib['Lives'] == '2':
                    entities["Layered2"] += 1
                    total_bloons_in_level += 2 # 2 layers
                    
            elif j.attrib['type'] == "Blooming":
                entities["Blooming"] += 1
                total_bloons_in_level += 8 # spawns 7 bloons when popped

        level_number = int(i) % 12
        if level_number == 0: level_number = 12

        level_name = level_data.attrib['name']

        str = f"""{{{{-start-}}}}
'''{level_name}'''
{{{{bot generated}}}}
{{{{B2 level info
|name M ={level_name}
|image M=B2M {level_name}.png

|level M={i}
|zone M ={zone_names[int(level_data[0][1].attrib['number'])]}

|darts M ={level_data[0][2].attrib['number']}
|target M={level_data[0][3].attrib['number']}
|total M ={total_bloons_in_level}

|bloon M={8}
|tack M={9}
|nested3 M={10}
|nested2 M={11}
|extra dart M={13}
|triple shot M={14}
|bee M={15}
|spikey ball M={16}
|blooming M={17}
|bomb M={18}
|ace M={19}
|camo M={20}
|boomerang M={21}
|ice M={22}
|reverse gravity M={23}
|solid M={24}
|angled solid M={25}
|breakable M={26}
|angled breakable M={27}
|rubber M={28}
|angled rubber M={29}
|strong breakable M={30}
|angled strong breakable M={31}
|breakable rubber M={32}
|angled breakable rubber M={33}
}}}}
'''{level_name}''' is the {5} level of {6} in the [[Bloons 2 (mobile)|mobile version of ''Bloons 2'']].

==Solution==
{{{{empty}}}}
{{{{clear|right}}}}
==Navigation==
{{{{B2M level nav}}}}
{{{{-stop-}}}}
""".format(myroot[0][0].attrib['name'], , myroot[0][2].attrib['number'], myroot[0][3].attrib['number'], total_bloons_in_level, suffix(level_number), zone, suffix(i),
           bloons, tacks, nests3, nests2, nests1, extras, triples, bees, spikeys, blooms, bombs, aces, camos, booms, ices, revs,
           solids, angsolids, breaks, angbreaks, rubs, angrubs, strongs, angstrongs, brubs, angbrubs, i)
        f.write(str)
f.close()