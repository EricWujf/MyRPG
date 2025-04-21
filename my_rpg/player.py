class Player:
    def __init__(self, name: str, uid: int):
        self.name = name
        self.uid = uid
        self.level = 1 #等級
        self.exp = 0 #經驗值
        self.hp = 100 #當前血量
        self.max_hp = 100 #最大血量
        self.mp = 20 #當前魔力
        self.max_mp = 20 #最大魔力
        self.dmg = 10 #物理攻擊
        self.mdmg = 20 #魔法攻擊
        self.defense = 5 #防禦
        self.speed = 1.0 #移動速度 (%)
        self.hit_rate = 0.2 #命中率 (%)
        self.dodge_rate = 0.05 #迴避率 (%)
        self.crit_rate = 0.05 #爆擊率 (%)
        self.crit_damage = 0.2 #爆擊傷害 (%)
        self.life_steal = 0.0 #血量吸取量 (%)
        self.mana_steal = 0.0 #魔力吸取量 (%)
        self.hp_regen = 0.2 #血量恢復速度 (%)
        self.mp_regen = 0.1 #魔力恢復速度 (%)