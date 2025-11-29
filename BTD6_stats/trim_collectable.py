from trim_common import *
from trim_attack import *
from trim_projectile import *
from trim_ability import *

def parse_coll(parent, name, behavs):
    data = {}

    for i in behavs:
        mname = get_model_name(i)

        match mname:
            case 'PickupModel':
                data['collectRadius'] = frnd(i['collectRadius'])
                data['delay'] = frnd(i['delay'])
            
            case 'CashModel':
                data['cashMinimum'] = frnd(i['minimum'])
                data['cashMaximum'] = frnd(i['maximum'])
                data['bonusMultiplier'] = frnd(i['bonusMultiplier'])
                data['salvage'] = frnd(i['salvage'])
                data['noTransformCash'] = i['noTransformCash']
                data['distributeSalvage'] = i['distributeSalvage']
                data['forceCreateProjectile'] = i['forceCreateProjectile']
                data['isDoubleable'] = i['isDoubleable']
                data['distributeBonusIncome'] = i['distributeBonusIncome']
                data['emittedByCashEarnedMultiplier'] = frnd(i['emittedByCashEarnedMultiplier'])

            case 'LivesModel':
                data["livesMinimum"] = frnd(i["minimum"])
                data["livesMaximum"] = frnd(i["maximum"])
                data['salvage'] = frnd(i['salvage'])

            case 'AgeModel':
                data['rounds'] = frnd(i['rounds'])
                data['lifespan'] = frnd(i['lifespan'])

    ret = {name: data}

    add_sub(parent["collectables"], ret)
