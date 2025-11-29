from trim_common import *
from trim_attack import *
from trim_ability import *
from trim_buff import *
from trim_effect import *
import trim_collectable
import trim_tower

def parse_prj(tower, parent, m_prj, m_em, owner_name="", retval=False, prepend_name = ""):
    do_return = True

    data = {
        'pierce': frnd(m_prj['pierce']),
        'maxPierce': frnd(m_prj['maxPierce']),
        'ignoreBlockers': m_prj['ignoreBlockers'],
        'usePointCollisionWithBloons': m_prj['usePointCollisionWithBloons'],
        'canCollisionBeBlockedByMapLos': m_prj['canCollisionBeBlockedByMapLos'],
        'canCollisionBeBlockedByMapLos': m_prj['canCollisionBeBlockedByMapLos'],
        'radius': frnd(m_prj['radius']),
        'vsBlockerRadius': frnd(m_prj['vsBlockerRadius']),
        'effects': {},
        'buffs': {}
    }

    if m_prj['dontUseCollisionChecker'] and get_obj_name(m_prj) != 'Cluster' and get_obj_name(m_prj) != "SecondCluster" and get_obj_name(m_prj) != "BallLightningProj" and get_obj_name(m_prj) != "LightningProj": do_return = False

    # EMISSION
    if m_em != {}:
        match get_model_name(m_em):
            case 'ArcEmissionModel':
                data['angle'] =  frnd(m_em['angle'])
                data['offset'] = frnd(m_em['offset'])
                data['count'] = m_em['Count']

            case 'AdoraEmissionModel':
                data['angle'] = frnd(m_em['angleBetween']) * (m_em['count']-1)
                data['count'] = m_em['count']

            case 'ParallelEmissionModel':
                data['count'] = m_em['count']
                data['spreadLength'] = frnd(m_em['spreadLength'])
                data['offset'] = frnd(m_em['offsetStart'])

            case 'RandomEmissionModel':
                data['angle'] = frnd(m_em['angle'])
                data['count'] = m_em['count']

            case 'RandomArcEmissionModel':
                data['angle'] = frnd(m_em['angle'])
                data['randomAngle'] = frnd(m_em['randomAngle'])
                data['count'] = m_em['count']

            case 'EmissionOverTimeModel':
                data['count'] = m_em['count']
                data['timeBetween'] = frnd(m_em['timeBetween'])

            case 'EmissionWithOffsetsModel':
                data['count'] = m_em['projectileCount']
                data['angle'] = frnd(m_em['randomRotationCone'])

            case 'fuckemissionmodel':
                data['count'] = m_em['count']

            case 'MultiEmissionModel':
                parse_prj(tower, parent, m_em["secondaryProjectileModel"], {})


            case 'LineProjectileEmissionModel':
                data['speed'] = frnd(m_em["lengthSpeed"])

                if m_em["projectileInitialHitModel"] != {} and m_em["projectileInitialHitModel"] != None: parse_prj(tower, parent, m_em["projectileInitialHitModel"], {})
                if m_em["projectileAtEndModel"] != {} and m_em["projectileAtEndModel"] != None: parse_prj(tower, parent, m_em["projectileAtEndModel"], m_em["emissionAtEndModel"])

            case 'PrinceOfDarknessEmissionModel':
                parse_prj(tower, parent, m_em["alternateProjectile"], {})
    
    data.update(filt(m_prj['filters']))

    if m_prj['filters']:
        for i in m_prj['filters']:
            mname = get_model_name(i)
            
            match mname:
                case 'FilterAllModel':
                    do_return = False
                
    #
    # DAMAGE
    #
    for i in m_prj['behaviors']:
        mname = get_model_name(i)

        match mname:
            case 'DamageModel':
                data['damage'] = frnd(i['damage'])
                data['maxDamage'] = frnd(i['maxDamage'])
                data['immuneBloonProperties'] = i['immuneBloonProperties']
                data['distributeToChildren'] = i['distributeToChildren']
                data["overrideDistributeBlocker"] = i["overrideDistributeBlocker"]
                data["ignoreImmunityDestroy"] = i["ignoreImmunityDestroy"]

            case 'DamageInRingRadiusModel':
                data['damage'] = frnd(i['damage'])
                data['maxDamage'] = frnd(i['maxDamage'])
                data['immuneBloonProperties'] = i['immuneBloonProperties']
                data['distributeToChildren'] = i['distributeToChildren']
                data["overrideDistributeBlocker"] = i["overrideDistributeBlocker"]
                data["ignoreImmunityDestroy"] = i["ignoreImmunityDestroy"]
                data['innerRingRadius'] = frnd(i['innerRingRadius'])

            case 'DistributeToChildrenSetModel':
                data["overrideDistributeBlocker"] = True

            case 'DistributeToChildrenBloonModifierModel':
                data["overrideDistributeBlocker"] = True

            case 'DamagePercentOfMaxModel':
                data['damagePercent'] = frnd(i['percent'])

            case 'DamageModifierForTagModel':
                if i['damageAddative'] > 0:
                    for k, v in parse_dmg(i).items():
                        if k in data: data[k] += v
                        else: data[k] = v

            case 'DamageModifierForBloonTypeModel':
                if i['bloonId'] == "Ceramic": data['damageModifierForCeramicExceptCAS'] = frnd(i["damageAdditive"])
                if i['bloonId'] == "MOAB": data['damageModifierForMoab'] = frnd(i["damageAdditive"])

            case 'DamageModifierForBloonStateModel':
                match i['bloonState']:
                    case 'Ice':
                        data['damageModifierForFrozen'] = frnd(i["damageAdditive"])
                    case 'Stun':
                        data['damageModifierForStunned'] = frnd(i["damageAdditive"])
                    case 'StickyBomb' | 'ParagonSticky,StickyBomb':
                        data['damageModifierForStickied'] = frnd(i["damageAdditive"])
                    case 'LaserShock1':
                        data['damageModifierForShocked1'] = frnd(i["damageAdditive"])
                    case 'LaserShock2':
                        data['damageModifierForShocked2'] = frnd(i["damageAdditive"])
                    case 'LaserShock3':
                        data['damageModifierForShocked3'] = frnd(i["damageAdditive"])
                    case 'LaserShock4':
                        data['damageModifierForShocked4'] = frnd(i["damageAdditive"])

                    case _: print("UNKNOWN BLOONSTATE " + i["bloonState"])

            case 'SaudaAfflictionDamageModifierModel':
                data['damageModifierForStun'] = frnd(i["lv7NonMoabBonus"])
                data['damageModifierForStunMoabs'] = frnd(i["lv7MoabBonus"]) - frnd(i["lv7NonMoabBonus"])

                data['damageModifierForTagged'] = frnd(i["lv11NonMoabBonus"])
                data['damageModifierForTaggedMoabs'] = frnd(i["lv11NonMoabBonus"]) - frnd(i["lv11NonMoabBonus"])

                data['damageModifierForCamoOrRegrowOrFortified'] = frnd(i["lv19NonMoabBonus"])
                data['damageModifierForCamoOrRegrowOrFortifiedMoabs'] = frnd(i["lv19MoabBonus"]) - frnd(i["lv19NonMoabBonus"])

            case 'ScaleDamageWithTimeModel':
                data["baseDamageScale"] = frnd(i["baseDamage"])
                data["scaleDamagePerSecond"] = frnd(i["scalePerSecond"])
                data["maxScaleDamage"] = frnd(i["maxDamage"])

            case 'DamageModifierUnstableConcoctionModel':
                data['damageModifierUnstableConcoction'] = True

    #
    # OTHER BEHAVS
    #
    for i in m_prj['behaviors']:
        mname = get_model_name(i)

        match mname:
            case 'ScaleProjectileOverTimeModel':
                if i['bonusProjectileModel']: parse_prj(tower, parent, i['bonusProjectileModel'], i['emission'])
                data["baseScaleProjectile"] = frnd(i["baseScale"])
                data["scaleProjectilePerSecond"] = frnd(i["scalePerSecond"])
                data["maxScaleProjectile"] = frnd(i["maxScale"])

            case 'RemoveBloonModifiersModel':
                data['cleanseRegen'] = i["cleanseRegen"]
                data['cleanseCamo'] = i["cleanseCamo"]
                data['cleanseLead'] = i["cleanseLead"]
                data['cleanseFortified'] = i["cleanseFortified"]
                data['cleanseOnlyIfDamaged'] = i["cleanseOnlyIfDamaged"]
                data['cleanseExcludeList'] = (", ").join(i["bloonTagExcludeList"]).replace("Ddt", "DDT").replace("Bad", "BAD").replace("Zomg", "ZOMG")
                data['cleanseExplicitList'] = (", ").join(i["bloonTagExplicitList"])

            case 'RandomRangeTravelStraitModel':
                data['minDistance'] = frnd(i['minRange'])
                data['maxDistance'] = frnd(i['maxRange'])
                data['speed'] = frnd(i['speed'])

            case 'FallToGroundModel':
                data['delay'] = frnd(i["timeToTake"])

            case 'FollowPathModel':
                maxDist = 0
                for dist in i["path"]:
                    if dist[1] > maxDist: maxDist = dist[1]
                data["followPathMaxY"] = frnd(maxDist)
                data['speed'] = frnd(i['speed'])

            case 'AgeRandomModel':
                data['rounds'] = frnd(i['rounds'])
                data['minLifespan'] = frnd(i['minLifespan'])
                data['maxLifespan'] = frnd(i['maxLifespan'])

            case 'RetargetOnContactModel':
                data['bounceDistance']  = frnd(i['distance'])
                data['bounceMinDistance']  = frnd(i['minDistance'])
                data['maxBounces']  = frnd(i['maxBounces'])
                data['bounceDelay']  = frnd(i['delay'])
                data['bounceTargeting'] = i['targetType']['id']

            case 'LightningModel':
                data['bounceDistance']  = frnd(i['splitRange'])
                data['maxBounces']  = frnd(i['splits'])
                data['bounceDelay']  = frnd(i['delay'])

            case 'TrackTargetModel':
                data["seekDistance"] = frnd(i["distance"])
                data['trackNewTargets'] = i['trackNewTargets']
                data['constantlyAquireNewTarget'] = i['constantlyAquireNewTarget']
                data["maxSeekAngle"] = frnd(i["maxSeekAngle"])
                data["ignoreSeekAngle"] = i["ignoreSeekAngle"]
                data["overrideRotation"] = i["overrideRotation"]
                data["useLifetimeAsDistance"] = i["useLifetimeAsDistance"]
                data["turnRate"] = frnd(i["turnRate"])

            case 'TrackTargetWithinTimeModel':
                data["seekDistance"] = frnd(i["distance"])
                data['trackNewTargets'] = i['trackNewTargets']
                data['constantlyAquireNewTarget'] = i['constantlyAquireNewTarget']
                data["maxSeekAngle"] = frnd(i["maxSeekAngle"])
                data["ignoreSeekAngle"] = i["ignoreSeekAngle"]
                data["overrideRotation"] = i["overrideRotation"]
                data["useLifetimeAsDistance"] = i["useLifetimeAsDistance"]
                data["turnRate"] = frnd(i["TurnRate"])
                data['trackTime'] = frnd(i["timeInFrames"])

            case 'AdoraTrackTargetModel':
                data['rotation'] = frnd(i["rotation"])
                data['speed'] = frnd(i['minimumSpeed'])
                data['maxSpeed'] = frnd(i['maximumSpeed'])
                data['acceleration'] = frnd(i['acceleration'])
                data['accelerateInAngle'] = frnd(i['accelerateInAngle'])
                data['startDeceleratingIfAngleGreaterThan'] = frnd(i['startDeceleratingIfAngleGreaterThan'])
                data['lifespanWhileSeeking'] = frnd(i['lifespan'])

            case 'AccelerateModel':
                data['acceleration'] = frnd(i['acceleration'])
                data['maxSpeed'] = frnd(i['maxSpeed'])
                data['turnRateChange'] = frnd(i['turnRateChange'])
                data['maxTurnRate'] = frnd(i['maxTurnRate'])
                data['decelerate'] = i['decelerate']

            case 'RefreshPierceModel':
                data['refreshPierceInterval'] = frnd(i['interval'])

            case 'ClearHitBloonsModel':
                data['clearHitBloonsInterval'] = frnd(i['interval'])

            case 'CollideExtraPierceReductionModel':
                match i['bloonTag']:
                    case "Moabs":
                        data["piercePenaltyForMoabs"] = i["extraAmount"]
                    case "Moab":
                        data["piercePenaltyForMoab"] = i["extraAmount"]
                    case "Bfb":
                        data["piercePenaltyForBfb"] = i["extraAmount"]
                    case "Zomg":
                        data["piercePenaltyForZomg"] = i["extraAmount"]
                    case "Ddt":
                        data["piercePenaltyForDdt"] = i["extraAmount"]
                    case "Bad":
                        data["piercePenaltyForBad"] = i["extraAmount"]
                    case "Ceramic":
                        data["piercePenaltyForCeramic"] = i["extraAmount"]
                    case "":
                        data["piercePenalty"] = i["extraAmount"]

            case 'ExpireProjectileAtScreenEdgeModel':
                data['expireProjectileAtScreenEdge'] = True

            case 'ProjectileBlockerCollisionReboundModel':
                data['blockerCollisionRebound'] = True
                data["clearCollidedWith"] = True

            case 'MapBorderReboundModel':
                data["mapBorderRebound"] = True

            case 'PushBackModel':
                data['pushAmount'] = frnd(i["pushAmount"])
                data['pushTag'] = i['tag']
                data['pushMultiplierForMoab'] = frnd(i["multiplierMOAB"])
                data['pushMultiplierForBfb'] = frnd(i["multiplierBFB"])
                data['pushMultiplierForZomg'] = frnd(i["multiplierZOMG"])
                data['pushMultiplierForDdt'] = frnd(i["multiplierDDT"])
                data['pushOnlyIfDamaged'] = i['onlyIfDamaged']

            case 'InstantModel':
                data["ignoreTargetZ"] = i["ignoreTargetZ"]

            case 'MoabTakedownModel':
                do_return = False

            case 'CantBeReflectedModel':
                data["cantBeReflected"] = True

            case 'DestroyProjectileIfTowerDestroyedModel':
                data["destroyProjectileIfTowerDestroyed"] = True

            case 'ExpireProjectileOnBossSpawnedModel':
                data['expireProjectileOnBossSpawned'] = True

            case 'IncreaseBloonWorthModel':
                if i["mutatorId"] == "LeadToGold":
                    data["increaseBloonWorthLeadCash"] = frnd(i["cash"])
                else:
                    data["increaseBloonWorthMultiplier"] = frnd(i["cashMultiplier"])

            case 'PickupModel':
                do_return = False
                trim_collectable.parse_coll(parent, get_obj_name(m_prj), m_prj['behaviors'])

    for i in m_prj['behaviors']:
        mname = get_model_name(i)

        match mname:
            case 'TravelStraitModel' | 'TravelAlongPathModel' | 'TravelCurvyModel' | 'TravelStraitSlowdownModel':
                data['speed'] = frnd(i['speed'])
                if 'lifespan' not in data or data['lifespan'] > i['lifespan']:
                    data['lifespan'] = frnd(i['lifespan'])
        
            case 'AgeModel':
                data['rounds'] = frnd(i['rounds'])
                if 'lifespan' not in data or data['lifespan'] > i['lifespan']:
                    data['lifespan'] = frnd(i['lifespan'])

    #
    # CREATE TOWERS
    #
    for i in m_prj['behaviors']:
        mname = get_model_name(i)
        match mname:
            case 'CreateTowerModel':
                trim_tower.parse_tow(tower, i['tower'])
                #print(tower['subtowers'])
                do_return = False

            case 'CreateTypedTowerModel':
                trim_tower.parse_tow(tower, i['crushingTower'])
                trim_tower.parse_tow(tower, i['boomTower'])
                trim_tower.parse_tow(tower, i['coldTower'])
                trim_tower.parse_tow(tower, i['energyTower'])


    


    #
    # CREATE PROJECTILES BEFORE DO_RET
    #
    for i in m_prj['behaviors']:
        mname = get_model_name(i)
        match mname:
            case 'CreateProjectilesAlongPathWhenCloseModel':
                do_return = False

                parse_prj(tower, parent, i['projectile'], {
                    "$type": "SingleEmissionModel"
                })

    if do_return:
        ret = {
            prepend_name + get_obj_name(m_prj): data
        }
    else:
        ret = {}




    #
    # EFFECTS
    #
    parse_effs(tower, data['effects'], parent, m_prj['behaviors'])
    parse_buffs(data['buffs'], m_prj['behaviors'], prj_parent=parent['buffs'])
    #if data['buffs'] != {}: print('b', data['buffs'])
                

    #
    # EFFECT MODIFIERS
    #
    for i in m_prj['behaviors']:
        mname = get_model_name(i)

        match mname:
            case 'SlowModifierForTagModel':
                for k, v in data["effects"].items():
                    if k != "_order" and "mutationId" in v and "multiplier" in v and (v["mutationId"].split(":")[0]) == (i['slowId'].split(":")[0]):

                        
                        if i["makeNotTag"]:
                            v["multiplier"] = frnd(i["slowMultiplier"])
                        else:

                            match i['tag']:
                                case 'Moabs':
                                    if i["slowMultiplier"] != 1: v["multiplierForMoabs"] = frnd(i["slowMultiplier"])
                                    v["lifespanForMoabs"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Moab':
                                    if i["slowMultiplier"] != 1: v["multiplierForMoab"] = frnd(i["slowMultiplier"])
                                    v["lifespanForMoab"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Bfb':
                                    if i["slowMultiplier"] != 1: v["multiplierForBfb"] = frnd(i["slowMultiplier"])
                                    v["lifespanForBfb"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Zomg':
                                    if i["slowMultiplier"] != 1: v["multiplierForZomg"] = frnd(i["slowMultiplier"])
                                    v["lifespanForZomg"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Ddt':
                                    if i["slowMultiplier"] != 1: v["multiplierForDdt"] =frnd( i["slowMultiplier"])
                                    v["lifespanForDdt"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Bad':
                                    if i["slowMultiplier"] != 1: v["multiplierForBad"] =frnd(i["slowMultiplier"])
                                    v["lifespanForBad"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Miniboss':
                                    if i["slowMultiplier"] != 1: v["multiplierForMiniboss"] =frnd(i["slowMultiplier"])
                                    v["lifespanForMiniboss"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Black':
                                    if i["slowMultiplier"] != 1: v["multiplierForBlack"] =frnd(i["slowMultiplier"])
                                    v["lifespanForBlack"] = frnd(frnd(i["lifespanOverride"]))
                                case 'Zebra':
                                    if i["slowMultiplier"] != 1: v["multiplierForZebra"] =frnd(i["slowMultiplier"])
                                    v["lifespanForZebra"] = frnd(frnd(i["lifespanOverride"]))

                                case _: print('UNKNOWN SLOWMOD '  + i['tag'])

    #
    # CREATE MORE PROJECTILES
    #
    for i in m_prj['behaviors']:
        mname = get_model_name(i)
        match mname:
            case 'CreateProjectileOnExhaustFractionModel' | 'CreateProjectileOnExhaustPierceModel' | 'CreateProjectileOnIntervalModel' | 'CreateProjectileOnContactModel' | 'CreateProjectileOnExpireModel' | 'EmitOnDamageModel':
                
                x = parse_prj(tower, parent, i['projectile'], i['emission'], retval=True)
                
                #x = parse_prj(tower, parent, i['projectile'], i['emission'], retval=True, prepend_name=get_obj_name(i) if get_obj_name(i) != "" else prepend_name+"2" if prepend_name != "" else "")
                # special case for glord/gdom dot
                if 'MoabDot' in x:
                    print(x["MoabDot"]["effects"])
                    data["effects"].update(x["MoabDot"]["effects"])
                # special case for glord/gdom dot
                else:
                    if mname == "CreateProjectileOnExhaustPierceModel": print(x)
                    parse_prj(tower, parent, i['projectile'], i['emission'])
                    #parse_prj(tower, parent, i['projectile'], i['emission'], prepend_name=get_obj_name(i) if get_obj_name(i) != "" else prepend_name+"2" if prepend_name != "" else "")
                 
            case 'CreateGreatWhiteEffectModel':
                parse_prj(tower, parent, i['thrashingProjectileModel'], i["emissionModel"])
                parent['thrashingProjectileRate'] = frnd(i['thrashingProjectileRate'])
            
            case 'CreateProjectilesOnTrackOnExpireModel':
                    parse_prj(tower, parent, i['projectile'], {
                        "$type": "EmissionWithOffsetsModel",
                        "behaviors": [],
                        'projectileCount': i['count']
                    })

            case 'CreateProjectilesOnTrackOnExhaustFractionModel':
                    parse_prj(tower, parent, i['projectile'], {
                        "$type": "fuckemissionmodel",
                        'count': i['amtOfEmissions']
                    })

            case 'AcidPoolModel':
                data['lifespan'] = frnd(i['Lifespan'])

                if frnd(i["lifespanIfMisses"]) != 0:
                    x = copy.deepcopy(data)

                    x['radius'] = frnd(i['radiusIfMisses'])
                    x['lifespan'] = frnd(i['lifespanIfMisses'])
                    x['pierce'] = frnd(i['pierce'])

                    ret["Acid Pool"] = x

            case 'SpawnZombieOnBloonDestroyedModel':
                parse_prj(tower, parent, i['zombieProjectile'], i['singleEmissionModel'])

            case 'EatBloonModel' | 'WallOfTreesModel':
                data['capacity'] = frnd(i['rbeCapacity'])
                data['cashMultiplier'] = frnd(i['rbeCashMultiplier'])

    #if m_prj["name"] == 'ProjectileModel_SpawningProjectile': print(owner_name, retval)
    

    if retval:
        return ret
    else:
        add_sub(parent["projectiles"], ret, owner_name=owner_name, reverse=True)