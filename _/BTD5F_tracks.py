import os, math, numpy as np
s = """Vector.<Vector.<Tile>>([
    Vector.<Tile>([
    new StraightTile().ini_startPoint(new Vector2(42,-40)).ini_endPoint(new Vector2(42,41)).ini_nextTileIndices(Vector.<int>([1,7])).ini_transitionType(2),
    new StraightTile().ini_startPoint(new Vector2(42,41)).ini_endPoint(new Vector2(342,-50)).ini_nextTileIndices(Vector.<int>([2])).ini_transitionType(2),
    new StraightTile().ini_startPoint(new Vector2(342,-50)).ini_endPoint(new Vector2(440,29)).ini_nextTileIndices(Vector.<int>([3])).ini_transitionType(0),
    new ArcTile().ini_baseCentre(new Vector2(376.59499536607973,107.6543095458758)).ini_baseStart(new Vector2(440,29)).ini_baseEnd(new Vector2(410,203)).ini_reflex(false).ini_nextTileIndices(Vector.<int>([4])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(410,203)).ini_endPoint(new Vector2(254,294)).ini_nextTileIndices(Vector.<int>([5])).ini_transitionType(0),
    new ArcTile().ini_baseCentre(new Vector2(316.52159172019986,401.1798715203426)).ini_baseStart(new Vector2(254,294)).ini_baseEnd(new Vector2(272,517)).ini_reflex(false).ini_nextTileIndices(Vector.<int>([6])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(272,517)).ini_endPoint(new Vector2(338,569)).ini_nextTileIndices(Vector.<int>([])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(42,41)).ini_endPoint(new Vector2(-68,264)).ini_nextTileIndices(Vector.<int>([8])).ini_transitionType(2),
    new StraightTile().ini_startPoint(new Vector2(-68,264)).ini_endPoint(new Vector2(11,202)).ini_nextTileIndices(Vector.<int>([9])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(11,202)).ini_endPoint(new Vector2(80,116)).ini_nextTileIndices(Vector.<int>([10])).ini_transitionType(0),
    new ArcTile().ini_baseCentre(new Vector2(151.03994966970745,172.99716892104436)).ini_baseStart(new Vector2(80,116)).ini_baseEnd(new Vector2(178,86)).ini_reflex(false).ini_nextTileIndices(Vector.<int>([11])).ini_transitionType(0),
    new ArcTile().ini_baseCentre(new Vector2(-79.613555843494,917.2911051536659)).ini_baseStart(new Vector2(178,86)).ini_baseEnd(new Vector2(267,119)).ini_reflex(false).ini_nextTileIndices(Vector.<int>([12])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(267,119)).ini_endPoint(new Vector2(389,348)).ini_nextTileIndices(Vector.<int>([13])).ini_transitionType(0),
    new ArcTile().ini_baseCentre(new Vector2(478.5624260004736,300.28551977267347)).ini_baseStart(new Vector2(389,348)).ini_baseEnd(new Vector2(491,401)).ini_reflex(false).ini_nextTileIndices(Vector.<int>([14])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(491,401)).ini_endPoint(new Vector2(521,402)).ini_nextTileIndices(Vector.<int>([15])).ini_transitionType(0),
    new ArcTile().ini_baseCentre(new Vector2(525.7057919015889,260.8262429523321)).ini_baseStart(new Vector2(521,402)).ini_baseEnd(new Vector2(642,341)).ini_reflex(false).ini_nextTileIndices(Vector.<int>([16])).ini_transitionType(0),
    new StraightTile().ini_startPoint(new Vector2(642,341)).ini_endPoint(new Vector2(757,226)).ini_nextTileIndices(Vector.<int>([])).ini_transitionType(0)])]);
"""
s = """Vector.<Vector.<Tile>>([
    Vector.<Tile>([
        new StraightTile().ini_startPoint(new Vector2(600,600)).ini_endPoint(new Vector2(600,593)).ini_nextTileIndices(Vector.<int>([1])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(600,593)).ini_endPoint(new Vector2(531,407)).ini_nextTileIndices(Vector.<int>([2])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(531,407)).ini_endPoint(new Vector2(481,305)).ini_nextTileIndices(Vector.<int>([3])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(481,305)).ini_endPoint(new Vector2(448,257)).ini_nextTileIndices(Vector.<int>([4])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(448,257)).ini_endPoint(new Vector2(401,215)).ini_nextTileIndices(Vector.<int>([5])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(401,215)).ini_endPoint(new Vector2(368,205)).ini_nextTileIndices(Vector.<int>([6])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(368,205)).ini_endPoint(new Vector2(345,206)).ini_nextTileIndices(Vector.<int>([7])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(345,206)).ini_endPoint(new Vector2(310,217)).ini_nextTileIndices(Vector.<int>([8])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(310,217)).ini_endPoint(new Vector2(275,247)).ini_nextTileIndices(Vector.<int>([9])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(275,247)).ini_endPoint(new Vector2(234,304)).ini_nextTileIndices(Vector.<int>([10])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(234,304)).ini_endPoint(new Vector2(192,388)).ini_nextTileIndices(Vector.<int>([11])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(192,388)).ini_endPoint(new Vector2(113,604)).ini_nextTileIndices(Vector.<int>([])).ini_transitionType(0).ini_layer(0)]),
    Vector.<Tile>([
        new StraightTile().ini_startPoint(new Vector2(-99,477)).ini_endPoint(new Vector2(80,436)).ini_nextTileIndices(Vector.<int>([1])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(80,436)).ini_endPoint(new Vector2(211,398)).ini_nextTileIndices(Vector.<int>([2])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(211,398)).ini_endPoint(new Vector2(298,365)).ini_nextTileIndices(Vector.<int>([3])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(298,365)).ini_endPoint(new Vector2(375,320)).ini_nextTileIndices(Vector.<int>([4])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(375,320)).ini_endPoint(new Vector2(396,290)).ini_nextTileIndices(Vector.<int>([5])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(396,290)).ini_endPoint(new Vector2(399,263)).ini_nextTileIndices(Vector.<int>([6])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(399,263)).ini_endPoint(new Vector2(395,238)).ini_nextTileIndices(Vector.<int>([7])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(395,238)).ini_endPoint(new Vector2(367,208)).ini_nextTileIndices(Vector.<int>([8])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(367,208)).ini_endPoint(new Vector2(327,179)).ini_nextTileIndices(Vector.<int>([9])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(327,179)).ini_endPoint(new Vector2(241,144)).ini_nextTileIndices(Vector.<int>([10])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(241,144)).ini_endPoint(new Vector2(93,99)).ini_nextTileIndices(Vector.<int>([11])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(93,99)).ini_endPoint(new Vector2(-103,54)).ini_nextTileIndices(Vector.<int>([])).ini_transitionType(0).ini_layer(0)
    ]),
    Vector.<Tile>([
        new StraightTile().ini_startPoint(new Vector2(108,-91)).ini_endPoint(new Vector2(191,139)).ini_nextTileIndices(Vector.<int>([1])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(191,139)).ini_endPoint(new Vector2(231,221)).ini_nextTileIndices(Vector.<int>([2])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(231,221)).ini_endPoint(new Vector2(279,287)).ini_nextTileIndices(Vector.<int>([3])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(279,287)).ini_endPoint(new Vector2(311,313)).ini_nextTileIndices(Vector.<int>([4])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(311,313)).ini_endPoint(new Vector2(340,323)).ini_nextTileIndices(Vector.<int>([5])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(340,323)).ini_endPoint(new Vector2(379,323)).ini_nextTileIndices(Vector.<int>([6])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(379,323)).ini_endPoint(new Vector2(416,305)).ini_nextTileIndices(Vector.<int>([7])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(416,305)).ini_endPoint(new Vector2(449,266)).ini_nextTileIndices(Vector.<int>([8])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(449,266)).ini_endPoint(new Vector2(484,217)).ini_nextTileIndices(Vector.<int>([9])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(484,217)).ini_endPoint(new Vector2(532,117)).ini_nextTileIndices(Vector.<int>([10])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(532,117)).ini_endPoint(new Vector2(608,-89)).ini_nextTileIndices(Vector.<int>([])).ini_transitionType(0).ini_layer(0)
    ]),
    Vector.<Tile>([
        new StraightTile().ini_startPoint(new Vector2(816,58)).ini_endPoint(new Vector2(596,108)).ini_nextTileIndices(Vector.<int>([1])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(596,108)).ini_endPoint(new Vector2(470,149)).ini_nextTileIndices(Vector.<int>([2])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(470,149)).ini_endPoint(new Vector2(382,186)).ini_nextTileIndices(Vector.<int>([3])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(382,186)).ini_endPoint(new Vector2(333,221)).ini_nextTileIndices(Vector.<int>([4])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(333,221)).ini_endPoint(new Vector2(311,254)).ini_nextTileIndices(Vector.<int>([5])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(311,254)).ini_endPoint(new Vector2(311,277)).ini_nextTileIndices(Vector.<int>([6])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(311,277)).ini_endPoint(new Vector2(325,301)).ini_nextTileIndices(Vector.<int>([7])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(325,301)).ini_endPoint(new Vector2(354,332)).ini_nextTileIndices(Vector.<int>([8])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(354,332)).ini_endPoint(new Vector2(395,356)).ini_nextTileIndices(Vector.<int>([9])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(395,356)).ini_endPoint(new Vector2(460,386)).ini_nextTileIndices(Vector.<int>([10])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(460,386)).ini_endPoint(new Vector2(591,428)).ini_nextTileIndices(Vector.<int>([11])).ini_transitionType(0).ini_layer(0),
        new StraightTile().ini_startPoint(new Vector2(591,428)).ini_endPoint(new Vector2(811,484)).ini_nextTileIndices(Vector.<int>([])).ini_transitionType(0).ini_layer(0)
    ])
]);"""

for i in os.listdir('delooxe'):
    if i not in ["BloonHengePillarsDef.as"]: continue
    
    f = open(f'delooxe/{i}', 'r', encoding='utf-8')
    fd = f.read()

    tiles = []

    start = fd.find('tileSets = ') + 11
    #print(start)

    end = fd[start:].find(';') - 4

    print('===', i, '===')

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
            #print(len)

        if tile['transition'] == 2: len = 0

        for t in tile['next']:
            for tt in calc_length(tiles[t]):
                lens.append(len + tt)

        if lens == []: return [len]
        return lens


    # alternating paths have separate tile groups
    for j in fd[start:start+end].split('Vector.<Tile>([new ')[1:]:
        tiles = []

        # split tiles in group
        for k in j.split(',new '):
            #print(k)
            tile = {}

            # parse tiles
            for x in k.split(').'):
                if 'ini_startPoint' in x: tile['p_start'] = [x.replace('ini_startPoint(new Vector2(', '').replace('))', '').split(',')[0],x.replace('ini_startPoint(new Vector2(', '').replace(')', '').split(',')[1]]
                elif 'ini_endPoint' in x: tile['p_end'] = [x.replace('ini_endPoint(new Vector2(', '').replace('))', '').split(',')[0],x.replace('ini_endPoint(new Vector2(', '').replace(')', '').split(',')[1]]
                elif 'ini_baseCentre' in x: tile['b_center'] = [x.replace('ini_baseCentre(new Vector2(', '').replace('))', '').split(',')[0],x.replace('ini_baseCentre(new Vector2(', '').replace(')', '').split(',')[1]]
                elif 'ini_baseStart' in x: tile['b_start'] = [x.replace('ini_baseStart(new Vector2(', '').replace('))', '').split(',')[0],x.replace('ini_baseStart(new Vector2(', '').replace(')', '').split(',')[1]]
                elif 'ini_baseEnd' in x: tile['b_end'] = [x.replace('ini_baseEnd(new Vector2(', '').replace('))', '').split(',')[0],x.replace('ini_baseEnd(new Vector2(', '').replace(')', '').split(',')[1]]
                elif 'ini_reflex' in x: tile['reflex'] = eval(x.replace('ini_reflex(', '').capitalize())
                
                elif 'ini_transitionType' in x: tile['transition'] = int(x.replace('ini_transitionType(','').replace(')',""))
                elif 'ini_layer' in x: tile['layer'] = int(x.replace('ini_layer(','').replace(')',""))
                elif 'ini_nextTileIndices(Vector.<int>(' in x:
                    x2 = x.replace('ini_nextTileIndices(Vector.<int>(', '').replace(')', '')
                    #print(x2)
                    tile['next'] = eval(x2)

            tiles.append(tile)

            #print(tile)

    #print(round(tlen, 2))
        gbssrb = []
        for i in calc_length(tiles[0]): gbssrb.append(f"{i:.2f}")
        print(gbssrb)

    if '§6j§ = true' in fd: print('coop')
    print(fd[fd.find('music = '):fd.find('music = ') + 30])
    
    #print(i, fd[start:start+end].split('Vector.<Tile>(['))

    f.close()