from trim_common import *
from trim_attack import *
from trim_projectile import *
from trim_ability import *




def parse_buffs(parent, behavs, prj_parent={}):
    def add_to_parent(name, data):
        if "_order" not in parent: parent["_order"] = []
        parent[name] = data
        if name not in parent["_order"]: parent["_order"].append(name)
    def add_to_prj_parent(name, data):
        if name not in ['AddBehaviorToBloonModel_Explosion']:
            if "_order" not in prj_parent: prj_parent["_order"] = []
            prj_parent[name] = data
            if name not in prj_parent["_order"]: prj_parent["_order"].append(name)

    for i in behavs:
        if isinstance(i, int): continue
        model_name = get_model_name(i)
        #print(model_name)

        # from towers
        match model_name:
            case 'VisibilitySupportModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"]
                })
            
            case 'RangeSupportModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "rangePercentage": frnd(i["multiplier"]), # 0.1 multiplier means +10%
                    "rangeAdditive": frnd(i["additive"]) # 5.0 means +5 flat range
                })
                parent[name_mut(i['mutatorId'])].update(filt(i['filters']))

            case 'PierceSupportModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "pierceAdditive": frnd(i["pierce"]) # 5.0 means +5 flat pierce
                })
                parent[name_mut(i['mutatorId'])].update(filt(i['filters']))

            case 'AbilityCooldownScaleSupportModel':
                add_to_parent("Ability cooldown buff", {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "abilityCooldownMultiplier": frnd(i["abilityCooldownSpeedScale"]),
                    "affectsOnlyWater": i["affectsOnlyWater"]
                })
                parent['Ability cooldown buff'].update(filt(i['filters']))

            case 'RateSupportModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "rateMultiplier": frnd(i["multiplier"])
                })
                parent[name_mut(i['mutatorId'])].update(filt(i['filters']))

            case 'PiercePercentageSupportModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "pierceMultiplier": frnd(i["percentIncrease"])
                })
                parent[name_mut(i['mutatorId'])].update(filt(i['filters']))

            case 'DamageModifierSupportModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"]
                })
                parent[name_mut(i['mutatorId'])].update(filt(i['filters']))
                parent[name_mut(i['mutatorId'])].update(parse_dmg(i['damageModifierModel'], 'damageAdditive'))

            case 'FlagshipAttackSpeedIncreaseModel':
                add_to_parent('Flagship buff', {
                    "maxStacks": i["maxStackSize"],
                    'isGlobal': i['isGlobalRange'],
                    "rateMultiplier": frnd(i["attackSpeedIncrease"])
                })
            case 'SupportShinobiTacticsModel':
                add_to_parent(name_mut(i['mutatorId']), {
                    'isGlobal': i['isGlobalRange'],
                    "maxStackSize": i["maxStackSize"],
                    "rateMultiplier": frnd(i["multiplier"]),
                    "piercePercentage": 0.08
                })
                parent[name_mut(i['mutatorId'])].update(filt(i['filters']))

            case 'SubCommanderSupportModel':
                add_to_parent('Sub Commander buff', {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "pierceAdditive": frnd(i["pierceIncrease"]),
                    "damageAdditive": frnd(i["damageIncrease"]),
                    "damageMultiplier": frnd(i["damageScale"])
                })
                parent['Sub Commander buff'].update(filt(i['filters']))

            case 'PoplustSupportModel':
                add_to_parent('Poplust buff', {
                    'isGlobal': i['isGlobalRange'],
                    "maxStackSize": i["maxStackSize"],
                    "ratePercentage": frnd(i["ratePercentIncrease"]),
                    "piercePercentage": frnd(i["piercePercentIncrease"])
                })

            

            case "TradeEmpireBuffModel":
                add_to_parent('Trade Empire buff', {
                    "maxStacks": i["maxStackSize"],
                    'isGlobal': i['isGlobalRange'],
                    'cashPerRoundPerMechantship': frnd(i['cashPerRoundPerMechantship']),
                    'cashPerRoundPerFavouredTrades': frnd(i['cashPerRoundPerFavouredTrades']),
                    "damageAdditive": i["damageBuff"],
                    "damageAdditiveForCeramic": i["ceramicDamageBuff"],
                    "damageAdditiveForMoabs": i["moabDamageBuff"]
                })

            case 'CashbackZoneModel':
                add_to_parent('Sellback rate buff', {
                    "maxStacks": i["maxStacks"],
                    'isGlobal': i['isGlobalRange'],
                    "cashbackZoneMultiplier": frnd(i["cashbackZoneMultiplier"])
                })

            case 'PlacementAreaTypeRangeBuffModel':
                add_to_parent('Buff when in water', {
                    "rangeMultiplier": frnd(i["rangeMultiplier"])
                })
            case 'PrinceOfDarknessZombieBuffModel':
                add_to_parent('Undead Bloon buff', {
                    "damageAdditive": frnd(i["damageIncrease"]),
                    "lifespanMultiplier": frnd(i["distanceMultiplier"])
                })
            case 'SupportStackingRangeModel':
                add_to_parent('Echosense Network', {
                    'isGlobal': i['isGlobalRange'],
                    "rangePercentage": frnd(i["rangeMultiplier"]),
                    "maxStackSize": i["maxStackSize"]
                })

            case 'StartOfRoundRateBuffModel':
                add_to_parent('Start-of-round buff', {
                    "rateMultiplier": frnd(i["modifier"]),
                    "lifespan": frnd(i["duration"])
                })

            # from abilities
            case 'LongArmOfLightModel':
                add_to_parent('Buff', {
                    "damageAdditive": i["damageIncrease"],
                    "pierceMultiplier": frnd(i["multiplier"]),
                    "rangeMultiplier": frnd(i["multiplier"]),
                    "radiusMultiplier": frnd(i['projectileRadiusMultiplier']),
                    "immuneBloonProperties": i["immuneBloonProperties"],
                    "lifespan": frnd(i["lifespan"])
                })

            case 'BloodSacrificeModel':
                add_to_parent('Buff', {
                    "lifespan": frnd(i["buffDuration"]),
                    "maxStackSize": i["maxBonusCount"]
                })

            case 'IncreaseRangeModel':
                add_to_parent('Range buff', {
                    "rangeAdditive": frnd(i["addative"]),
                    "lifespan": i["lifespanFrames"] / 60
                })

            case 'MutateDamageOnAbilityModel':
                add_to_parent('Explosion buff', {
                    "damage": i["damageIncrease"],
                    "lifespan": i["lifespanFrames"] / 60
                })

            
            case 'DamageUpModel':
                add_to_parent('Buff', {
                    "damageAdditive": i["additionalDamage"],
                    "lifespan": frnd(i["lifespanFrames"] / 60)
                })

            case 'TurboModel':
                add_to_parent('Buff', {
                    "rateMultiplier": frnd(i["multiplier"]),
                    "damageAdditive": i["extraDamage"],
                    "lifespan": frnd(i["lifespan"]),
                    "radiusPercentage": frnd(i['projectileRadiusScaleBonus'])
                })

            case 'EruptionModel':
                add_to_parent('Buff', {
                    'lifespanMultiplier': frnd(i['projectileLifespanMult'])
                })
            case 'MonkeyFanClubModel':
                add_to_parent('Buff', {
                    "lifespan": frnd(i["lifespan"]),
                    "rateMultiplier": frnd(i["reloadModifier"]),
                    "pierceAdditive": frnd(i["bonusPierce"]),
                    "damageAdditive": frnd(i["bonusDamage"]),
                    "projectileRadius":frnd(i["projectileRadius"]),
                    "eject": ', '.join(map(str, [frnd(i['ejectX']), frnd(i['ejectY']), frnd(i['ejectZ'])])),

                })

            case 'OverclockModel':
                add_to_parent('Buff', {
                    "lifespan": i["lifespanFrames"] / 60,
                    "rateMultiplier": frnd(i["rateModifier"]),
                    "rangeMultiplierForVillages": frnd(i["villageRangeModifier"]),
                    "maxStackSize": i["maxStacks"]
                })
                if i["isParagonMode"]:
                    add_to_parent('Zone buff', {
                        "lifespan": i["paragonZoneLifespanFrames"] / 60,
                        "rateMultiplier": frnd(i["rateModifier"]),
                        "rangeMultiplierForVillages": frnd(i["villageRangeModifier"]),
                        "maxStackSize": i["maxStacks"],
                        "range": frnd(i["paragonZoneRange"])
                    })  

            case 'TakeAimModel':
                add_to_parent('Buff', {
                    "lifespan": i["lifespanFrames"] / 60,
                    "rangeMultiplier": frnd(i["rangeModifier"]),
                    "spreadMultiplier": frnd(i["spreadModifier"]),
                    "immunitiesGranted": i["immunitiesGranted"]
                })

            case 'VigilanteTowerBehaviorModel':
                add_to_parent('Nomad buff', {
                    "lifespan": i["loseLifeBuffDurationFrames"] / 60,
                    "cooldown": i["loseLifeBuffCooldownFrames"] / 60,
                    "rateMultiplier": frnd(i["loseLifeAttackSpeedBuff"]),
                    "rangeAdditive": frnd(i["loseLifeRangeBuff"])
                })

            case 'OverclockPermanentModel':
                add_to_parent('Ultraboost buff', {
                    "rateMultiplier": frnd(i["rateModifier"]),
                    "rangeMultiplierForVillages": frnd(i["villageRangeModifier"]),
                    "maxStackSize": i["maxStacks"]
                })


            # from projs
            case 'AddAcidicMixtureToProjectileModel':
                add_to_prj_parent('Buff', {
                    'damageAdditiveForCeramic': 1,
                    'damageAdditiveForMoabs': 1,
                    'damageAdditiveForFortifiedLead': 1,
                    'charges': i['towerBehaviors'][0]['maxCount'],
                    'maxCharges': i['cap']
                })

            case 'AddBerserkerBrewToProjectileModel':
                add_to_prj_parent('Buff', {
                    'lifespan': frnd(i["lifespan"]),
                    'damageAdditive': frnd(i["damageUp"]),
                    'pierceAdditive': frnd(i["pierceUp"]),
                    'ratePercentage': frnd(i['rateUp']),
                    'rangePercentage': frnd(i['rangeUp']),
                    'charges': i['towerBehaviors'][0]['maxCount'],
                    'rebuffCooldown': frnd(i['rebuffBlockTime'])
                })

            case 'PierceUpTowersModel':
                add_to_prj_parent('Pierce buff', {
                    'lifespan': frnd(i["lifespan"]),
                    'pierceAdditive': frnd(i["increase"])
                })

            case 'DamageUpTowersModel':
                add_to_prj_parent('Damage buff', {
                    'lifespan': frnd(i["lifespan"]),
                    'damageAdditive': frnd(i["increase"])
                })

            case 'DamageUpTagTowersModel':
                eff = {
                    'lifespan': frnd(i["lifespan"]),
                    'pierceAdditive': frnd(i["increase"])
                }
                match i['bloonTag']:
                    case 'Lead, Ddt': eff['damageAdditiveForLeadOrDdt'] = frnd(i["increase"])
                    case _: print("UNKNOWN DAMAGEUPTAGTOWERS", get_obj_name(i))

                add_to_prj_parent('Damage bonus buff', eff)

            case 'RateSupportExplosiveModel':
                add_to_parent('Attack speed buff', {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "rateMultiplier": frnd(i["multiplier"])
                })
                parent['Attack speed buff'].update(filt(i['filters']))

            case 'ProjectileRadiusSupportModel':
                add_to_parent('Projectile radius buff', {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "radiusMultiplier": frnd(i["multiplier"])
                })
                ids = []
                for j in i["filterTowers"]:
                    ids.append(tname(j))
                parent['Projectile radius buff']['filterInBaseTowerId'] = ', '.join(ids)

            case 'RateSupportBombExpertModel':
                add_to_parent('Bomb Shooter buff', {
                    'isGlobal': i['isGlobal'],
                    "customRadius": frnd(i["customRadius"]),
                    "appliesToOwningTower": i["appliesToOwningTower"],
                    "maxStackSize": i["maxStackSize"],
                    "rangePercentage": frnd(i["rangeMultiplier"]),
                    "piercePercentage": frnd(i["pierceMultiplier"])
                })

            case 'ObynGlobalSupportModel':
                add_to_parent('Druid of the Jungle buff', {
                    'rangePercentage': frnd(i['dotjRangeMultiplier'])
                })
                add_to_parent('Druid of the Storm buff', {
                    'radiusMultiplier': frnd(i['dotsProjectileRadius']),
                    'rateMultiplier': frnd(i['tornadoAttackCooldownReduction'])
                })
                add_to_parent('Magic Monkeys buff', {
                    'abilityCooldownPercentage': frnd(i['mmAbilityCooldownMultiplier'])
                })




            case 'SubmergeModel':
                #tow['attacks'].update(parse_atk(i['submergeAttackModel']))
                if frnd(i["abilityCooldownSpeedScale"]) > 1: add_to_parent("Ability cooldown buff", {
                    'isGlobal': False,
                    "abilityCooldownMultiplier": frnd(i["abilityCooldownSpeedScale"])
                })
                if frnd(i["abilityCooldownSpeedScaleGlobal"]) > 1: add_to_parent("Ability cooldown buff (global)", {
                    'isGlobal': True,
                    "abilityCooldownMultiplier": frnd(i["abilityCooldownSpeedScaleGlobal"]),
                    "heroXpMultiplier": frnd(i['heroXpScale'])
                })
                if frnd(i["abilityCooldownSpeedScaleParagon"]) > 0: add_to_parent("Ability cooldown buff (Paragon)", {
                    'isGlobal': False,
                    "abilityCooldownMultiplier": frnd(i["abilityCooldownSpeedScaleParagon"]),
                    "filterOutNonParagon": True
                })
                if i["monkeySubParagonSupportModel"]:
                    add_to_parent("Sub buff", {
                        'isGlobal': i["monkeySubParagonSupportModel"]['isGlobal'],
                        "customRadius": frnd(i["monkeySubParagonSupportModel"]["customRadius"]),
                        "appliesToOwningTower": i["monkeySubParagonSupportModel"]["appliesToOwningTower"],
                        "maxStackSize": i["monkeySubParagonSupportModel"]["maxStackSize"],
                        "piercePercentage": frnd(i["monkeySubParagonSupportModel"]["subBonusPierceMultiplier"]),
                        "damagePercentage": frnd(i["monkeySubParagonSupportModel"]["subBonusDamageMultiplier"]),
                        "filterInBaseTowerId": "Monkey Sub"
                    })
                    add_to_parent("Hero buff", {
                        'isGlobal': i["monkeySubParagonSupportModel"]['isGlobal'],
                        "customRadius": frnd(i["monkeySubParagonSupportModel"]["customRadius"]),
                        "appliesToOwningTower": i["monkeySubParagonSupportModel"]["appliesToOwningTower"],
                        "maxStackSize": i["monkeySubParagonSupportModel"]["maxStackSize"],
                        "piercePercentage": frnd(i["monkeySubParagonSupportModel"]["heroBonusPierceMultiplier"]),
                        "damagePercentage": frnd(i["monkeySubParagonSupportModel"]["heroBonusDamageMultiplier"]),
                        "rateMultiplier": frnd(i["monkeySubParagonSupportModel"]["heroRateMultiplier"]),
                        "heroXpMultiplier": frnd(i["monkeySubParagonSupportModel"]['heroXpMultiplier']),
                        'filterInSets': "Hero"
                    })

    #if parent != {}: print('a', parent)