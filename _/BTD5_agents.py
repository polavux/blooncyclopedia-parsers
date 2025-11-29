import xml.etree.ElementTree as ET
import os
import json

en = ET.parse('English.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ar = ET.parse('Arabic_pres.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
da = ET.parse('Danish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
de = ET.parse('German.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
es = ET.parse('Spanish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fi = ET.parse('Finnish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
fr = ET.parse('French.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
it = ET.parse('Italian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ja = ET.parse('Japanese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ko = ET.parse('Korean.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
no = ET.parse('Norwegian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ptbr = ET.parse('BrazilianPortuguese.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
ru = ET.parse('Russian.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
sv = ET.parse('Swedish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()
tr = ET.parse('Turkish.xml',parser=ET.XMLParser(encoding="utf-8")).getroot()


fdescs={
	"PortableLake": "Nowhere to float your boat? Smart monkeys know they can place a Portable Lake on land, allowing any water unit to be deployed within its waters.",
	"Pontoon": "Place almost any land tower on water with the Pontoon! Deploy the Pontoon on water, then place your land tower on top.",
	"TribalTurtle": "Tribal Turtle can live on land or water. Throws spears and coconuts, coconuts do extra damage to ceramic bloons and can pop frozen and lead bloons.",
	"BloonsdayDevice": "The apex of monkey tech, the otherworldly Bloonsday Device gives you temporary control of their orbital strike satellite, whose beam destroys all bloons and does big damage to MOAB-class bloons.",
	"MeerkatSpy": "Meerkat Spy has no attack, but instead uses his super keen senses to spot Camo Bloons, granting Camo Detection for all towers within his radius.",
	"BloonberryBush": "Plant this fast-growing bloon killer right on the track. Loses a thorn for each bloon popped, but grows 5 thorns between each round (up to 200). You protect it, it\'ll protect you.",
	"BeeKeeper": "This special agent has a hive of angry bees that zip to their targets and sting bloons until all layers are popped. Stingers can\'t get through lead or ice but regrower bloons beware.",
	"AngrySquirrel": "Armed with sharp acorns, this special agent goes berserk when bloons leak. For a few seconds, he attacks super fast, can spot camo, and pop lead.",
	"SuperMonkeyStorm": "It\'s a bird. It\'s a plane. It\'s a squadron of flying super-powered laser-beamin\' monkeys who destroy every single bloon on screen and do big damage to MOAB-class bloons."
}

""" var _loc1_:ConsumableDef = new ConsumableDef(CONS_PORTABLE_LAKE).Label("Portable Lake").Description("").Thumb(pool_tn).Tower(new TowerDef(CONS_PORTABLE_LAKE).Label("Portable Lake").Description("Nowhere to float your boat? Smart monkeys know they can place a Portable Lake on land, allowing any water unit to be deployed within its waters.").Display(PaddlingPool).DetailSmall(Pool).OccupiedSpace(PortableLakeSpace).RangeOfVisibility(64).ChangesTerrain(TowerDef.CHANGE_TERRAIN_TO_WATER).IsPlatform(true).Rotates(false).CanPriorityTarget(false));
this.allConsumables.push(_loc1_);
var _loc2_:ConsumableDef = new ConsumableDef(CONS_PORTABLE_LAKE_PRO).Label("Portable Lake Pro").Description("Pro Upgrade - Sea Monster! New Activated Ability temporarily awakens the Sea Monster, which bashes nearby bloons, popping 5 layers and sometimes stunning them. Any water unit can be placed in the Lake.").Thumb(propool_tn).Tower(new TowerDef(CONS_PORTABLE_LAKE_PRO).Label("Portable Lake Pro").Description("Pro Upgrade - Sea Monster! New Activated Ability temporarily awakens the Sea Monster, which bashes nearby bloons, popping 5 layers and sometimes stunning them. Any water unit can be placed in the Lake.").Display(OctopusPool).DetailSmall(assets.PlayUI.ProPool).OccupiedSpace(PortableLakeSpace).RangeOfVisibility(180).ChangesTerrain(TowerDef.CHANGE_TERRAIN_TO_WATER).IsPlatform(true).Rotates(false).DisplayAddons(Vector.<DisplayAddonDef>([new DisplayAddonDef().Clip(OctopusPoolTentacle).Z(1).Ref("tenticle").Loop(false)])).Weapons(Vector.<Weapon>([new PoolProWeapon().Range(180).Power(720).ReloadTime(1.714).ProjectileD(new ProjectileDef().Pierce(20).Radius(30).DamageEffect(new DamageEffectDef().Damage(5).CanBreakIce(true)).StunEffect(new StunEffectDef().Lifespan(1).CantEffect(Vector.<int>([Bloon.MOAB,Bloon.BFB,Bloon.BOSS])).StunsOnEveryNthBloonHit(3)))])).Behavior(new towers.behavior.BehaviorDef().Initialise(new PoolProInit())).Abilities(Vector.<AbilityDef>([new RagingSeaMonsterDef("RagingSeaMonster").Cooldown(45).Sound(PoolAbility).Thumb(ActivatedAbilityOctopusPool).Label("Activate Sea Monster!").Description("Out of the Lake comes a legendary Sea Monster that furiously attacks bloons for a short duration.").AbilityClass(RagingSeaMonster)])));
this.allConsumables.push(_loc2_);
_loc1_.Pro(new ProDef().Def(_loc2_).UnlockUseThreashold(50).DetailImage(assets.detailView.ProPool));
var _loc3_:ConsumableDef = new ConsumableDef(CONS_PONTOON).Label("Pontoon").Description("").Thumb(pontoon_tn).Tower(new TowerDef(CONS_PONTOON).Label("Pontoon").Description("Place almost any land tower on water with the Pontoon! Deploy the Pontoon on water, then place your land tower on top.").Display(assets.towers.Pontoon).DetailSmall(assets.PlayUI.Pontoon).OccupiedSpace(PontoonSpace).IsBoat(true).IsLand(false).RangeOfVisibility(58).ChangesTerrain(TowerDef.CHANGE_TERRAIN_TO_LAND).IsPlatform(true).Rotates(false).CanPriorityTarget(false));
this.allConsumables.push(_loc3_);
var _loc4_:ConsumableDef = new ConsumableDef(CONS_PONTOON_PRO).Label("Pontoon Pro").Description("Pro Upgrade - Primo Pontoon! In addition to luxury fittings, the Primo Pontoon has an uplink to Monkey Town HQ, granting any attached tower a range bonus. Place on water then place your land tower on top.").Thumb(propontoon_tn).Tower(new TowerDef(CONS_PONTOON_PRO).Label("Pontoon Pro").Description("Pro Upgrade - Primo Pontoon! In addition to luxury fittings, the Primo Pontoon has an uplink to Monkey Town HQ, granting any attached tower a range bonus. Place on water then place your land tower on top.").Display(PontoonPro).DetailSmall(assets.PlayUI.ProPontoon).OccupiedSpace(PontoonSpace).IsBoat(true).IsLand(false).RangeOfVisibility(58).ChangesTerrain(TowerDef.CHANGE_TERRAIN_TO_LAND).IsPlatform(true).Rotates(false).CanPriorityTarget(false).PlatformEffects(Vector.<AreaEffectDef>([new AreaEffectDef().Upgrade(new UpgradeDef().Id("PontoonProRangeUpgrade").Add(new AddDef().RangeOfVisibility(1.15).RangeOfVisibilityAsScale(true).WeaponMod(new WeaponModDef().Range(1.1).RangeAsScale(true))))])));
this.allConsumables.push(_loc4_);
_loc3_.Pro(new ProDef().Def(_loc4_).UnlockUseThreashold(50).DetailImage(assets.detailView.ProPontoon));
var _loc5_:ConsumableDef = new ConsumableDef(CONS_TURTLE).Label("Tribal Turtle").Description("").Thumb(tribal_tn).Tower(new TowerDef(CONS_TURTLE).Label("Tribal Turtle").Description("Tribal Turtle can live on land or water. Throws spears and coconuts, coconuts do extra damage to ceramic bloons and can pop frozen and lead bloons.").Display(assets.towers.TribalTurtle).DetailSmall(assets.PlayUI.TribalTurtle).OccupiedSpace(Medium).IsBoat(true).IsLand(true).RangeOfVisibility(120).Behavior(new towers.behavior.BehaviorDef().Process(new ProcessTurtle())).DisplayAddons(Vector.<DisplayAddonDef>([new DisplayAddonDef().Clip(TribalSpearArm).Z(-1).Ref("arm_right").Loop(false),new DisplayAddonDef().Clip(TribalCoconutArm).Z(-1).Ref("arm_left").Loop(false)])).Weapons(Vector.<Weapon>([new SequenceTurtle().ReloadTime(0.657).WeaponOffsets(Vector.<Vector2>([new Vector2(13,15),new Vector2(6,-15)])).ChildWeapons(Vector.<Weapon>([new Single().ReloadTime(0.657).Projectile(new ProjectileDef().Display(TribalSpear).Pierce(2).Radius(4).DamageEffect(new DamageEffectDef().Damage(1).CantBreak(Vector.<int>([Bloon.LEAD])).CanBreakIce(false))).Power(700).Range(600),new Single().ReloadTime(0.657).Projectile(new ProjectileDef().Display(TribalCoconut).Pierce(5).Radius(4).DamageEffect(new DamageEffectDef().Damage(1).CanBreakIce(true).CeramicScale(3))).Power(700).Range(600)]))])));
this.allConsumables.push(_loc5_);
var _loc6_:ConsumableDef = new ConsumableDef(CONS_TURTLE_PRO).Label("Tribal Turtle Pro").Description("Pro Upgrade - Ambidexterity! Elite level training allows the Turtle Pro to throw spear and coconut simultaneously for maximum bloon hurt. Coconuts do extra damage to ceramic bloons and can pop frozen and lead bloons.").Thumb(protribal_tn).Tower(new TowerDef(CONS_TURTLE_PRO).Label("Tribal Turtle Pro").Description("Pro Upgrade - Ambidexterity! Elite level training allows the Turtle Pro to throw spear and coconut simultaneously for maximum bloon hurt. Coconuts do extra damage to ceramic bloons and can pop frozen and lead bloons.").Display(TribalTurtleAmbi).DetailSmall(assets.PlayUI.ProTribalTurtle).OccupiedSpace(Medium).IsBoat(true).IsLand(true).RangeOfVisibility(120).Behavior(new towers.behavior.BehaviorDef().Process(new ProcessTurtle())).DisplayAddons(Vector.<DisplayAddonDef>([new DisplayAddonDef().Clip(TribalSpearArm).Z(-1).Ref("arm_right").Loop(false),new DisplayAddonDef().Clip(TribalCoconutArm).Z(-1).Ref("arm_left").Loop(false)])).Weapons(Vector.<Weapon>([new SequenceTurtle().ReloadTime(0.657).Both(true).WeaponOffsets(Vector.<Vector2>([new Vector2(13,15),new Vector2(6,-15)])).ChildWeapons(Vector.<Weapon>([new Single().ReloadTime(0.657).Projectile(new ProjectileDef().Display(TribalSpear).Pierce(2).Radius(4).DamageEffect(new DamageEffectDef().Damage(1).CantBreak(Vector.<int>([Bloon.LEAD])).CanBreakIce(false))).Power(700).Range(600),new Single().ReloadTime(0.657).Projectile(new ProjectileDef().Display(TribalCoconut).Pierce(5).Radius(4).DamageEffect(new DamageEffectDef().Damage(1).CanBreakIce(true).CeramicScale(3))).Power(700).Range(600)]))])));
this.allConsumables.push(_loc6_);
_loc5_.Pro(new ProDef().Def(_loc6_).UnlockUseThreashold(50).DetailImage(assets.detailView.ProTribalTurtle));
var _loc7_:ConsumableDef = new ConsumableDef(CONS_BLOONSDAY).Label("Bloonsday Device").Description("").Thumb(doomsday_tn).Tower(new TowerDef(CONS_BLOONSDAY).Label("Bloonsday Device").Description("The apex of monkey tech, the otherworldly Bloonsday Device gives you temporary control of their orbital strike satellite, whose beam destroys all bloons and does big damage to MOAB-class bloons.").Display(BloonsDayDevice).DetailSmall(DoomsDay).OccupiedSpace(BloonsdaySpace).RangeOfVisibility(50).CanPriorityTarget(false).Rotates(false).Abilities(Vector.<AbilityDef>([new BloonsdayRayDef("BloonsdayRay").Cooldown(80).Sound(BloonsdayFire).Thumb(ActivatedAbilityBloonsdayDevice).Label("Orbital Strike").Description("Creates a beam that destroys all bloons and does big damage to MOAB-class bloons.").AbilityClass(BloonsdayRay)])));
this.allConsumables.push(_loc7_);
var _loc8_:ConsumableDef = new ConsumableDef(CONS_BLOONSDAY_PRO).Label("Bloonsday Device Pro").Description("Pro Upgrade - Plasmatic Fusion! Focal doubling at the point of impact leaves a trail of plasma along the strike path, so hot it will continue to damage all bloons and MOAB-classes until spent or dissipated.").Thumb(prodoomsday_tn).Tower(new TowerDef(CONS_BLOONSDAY_PRO).Label("Bloonsday Device Pro").Description("Pro Upgrade - Plasmatic Fusion! Focal doubling at the point of impact leaves a trail of plasma along the strike path, so hot it will continue to damage all bloons and MOAB-classes until spent or dissipated.").Display(BloonsDayDevicePro).DetailSmall(assets.PlayUI.ProDoomsDay).OccupiedSpace(BloonsdaySpace).RangeOfVisibility(50).CanPriorityTarget(false).Rotates(false).Abilities(Vector.<AbilityDef>([new BloonsdayRayDef("BloonsdayRayPro").Cooldown(80).Sound(BloonsdayFire).Thumb(ActivatedAbilityBloonsdayDevice).Label("Orbital Strike").Description("Creates a beam that destroys all bloons and does big damage to MOAB-class bloons.").HasTrail(true).AbilityClass(BloonsdayRay)])));
this.allConsumables.push(_loc8_);
_loc7_.Pro(new ProDef().Def(_loc8_).UnlockUseThreashold(20).DetailImage(assets.detailView.ProDoomsDay));
var _loc9_:ConsumableDef = new ConsumableDef(CONS_MEERKAT).Label("Meerkat Spy").Description("Meerkat Spy has no attack, but instead uses his super keen senses to spot Camo Bloons, granting Camo Detection for all towers within his radius.").Thumb(meerkat_tn).Tower(new TowerDef(CONS_MEERKAT).Label("Meerkat Spy").Description("Meerkat Spy has no attack, but instead uses his super keen senses to spot Camo Bloons, granting Camo Detection for all towers within his radius.").Display(MeerkatHead).DetailSmall(assets.PlayUI.Meerkat).OccupiedSpace(Small).RangeOfVisibility(80).CanPriorityTarget(false).DisplayAddons(Vector.<DisplayAddonDef>([new DisplayAddonDef().Clip(MeerkatMound).Z(-2).Rotate(false),new DisplayAddonDef().Clip(assets.towers.Meerkat).Z(-1).Rotate(true)])).AreaEffects(Vector.<AreaEffectDef>([new AreaEffectDef().Upgrade(new UpgradeDef().Id("Test6").Add(new AddDef().RemoveFromTargetMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION])).WeaponMod(new WeaponModDef().ProjectileMod(new ProjectileModDef().RemoveFromEffectMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION]))))))])).Behavior(new towers.behavior.BehaviorDef().Process(new FaceCamo()).Destroy(new FaceCamoDestroy())));
this.allConsumables.push(_loc9_);
var _loc10_:ConsumableDef = new ConsumableDef(CONS_MEERKAT_PRO).Label("Meerkat Spy Pro").Description("Pro Upgrade - Cyber Eye! No longer weaponless, the Meerkat Pro can now blast any single bloon into dust and help put the hurt on MOAB-class bloons. Grants camo detection to all towers in his radius.").Thumb(promeerkat_tn).Tower(new TowerDef(CONS_MEERKAT_PRO).Label("Meerkat Spy Pro").Description("Pro Upgrade - Cyber Eye! No longer weaponless, the Meerkat Pro can now blast any single bloon into dust and help put the hurt on MOAB-class bloons. Grants camo detection to all towers in his radius.").Display(MeerkatHeadPro).DetailSmall(assets.PlayUI.ProMeerkat).OccupiedSpace(Small).RangeOfVisibility(81).TargetMask(Vector.<int>([Bloon.IMMUNITY_NONE])).Weapons(Vector.<Weapon>([new MeerkatSingle().Range(161).Power(1000).ReloadTime(0.94).Rotate(true).Projectile(new ProjectileDef().Display(DoomPatchBeam).Pierce(1).EffectMask(Vector.<int>([Bloon.IMMUNITY_NONE])).DamageEffect(new DamageEffectDef().Damage(6)))])).WeaponOffsets(Vector.<Vector2>([new Vector2(0,-12)])).DisplayAddons(Vector.<DisplayAddonDef>([new DisplayAddonDef().Clip(MeerkatMound).Z(-2).Rotate(false),new DisplayAddonDef().Clip(assets.towers.Meerkat).Z(-1).Rotate(true)])).AreaEffects(Vector.<AreaEffectDef>([new AreaEffectDef().Upgrade(new UpgradeDef().Id("Test6").Add(new AddDef().RemoveFromTargetMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION])).WeaponMod(new WeaponModDef().ProjectileMod(new ProjectileModDef().RemoveFromEffectMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION]))))))])).Behavior(new towers.behavior.BehaviorDef().Process(new FaceCamo().IsPro(true)).Destroy(new FaceCamoDestroy())));
this.allConsumables.push(_loc10_);
_loc9_.Pro(new ProDef().Def(_loc10_).UnlockUseThreashold(50).DetailImage(assets.detailView.ProMeerkat));
var _loc11_:ConsumableDef = new ConsumableDef(CONS_BLOONSBERRY).Label("Bloonberry Bush").Description("Plant this fast-growing bloon killer right on the track. Loses a thorn for each bloon popped, but grows 5 thorns between each round (up to 200). You protect it, it\'ll protect you.").Thumb(bush_tn).Tower(new TowerDef(CONS_BLOONSBERRY).Label("Bloonberry Bush").Description("Plant this fast-growing bloon killer right on the track. Loses a thorn for each bloon popped, but grows 5 thorns between each round (up to 200). You protect it, it\'ll protect you.").Display(BloonsBush).DetailSmall(Bush).OccupiedSpace(Small).RangeOfVisibility(20).CanPlaceOnTrack(true).CanPriorityTarget(false).Rotates(false).Behavior(new towers.behavior.BehaviorDef().Initialise(new BloonberryInit().ProjectileDefine(new ProjectileDef().Pierce(200).Radius(20).EffectMask(Vector.<int>([Bloon.IMMUNITY_NONE])).Behavior(new projectiles.behavior.BehaviorDef().Collision(new BloonberryCollision())).CanMultiEffect(true).DamageEffect(new DamageEffectDef().Damage(1).CanBreakIce(false).CantBreak(Vector.<int>([Bloon.LEAD]))))).RoundOver(new BloonberryGrow())));
this.allConsumables.push(_loc11_);
var _loc12_:ConsumableDef = new ConsumableDef(CONS_BLOONSBERRY_PRO).Label("Bloonberry Bush Pro").Description("Pro Upgrade - Creepers! Creepers appear every 3 rounds and can grow up to 15 thorns each. Protect them as Creepers are destroyed if stripped of thorns. Main bush still grows 5 thorns per round up to 200.").Thumb(probush_tn).Tower(new TowerDef(CONS_BLOONSBERRY_PRO).Label("Bloonberry Bush Pro").Description("Pro Upgrade - Creepers! Creepers appear every 3 rounds and can grow up to 15 thorns each. Protect them as Creepers are destroyed if stripped of thorns. Main bush still grows 5 thorns per round up to 200.").Display(BloonsBushPro).DetailSmall(assets.PlayUI.ProBush).OccupiedSpace(Small).RangeOfVisibility(20).CanPlaceOnTrack(true).CanPriorityTarget(false).Rotates(false).Behavior(new towers.behavior.BehaviorDef().Initialise(new BloonberryInit().ProjectileDefine(new ProjectileDef().Pierce(200).Radius(20).EffectMask(Vector.<int>([Bloon.IMMUNITY_NONE])).Behavior(new projectiles.behavior.BehaviorDef().Collision(new BloonberryCollision())).CanMultiEffect(true).DamageEffect(new DamageEffectDef().Damage(1).CanBreakIce(false).CantBreak(Vector.<int>([Bloon.LEAD]))))).RoundOver(new BloonberryGrowPro().CreeperDef(new ProjectileDef().Pierce(15).Radius(20).Display(BloonsBushCreeper).EffectMask(Vector.<int>([Bloon.IMMUNITY_NONE])).Behavior(new projectiles.behavior.BehaviorDef().Collision(new CreeperCollision())).CanMultiEffect(true).DamageEffect(new DamageEffectDef().Damage(1).CanBreakIce(false).CantBreak(Vector.<int>([Bloon.LEAD])))))));
this.allConsumables.push(_loc12_);
_loc11_.Pro(new ProDef().Def(_loc12_).UnlockUseThreashold(50).DetailImage(assets.detailView.ProBush));
var _loc13_:ConsumableDef = new ConsumableDef(CONS_BEEKEEPER).Label("Beekeeper").Description("This special agent has a hive of angry bees that zip to their targets and sting bloons until all layers are popped. Stingers can\'t get through lead or ice but regrower bloons beware.").Thumb(bear_tn).Tower(new TowerDef(CONS_BEEKEEPER).Label("Beekeeper").Description("This special agent has a hive of angry bees that zip to their targets and sting bloons until all layers are popped. Stingers can\'t get through lead or ice but regrower bloons beware.").Display(Beekeeper).DetailSmall(Bear).OccupiedSpace(Small).RangeOfVisibility(150).Weapons(Vector.<Weapon>([new LaunchBee().ReloadTime(0.57)])));
this.allConsumables.push(_loc13_);
var _loc14_:ConsumableDef = new ConsumableDef(CONS_BEEKEEPER_PRO).Label("Beekeeper Pro").Description("Pro Upgrade - Swarm! The Swarm Activated Ability launches 100 bees that will seek targets and pop them mercilessly for a short duration. Can\'t pop lead or ice but regrower bloons beware!").Thumb(probear_tn).Tower(new TowerDef(CONS_BEEKEEPER_PRO).Label("Beekeeper Pro").Description("Pro Upgrade - Swarm! The Swarm Activated Ability launches 100 bees that will seek targets and pop them mercilessly for a short duration. Can\'t pop lead or ice but regrower bloons beware!").Display(BeekeeperSwarm).DetailSmall(assets.PlayUI.ProBear).OccupiedSpace(Small).RangeOfVisibility(150).Weapons(Vector.<Weapon>([new LaunchBee().ReloadTime(0.57)])).Abilities(Vector.<AbilityDef>([new BeekeeperProDef("BeekeeperPro").Cooldown(45).Sound(Swarm).Thumb(ActivatedAbilityBeekeeper).Label("Swarm!").Description("Will create a swarm of 100 bees that will seek targets and pop them mercilessly for a short duration.").AbilityClass(BeeSwarm)])));
this.allConsumables.push(_loc14_);
_loc13_.Pro(new ProDef().Def(_loc14_).UnlockUseThreashold(40).DetailImage(assets.detailView.ProBear));
         var _loc15_:ConsumableDef = new ConsumableDef(CONS_SQUIRREL).Label("Angry Squirrel").Description("Armed with sharp acorns, this special agent goes berserk when bloons leak. For a few seconds, he attacks super fast, can spot camo, and pop lead.").Thumb(squirrel_tn).Tower(new TowerDef(CONS_SQUIRREL).Label("Angry Squirrel").Description("Armed with sharp acorns, this special agent goes berserk when bloons leak. For a few seconds, he attacks super fast, can spot camo, and pop lead.").Display(AngrySquirrel).DetailSmall(Squirrel).OccupiedSpace(Small).RangeOfVisibility(90).Weapons(Vector.<Weapon>([new Single().ReloadTime(0.714).Projectile(new ProjectileDef().Display(Acorn).Pierce(1).DamageEffect(new DamageEffectDef().Damage(1).CantBreak(Vector.<int>([Bloon.LEAD])).CanBreakIce(false))).Power(595).Range(170)])).WeaponOffsets(Vector.<Vector2>([new Vector2(6,10)])).Behavior(new towers.behavior.BehaviorDef().Initialise(new Anger().Upgrade(new UpgradeDef().Add(new AddDef().Display(Vector.<TowerDisplayMod>([new TowerDisplayMod().UseFor(AngrySquirrel).Display(HulkSquirrel)])).RangeOfVisibility(60).RemoveFromTargetMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION])).WeaponMod(new WeaponModDef().ReloadTime(-0.57).ProjectileMod(new ProjectileModDef().Pierce(1).RemoveFromEffectMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION])).DamageEffectMod(new DamageEffectModDef().CanBreakIce(true).RemoveFromCantBreak(Vector.<int>([Bloon.LEAD])))))))).Destroy(new RemoveAnger()).Process(new RotateToTarget())));
         this.allConsumables.push(_loc15_);
         var _loc16_:ConsumableDef = new ConsumableDef(CONS_SQUIRREL_PRO).Label("Angry Squirrel Pro").Description("Pro Upgrade - Anger Mismanagement! Despite counselling the squirrel agent is even angrier. He gets so worked up that every 50 acorns he goes berserk even if bloons haven\'t leaked, attacking super fast, spotting camo, and popping lead.").Thumb(prosquirrel_tn).Tower(new TowerDef(CONS_SQUIRREL_PRO).Label("Angry Squirrel Pro").Description("Pro Upgrade - Anger Mismanagement! Despite counselling the squirrel agent is even angrier. He gets so worked up that every 50 acorns he goes berserk even if bloons haven\'t leaked, attacking super fast, spotting camo, and popping lead.").Display(AngrySquirrel).DetailSmall(assets.PlayUI.ProSquirrel).OccupiedSpace(Small).RangeOfVisibility(90).Weapons(Vector.<Weapon>([new Single().ReloadTime(0.714).Projectile(new ProjectileDef().Display(Acorn).Pierce(1).DamageEffect(new DamageEffectDef().Damage(1).CantBreak(Vector.<int>([Bloon.LEAD])).CanBreakIce(false))).Power(595).Range(170)])).WeaponOffsets(Vector.<Vector2>([new Vector2(6,10)])).Behavior(new towers.behavior.BehaviorDef().Initialise(new AngerPro().Upgrade(new UpgradeDef().Add(new AddDef().Display(Vector.<TowerDisplayMod>([new TowerDisplayMod().UseFor(AngrySquirrel).Display(WildSquirrel)])).RangeOfVisibility(60).RemoveFromTargetMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION])).WeaponMod(new WeaponModDef().ReloadTime(-0.57).ProjectileMod(new ProjectileModDef().Pierce(1).RemoveFromEffectMask(Vector.<int>([Bloon.IMMUNITY_NO_DETECTION])).DamageEffectMod(new DamageEffectModDef().CanBreakIce(true).RemoveFromCantBreak(Vector.<int>([Bloon.LEAD])))))))).Destroy(new RemoveAnger()).Process(new RotateToTarget())));
         this.allConsumables.push(_loc16_);
         _loc15_.Pro(new ProDef().Def(_loc16_).UnlockUseThreashold(50).DetailImage(assets.detailView.ProSquirrel));
         var _loc17_:ConsumableDef = new ConsumableDef(CONS_MONKEY_STORM).Label("Super Monkey Storm").Description("It\'s a bird. It\'s a plane. It\'s a squadron of flying super-powered laser-beamin\' monkeys who destroy every single bloon on screen and do big damage to MOAB-class bloons.").Thumb(storm_tn).Instant(new MonkeyStorm());
         this.allConsumables.push(_loc17_);
         var _loc18_:ConsumableDef = new ConsumableDef(CONS_MONKEY_STORM_PRO).Label("Super Monkey Storm Pro").Description("Pro Upgrade - Double Storm! A second pass of Super Monkeys follows the first after a short delay, destroying every bloon on screen and damaging MOAB-classes.").Thumb(prostorm_tn).Instant(new MonkeyStormPro());
         this.allConsumables.push(_loc18_);"""

a = open("pywiki_BTD5_agents.txt", "w", encoding="utf-8")


bd = [
		{ "Type" : "MeerkatSpy", "Icon" : "meerkat_icon" },
		{ "Type" : "MeerkatSpyPro", "Icon" : "meerkat_pro_icon" },
		{ "Type" : "PortableLake", "Icon" : "portable_icon" },
		{ "Type" : "PortableLakePro", "Icon" : "portable_lake_pro_icon" },
		{ "Type" : "Pontoon", "Icon" : "pontoon_icon" },
		{ "Type" : "PontoonPro", "Icon" : "pontoon_pro_icon" },
		{ "Type" : "BloonsdayDevice", "Icon" : "bloonsday_icon" },
		{ "Type" : "BloonsdayDevicePro", "Icon" : "bloonsday_pro_icon" },
		{ "Type" : "SuperMonkeyStorm", "Icon" : "supermonkey_storm_icon", "AutoPlace": True },
		{ "Type" : "SuperMonkeyStormPro", "Icon" : "supermonkey_storm_pro_icon", "AutoPlace": True },
        { "Type" : "TribalTurtle", "Icon" : "turtle_icon" },
        { "Type" : "TribalTurtlePro", "Icon" : "turtle_pro_icon" },
        { "Type" : "AngrySquirrel", "Icon" : "squirrel_icon" },
        { "Type" : "AngrySquirrelPro", "Icon" : "squirrel_pro_icon" },
        { "Type" : "BeeKeeper", "Icon" : "beekeeper_icon" },
        { "Type" : "BeeKeeperPro", "Icon" : "beekeeper_pro_icon" },
        { "Type" : "BloonberryBush", "Icon" : "bloonberry_icon" },
        { "Type" : "BloonberryBushPro", "Icon" : "bloonberry_pro_icon" },
        { "Type" : "Radadactyl", "Icon" : "radadactyl_icon" },
        { "Type" : "RadadactylPro", "Icon" : "radadactyl_pro_icon" },
        { "Type" : "BananaFarmer", "Icon" : "farmer_icon" },
        { "Type" : "BananaFarmerPro", "Icon" : "farmer_pro_icon" },
        { "Type" : "NinjaKiwi", "Icon" : "ninja_kiwi_icon" },
        { "Type" : "NinjaKiwiPro", "Icon" : "ninja_kiwi_pro_icon" }
]



jeh = 0
des = 0
def g(lang):
    v = lang[0][jeh].text

    return v.replace("\\n"," ")
def d(lang):
    v = lang[0][des].text

    return v.replace("\\n"," ")

for i in bd:
	if "Pro" in i["Type"] or i["Type"] in ["Radadactyl", "BananaFarmer", "NinjaKiwi"]: continue
	for k in range(len(en[0])):
		t = i["Type"]
		if en[0][k].attrib["id"] == f"LOC_{t}_TOWER":
			jeh = k
		if en[0][k].attrib["id"] == f"LOC_TOWER_DESC_{t}":
			des = k

	port = ""
	cost = 0
	rank = 0

	for k in os.listdir("TowerDefinitions"):
		t = i["Type"]
		if k == f"{t}.tower":
			m = open(f"TowerDefinitions/{k}","r", encoding="utf-8")
			md = json.load(m)
			port = md["Icon"]
			cost = md["BaseCost"]
			rank = md["RankToUnlock"]
			m.close()
			break

	a.write(f'''{{{{-start-}}}}
\'\'\'{g(en)}\'\'\'
{{{{bot generated}}}}
{{{{BTD5 special agent info
|id F={i["Type"]}
|id D={i["Type"]}
|id M={i["Type"]}
|id C={i["Type"]}

|name F       ={g(en)}
|name M       ={g(en)}
|image F      =BTD5F {i["Type"]}.png
|image M      =BTD5M {port}.png
|icon F       =BTD5F icon {i["Type"]}.png
|icon M       =BTD5M {i["Icon"]}.png
|description F={fdescs[i["Type"]]}
|description M={d(en)}

|cost={cost}
}}}}
The \'\'\'{g(en)}\'\'\' is a [[Special Agent]] in ''[[Bloons TD 5]]''.
{{{{TOC}}}}
{{{{clear|right}}}}
==Gallery==
===Screenshots===
{{{{screenshot needed}}}}

===Assets===
<gallery>
BTD5M {port}.png
BTD5M {i["Icon"]}.png
BTD5F {i["Type"]}.png
BTD5F icon {i["Type"]}.png
</gallery>

==In other languages==
{{{{langlist
|label=Name
|key=LOC_{i["Type"]}_TOWER
|ar   ={g(ar)}
|da   ={g(da)}
|de   ={g(de)}
|es   ={g(es)}
|fi   ={g(fi)}
|fr   ={g(fr)}
|it   ={g(it)}
|ja   ={g(ja)}
|ko   ={g(ko)}
|no   ={g(no)}
|pt-br={g(ptbr)}
|ru   ={g(ru)}
|sv   ={g(sv)}
|tr   ={g(tr)}
}}}}
{{{{langlist
|label=Description
|key=LOC_LOC_TOWER_DESC_{i["Type"]}
|ar   ={d(ar)}
|da   ={d(da)}
|de   ={d(de)}
|es   ={d(es)}
|fi   ={d(fi)}
|fr   ={d(fr)}
|it   ={d(it)}
|ja   ={d(ja)}
|ko   ={d(ko)}
|no   ={d(no)}
|pt-br={d(ptbr)}
|ru   ={d(ru)}
|sv   ={d(sv)}
|tr   ={d(tr)}
}}}}

==Navigation==
{{{{BTD5 special agent nav}}}}
{{{{-stop-}}}}
''')





a.close()