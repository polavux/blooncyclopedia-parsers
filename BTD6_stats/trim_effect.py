from trim_common import *
from trim_attack import *
import trim_projectile
from trim_ability import *




def parse_effs(tower, parent, prj_parent, behavs):
    def add_to_parent(name, data):
        if name not in ['AddBehaviorToBloonModel_Explosion', 'AddBehaviorToBloonModel_DegradeSplatEffect']:
            if "_order" not in parent: parent["_order"] = []
            parent[name] = data
            if name not in parent["_order"]: parent["_order"].append(name)
    def add_to_prj_parent(name, data):
        if name not in ['AddBehaviorToBloonModel_Explosion', 'AddBehaviorToBloonModel_DegradeSplatEffect']:
            if "_order" not in prj_parent['buffs']: prj_parent['buffs']["_order"] = []
            prj_parent['buffs'][name] = data
            if name not in prj_parent['buffs']["_order"]: prj_parent['buffs']["_order"].append(name)

    for i in behavs:
        if isinstance(i, int): continue
        model_name = get_model_name(i)
        #print(model_name)for i in m_prj['behaviors']:
        mname = get_model_name(i)

        match mname:
            case 'SlowModel':
                add_to_parent(name_mut(i['mutationId']), {
                    "layers": i["layers"],
                    "glueLevel": i["glueLevel"],
                    "isUnique": i["isUnique"],
                    "dontRefreshDuration": i["dontRefreshDuration"],
                    "cascadeMutators": i["cascadeMutators"],
                    "removeMutatorIfNotMatching": i["removeMutatorIfNotMatching"],
                    "matchLayersWithDamage": i["matchLayersWithDamage"],
                    "mutationId": i["mutationId"],
                    "glueLevel": i["glueLevel"],
                    "lifespan": frnd(i["lifespan"]),
                    "multiplier": frnd(i["multiplier"]),
                })
            case 'SlowMinusAbilityDurationModel':
                add_to_parent(name_mut(i['mutationId']), {
                    "layers": i["layers"],
                    "glueLevel": i["glueLevel"],
                    "isUnique": i["isUnique"],
                    "dontRefreshDuration": i["dontRefreshDuration"],
                    "cascadeMutators": i["cascadeMutators"],
                    "removeMutatorIfNotMatching": i["removeMutatorIfNotMatching"],
                    "matchLayersWithDamage": i["matchLayersWithDamage"],
                    "mutationId": i["mutationId"],
                    "glueLevel": i["glueLevel"],
                    "lifespan": frnd(i["Lifespan"]),
                    "multiplier": frnd(i["Multiplier"]),
                })
            case 'SlowForBloonModel':
                if name_mut(i['mutationId']) not in parent:
                    add_to_parent(name_mut(i['mutationId']), {
                        "layers": i["layers"],
                        "glueLevel": i["glueLevel"],
                        "isUnique": i["isUnique"],
                        "dontRefreshDuration": i["dontRefreshDuration"],
                        "cascadeMutators": i["cascadeMutators"],
                        "removeMutatorIfNotMatching": i["removeMutatorIfNotMatching"],
                        "matchLayersWithDamage": i["matchLayersWithDamage"],
                        "mutationId": i["mutationId"]
                    })
                if i['excluding']:
                    for j in i['bloonTags']:
                        match(j):
                            case "Moabs":
                                parent[name_mut(i['mutationId'])]['multiplier'] = frnd(i["Multiplier"])
                                parent[name_mut(i['mutationId'])]['lifespan'] = frnd(i["Lifespan"])
                            
                            case _: print("UNKNOWN SLOWFORBLOON A", j)

                    for j in i['bloonIds']: print("UNKNOWN SLOWFORBLOON A2", j)
                else:
                    for j in i['bloonTags']:
                        match(j):
                            case "Moabs":
                                parent[name_mut(i['mutationId'])]['multiplierForMoabs'] = frnd(i["Multiplier"])
                                parent[name_mut(i['mutationId'])]['lifespanForMoabs'] = frnd(i["Lifespan"])

                            case _: print("UNKNOWN SLOWFORBLOON B", j)

                    for j in i['bloonIds']:
                        match(j):
                            case "Moab":
                                parent[name_mut(i['mutationId'])]['multiplierForMoab'] = frnd(i["Multiplier"])
                                parent[name_mut(i['mutationId'])]['lifespanForMoab'] = frnd(i["Lifespan"])
                            case "Bfb":
                                parent[name_mut(i['mutationId'])]['multiplierForBfb'] = frnd(i["Multiplier"])
                                parent[name_mut(i['mutationId'])]['lifespanForBfb'] = frnd(i["Lifespan"])
                            case "Zomg":
                                parent[name_mut(i['mutationId'])]['multiplierForZomg'] = frnd(i["Multiplier"])
                                parent[name_mut(i['mutationId'])]['lifespanForZomg'] = frnd(i["Lifespan"])
                            case "Ddt":
                                parent[name_mut(i['mutationId'])]['multiplierForDdt'] = frnd(i["Multiplier"])
                                parent[name_mut(i['mutationId'])]['lifespanForDdt'] = frnd(i["Lifespan"])

                            case _: print("UNKNOWN SLOWFORBLOON B2", j)

                #add_to_parent(name_mut(i['mutationId']), eff)

            case 'SlowOnPopModel':
                add_to_parent(name_mut(i['mutationId']), {
                    "layers": i["layers"],
                    "glueLevel": i["glueLevel"],
                    "isUnique": i["isUnique"],
                    "dontRefreshDuration": i["dontRefreshDuration"],
                    "cascadeMutators": i["cascadeMutators"],
                    "removeMutatorIfNotMatching": i["removeMutatorIfNotMatching"],
                    "matchLayersWithDamage": i["matchLayersWithDamage"],
                    "mutationId": i["mutationId"],
                    "lifespan": frnd(i["Lifespan"]),
                    "multiplier": frnd(i["Multiplier"])
                })

            case 'SlowMaimMoabModel':
                add_to_parent('Maim MOAB', {
                    "multiplier": frnd(i["multiplier"]),
                    "lifespanForMoab": frnd(i['moabDuration']),
                    "lifespanForBfb": frnd(i['bfbDuration']),
                    "lifespanForZomg": frnd(i['zomgDuration']),
                    "lifespanForDdt": frnd(i['ddtDuration']),
                    "lifespanForBad": frnd(i['badDuration']),
                    "addDamagePerHit": frnd(i["bloonPerHitDamageAddition"])
                })

            case 'FreezeModel':
                eff = {
                    "layers": i["layers"],
                    "lifespan": frnd(i["lifespan"]),
                    "multiplier": frnd(i["speed"]),
                    "canFreezeMoabs": i['canFreezeMoabs'],
                    "mutationId": i["mutationId"],
                    "cascadeMutators": i["cascadeMutators"],
                    "applyAfterDamage": i["applyAfterDamage"]
                }
                if i["enablePercentChanceToFreeze"]: eff["percentChanceToFreeze"] = i["percentChanceToFreeze"]
                add_to_parent(name_mut(i['mutationId']), eff)

            case 'AddTagToBloonModel':
                add_to_parent('Radiation', {
                    "layers": i["layers"],
                    "isUnique": i["isUnique"],
                    "mutationId": i["mutationId"],
                    "lifespan": frnd(i["lifespan"])
                })

            case 'RemoveDamageTypeModifierModel':
                add_to_parent('Remove immunities', {
                    "layers": i["layers"],
                    "mutationId": i["mutationId"],
                    "lifespan": frnd(i["lifespan"])
                })

            case 'IncreaseBloonWorthModel':
                eff = {
                    "cash": frnd(i['cash']),
                    "cashMultiplier": frnd(i['cashMultiplier']),
                    "lifespan": frnd(i["duration"]),
                    "mutationId": i['mutatorId']
                }
                if i['filter'] != None: eff.update(filt([i['filter']]))
                add_to_parent(name_mut(i['mutatorId']), eff)

            case 'AddBehaviorToBloonModel':
                eff = {
                    'layers': i['layers'],
                    'lifespan': frnd(i['lifespan']),
                    "glueLevel": i["glueLevel"],
                    "applyOnlyIfDamaged": i["applyOnlyIfDamaged"],
                    'chance': frnd(i['chance'])
                }

                if i['filter'] != {} and i['filter'] != None:
                    eff.update(filt([i['filter']]))

                for j in i['behaviors']:
                    jmname = get_model_name(j)

                    match jmname:
                        case 'DamageOverTimeModel':
                            eff['damage'] = frnd(j["damage"])
                            eff['immuneBloonProperties'] = j["immuneBloonProperties"]
                            eff['interval'] = frnd(j["interval"])
                            eff['initialDelay'] = frnd(j["initialDelay"])
                            eff["triggerImmediate"] = j["triggerImmediate"]
                            eff['distributeToChildren'] = j['distributeToChildren']
                            if j["damageModifierModels"]:
                                for k in j["damageModifierModels"]:
                                    #print(k)
                                    if k['damageAddative'] > 0: eff.update(parse_dmg(k))

                        case 'DamageOverTimeForTagModel':
                            eff['damage'] = frnd(j["damage"])
                            eff['immuneBloonProperties'] = j["immuneBloonProperties"]
                            eff['interval'] = frnd(j["interval"])
                            eff['initialDelay'] = frnd(j["initialDelay"])
                            eff["triggerImmediate"] = j["triggerImmediate"]
                            eff['distributeToChildren'] = j['distributeToChildren']

                        case 'CarryProjectileModel':
                            trim_projectile.parse_prj(tower, prj_parent, j['projectile'], j['emission'])

                        case 'ProjectileOverTimeModel':
                            eff['interval'] = frnd(j["interval"])
                            eff["triggerImmediate"] = j["triggerImmediate"]
                            eff["initialDelay"] = j["initialDelay"]
                            eff["emitOnDestroy"] = j["emitOnDestroy"]

                            trim_projectile.parse_prj(tower, prj_parent, j['projectileModel'], j['emissionModel'])

                        case 'UnstableConcoctionSplashModel' | 'EmitOnPopModel' | 'EmitOnDestroyModel':
                            trim_projectile.parse_prj(tower, prj_parent, j['projectile'], j['emission'])
                            eff = {}

                            
                if eff != {}:
                    add_to_parent(name_mut(i['mutationId']) if get_obj_name(i) == '' else name(i["name"]), eff)   

            case 'WindModel':
                if frnd(i["chance"]) > 0:
                    eff = {
                        'distanceMin': frnd(i['distanceMin']),
                        'distanceMax': frnd(i['distanceMax']),
                        "chance": frnd(i["chance"]),
                        "affectMoab": i["affectMoab"]
                    }
                
                    match i["distanceScaleForTagsTags"]:
                        case 'Ceramic':
                            eff['ceramicMultiplier'] = frnd(i["distanceScaleForTags"])
                        case 'Zomg':
                            eff['zomgMultiplier'] = frnd(i["distanceScaleForTags"])

                    add_to_parent('Blowback', eff)

            case 'TranceBloonModel':
                add_to_parent('Trance', {
                    "multiplier": i["speedMultiplier"],
                    "multiplierForMoabs": i["moabOrbitSpeed"],
                    "lifespan": i['duration'],
                    "orbitRadius": i["orbitRadius"],
                    "radiusBloonSizeMultiplier": i["radiusBloonSizeMultiplier"],
                    "cooldown": i["cooldown"],
                    "immuneBloonProperties": i['fakeDamage']["immuneBloonProperties"],
                    "maxDotDamage": i["maxDotDamage"]
                })

            case 'AddBonusDamagePerHitToBloonModel':
                add_to_parent('Bonus damage', {
                    "collisionPass": i["collisionPass"],
                    "mutationId": i["mutationId"],
                    "lifespan": frnd(i["lifespan"]),
                    "perHitDamageAddition": frnd(i["perHitDamageAddition"]),
                    "layers": i["layers"],
                    "isUnique": i["isUnique"],
                    "lastAppliesFirst": i["lastAppliesFirst"],
                    "cascadeMutators": i["cascadeMutators"],
                    "overlayType": i["overlayType"]
                })

                        
            case 'KnockbackModel':
                add_to_parent('Knockback', {
                    "multiplier": frnd(1-i["lightMultiplier"]),
                    "multiplierForLead": frnd(1-i["heavyMultiplier"]),
                    "multiplierForCeramic": frnd(1-i["heavyMultiplier"]),
                    "multiplierForMoabs": frnd(1-i["moabMultiplier"]),
                    "mutationId": i["mutationId"],
                    "lifespan": frnd(i["lifespan"])
                })