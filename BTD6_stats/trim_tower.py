from trim_common import *
from trim_attack import *
from trim_projectile import *
from trim_ability import *
from trim_buff import *

def atk_cmp(a, b):
    ejects = ""
    tts = ""
    rots = ""

    for k, v in a.items():
        if k == 'count': continue
        elif k == 'sharedGridRange': continue

        elif k == 'eject' and v != b[k]: ejects = b[k]
        elif k == 'targetTypes' and v != b[k]: tts = b[k]
        elif k == 'rotateRate' and v != b[k]: rots = b[k]
        elif v != b[k]:
            return {'result': False}

    return {'result': True, 'ejects': ejects, 'tts': tts, 'rots': rots}

def parse_tow(tower, m_tow):
    tow = {
        'placeableOnLand': False,
        'placeableOnWater': False,
        'placeableOnTrack': False,
        'range': frnd(m_tow['range']),
        "towerSelectionMenuThemeId": m_tow["towerSelectionMenuThemeId"],
        'attacks': {},
        'projectiles': {},
        'collectables': {},
        'abilities': {},
        'zones': {},
        'buffs': {},
        'subtowers': {},
        'collectables': {}
    }

    for i in m_tow['areaTypes']:
        match i:
            case 0:
                tow['placeableOnTrack'] = True
            case 1:
                tow['placeableOnWater'] = True
            case 2:
                tow['placeableOnLand'] = True
            case _:
                print("UNKNOWN AREATYPE " + i)

    if get_model_name(m_tow['footprint']) == "CircleFootprintModel":
        tow['footprintRadius'] = frnd(m_tow['footprint']['radius'])
        tow["doesntBlockTowerPlacement"] = m_tow['footprint']["doesntBlockTowerPlacement"]
    elif get_model_name(m_tow['footprint']) == "RectangleFootprintModel":
        tow['footprintX'] = frnd(m_tow['footprint']['xWidth'])
        tow['footprintY'] = frnd(m_tow['footprint']['yWidth'])
        tow["doesntBlockTowerPlacement"] = m_tow['footprint']["doesntBlockTowerPlacement"]
    else:
        print("UNKNOWN FOOTPRINT", get_model_name(m_tow['footprint']))

    for i in m_tow["behaviors"]:
        model_name = get_model_name(i)
        match model_name:
            case "DamageBasedAttackSpeedModel":
                tow["damageBasedAttackSpeedDamageThreshold"] = frnd(i["damageThreshold"])
                tow["damageBasedAttackSpeedIncreasePerThreshold"] = frnd(i["increasePerThreshold"])
                tow["damageBasedAttackSpeedMaxStacks"] = i["maxStacks"]
                tow["damageBasedAttackSpeedMaxTimeWithoutDamage"] = frnd(i["maxTimeInFramesWithoutDamage"] / 60)

            case "DruidVengeanceEffectModel":
                tow["vengeanceRbeThreshold"] = i["damageModifierWrathModel"]["rbeThreshold"]
                tow["vengeanceDamage"] = i["damageModifierWrathModel"]["damage"]
                tow["vengeanceMaxDamageBoost"] = i["damageModifierWrathModel"]["maxDamageBoost"]

    #
    # ATTACKS
    #
    for i in m_tow['behaviors']:
        model_name = get_model_name(i)

        match model_name:

            # ATTACKS
            case 'AttackModel' | 'AttackAirUnitModel':
                atk_list = parse_atk(tower, tow, i, retval=True, owner_name=m_tow["baseId"])
                for k, v in parse_atk(tower, tow, i, retval=True, owner_name=m_tow["baseId"]).items():
                    for kk, vv in tow['attacks'].items():
                        if kk != "_order":
                            cmp = atk_cmp(vv, v)
                            if cmp["result"]:
                                del atk_list[k]

                                tow['attacks'][kk]['count'] += 1
                                
                                if cmp["ejects"] != "":
                                        if tow['attacks'][kk]['count'] == 2: tow['attacks'][kk]['eject'] += " (1)"
                                        tow['attacks'][kk]['eject'] += "<br>" + cmp["ejects"] + ' (' + str(tow['attacks'][kk]['count']) + ')'
                                if cmp["tts"] != "":
                                        if tow['attacks'][kk]['count'] == 2: tow['attacks'][kk]['targetTypes'] += " (1)"
                                        tow['attacks'][kk]['targetTypes'] += "<br>" + cmp["tts"] + ' (' + str(tow['attacks'][kk]['count']) + ')'
                                if cmp["rots"] != "":
                                        if tow['attacks'][kk]['count'] == 2: tow['attacks'][kk]['rots'] += " (normal)"
                                        tow['attacks'][kk]['rotateRate'] += "<br>" + cmp["rots"] + ' (inverse)'
                                print('cmp', k, kk)

                    if k == "Attack_ WeaponSecondaryDarts" and m_tow["name"] != "ComancheDefenceHeli":
                        del atk_list[k]
                        atk_list['Attack_ WeaponPrimaryDarts']['count'] += 1
                        atk_list['Attack_ WeaponPrimaryDarts']['eject'] = atk_list['Attack_ WeaponPrimaryDarts']['eject'].replace("side", "primary") + "<br>" + v["eject"].replace("side", 'secondary')

                    if k == 'Attack_ WeaponInverse':
                        del atk_list[k]
                        atk_list['Attack_ Weapon']['count'] += 2
                        atk_list['Attack_ Weapon']['rotateRate'] += " (1)<br>" + v['rotateRate'] + ' (2)'

                    #elif k == "SabotageAttack_ SabotageWeapon":
                    #    del atk_list[k]
                    #    add_sub(tow['effects'], atk_list[k]['projectiles']['SabotageProjectile']['effects']['Sabotage'])

                    if 'fireWhenAlternateWeaponIsReady' in v:
                        del atk_list[k]

                        to_alter = {
                            'Attack_ Weapon Secondary': 'Attack_ Weapon',
                            'Attack_ Weapon Grape Shot Secondary': 'Attack_ Weapon Grape Shot Primary',
                            'Attack_ Weapon Cannon Secondary': 'Attack_ Weapon Cannon Primary',
                            'Attack_ Weapon Cannon Arc Secondary': 'Attack_ Weapon Cannon Arc Primary'
                        }[k]

                        if to_alter in atk_list:
                            atk_list[to_alter]['count'] += 1
                            atk_list[to_alter]['eject'] += " (main)<br>" + v['eject'] + " (alt)"

                add_sub(tow["attacks"], atk_list)


            # PROJECTILES
            case 'PreEmptiveStrikeLauncherModel':       parse_prj(tower, tow, i["projectileModel"], i['emissionModel'], owner_name=m_tow["baseId"])
            case 'CreateProjectileOnTowerDestroyModel': parse_prj(tower, tow, i['projectileModel'], i["emissionModel"], owner_name=m_tow["baseId"])
                
    #
    # ZONES
    #
    for i in m_tow['behaviors']:
        model_name = get_model_name(i)
        #print(model_name)

        match model_name:
            case 'SlowBloonsZoneModel':
                zone = {
                    "radius": frnd(i["zoneRadius"])
                }

                if i["inclusive"]: zone["multiplierForMoabs"] = frnd(i["speedScale"])
                else: zone["multiplier"] = frnd(i["speedScale"])
    
                zone.update(filt(i['filters']))
                if "Arctic Wind" in tow["zones"]:
                    tow["zones"]["Arctic Wind"].update(zone)
                else:
                    add_sub(tow["zones"], {"Arctic Wind": zone}, owner_name=m_tow['baseId'])

            case 'MoabShoveZoneModel':
                zone = {
                    "radius": frnd(i["range"]),
                    "multiplierForMoab": frnd(i["moabPushSpeedScaleCap"]),
                    "multiplierForBfb": frnd(i["bfbPushSpeedScaleCap"]),
                    "multiplierForZomg": frnd(i["zomgPushSpeedScaleCap"]),
                    "multiplierForDdt": frnd(i["zomgPushSpeedScaleCap"])
                }
    
                zone.update(filt([i['filterInvisibleModel']]))
                add_sub(tow["zones"], {"MOAB Shove": zone}, owner_name=m_tow['baseId'])
            
            case 'AddBehaviorToBloonInZoneModel':
                zone = {
                    "radius": frnd(i["zoneRadius"])
                }

                for j in i['behaviors']:
                    model_name_j = get_model_name(j)

                    match model_name_j:
                        case 'IgnoreDmgImmunityModel':
                            zone['chance'] = frnd(j['chance'])

                add_sub(tow["zones"], {name_mut(i['mutationId']): zone}, owner_name=m_tow['baseId'])

            case "SpikeParagonDamageZoneModel":
                zone = {
                    "radius": frnd(i["circleRadius"])
                }

                
                zone['damage'] = frnd(i["damageOverTimeZoneModel"]["behaviorModel"]["damage"])
                zone['immuneBloonProperties'] = i["damageOverTimeZoneModel"]["behaviorModel"]["immuneBloonProperties"]
                zone['interval'] = frnd(i["damageOverTimeZoneModel"]["behaviorModel"]["interval"])
                zone['initialDelay'] = frnd(i["damageOverTimeZoneModel"]["behaviorModel"]["initialDelay"])
                zone["triggerImmediate"] = i["damageOverTimeZoneModel"]["behaviorModel"]["triggerImmediate"]
                zone['distributeToChildren'] = i["damageOverTimeZoneModel"]["behaviorModel"]['distributeToChildren']
                for j in i["damageOverTimeZoneModel"]["behaviorModel"]["damageModifierModels"]:
                    #print(k)
                    if j['damageAddative'] > 0: zone.update(parse_dmg(j))

                add_sub(tow["zones"], {name_mut(i["damageOverTimeZoneModel"]['mutatorId']): zone}, owner_name=m_tow['baseId'])

            case "SpiritOfTheForestModel":
                beh = i["damageOverTimeZoneModelFar"]["behaviorModel"]
                zo1 = {
                    "damage": frnd(beh["damage"]),
                    "immuneBloonProperties": beh["immuneBloonProperties"],
                    'interval': frnd(beh["interval"]),
                    'initialDelay': frnd(beh["initialDelay"]),
                    'distributeToChildren': beh["distributeToChildren"],
                    "damageModifierForCeramicOrMoabs": beh["additive"]
                }
                beh = i["damageOverTimeZoneModelMiddle"]["behaviorModel"]
                zo2 = {
                    "damage": frnd(beh["damage"]),
                    "immuneBloonProperties": beh["immuneBloonProperties"],
                    'interval': frnd(beh["interval"]),
                    'initialDelay': frnd(beh["initialDelay"]),
                    'distributeToChildren': beh["distributeToChildren"],
                    "damageModifierForCeramicOrMoabs": beh["additive"],
                    "radius": frnd(i["middleRange"])
                }
                beh = i["damageOverTimeZoneModelClose"]["behaviorModel"]
                zo3 = {
                    "damage": frnd(beh["damage"]),
                    "immuneBloonProperties": beh["immuneBloonProperties"],
                    'interval': frnd(beh["interval"]),
                    'initialDelay': frnd(beh["initialDelay"]),
                    'distributeToChildren': beh["distributeToChildren"],
                    "damageModifierForCeramicOrMoabs": beh["additive"],
                    "radius": frnd(i["closeRange"])
                }
                add_sub(tow["zones"], {name_mut(i["damageOverTimeZoneModelFar"]['mutatorId']) : zo1}, owner_name=m_tow['baseId'])
                add_sub(tow["zones"], {name_mut(i["damageOverTimeZoneModelMiddle"]['mutatorId']) if i["damageOverTimeZoneModelMiddle"]['mutatorId'] != "" else "Thorn zone (middle)": zo2}, owner_name=m_tow['baseId'])
                add_sub(tow["zones"], {name_mut(i["damageOverTimeZoneModelClose"]['mutatorId']): zo3}, owner_name=m_tow['baseId'])

    #
    # ABILITIES
    #
    for i in m_tow['behaviors']:
        model_name = get_model_name(i)

        match model_name:
            case 'AbilityModel':
                parse_abil(tow, m_tow["name"], i)

            #case 'ActivateAbilityAfterIntervalModel':
            #    ab = parse_abil(i["abilityModel"])
            #    ab["interval"] = frnd(i["interval"]) 
            #    tow['abilities'][name(i) + ' passive'] = ab
                

    #
    # BUFFS
    #
    parse_buffs(tow['buffs'], m_tow['behaviors'])

    #
    # SUBTOWERS
    #
    for i in m_tow['behaviors']:
        model_name = get_model_name(i)

        match model_name:
            case 'TowerExpireModel':
                tow['lifespan'] = frnd(i['lifespan'])

            #case 'TowerExpireOnParentDestroyedModel':
            #    tow['towerExpireOnParentDestroyed'] = True

            case 'TranceTotemSpawnerModel':
                parse_tow(tow, i['tower'])

            case 'TowerCreateTowerModel':
                parse_tow(tow, i['towerModel'])

            case 'TowerCreateParagonTowerModel':
                parse_tow(tow, i['towerModels'][0])

            case "PerRoundCashBonusTowerModel":
                tow["cashPerRound"] = frnd(i["cashPerRound"])


            case "MultiHookManagerModel":
                tow["minTimeBetweenHooks"] = frnd(i["minTimeBetweenHooks"])
                tow["hookreloadTime"] = frnd(i["reloadTime"])

            case 'PathMovementFromScreenCenterModel':
                tow["speed"] = frnd(i["speed"])

            case "ComancheDefenceModel":
                parse_tow(tow, i["towerModel"])


            case "AirUnitModel":
                for j in i['behaviors']:
                    model_name_j = get_model_name(j)

                    match model_name_j:
                        case 'PathMovementModel':
                            if "speed" not in tow: tow["speed"] = frnd(j["speed"])

                        case 'HeliMovementModel':
                            tow["speed"] = frnd(j["maxSpeed"])
                            tow["rotationSpeed"]= frnd(j["rotationSpeed"])
                            tow["strafeDistance"]= frnd(j["strafeDistance"])
                            tow["strafeDistanceSquared"]= frnd(j["strafeDistanceSquared"])
                            tow["otherHeliRepulsionRange"]= frnd(j["otherHeliRepulsionRange"])
                            tow["otherHeliRepulsionRangeSquared"]= frnd(j["otherHeliRepulsionRangeSquared"])
                            tow["movementForceStart"]= frnd(j["movementForceStart"])
                            tow["movementForceEnd"]= frnd(j["movementForceEnd"])
                            tow["movementForceEndSquared"]= frnd(j["movementForceEndSquared"])
                            tow["brakeForce"]= frnd(j["brakeForce"])
                            tow["otherHeliRepulsonForce"]= frnd(j["otherHeliRepulsonForce"])
                            tow["slowdownRadiusMax"]= frnd(j["slowdownRadiusMax"])
                            tow["slowdownRadiusMaxSquared"]= frnd(j["slowdownRadiusMaxSquared"])
                            tow["slowdownRadiusMin"]= frnd(j["slowdownRadiusMin"])
                            tow["slowdownRadiusMinSquared"]= frnd(j["slowdownRadiusMinSquared"])
                            tow["minVelocityCapScale"]= frnd(j["minVelocityCapScale"])
                            tow["destinationYOffset"]= frnd(j["destinationYOffset"])
                            tow["tiltAngle"]= frnd(j["tiltAngle"])
                            tow["patrolPursuitRadius"]= frnd(j["patrolPursuitRadius"])

                        case "FighterMovementModel":
                            tow["speed"]                            = frnd(j["maxSpeed"])
                            tow["turningSpeed"]                     = frnd(j["turningSpeed"])
                            tow["minDistanceToTargetBeforeFlyover"] = frnd(j["minDistanceToTargetBeforeFlyover"])
                            tow["distanceOfFlyover"]                = frnd(j["distanceOfFlyover"])
                            tow["bankAngleMax"]                     = frnd(j["bankAngleMax"])
                            tow["bankSmoothness"]                   = frnd(j["bankSmoothness"])
                            tow["rollTotalTime"]                    = frnd(j["rollTotalTime"])
                            tow["rollRunUpDistance"]                = frnd(j["rollRunUpDistance"])
                            tow["rollTimeBeforeNext"]               = frnd(j["rollTimeBeforeNext"])
                            tow["rollChancePerSecondPassed"]        = frnd(j["rollChancePerSecondPassed"])
                            tow["loopTotalTime"]                    = frnd(j["loopTotalTime"])
                            tow["loopRunUpDistance"]                = frnd(j["loopRunUpDistance"])
                            tow["loopTimeBeforeNext"]               = frnd(j["loopTimeBeforeNext"])
                            tow["loopChancePerSecondPassed"]        = frnd(j["loopChancePerSecondPassed"])
                            tow["loopRadius"]                       = frnd(j["loopRadius"])
                            tow["loopModelScale"]                   = frnd(j["loopModelScale"])

            case "BeastHandlerLeashModel":
                if i["towerModel"] != None:
                    parse_tow(tow, i['towerModel'])

            case "BeastHandlerPetModel":
                tow["cooldownScaleRange"] = frnd(i["cooldownScaleRange"])
                tow["pierceRange"] = i["pierceRange"]
                tow["damageRange"] = i["damageRange"]
                tow["thrashKnockbackLifetimeRange"] = frnd(i["thrashKnockbackLifetimeRange"])
                tow["stunBonusDivideMicroraptor"] = frnd(i["stunBonusDivideMicroraptor"])
                tow["damageRangeGrappleGyrfalcon"] = frnd(i["damageRangeGrappleGyrfalcon"])
                tow["speedRangeGyrfalcon"] = frnd(i["speedRangeGyrfalcon"])
             
    #
    # BEHAVS THAT DEPEND ON EXISTINGS
    #
    for i in m_tow['behaviors']:
        model_name = get_model_name(i)
        #print(model_name)

        match model_name:

            case 'LinkProjectileRadiusToTowerRangeModel':
                #print(i['projectileModel']["name"])
                if get_model_name(i['projectileModel']) in tow['projectiles']:
                    tow['projectiles'][name(i['projectileModel'])]["projectileRadiusOffset"] = frnd(i["projectileRadiusOffset"])
                else:
                    for k, v in tow['attacks'].items():
                        if k != "_order" and 'projectiles' in v and get_model_name(i['projectileModel']) in v['projectiles']:
                            v['projectiles'][name(i['projectileModel'])]["projectileRadiusOffset"] = frnd(i["projectileRadiusOffset"])


    #
    # TARGETING
    #
    if m_tow['targetTypes'] != 4 and m_tow['targetTypes']:
        for i in m_tow["targetTypes"]:
            match i["id"]:
                case 'First':           tow["targetTypeFirst"] = True
                case 'Last':            tow["targetTypeLast"] = True
                case 'Close':           tow["targetTypeClose"] = True
                case 'Strong':          tow["targetTypeStrong"] = True
                case 'Elite':           tow["targetTypeElite"] = True
                case 'Normal':          tow["targetTypeNormal"] = True
                case 'Locked':          tow["targetTypeLocked"] = True
                case 'Circle':          tow["targetTypeCircle"] = True
                case 'Track':           tow["targetTypeTrack"] = True
                case 'CloseTrack':      tow["targetTypeCloseTrack"] = True
                case 'FarTrack':        tow["targetTypeFarTrack"] = True
                case 'SmartTrack':      tow["targetTypeSmartTrack"] = True
                case 'FigureInfinite':  tow["targetTypeFigureInfinite"] = True
                case 'FigureEight':     tow["targetTypeFigureEight"] = True
                case 'Centered':        tow["targetTypeCentered"] = True
                case 'TargetSelectedPoint': tow["targetTypeTargetSelectedPoint"] = True
                case 'TargetIndependant': tow["targetTypeTargetIndependant"] = True
                case 'FollowTouch':     tow["targetTypeFollowTouch"] = True
                case 'LockInPlace':     tow["targetTypeLockInPlace"] = True
                case 'PatrolPoints':    tow["targetTypePatrolPoints"] = True
                case 'Pursuit':         tow["targetTypePursuit"] = True
                case 'AutoTrack':       tow["targetTypeAutoTrack"] = True
                case 'Gyrfalcon':       tow["targetTypeGyrfalcon"] = True
                case _: print("UNKNOWN TTYPE", i["id"])

    ret = {
        m_tow["name"]: tow
    }
    add_sub(tower['subtowers'], ret)