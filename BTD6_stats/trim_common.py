import copy

def combiner(a, b):
    ret = a
    for k,v in b.items():
        ret[k].update(v)

    return ret

def add_sub(parent, children, reverse=False, owner_name=""):
    if "_order" not in parent: parent["_order"] = []
    #print(owner_name)
    for k, v in children.items():
        namek = name(k)

        if owner_name not in towers_cleanup or namek not in towers_cleanup[owner_name]:
            if namek not in parent["_order"]:
                if reverse: parent["_order"].insert(0, namek)
                else: parent["_order"].append(namek)
            
            parent[namek] = {kk:vv for (kk,vv) in v.items() if (vv != {} and vv != {
                "_order": []
            })}

def get_model_name(model):
    return model["$type"].split(".")[-1].split(",")[0]

def get_obj_name(model):
    l = model["name"].split('_', 1)
    if len(l) >= 2: return l[1]
    else: return ""

def frnd(amt):
    if amt == "NaN": return 999999999
    r = round(amt, 4)
    if str(r)[-1] == '0' and str(r) != '0': return int(str(r)[:-2])
    return r

def filt(array):
    filts = dict()
    if array:
        for i in array:
            match get_model_name(i):
                case 'FilterInvisibleModel': filts["filterInvisible"] = i["isActive"]
                case 'FilterOnlyCamoInModel': filts['filterOutNonCamo'] = True
                case 'FilterInvisibleSubIntelModel': filts["filterInvisible"] = i["isActive"]
                case 'FilterBloonsToWithinAngleModel': filts['filterBloonsToWithinAngle'] = frnd(i["angleDegrees"])
                case 'FilterOfftrackModel': filts["filterOfftrack"] = True
                case 'FilterGlueLevelModel': filts['filterGlueLevel'] = i["glueLevel"]
                case 'FilterAllExceptTargetModel': filts['filterAllExceptTarget'] = True
                case 'FilterMoabModel':
                    if i['flip']: filts['filterOutMoabs'] = True
                    else: filts['filterOutNonMoabs'] = True
                case 'FilterOutBloonModel':
                    match(i["bloonId"]):
                        case "Ceramic": filts["filterOutCeramic"] = True
                        case "Bad": filts["filterOutBad"] = True
                        case 'Zomg': filts["filterOutZomg"] = True

                case 'FilterFrozenBloonsModel': filts['filterOutFrozen'] = True

                case 'FilterWithTagModel':
                    if i['inclusive']:
                        match(i['tag']):
                            case 'Moabs': filts['filterOutMoabs'] = True
                            case 'Camo': filts['filterOutCamo'] = True
                            case 'Grow': filts['filterOutGrow'] = True
                            case 'Lead': filts['filterOutLead'] = True
                            case 'Boss': filts['filterOutBoss'] = True
                            case _: print("UNKNOWN FILTWITHTAGA", i['tag'])
                    else:
                        match(i['tag']):
                            case 'Moabs': filts['filterOutNonMoabs'] = True
                            case 'Camo': filts['filterOutNonCamo'] = True
                            case 'Grow': filts['filterOutNonGrow'] = True
                            case 'Lead': filts['filterOutNonLead'] = True
                            case 'Boss': filts['filterOutNonBoss'] = True
                            case _: print("UNKNOWN FILTWITHTAGB", i['tag'])
                    
                case "FilterWithTagsModel":
                    if i['inclusive']:
                        for j in i['tags']:
                            match(j):
                                case "Moabs": filts['filterOutMoabs'] = True
                                case "Camo": filts['filterOutCamo'] = True
                                case "Grow": filts['filterOutGrow'] = True
                                case "Lead": filts['filterOutLead'] = True
                                case "Boss": filts['filterOutBoss'] = True
                                case 'Bfb': filts['filterOutBfb'] = True
                                case 'Zomg': filts['filterOutZomg'] = True
                                case 'Ddt': filts['filterOutDdt'] = True
                                case 'Bad': filts['filterOutBad'] = True
                                case 'Rock': filts['filterOutRock'] = True
                                case _: print("UNKNOWN FILTWITHTAGS A", j)
                    else:
                        for j in i['tags']:
                            match(j):
                                case "Moabs": filts['filterOutNonMoabs'] = True
                                case "Camo": filts['filterOutNonCamo'] = True
                                case "Grow": filts['filterOutNonGrow'] = True
                                case "Lead": filts['filterOutNonLead'] = True
                                case "Boss": filts['filterOutNonBoss'] = True
                                case _: print("UNKNOWN FILTWITHTAGS B", j)

                case 'FilterOutTagModel': 
                    match(i['tag']):
                        case "": None
                        case 'Lead':                 filts['filterOutLead'] = True
                        case 'Bfb':                 filts['filterOutBfb'] = True
                        case 'Zomg':                filts['filterOutZomg'] = True
                        case 'Bad':                 filts['filterOutBad'] = True
                        case 'Ddt':                 filts['filterOutDdt'] = True
                        case 'Miniboss':            filts['filterOutMiniboss'] = True
                        case 'Boss':                filts['filterOutBoss'] = True
                        case 'Moabs':               filts['filterOutMoabs'] = True
                        case 'ReactorDamage':       filts['filterOutReactorDamage'] = True
                        case 'ReactorDamageParagon':filts['filterOutReactorDamageParagon'] = True
                        case 'Ice':                 filts["filterOutFrozen"] = True
                        case _:
                            print("UNKOWN FILTOUTTAG " + i["tag"] + "!")

                case 'FilterMutatedTargetModel':
                    muts = []
                    for j in i['mutationIds']:
                        match j:
                            case 'Sabotage':            muts.append("Sabotage")
                            case 'StickyBomb':          muts.append("Sticky Bomb")
                            case 'MasterSticky':        muts.append("Master Sticky")
                            case 'ParagonSticky':       muts.append("Paragon Sticky")
                            case 'RubberToGold':        muts.append("Rubber to Gold")
                            case 'Trance':              muts.append("Trance")
                            case 'UnstableExplosion':   muts.append("Unstable Concoction")
                            case 'Ice':                 muts.append('Frozen')
                            case 'DesperadoMark':       muts.append("Marked")
                            case 'Wind':                muts.append("Blowback")
                            case 'AbsoluteZero':        muts.append("Absolute Zero freeze")
                            case _: print("UNKNOWN FILTMUTATED", j)

                    filts['filterMutatedTarget'] = ', '.join(muts)

                case 'FilterInSetModel':
                    sets = []
                    for j in i['towerSets']:
                        match j:
                            case 1: sets.append("Primary")
                            case 2: sets.append("Military")
                            case 4: sets.append("Magic")
                            case 8: sets.append("Support")
                            case 16: sets.append("Heroes")
                            case _: print("UNKNOWN SET", j)

                    filts['filterInSets'] = ', '.join(sets)

                case 'FilterInBaseTowerIdModel':
                    ids = []
                    for j in i["baseIds"]:
                        ids.append(tname(j))

                    filts['filterInBaseTowerId'] = ', '.join(ids)

                case 'FilterInTowerTiersModel':
                    aa = "X" if i['path1MinTier'] >= 0 and i['path1MaxTier'] <= 2 else str(i['path1MaxTier'])
                    bb = "X" if i['path2MinTier'] >= 0 and i['path2MaxTier'] <= 2 else str(i['path2MinTier']) + "+"
                    cc = "X" if i['path3MinTier'] >= 0 and i['path3MaxTier'] <= 2 else str(i['path3MaxTier'])

                    filts['filterInTowerTiers'] = aa + "-" + bb + "-" + cc

                case 'FilterTowerParentModel':
                    filts['filterTowerParent'] = True
                    
                case "FilterBloonIfDamageTypeModel":
                    props = []
                    if i["ifCantHitBloonProperties"] & 1: props.append("Lead")
                    if i["ifCantHitBloonProperties"] & 2: props.append("Black")
                    if i["ifCantHitBloonProperties"] & 4: props.append("White")
                    if i["ifCantHitBloonProperties"] & 8: props.append("Purple")
                    if i["ifCantHitBloonProperties"] & 16: props.append("Frozen")
                    
                    filts['filterBloonIfDamageType'] = ' or '.join(props)

                case 'FilterWithChanceModel':
                    filts['filterWithChance'] = frnd(i['filterChance'])

                case 'FilterOutOffscreenModel':
                    filts['filterOutOffscreen'] = True

                case 'FilterAllModel': None
                 
                case 'FilterIfAttackHasTargetModel':
                    filts["filterIfAttackHasTarget"] = name(i["attackName"].split('_', 1)[1] + " Weapon")

                case 'FilterMarkedToPopModel':
                    filts["filterMarkedToPop"] = True

                case 'FilterOveridingMutatedTargetModel':
                      None
                
                case "FilterTargetAngleModel":
                    filts['filterBloonsToWithinAngle'] = frnd(i["fieldOfView"])

                case _: print("UNKNOWN FILTER", i)

    return filts

#
# DAMAGE
#
def parse_dmg(d, s = "damageModifier"):
    prj = {}
    if d["mustIncludeAllTags"] == 1 and len(d["tags"]) > 1:
        match d["tag"]:
            case "Moabs,Fortified":     prj[f'{s}ForFortifiedMoabs'] =frnd(d["damageAddative"])
            case "Lead,Fortified":      prj[f'{s}ForFortifiedLead'] = frnd(d["damageAddative"])
            case _:                     print("UNKNOWN DAMAGE 1 " + d["tag"])
    else:
        match d["tag"]:
            case "Lead":                prj[f'{s}ForLead'] =          frnd(d["damageAddative"])
            case "Ceramic":             prj[f'{s}ForCeramic'] =       frnd(d["damageAddative"])
            case "Bad":                 prj[f'{s}ForBad'] =           frnd(d["damageAddative"])
            case "Bad,Boss":            prj[f'{s}ForBadOrBoss'] =     frnd(d["damageAddative"])
            case "Moabs":               prj[f'{s}ForMoabs'] =         frnd(d["damageAddative"])
            case "Boss":                prj[f'{s}ForBoss'] =          frnd(d["damageAddative"])
            case "Camo":                prj[f'{s}ForCamo'] =          frnd(d["damageAddative"])
            case "Grow":                prj[f'{s}ForRegrow'] =        frnd(d["damageAddative"])
            case "Fortified":           prj[f'{s}ForFortified'] =     frnd(d["damageAddative"])
            case "Lead, Ddt":           prj[f'{s}ForLeadOrDdt'] =     frnd(d["damageAddative"])
            case 'Ceramic, Moabs':      prj[f'{s}ForCeramicOrMoabs'] =frnd(d["damageAddative"])
            case 'Ceramic, Fortified, Moabs': prj[f'{s}ForCeramicOrFortifiedOrMoabs']=frnd(d["damageAddative"])
            case 'Ceramic,Moabs':       prj[f'{s}ForCeramicOrMoabs'] =frnd(d["damageAddative"])
            case 'Lead,Ddt':            prj[f'{s}ForLeadOrDdt'] =     frnd(d["damageAddative"])
            case _:                     print("UNKNOWN DAMAGE 2 " + d["tag"])
    return prj

def blacklist(parent_name, child_name):
    match parent_name:
        case "Storm of Arrows": return not child_name == "Projectile"


towers_cleanup = {
    "": {},
    "Unstable Concoction_ Weapon": {"AddBehaviorToBloonModel_Explosion"},
    "StormOfArrowsAbility": {"Projectile"},
    "Quincy": {"ExplodingProjectile"}
}

def tname(name):
    match name:
        # tower names
        case 'DartMonkey':      return 'Dart Monkey'
        case 'BoomerangMonkey': return 'Boomerang Monkey'
        case 'BombShooter':     return 'Bomb Shooter'
        case 'SniperMonkey':    return 'Sniper Monkey'
        case 'MonkeySub':       return 'Monkey Sub'
        case 'MortarMonkey':    return 'Mortar Monkey'
        case 'NinjaMonkey':     return 'Ninja Monkey'
        case 'BananaFarm':      return 'Banana Farm'
        case 'MonkeyVillage':   return 'Monkey Village'
        case 'BeastHandler':    return 'Beast Handler'
        
        case 'NaturesWardTotem':return "Nature's Ward Totem"

        case 'PortableLake':    return 'Portable Lake'
        case 'BananaFarmer':    return 'Banana Farmer'
        case 'TechBot':         return 'Tech Bot'
        case 'EnergisingTotem': return 'Energizing Totem'
        case 'DungeonStatue':   return 'Dungeon Statue'
        case 'MonkeyAcademy' | 'Etienne' | 'Psi' | 'Mermonkey' | 'Pontoon' | 'Benjamin' | 'Alchemist' | 'Druid': return name
        
        case _:
            print("UNKNOWN TOWERNAME " + name)
            return name

def name(name):
    match name:
         
        # common
        case 'Attack_ Weapon':                      return 'Attack'
        case 'Projectile' | 'Explosion':            return name
        case 'Blast':                               return 'Explosion'
        case 'Ability':                             return 'Ability'
        
        

        # dart
        case 'JuggernautProjectile':                return 'Mini-projectile'
        
        # boomer
        case 'OrbitAttack_ OrbitDamage':            return 'Orbital glaives'
        case 'MOABPressAttack_ MOABPress':          return 'MOAB Press'
        
        # bomb
        case 'fragFrag':                            return 'Frag'
        case 'Recursive':                           return 'Projectile'
        case 'fragCluster':                         return 'Secondary Projectile'
        case 'fragExploProjSecondCluster':          return 'Tertiary Projectile'
        case 'exploExplosion':                      return 'Secondary explosion'
        case 'frag2Explosion':                      return 'Secondary explosion'
        case 'fragExploProj2Explosion':             return 'Tertiary explosion'
        case 'Instakill':                           return 'Instakill'

        # tack
        case 'AttackHomingMeteor_ Weapon':          return "Meteor"
        case 'FireballProjectile':                  return 'Projectile'
        
        case 'AbilityEruption':                     return 'Maelstrom'
        case 'AbilityMeteorImpact':                 return 'Meteor Impact'
        case 'SubProjectile':                       return 'Sub-projectile'
        case 'HomingProjectile':                    return 'Fireball'

        # glue
        case 'Splat':                               return 'Splat'
        case 'SplatOnPop':                          return 'Splat on pop'
        case 'DegradeSplatEffect':                  return 'Degrade splat'
        case 'Linger':                              return 'Puddle'
        case 'Stun':                                return 'Stun'
        case 'AddBehaviorToBloonModel_GlueDot':     return 'Damage over time'
        case 'AddBehaviorToBloonModel_DamageOnHitTOMoabAddBehavior':        return 'Super Glue damage'
        case 'SlowForBloonModel_NonMoabs':          return 'Super Glue (non-MOAB-class)'
         
        # ice
        case 'GlobalProjectile':                    return 'Global projectile'
        case 'AbilitySnowstorm':                    return 'Ability'
        case 'Cryo':                                return 'Ice bomb'
        case 'Icicle':                              return 'Icicle'
        case 'AddBehaviorToBloonModel_Icicles':     return 'Carry icicles'
        case 'Shard':                               return 'Ice shard'
         
        # desperado
        case 'AttackRifle_ Weapon':                 return 'Rifle attack'
        case 'AttackShotgun_ Weapon':               return 'Shotgun attack'
        case 'AbilityTakeAim':                      return 'Take Aim'
        case 'AbilityMarkedToPop':                  return 'Marked to Pop'
        case 'AttackMark_ Weapon':                  return 'Mark attack'
        case 'AddBehaviorToBloonModel_DesertPhantomFireDot': return 'Damage over time'
        case 'MarkingAttack_ Weapon':               return 'Marking attack'
        case 'ExecutionAttack_ Weapon':             return 'Execution attack'
        case 'BlazingSunAreaProjectile':            return 'Area of effect'
        
        # sniper
        case 'Shrapnel':                            return 'Shrapnel'
        case 'Plane':                               return 'Plane'
        case 'Collectable':                         return 'Collectable'

        # sub
        case 'Pulse':                                       return 'Projectile'
        case 'SubmergedAttack_SubmergeAttack Weapon':       return 'Pulse (decamo)'
        case 'SubmergedAttack_SubmergeAttack WeaponDamage': return 'Pulse (damage)'
        case 'FirstStrikeCapability':                       return 'Ability'
        case 'BallisticMissile_BallisticMissile Weapon':    return 'Ballistic Missile'
        case 'TargetDamage':                                return 'Pre-emptive missile'
        case 'SingleTarget':                                return 'Missile'
        case 'MissileExplosion':                            return 'Explosion'
        case 'AirburstSplit':                               return 'Airburst dart'
         
        case 'Fallout':                                     return 'Fallout'
        case 'FinalStrikeAbility':                          return 'Ability'
        case 'Aftershock':                                  return 'Aftershock'

        # bucc
        case 'Anti-MoabMissile_ Weapon':            return 'Missile attack'
        case 'Attack_ Weapon Grape Shot Primary':   return 'Grape attack'
        case 'Attack_ Weapon Cannon Primary':       return 'Bomb attack'
        case 'Attack_ Weapon Cannon Arc Primary':   return 'Bomb attack'
        case 'BuccaneerPlane':                      return 'Plane'
        case 'Ability Takedown':                    return 'Ability'

        case 'TurretRight1_ WeaponCannonballs':     return 'Cannonball attack'
        case 'TurretRight1_ WeaponGrapeShot':       return 'Grape attack'
        case 'AbilityLargeBadHarpoon':              return 'Ability'
        case 'Grapple1_ Weapon':                    return 'Grappling hooks' # mini harpoons
        case 'Grapple_ Weapon':                     return 'Grappling hook' # ability harpoon
        case 'Plane Spawner_ Weapon':               return 'Plane spawner'
        case 'Attack Radial_ Weapon':               return 'Radial attack'
        case 'BuccaneerParagonPlane':               return 'Plane'

        # ace
        case 'PineappleBombs_ PineappleWeapon':     return 'Bomb attack'
        case 'SpectreDartProjectile':               return 'Dart'
        case 'BombProjectile':                      return 'Bomb'
        case 'BombExplosion':                       return 'Explosion'
        case 'SpectreAttack_ Weapon':               return 'Front attack'
        case 'SpectreAttackCenter_ Weapon':         return 'Side attacks'
        case 'SpectreAttackRear_ Weapon':           return 'Sides attack3'

        case 'Attack-Seeking_ Weapon':              return 'Seeking attack'
        case 'MainProjectile':                      return 'Main projectile'
        case 'Attack-RedTippedDarts_ Weapon':       return 'Forward attack'
        case 'Ability-CarpetBomb':                  return 'Ability'
        case 'ProjectileDamage':                    return 'Explosion'
         
        # heli
        case 'Attack_ WeaponPrimaryDarts':          return 'Attack'
        case 'Attack_ WeaponSecondaryDarts':        return 'Attack (secondary)'
        case 'Attack_ MachineGun':                  return 'Machine gun'
        case 'Missiles_MissileArrayFirst Weapon':   return 'Missile array'
        case 'Rotor Blades_RotorBlades WeaponRotorBlades': return 'Rotors'
        case 'Downdraft_Downdraft Weapon':          return 'Downdraft'
        case 'ProjectileDowndraft':                 return 'Projectile'
        case 'Redeploy':                            return 'Redeploy'
        case 'SupportDrop':                         return 'Support Drop'
        case 'SpecialPoperations':                  return 'Special Poperations'
        case 'ComancheDefenceHeli':                 return 'Mini-Comanche'
         
        # mortar
        case 'Shockwave':                           return 'Shockwave'
        case 'PopAndAweAbility':                    return 'Ability'
        case 'StripExplosion':                      return 'DDT defort projectile'
        case 'CamoRemoval':                         return 'Decamo projectile'
        case 'NormalBurn':                          return 'Burn projectile'
        case 'MoabBurn':                            return 'MOAB burn projectile'
         
        # dartling
        case 'AddBehaviorToBloonModel_LaserShock':  return 'Laser Shock'
        case 'ProjectileInitialHit':                return 'Initial hit'
        case 'RocketStorm':                         return 'Ability'
        case 'Attack1_ Weapon':                     return 'Attack'
        case 'AttackBloonExclusionZone1_ Weapon':   return 'Attack'

        # wiz
        case 'Attack Fireball_ Weapon':                 return 'Fireball'
        case 'Attack Wall of Fire_ Weapon':             return 'Wall of Fire'
        case "Attack Dragon's Breath_ Weapon":          return "Dragon's Breath"
        case 'Attack Shimmer_ Weapon':                  return 'Shimmer'
        case 'Attack Flaming Balls_ Weapon':            return 'Fireballs'
        case 'DBProjectile':                            return 'Projectile'
        case 'Attack Necromancer_ Weapon':              return 'Reanimate'
        case 'Attack Necromancer_ Weapon Ghost Moab ':  return 'MOAB'
        case 'ProjectileMoab':                          return 'MOAB'
        case 'ProjectileBfb':                           return 'BFB'
        case 'Phoenix':                                 return 'Phoenix'
        case 'PermaPhoenix':                            return 'Phoenix'
        case 'LordPhoenix':                             return "Lava Phoenix"
        case 'Ability Summon Phoenix':                  return 'Ability'
        case 'Ability Summon Lord Phoenix':             return 'Ability'
         
        case 'Attack Arcane Spike_ Weapon':             return 'Arcane Spike'
        case 'Attack Draining Beam_ Weapon':            return 'Draining Beam'
        case 'ZombieBloonProjectile':                   return 'Undead Bloon'
        case 'Attack Flamethrower_ Weapon':             return 'Flame cascade'
        case 'GroundProjectile':                        return 'Ground projectile'
        case 'Attack Walls of Fire_ Weapon':            return 'Walls of Fire'
        case 'Ability Arcane Metamorphosis':            return 'Arcane Metamorphosis'
        case 'Ability Phoenix Rebirth':                 return 'Phoenix Rebirth'
        case 'DarkPhoenixV1':                           return 'Phoenix'
        case 'Attack Dark Firebomb Breath_ Weapon':     return 'Dragon\'s Breath'
        case 'Attack Dark Flaming Balls_ Weapon':       return 'Fireballs'
        case 'AddBehaviorToBloonModel_FireDoT':         return 'Damage over time'
        case 'ZombieZOMGProjectile':                    return 'ZOMG'
        case 'ZombieBFBProjectile':                     return 'BFB'
        #case 'Attack Flamethrower_ Weapon'

        # super
        case 'DarkshiftAbility':                    return 'Ability'

        # ninja
        case 'Caltrops_ Weapon':                        return 'Caltrops'
        case 'FlashBombAttack_ Weapon':                 return 'Flash Bomb'
        #case 'FlashBomb':                               return 'Projectile' # enable for ascended shadow
        case 'FlashBomb':                               return 'Flash Bomb'
        case 'Shurikens':                               return 'Shurikens'
        case 'StickyBombAttack_ Weapon':                return 'Sticky Bomb'
        case 'StickyBombProjectile':                    return 'Projectile'
        case 'StickyBombExplosion':                     return 'Explosion'
        case 'AddBehaviorToBloonModel_StickyBombSplash':return 'Delay'
        
        case 'SabotageAttack_ SabotageWeapon':          return "Sabotage"
        case 'SabotageProjectile':                      return "Projectile"
         
        # drood
        case "Attack_ BallLightning":                   return 'Ball Lightning'
        case 'SpawningProjectile':                      return 'Spawning projectile'
        case 'LightningProj':                           return 'Lightning'
        case 'BallLightningProj':                       return 'Lightning'
        case "Attack_ SuperstormTornado":               return "Superstorm"
        case 'Attack_ Lightning':                       return "Lightning"
        case "TornadoAttack_ Tornado":                  return "Tornado"
        case 'JungleVine_ Weapon':                      return 'Vine'

        # alch
        case 'AcidSplash':                              return 'Splash'
        case 'Acid Pool':                               return 'Acid Pool'
        case 'AcidicMixture_ Weapon':                   return 'Acidic Mixture Dip'
        case 'BeserkerBrewAttack_ Weapon':              return 'Berserker Brew'
        case 'ShrinkPotion_ Weapon':                    return 'Shrink Potion'
        case 'MoabExplode':                             return 'Explosion'
        case 'TransformedBaseMonkey':                   return 'Transformed Monkey'
        case 'Transformed Projectile':                  return 'Projectile'
        case 'TransformedAttack_ Weapon':               return 'Attack'
        case 'Transformed Attack_ Transformed Weapon':  return 'Transformed attack'
        case 'RubberSplash':                            return 'Splash'
        case 'ShrinkSplash':                            return 'Splash'
        case 'UnstableSplash':                          return 'Splash'
        case 'Unstable Concoction_ Weapon':             return 'Unstable Concoction'
        case 'RubberToGoldAttack_ Weapon':              return 'Rubber to Gold'
        case 'AddBehaviorToBloonModel_LeadToGoldEffect':return 'Lead to Gold'
        case 'DoT':                                     return 'Track projectile'
         
        case 'AddBehaviorToBloonModel_Explosion':       return name

        # mermonkey
        case 'TridentAOE':                          return 'Splash'
        case 'AttackTentacle1_ Weapon':             return 'Tentacle'
        case 'AttackTrance_ Weapon':                return 'Trance attack'
        case 'TranceTotem':                         return 'Trance totem'
        case 'SplitProjectile':                     return 'Split projectile'
        case 'Attack_ Weapon2':                     return 'Side tridents'
        case 'Attack_ WeaponGlobalDamage':          return 'Flood'
        case 'SnowstormProjectile':                 return 'Projectile'

        # engi

        case 'Spawner_ Weapon':                     return 'Spawner'
        case 'Sentry':                              return 'Sentry'
        case 'SentryCrushing':                      return 'Crushing Sentry'
        case 'SentryBoom':                      return 'Boom Sentry'
        case 'SentryCold':                      return 'Cold Sentry'
        case 'SentryEnergy':                      return 'Energy Sentry'
        case 'SentryParagon':                       return 'Champion Sentry'
        case 'CleansingFoam_ Weapon':               return 'Cleansing Foam'
        case 'BloonTrap_ Weapon':                   return 'Bloon Trap'
        case 'Collidable':                          return 'Collidable'
        case 'CollidableXXXL':                      return 'Collidable'
        case 'ParagonOverClock':                    return 'Overclock'

        case 'AttackNailgunR_ Weapon' | 'AttackNailgunBackR_ Weapon' | 'AttackNailgunBackL_ Weapon':
                                                    return 'Nail gun'
        case 'SentryParagonGreen':                  return 'Green Sentry Paragon'
        case 'SentryParagonRed':                    return 'Red Sentry Paragon'
        case 'SentryParagonBlue':                   return 'Blue Sentry Paragon'
        case 'SentryParagonChild':                  return 'Modified Sentry Paragon'
        case 'ExplosionOnDestroy':                  return 'Self-destruct'
        case 'ProjectileAtEnd':                     return 'Projectile at tip'

        # spac
        case 'SmallExplosion':                      return 'Mini-explosion'
        case 'SpikeStorm_SpikeStorm Weapon':        return 'Attack'
        case 'MiniSpike':                           return 'Mini-spike'
        case 'CarpetSpikes':                        return 'Carpet of Spikes'
        case 'TurboCharge':                         return 'Controlled Burst'
        case 'Spikeageddon':                        return 'Spikeageddon'
        case 'SpikeageddonSpikePile':               return 'Projectile'
         
        # mrbeast
        case 'Splash':                              return 'Splash'
        case 'Piranha':                             return 'Beast'
        case 'Microraptor':                         return 'Beast'
        case 'Gyrfalcon':                           return 'Beast'
        case 'StompAbility':                        return 'Ability'
        case 'AttackAirUnitModel_Attack_':          return 'Grab'
        case 'GrabProjectile':                      return 'Carry projectile'
        case 'ThrashingProjectileExplosion':        return 'Trash projectile'
         
        # quincy
        case 'BaseProjectile':                      return 'Projectile'
        case 'Area':                                return 'Area'
        case 'RapidShotAbility':                    return 'Rapid Shot'
        case 'StormOfArrowsAbility':                return 'Storm of Arrows'

        # gwen
        #case 'WallOfFire':                          return 'Cocktail of Fire'
        case 'WallOfFire':                          return 'Wall of Fire'
        case 'FireStorm':                           return 'Firestorm'
        case 'AddBehaviorToBloonModel_MoabDot':     return 'Damage over time'
        case 'Heat It Up':                          return 'Heat It Up'
        case 'FireSplash':                          return 'Projectile'
        case 'Wall_ Weapon':                        return 'Attack'
        case 'MOAB projectile': return name
        #case 'Wall_':                               return 'Attack'
        #case 'Heat It Up':                          return 'Heat It Up'
        #case 'Firestorm':                           return 'Firestorm'
        #case 'FireSplash':                          return 'Projectile'
        #case 'MOABAttack_':                         return 'MOAB attack'

        # striker
        case 'BaseExplosion':                       return 'Explosion'
        case 'BaseAttack_ Weapon':                  return 'Attack'
        case 'ConcussiveShell':                     return 'Concussive Shell'
        case 'TargetFocus':                         return 'TargetFocus'
        case 'ArtillerySupport':                    return 'Artillery Command'
         
        # obin
        case 'NaturesWardTotem':                    return "Nature's Ward Totem"
        case 'TotemSpawner_ Weapon':                return 'Spawner'
        case 'AbilityBrambles':                     return 'Brambles'
        case 'AbilityWallOfTrees':                  return 'Wall of Trees'
         
        # adora
        case 'BallOfLightTower':                    return 'Ball of Light'
        case 'TheLongArmOfLight':                   return 'The Long Arm of Light'
        case 'BloodSacrifice':                      return 'Blood Sacrifice'
        case 'BallOfLight':                         return 'Ball of Light sub-tower'
        
        # souda
        case 'Impact':                              return 'Impact'
        case 'LeapingSword':                        return 'Leaping Sword Attack'
        case 'SwordChargeProjectile':               return 'Projectile'
        case 'SwordCharge':                         return 'Sword Charge'
        case 'AddBehaviorToBloonModel_BleedNonMoab':return 'Bloon Bleed'
        case 'AddBehaviorToBloonModel_BleedMoab':   return 'Bloon Bleed (MOAB-Class)'
         
        # cate
        case 'AoeProjectile':                       return 'AOE'
        case 'TransformedAttack_ TransformedWeapon':return 'Attack'
        case 'AddBehaviorToBloonModel_DoT':         return 'Damage over time'
        case 'TransformedAoeProjectile':            return 'AOE'
        case 'TransformedProjectile':               return 'Projectile'
        
        case _:
            print("UNKNOWN NAME " + name)
            return name
        
def name_mut(nam):
    match nam:
        case 'Stun:Strong':                         return 'Stun'
        # boomer
        case 'BoomerangMonkeyParagonRate':          return 'Buff'
        case 'Dot:BoomerangMoabRicochet':           return 'Damage over time'
        case 'Fire:Dot':                            return 'Damage over time'
        case 'Slow:MoabPressStunParagon':           return 'Stun (Paragon)'
        case 'Slow:MoabPressStun':                  return 'Stun'
         
        # tack
        case '5xxTackShooterMeteorDot':             return 'Damage over time'
         
        # glue
        case 'Glue':                                return 'Glue'
        case 'Stun':                                return 'Stun'
        case 'SuperGlue':                           return 'Super Glue'
         
        # ice
        case 'Ice:Regular:Freeze':                  return 'Freeze'
        case 'CryoIce:Regular:Freeze':              return 'Freeze'
        case 'Snowstorm:Regular:Freeze:Ice':        return 'Freeze'
        case 'AbsoluteZero:Regular:Freeze:Ice':     return 'Freeze'
        #case 'Permafrost':                          return 'Permafrost'
         
        # desperado
        case 'DesperadoMark':                       return 'Mark'
        case 'Dot:TheBlazingSun':                   return 'Damage over time'
         
        # sniper
        case 'EliteDefenderRate':                   return 'Attack speed buff'
         
        # bucc
        case 'Dot:Buccaneer':                       return 'Damage over time'
         
        # mortar
        case 'Stun:Shockwave':                      return 'Stun'
        case 'PopAndAweSupport':                    return 'Buff'
        case 'Dot:MortarMoab':                      return 'Damage over time'
        case 'Dot:MortarPaa':                       return 'Damage over time'
         
        # wiz
        case 'Dot:Mortar':                          return 'Damage over time'
         
        # ninja
        case 'Stun:Sticky':                         return 'Stun'
        case 'Sabotage':                            return 'Effect'
        case 'RangeSupport':                        return 'Range buff'
        case 'ShinobiTactics':                      return 'Shinobi Tactics'
        case 'NinjaParagonVisibility' | 'NinjaVisibilityParagon':   return 'Camo buff'
        case 'StickyBomb' | 'MasterSticky' | 'ParagonSticky':       return 'Damage to target'
         
        # mer
        case 'Mermonkey:CoralSharpening':           return 'Pierce buff'
        case 'SlowInk':                             return 'Ink'
        case 'Ice: MermonkeyFreeze':                return 'Freeze'
        case 'Mermonkey: Conch: Range':             return 'Range buff'
        case 'Mermonkey: Conch: Pierce':            return 'Pierce buff'
        case 'Permafrost:Normal':                   return 'Permafrost'
         
        # druid
        case 'SpiritOfTheForestClose':              return 'Thorn zone (close)'
        case 'SpiritOfTheForestMedium':              return 'Thorn zone (middle)'
        case 'SpiritOfTheForestFar':              return 'Thorn zone (far)'
         
        # alch
        case 'alchemist:acid':                      return 'Damage over time'
        case 'LeadToGold':                          return 'Lead to Gold'
        case 'RubberToGold':                        return 'Rubber to Gold'
         
        # engi
        case 'Slow':                                return 'Slow'
        case 'Stun:Weak':                           return 'Stun'
        case 'Stun:ParagonWeak':                    return 'Stun (weak Paragon)'
         
         
        case 'CarpetSpikes':                        return 'Carpet of Spikes'
         
        # gwen
        case 'Burn:Gwendolin':                      return 'Damage over time'
        case 'Firestorm':                           return 'Damage over time'
         
        # striker
        case 'BlackResist':                         return 'Black resistance modifier'
         
        # obin
        case 'Obyn:NaturesWrath:PierceDruid':       return 'Druid buff'

         
        case 'BattleCatSlow': return 'Slow'
        
        case _:
            print("UNKNOWN MUTNAME " + nam + "!")
            return nam