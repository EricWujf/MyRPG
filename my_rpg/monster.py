import yaml

class Monster:
    def __init__(self, name, level, base_exp, monster_type = "Normal", monster_ATK = 0, monster_DEF = 0, monster_CrisDMG = 0.0, monster_CrisRate = 0.0):
        self.name = name
        self.level = level
        self.base_exp = base_exp
        self.monster_type = monster_type
        self.monster_atk = monster_ATK
        self.monster_def = monster_DEF
        self.monster_crisrate = monster_CrisRate
        self.monster_crisdmg = monster_CrisDMG

    def __str__(self):
        tag_map = {
            'Normal': '怪物',
            'Elite': '菁英',
            'Boss': 'Boss',
            'SummonBoss': '召喚Boss',
            'Adv': '強化',
            'Event': '活動',
            'EventBoss': '事件Boss'
        }
        if self.monster_type in tag_map:
            tag = tag_map.get(self.monster_type)
            return f"[Lv.{self.level} {tag}] {self.name}"
        else:
            return f"[Lv.{self.level}] {self.name}"
        
    def drop_exp(self):
        multiplierlist = {
            'Adv': 1.25,
            'Elite': 1.5,
            'Boss': 2.0,
            'SummonBoss': 2.2,
            'EventBoss': 2.5
        }
        multiplier = multiplierlist.get(self.monster_type,1.0)
        DropExp = self.base_exp*(self.level//2)*multiplier
        return DropExp
        
    @classmethod
    def load_monsters_from_yaml(cls, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            monsters = []
            for m in data:
                monsters.append(cls(
                    name=m['name'],
                    level=m['level'],
                    base_exp=m['base_exp'],
                    monster_type=m.get('monster_type', 'Normal')
                ))
            return monsters