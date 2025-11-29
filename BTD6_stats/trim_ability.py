from trim_common import *
from trim_buff import *
import trim_attack
import trim_projectile
import trim_tower


def parse_abil(tower, tower_name, m_abil):
    data = {
        'cooldown': m_abil['cooldown'],
        'maxActivationsPerRound': m_abil['maxActivationsPerRound'],
        'canActivateBetweenRounds': m_abil['canActivateBetweenRounds'],
        "restrictAbilityAfterMaxRoundTimer": m_abil["restrictAbilityAfterMaxRoundTimer"],
        'attacks': {},
        'projectiles': {},
        'effects': {},
        'buffs': {},
        'collectables': {}
    }

    #
    # ABILITY BEHAVIORS
    #
    for i in m_abil['behaviors']:
        if isinstance(i, int): continue
        mname = get_model_name(i)

        match mname:
            case 'AbilityDamageAllModel':
                if i["inclusive"]: data['damageToBad'] = i['damage']
                else: data['damageToNonBad'] = i['damage']
            
            case 'CarpetBombAbilityModel':
                trim_projectile.parse_prj(tower, data, i['projectileModel'], i['singleEmissionModel'], owner_name=get_obj_name(m_abil))

            case 'ActivateTempTargetPrioSupportZoneModel':
                data['lifespan'] = i['lifespan']

            case 'ArtilleryCommandModel':
                data['lifespan'] = frnd(i["buffFrames"] / 60)

            case 'ImmunityModel':
                data['lifespan'] = frnd(i["lifespan"])

            case 'MutateRemoveAllAttacksOnAbilityActivateModel':
                data['pauseAllOtherAttacks'] = frnd(i['lifespan'])

            case 'ActivateAttackModel':
                if not i["isOneShot"]: data['lifespan'] = frnd(i['lifespan'])

                for j in i['attacks']:
                    atkdata = trim_attack.parse_atk(tower, data, j, retval=True, owner_name=get_obj_name(m_abil))
                    
                    for k, v in trim_attack.parse_atk(tower, data, j, retval=True, owner_name=get_obj_name(m_abil)).items():
                        # attack doesn't last
                        if i["isOneShot"] or v['rate'] > 999:
                            #print(v['rate'])
                            del atkdata[k]['rate']

                        
                        for kk, vv in data['attacks'].items():
                            if kk != "_order":
                                cmp = trim_tower.atk_cmp(vv, v)
                                if cmp['result']:
                                    del atkdata[k]

                                    data['attacks'][kk]['count'] += 1
                                    #print(tow['attacks'][kk]['eject'])
                                    if cmp['ejects'] != "":
                                        if data['attacks'][kk]['count'] == 2: data['attacks'][kk]['eject'] += " (1)"
                                        data['attacks'][kk]['eject'] += "<br>" + cmp['ejects'] + ' (' + str(data['attacks'][kk]['count']) + ')'
                                    if cmp['tts'] != "":
                                        if data['attacks'][kk]['count'] == 2: data['attacks'][kk]['targetTypes'] += " (1)"
                                        data['attacks'][kk]['targetTypes'] += "<br>" + cmp['tts'] + ' (' + str(data['attacks'][kk]['count']) + ')'
                                    print('cmp', k, kk)

                    if 'GroundZero_ Weapon' in atkdata:
                        add_sub(data["projectiles"], {'Explosion': atkdata['GroundZero_ Weapon']['projectiles']['Explosion']}, owner_name=get_obj_name(m_abil))
                    elif i["name"] == "ActivateAttackModel_StompAbility":
                        add_sub(data["projectiles"], {'Projectile': atkdata['Attack_ Weapon']['projectiles']['Explosion']}, owner_name=get_obj_name(m_abil))

                    elif m_abil["displayName"] == 'Snowstorm' or m_abil["displayName"] == 'Absolute Zero':
                        add_sub(data["projectiles"], {'Projectile': atkdata['Snowstorm_ Weapon']['projectiles']['Projectile']}, owner_name=get_obj_name(m_abil))

                    elif m_abil["displayName"] == "Support Drop":
                        if 'AttackCash_ Weapon' in atkdata: add_sub(data["collectables"], {'Cash crate': atkdata['AttackCash_ Weapon']['collectables']['Collectable']}, owner_name=get_obj_name(m_abil))
                        if 'AttackLives_ Weapon' in atkdata: add_sub(data["collectables"], {'Life crate': atkdata['AttackLives_ Weapon']['collectables']['Collectable']}, owner_name=get_obj_name(m_abil))

                    elif m_abil['displayName'] == 'Firestorm':
                        if 'Attack_ Weapon' in atkdata:
                            add_sub(data["projectiles"], {'Projectile': atkdata['Attack_ Weapon']['projectiles']['Projectile']}, owner_name=get_obj_name(m_abil))
                            data['buffs'].update(atkdata['Attack_ Weapon']['buffs'])
                        else:
                            add_sub(data["projectiles"], {'MOAB projectile': atkdata['MOABAttack_ Weapon']['projectiles']['Projectile']}, owner_name=get_obj_name(m_abil))
                    elif m_abil['displayName'] == 'Bomb Blitz':
                        add_sub(data["projectiles"], {'Explosion': atkdata['Attack_ Weapon']['projectiles']['Explosion']}, owner_name=get_obj_name(m_abil))
                        add_sub(data["projectiles"], {'Instakill': atkdata['Attack_ BelowBfbWeapon']['projectiles']['Explosion']}, owner_name=get_obj_name(m_abil))
                    elif m_abil['displayName'] == 'First Strike Capability':
                        add_sub(data["projectiles"], {'Missile': atkdata['Attack_ Weapon']['projectiles']['Missile']}, owner_name=get_obj_name(m_abil))
                        add_sub(data["projectiles"], {'Explosion': atkdata['Attack_ Weapon']['projectiles']['Explosion']}, owner_name=get_obj_name(m_abil))

                    elif 'Boom_ Weapon' in atkdata:
                            add_sub(data["projectiles"], {'Projectile': atkdata['Boom_ Weapon']['projectiles']['Projectile']}, owner_name=get_obj_name(m_abil))
                            add_sub(data["projectiles"], {'Explosion': atkdata['Boom_ Weapon']['projectiles']['Explosion']}, owner_name=get_obj_name(m_abil))

                    elif 'TechTerror_ Weapon' in atkdata:
                        add_sub(data["projectiles"], {'Projectile': atkdata['TechTerror_ Weapon']['projectiles']['Projectile']}, owner_name=get_obj_name(m_abil))
                    elif m_abil["displayName"] == 'Sabotage':
                        add_sub(data['projectiles'], {'Projectile': atkdata['Attack_ Weapon']['projectiles']['Projectile']}, owner_name=get_obj_name(m_abil))
                    elif m_abil['displayName'] == 'Supply Drop':
                        add_sub(data['collectables'], {'Collectable': atkdata['Attack_ Weapon']['collectables']['Collectable']}, owner_name=get_obj_name(m_abil))
                    else:
                        add_sub(data["attacks"], atkdata, owner_name=get_obj_name(m_abil))

            case 'ActivateAttackCreateTowerPlacementModel':
                for j in i['attacks']:
                    trim_attack.parse_atk(tower, data, j, owner_name=get_obj_name(m_abil))

            case 'FinalStrikeModel':
                data['pauseAllOtherAttacks'] = frnd(i['countdown'])
                trim_projectile.parse_prj(tower, data, i['projectileModel'], i['emissionModel'], owner_name=get_obj_name(m_abil))

            case 'PhoenixRebirthModel':
                trim_projectile.parse_prj(tower, data, i['projectileExplosionModel'],{"$type": "SingleEmissionModel","behaviors": []}, owner_name=get_obj_name(m_abil))
                trim_projectile.parse_prj(tower, data, i['projectileBFB'],{"$type": "SingleEmissionModel","behaviors": []}, owner_name=get_obj_name(m_abil))
                trim_projectile.parse_prj(tower, data, i['projectileZOMG'],{"$type": "SingleEmissionModel","behaviors": []}, owner_name=get_obj_name(m_abil))

            case 'SpikeaggedonModel':
                trim_projectile.parse_prj(tower, data, i['projectileModel'],i["singleEmissionModel"], owner_name=get_obj_name(m_abil))

            case 'MarkedToPopModel':
                trim_attack.parse_atk(tower, data, i["markingAttackModel"], owner_name=get_obj_name(m_abil))
                trim_attack.parse_atk(tower, data, i["executionAttackModel"], owner_name=get_obj_name(m_abil))
                data['lifespan'] = frnd(i['markingTimeFrames'] / 60) + frnd(i['executionTimeMaxFrames'] / 60)
                



            case 'LeapingSwordModel':
                trim_projectile.parse_prj(tower, data, i['impactProjectileModel'], i['singleEmissionModel'], owner_name=get_obj_name(m_abil))
                trim_projectile.parse_prj(tower, data, i['dotProjectileModel'], i['dotProjectileModel'], owner_name=get_obj_name(m_abil))
            
            case 'SwordChargeModel':
                trim_projectile.parse_prj(tower, data, i['projectileModel'], i['singleEmissionModel'], owner_name=get_obj_name(m_abil))

            case 'MoabBarrageModel':
                data['effects']['Effect'] = {
                    "damage": i["damageOverTimeModel"]["damage"],
                    "interval" : i["damageOverTimeModel"]["interval"]
                }

            case 'MorphTowerModel':
                trim_tower.parse_tow(tower, i['secondaryTowerModel'])

            case 'AbilityCreateTowerModel':
                trim_tower.parse_tow(tower, i['towerModel'])

    #     
    # BUFFS
    #
    parse_buffs(data['buffs'], m_abil['behaviors'])

    ret = {get_obj_name(m_abil): data}

    add_sub(tower["abilities"], ret, owner_name=tower_name)