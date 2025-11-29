from trim_common import *
from trim_projectile import *
import trim_tower
from trim_ability import *

def parse_wpn(tower, atk, atk_name, m_wpn, owner_name=""):
    data = {
        'rate': frnd(m_wpn['rate']),
        'eject': ', '.join(map(str, [frnd(m_wpn['ejectX']), frnd(m_wpn['ejectY']), frnd(m_wpn['ejectZ'])])),
        'fireWithoutTarget': m_wpn['fireWithoutTarget'],
        "fireBetweenRounds": m_wpn["fireBetweenRounds"],
        'projectiles': {},
        'buffs': {},
        'collectables': {}
    }
    data.update(atk)

    if m_wpn["startInCooldown"]: data["customStartCooldown"] = m_wpn["customStartCooldown"]

    if get_obj_name(m_wpn['projectile']) not in []:
        parse_prj(tower, data, m_wpn['projectile'], m_wpn['emission'], owner_name=owner_name)

    if get_model_name(m_wpn['emission']) == "RandomTargetSpreadModel":
        data['spread'] = frnd(m_wpn['emission']['spread'])

    if get_model_name(m_wpn['emission']) == "EmissionWithOffsetsModel" and m_wpn['emission']["throwMarkerOffsetModels"] != None:
        my_emis = []
        if m_wpn['emission']["throwMarkerOffsetModels"] != []:
            for i in range(len(m_wpn['emission']["throwMarkerOffsetModels"])):
                my_emis.append(f"{frnd(m_wpn['emission']['throwMarkerOffsetModels'][i]['ejectX'])}, {frnd(m_wpn['emission']['throwMarkerOffsetModels'][i]['ejectY'])}, {frnd(m_wpn['emission']['throwMarkerOffsetModels'][i]['ejectZ'])} (side {i+1})")
            data['eject'] = '<br>'.join(my_emis)

    #
    # WEAPON BEHAVIORS
    #
    if m_wpn['behaviors']:
        for i in m_wpn['behaviors']:
            model_name = get_model_name(i)

            match model_name:
                case 'AlternateProjectileModel':
                    parse_prj(tower, data, i['projectile'], i['emissionModel'], owner_name=owner_name)

                case 'BonusProjectileAfterIntervalModel':
                    parse_prj(tower, data, i['projectileModel'], i['emissionModel'], owner_name=owner_name)

                case 'CreateSequencedTypedTowerCurrentIndexModel':
                    for j in i['towers']:
                        trim_tower.parse_tow(tower, j)

                case 'WeaponRateMinModel':
                    data['rateMin'] = frnd(i['min'])

                case 'GreatWhiteLimitProjectileModel':
                    data['rateMin'] = data['rate']

                case 'SubTowerFilterModel':
                    tower["subtowers"][name(i['baseSubTowerId'])]['count'] = frnd(i["maxNumberOfSubTowers"])

                case 'SpinModel':
                    data["rotateRate"] = (str(frnd(i["rotationPerSecond"])) if i["rotationPerSecond"] < 999 else "∞") + " deg/s"

                case 'LimitProjectileModel':
                    data['delay'] = frnd(i['delayInFrames'] / 60)

                case 'RandomAngleOffsetModel':
                    data["randomAngleMinOffset"] = frnd(i["minOffset"])
                    data["randomAngleMaxOffset"] = frnd(i["maxOffset"])

                case 'FireWhenAlternateWeaponIsReadyModel':
                    data['fireWhenAlternateWeaponIsReady'] = True


        for i in m_wpn['behaviors']:
            model_name = get_model_name(i)

            match model_name:

                case 'CritMultiplierModel':
                    for k,v in data['projectiles'].items():
                        if k == "_order": continue
                        v["critDamage"] = frnd(i["damage"])
                        v["critUpper"] = i["upper"]
                        v["critLower"] = i["lower"]

                case 'PierceFromLivesGainedModel':
                    data["piercePercentPerLife"] = frnd(i["piercePercentPerLife"])
                    data["piercePercentPerLifeCap"] = i["lifeCap"]

                case 'LifeBasedAttackSpeedModel':
                    data["ratePerLife"] = frnd(i["ratePerLife"])
                    data["ratePerLifeCap"] = i["lifeCap"]
                    data["ratePerLifeBaseRateIncrease"] = frnd(i["baseRateIncrease"])

                case 'BurstWeaponBehaviorModel':
                    data['burstCount'] = i['count']
                    data['burstInterval'] = frnd(i['interval'])
                
                case 'CritRollWithDistanceModel':
                    data['critDamageMultiplier'] = frnd(i['damageMultiplier'])
                    data['critChance'] = frnd(i['chance'])
                    data['critBonusPerDistance'] = frnd(i["bonusPerDistance"])

                case 'BloonDistanceRateBonusModel':
                    data['rateBonusPerRange'] = frnd(i["rateBonusPerRange"])
                    data['rateBonusPerRangeMax'] = i["rangeMax"]

                case 'StandoffModel':
                    data['rateDecreasePerBloon'] = frnd(i["rateDecreasePerBloon"])
                    data['rateIncreaseWithNoBloons'] = frnd(i["maxRateIncrease"])

                case 'VagrantWeaponBehaviorModel':
                    data['noTowersRateBonus'] = frnd(i["noTowersRateBonus"])
                    data["towerRangeBonusReduction"] = frnd(i["towerRangeBonusReduction"])
                    data["bloonInRangeAttackSpeedBuff"] = frnd(i["bloonInRangeAttackSpeedBuff"])
                    data['maxBloonAttackSpeedBuff'] =frnd(i['maxBloonAttackSpeedBuff'])

                case 'TheBlazingSunModel':
                    parse_prj(tower, data, i["burnBehaviorArea"], {}, owner_name=owner_name)
                    

    ret = {
        atk_name + " " + get_obj_name(m_wpn): data
    }

    return ret

def parse_atk(tower, parent, m_atk, owner_name="", retval=False):
    data_base = {
        'count': 1,
        'targetTypes': [],
        'range': frnd(m_atk['range']),
        "attackThroughWalls": m_atk["attackThroughWalls"],
        "fireWithoutTarget": m_atk["fireWithoutTarget"],
        "framesBeforeRetarget" : m_atk["framesBeforeRetarget"]
    }

    gyr = False

    if m_atk["addsToSharedGrid"]:
        data_base['sharedGridRange'] = frnd(m_atk["sharedGridRange"])

    # common stuff
    if m_atk['behaviors']:
        for i in m_atk['behaviors']:
            model_name = get_model_name(i)

            match model_name:
                case 'TargetFirstModel' | 'TargetFirstPrioCamoModel' | 'FighterPilotPatternFirstModel' | 'TargetFirstAirUnitModel' | 'TargetFirstSharedRangeModel' | 'CirclePatternFirstModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('First')
                    if model_name == 'TargetFirstSharedRangeModel': data_base["isSharedRangeEnabled"] = i["isSharedRangeEnabled"]

                case 'TargetDesperadoFirstModel' | 'TargetDesperadoLastModel' | 'TargetDesperadoCloseModel' | 'TargetDesperadoStrongModel':
                    data_base['targetTypes'] = ["Depends on targeting option"]

                case 'TargetLastModel' | 'TargetLastPrioCamoModel' | 'FighterPilotPatternLastModel' | 'TargetLastAirUnitModel' | 'TargetLastSharedRangeModel' | 'CirclePatternLastModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Last')
                    if model_name == 'TargetLastSharedRangeModel': data_base["isSharedRangeEnabled"] = i["isSharedRangeEnabled"]

                case 'TargetCloseModel' | 'TargetClosePrioCamoModel' | 'FighterPilotPatternCloseModel' | 'TargetCloseAirUnitModel' | 'TargetCloseSharedRangeModel' | 'CirclePatternCloseModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Close')
                    if model_name == 'TargetCloseSharedRangeModel': data_base["isSharedRangeEnabled"] = i["isSharedRangeEnabled"]

                case 'TargetStrongModel' | 'TargetStrongPrioCamoModel' | 'FighterPilotPatternStrongModel' | 'TargetStrongAirUnitModel' | 'TargetStrongSharedRangeModel' | 'CirclePatternStrongModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Strong')
                    if model_name == 'TargetStrongSharedRangeModel': data_base["isSharedRangeEnabled"] = i["isSharedRangeEnabled"]

                case 'TargetEliteTargettingModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Elite')

                case 'TargetPointerModel':
                    data_base['targetTypes'].append('Target pointer')
                case 'TargetSelectedPointModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Locked')

                case 'RandomPositionModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Random position')

                case 'TargetTrackModel' | 'NecromancerTargetTrackWithinRangeModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Normal (track)')

                case 'CloseTargetTrackModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Close (track)')

                case 'FarTargetTrackModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Far (track)')

                case 'SmartTargetTrackModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Smart')

                case 'TargetTrackOrDefaultModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Track or Default')
                case 'TargetGrapplableModel':
                    if i["isSelectable"]: data_base['targetTypes'] = ["Depends on targeting option"]
                    else: data_base['targetTypes'].append('Grapplable')


                case 'AttackFilterModel':
                    data_base.update(filt(i['filters']))

                case 'RotateToPointerModel':
                    data_base['rotateRate'] = (str(frnd(i['rate'])) if i['rate'] < 999 else "∞") + " deg/s"

                case 'CheckTargetsWithoutOffsetsModel':
                    data_base['checkTargetsWithoutOffsets'] = True

                case 'TargetFriendlyModel':
                    nlist = []
                    for j in i['ignoreList'].split(","):
                        nlist.append(tname(j))
                    data_base['targetFriendlyIgnoreList'] = ', '.join(nlist)

                case 'BrewTargettingModel':
                    nlist = []
                    for j in i['towerIgnoreList']:
                        if j != 'MonkeyAcademy': nlist.append(tname(j))
                    data_base['targetFriendlyIgnoreList'] = ', '.join(nlist)

                case 'GyrfalconPatternModel':
                    gyr = True
                    data_base["projectiles"] = {}
                    data_base["buffs"] = {}
                    data_base['rate'] = frnd(i["cooldown"])
                    parent['speed'] = frnd(i["maxSpeed"])
                    parent['turningSpeed'] = frnd(i["rotationSpeed"])

                    data_base["initialDamage"] = frnd(i["initialDamageModel"]["damage"])
                    data_base["initialDamageImmuneBloonProperties"] = frnd(i["initialDamageModel"]["immuneBloonProperties"])
                    data_base["grapplingDamage"] = frnd(i["initialDamageModel"]["damage"])
                    data_base["grapplingDamageImmuneBloonProperties"] = frnd(i["initialDamageModel"]["immuneBloonProperties"])
                    data_base["grapplingDamageRate"] = frnd(i["grappleDamageRate"])
                    parse_prj(tower, data_base, i["grabProjectileModel"], {}, owner_name=owner_name)

                    data_base["projectiles"][name(get_obj_name(i["grabProjectileModel"]))]["piercePenaltyForLead"] = i["leadPiercePenalty"]
                    data_base["projectiles"][name(get_obj_name(i["grabProjectileModel"]))]["piercePenaltyForCeramic"] = i["ceramicPiercePenalty"]
                    data_base["projectiles"][name(get_obj_name(i["grabProjectileModel"]))]["piercePenaltyForMoab"] = i["moabPiercePenalty"]
                    data_base["projectiles"][name(get_obj_name(i["grabProjectileModel"]))]["piercePenaltyForBfb"] = i["bfbPiercePenalty"]
                    data_base["projectiles"][name(get_obj_name(i["grabProjectileModel"]))]["piercePenaltyForZomg"] = i["zomgPiercePenalty"]
                    data_base["projectiles"][name(get_obj_name(i["grabProjectileModel"]))]["piercePenaltyForDdt"] = i["ddtPiercePenalty"]
                    

                    if i["initialDamageMoabModifierModel"] != None: data_base.update(parse_dmg(i["initialDamageMoabModifierModel"]))
                    if i["regrowDamageModifierModel"] != None: data_base.update(parse_dmg(i["regrowDamageModifierModel"]))


    ret = {}

    data_base['targetTypes'] = (' / ').join(data_base['targetTypes'])

    for i in m_atk['weapons']: ret.update(parse_wpn(tower, data_base, get_obj_name(m_atk), i, owner_name=owner_name))

    if gyr:
        ret = {name(m_atk["name"]): data_base}
    
    if retval:
        return ret
    else:
        add_sub(parent["attacks"], ret, owner_name=owner_name)