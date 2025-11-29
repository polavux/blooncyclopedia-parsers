import os, math, numpy as np
s = """Vector.<Vector.<Tile>>([
    Vector.<Tile>([
    new StraightTile().§5\'§(new §52§(42,-40)).§6I§(new §52§(42,41)).§+\'§(Vector.<int>([1,7])).§&I§(2),
    new StraightTile().§5\'§(new §52§(42,41)).§6I§(new §52§(342,-50)).§+\'§(Vector.<int>([2])).§&I§(2),
    new StraightTile().§5\'§(new §52§(342,-50)).§6I§(new §52§(440,29)).§+\'§(Vector.<int>([3])).§&I§(0),
    new ArcTile().§!3§(new §52§(376.59499536607973,107.6543095458758)).§]Y§(new §52§(440,29)).§`&§(new §52§(410,203)).§^P§(false).§+\'§(Vector.<int>([4])).§&I§(0),
    new StraightTile().§5\'§(new §52§(410,203)).§6I§(new §52§(254,294)).§+\'§(Vector.<int>([5])).§&I§(0),
    new ArcTile().§!3§(new §52§(316.52159172019986,401.1798715203426)).§]Y§(new §52§(254,294)).§`&§(new §52§(272,517)).§^P§(false).§+\'§(Vector.<int>([6])).§&I§(0),
    new StraightTile().§5\'§(new §52§(272,517)).§6I§(new §52§(338,569)).§+\'§(Vector.<int>([])).§&I§(0),
    new StraightTile().§5\'§(new §52§(42,41)).§6I§(new §52§(-68,264)).§+\'§(Vector.<int>([8])).§&I§(2),
    new StraightTile().§5\'§(new §52§(-68,264)).§6I§(new §52§(11,202)).§+\'§(Vector.<int>([9])).§&I§(0),
    new StraightTile().§5\'§(new §52§(11,202)).§6I§(new §52§(80,116)).§+\'§(Vector.<int>([10])).§&I§(0),
    new ArcTile().§!3§(new §52§(151.03994966970745,172.99716892104436)).§]Y§(new §52§(80,116)).§`&§(new §52§(178,86)).§^P§(false).§+\'§(Vector.<int>([11])).§&I§(0),
    new ArcTile().§!3§(new §52§(-79.613555843494,917.2911051536659)).§]Y§(new §52§(178,86)).§`&§(new §52§(267,119)).§^P§(false).§+\'§(Vector.<int>([12])).§&I§(0),
    new StraightTile().§5\'§(new §52§(267,119)).§6I§(new §52§(389,348)).§+\'§(Vector.<int>([13])).§&I§(0),
    new ArcTile().§!3§(new §52§(478.5624260004736,300.28551977267347)).§]Y§(new §52§(389,348)).§`&§(new §52§(491,401)).§^P§(false).§+\'§(Vector.<int>([14])).§&I§(0),
    new StraightTile().§5\'§(new §52§(491,401)).§6I§(new §52§(521,402)).§+\'§(Vector.<int>([15])).§&I§(0),
    new ArcTile().§!3§(new §52§(525.7057919015889,260.8262429523321)).§]Y§(new §52§(521,402)).§`&§(new §52§(642,341)).§^P§(false).§+\'§(Vector.<int>([16])).§&I§(0),
    new StraightTile().§5\'§(new §52§(642,341)).§6I§(new §52§(757,226)).§+\'§(Vector.<int>([])).§&I§(0)])]);
"""
s = """Vector.<Vector.<Tile>>([
    Vector.<Tile>([
        new StraightTile().§5\'§(new §52§(600,600)).§6I§(new §52§(600,593)).§+\'§(Vector.<int>([1])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(600,593)).§6I§(new §52§(531,407)).§+\'§(Vector.<int>([2])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(531,407)).§6I§(new §52§(481,305)).§+\'§(Vector.<int>([3])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(481,305)).§6I§(new §52§(448,257)).§+\'§(Vector.<int>([4])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(448,257)).§6I§(new §52§(401,215)).§+\'§(Vector.<int>([5])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(401,215)).§6I§(new §52§(368,205)).§+\'§(Vector.<int>([6])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(368,205)).§6I§(new §52§(345,206)).§+\'§(Vector.<int>([7])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(345,206)).§6I§(new §52§(310,217)).§+\'§(Vector.<int>([8])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(310,217)).§6I§(new §52§(275,247)).§+\'§(Vector.<int>([9])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(275,247)).§6I§(new §52§(234,304)).§+\'§(Vector.<int>([10])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(234,304)).§6I§(new §52§(192,388)).§+\'§(Vector.<int>([11])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(192,388)).§6I§(new §52§(113,604)).§+\'§(Vector.<int>([])).§&I§(0).§;=§(0)]),
    Vector.<Tile>([
        new StraightTile().§5\'§(new §52§(-99,477)).§6I§(new §52§(80,436)).§+\'§(Vector.<int>([1])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(80,436)).§6I§(new §52§(211,398)).§+\'§(Vector.<int>([2])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(211,398)).§6I§(new §52§(298,365)).§+\'§(Vector.<int>([3])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(298,365)).§6I§(new §52§(375,320)).§+\'§(Vector.<int>([4])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(375,320)).§6I§(new §52§(396,290)).§+\'§(Vector.<int>([5])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(396,290)).§6I§(new §52§(399,263)).§+\'§(Vector.<int>([6])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(399,263)).§6I§(new §52§(395,238)).§+\'§(Vector.<int>([7])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(395,238)).§6I§(new §52§(367,208)).§+\'§(Vector.<int>([8])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(367,208)).§6I§(new §52§(327,179)).§+\'§(Vector.<int>([9])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(327,179)).§6I§(new §52§(241,144)).§+\'§(Vector.<int>([10])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(241,144)).§6I§(new §52§(93,99)).§+\'§(Vector.<int>([11])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(93,99)).§6I§(new §52§(-103,54)).§+\'§(Vector.<int>([])).§&I§(0).§;=§(0)
    ]),
    Vector.<Tile>([
        new StraightTile().§5\'§(new §52§(108,-91)).§6I§(new §52§(191,139)).§+\'§(Vector.<int>([1])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(191,139)).§6I§(new §52§(231,221)).§+\'§(Vector.<int>([2])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(231,221)).§6I§(new §52§(279,287)).§+\'§(Vector.<int>([3])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(279,287)).§6I§(new §52§(311,313)).§+\'§(Vector.<int>([4])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(311,313)).§6I§(new §52§(340,323)).§+\'§(Vector.<int>([5])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(340,323)).§6I§(new §52§(379,323)).§+\'§(Vector.<int>([6])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(379,323)).§6I§(new §52§(416,305)).§+\'§(Vector.<int>([7])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(416,305)).§6I§(new §52§(449,266)).§+\'§(Vector.<int>([8])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(449,266)).§6I§(new §52§(484,217)).§+\'§(Vector.<int>([9])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(484,217)).§6I§(new §52§(532,117)).§+\'§(Vector.<int>([10])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(532,117)).§6I§(new §52§(608,-89)).§+\'§(Vector.<int>([])).§&I§(0).§;=§(0)
    ]),
    Vector.<Tile>([
        new StraightTile().§5\'§(new §52§(816,58)).§6I§(new §52§(596,108)).§+\'§(Vector.<int>([1])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(596,108)).§6I§(new §52§(470,149)).§+\'§(Vector.<int>([2])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(470,149)).§6I§(new §52§(382,186)).§+\'§(Vector.<int>([3])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(382,186)).§6I§(new §52§(333,221)).§+\'§(Vector.<int>([4])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(333,221)).§6I§(new §52§(311,254)).§+\'§(Vector.<int>([5])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(311,254)).§6I§(new §52§(311,277)).§+\'§(Vector.<int>([6])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(311,277)).§6I§(new §52§(325,301)).§+\'§(Vector.<int>([7])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(325,301)).§6I§(new §52§(354,332)).§+\'§(Vector.<int>([8])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(354,332)).§6I§(new §52§(395,356)).§+\'§(Vector.<int>([9])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(395,356)).§6I§(new §52§(460,386)).§+\'§(Vector.<int>([10])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(460,386)).§6I§(new §52§(591,428)).§+\'§(Vector.<int>([11])).§&I§(0).§;=§(0),
        new StraightTile().§5\'§(new §52§(591,428)).§6I§(new §52§(811,484)).§+\'§(Vector.<int>([])).§&I§(0).§;=§(0)
    ])
]);"""

of = open("a.txt", "w", encoding="utf-8")

for i in os.listdir('bat'):    
    f = open(f'bat/{i}', 'r', encoding='utf-8')
    fd = f.read()

    tiles = []

    start = fd.find("§'T§ = ") + 7

    end = fd[start:].find('])]);')

    of.write('\n===' + fd[fd.find('name = ')+8:fd[fd.find('name = '):].find('";')+fd.find('name = ')] + "|"+ fd[fd.find('id = ')+6:fd.find('";')]+ '===\n')
    #of.write(start, end)

    tlen = 0

    def calc_length(tile):
        lens = []
        # arc tile
        if 'b_center' in tile:
            
            v_center = np.array([float(tile['b_center'][0]), float(tile['b_center'][1])])
            v_start = np.array([float(tile['b_start'][0]), float(tile['b_start'][1])])
            v_end = np.array([float(tile['b_end'][0]), float(tile['b_end'][1])])

            loc2 = v_start-v_center
            loc3 = v_end-v_center

            loc4 = np.linalg.norm(loc2)
            loc5 = math.acos(np.dot(loc2, loc3) / (np.linalg.norm(loc2)*np.linalg.norm(loc3)))
            if tile['reflex']:
                loc5 = 2 * math.pi - loc5

            len = loc5 * loc4

        # straight tile
        else:
            len = d = math.sqrt((float(eval(tile['p_start'][0])) - float(eval(tile['p_end'][0])))**2 +(float(eval(tile['p_start'][1])) - float(eval(tile['p_end'][1])))**2)
            #of.write(len)

        if tile['transition'] == 2: len = 0

        for t in tile['next']:
            for tt in calc_length(tiles[t]):
                lens.append(len + tt)

        if lens == []: return [len]
        return lens
#Vector.<Tile>([new


    #if '§6j§ = true' in fd: of.write('coop')
    of.write(fd[fd.find('music = '):fd.find('music = ') + 20])
    
    # alternating paths have separate tile groups
    for j in fd[start:start+end].split('Vector.<§7;§>([new ')[1:]:
        #of.write(j)
        jj = j.replace(")]),", ")")
        tiles = []

        # split tiles in group
        for k in jj.split(',new '):
            #of.write(k)
            tile = {}

            # parse tiles
            for x in k.split(').'):
                #of.write(x)
                #of.write(x)
                if '§5\'§' in x: tile['p_start'] = [x.replace('§5\'§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§5\'§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§6I§' in x: tile['p_end'] = [x.replace('§6I§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§6I§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§!3§' in x: tile['b_center'] = [x.replace('§!3§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§!3§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§]Y§' in x: tile['b_start'] = [x.replace('§]Y§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§]Y§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§`&§' in x: tile['b_end'] = [x.replace('§`&§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§`&§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§^P§' in x: tile['reflex'] = eval(x.replace('§^P§(', '').capitalize())
                
                elif '§&I§' in x: tile['transition'] = int(x.replace('§&I§(','').replace(')',""))
                elif '§;=§' in x: tile['layer'] = int(x.replace('§;=§(','').replace(')',""))
                elif '§+\'§(Vector.<int>(' in x:
                    x2 = x.replace('§+\'§(Vector.<int>(', '').replace(')', '')
                    #of.write(x2)
                    tile['next'] = eval(x2)

            tiles.append(tile)

            #of.write(tile)

    #of.write(round(tlen, 2))
        gbssrb = []
        for i in calc_length(tiles[0]): gbssrb.append(f"{i:.2f}")
        of.write(', '.join(gbssrb) + '\n')




    start = fd.find("§[X§ = ") + 7

    end = fd[start:].find('])]);')


        
    # alternating paths have separate tile groups
    for j in fd[start:start+end].split('Vector.<§7;§>([new ')[1:]:
        #of.write(j)
        jj = j.replace(")]),", ")")
        tiles = []

        # split tiles in group
        for k in jj.split(',new '):
            #of.write(k)
            tile = {}

            # parse tiles
            for x in k.split(').'):
                #of.write(x)
                #of.write(x)
                if '§5\'§' in x: tile['p_start'] = [x.replace('§5\'§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§5\'§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§6I§' in x: tile['p_end'] = [x.replace('§6I§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§6I§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§!3§' in x: tile['b_center'] = [x.replace('§!3§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§!3§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§]Y§' in x: tile['b_start'] = [x.replace('§]Y§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§]Y§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§`&§' in x: tile['b_end'] = [x.replace('§`&§(new §52§(', '').replace('))', '').split(',')[0],x.replace('§`&§(new §52§(', '').replace(')', '').split(',')[1]]
                elif '§^P§' in x: tile['reflex'] = eval(x.replace('§^P§(', '').capitalize())
                
                elif '§&I§' in x: tile['transition'] = int(x.replace('§&I§(','').replace(')',""))
                elif '§;=§' in x: tile['layer'] = int(x.replace('§;=§(','').replace(')',""))
                elif '§+\'§(Vector.<int>(' in x:
                    x2 = x.replace('§+\'§(Vector.<int>(', '').replace(')', '')
                    #of.write(x2)
                    tile['next'] = eval(x2)

            tiles.append(tile)

            #of.write(tile)

    #of.write(round(tlen, 2))
        gbssrb = []
        for i in calc_length(tiles[0]): gbssrb.append(f"{i:.2f}")
        of.write(', '.join(gbssrb) + '\n')
    
    #of.write(i, fd[start:start+end].split('Vector.<Tile>(['))

    f.close()
of.close()