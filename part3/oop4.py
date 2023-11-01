class Hero:
    def __init__(self, name, health, damage,defence):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
    def get_status(self):
        print(f'Имя: {self.name}')
        print(f'Здоровье: {self.health}')
        print(f'Урон: {self.damage}')
        print(f'Защита: {self.defence}')
        print('_'*15)
    def increase_defense(self):
        if self.defence*1.5<100:
            self.defence*=1.5
        else:
            print('Максимальная защита')
        print(f'Защита: {self.defence}')
        print('_'*15)
    def make_damage(self,enemy):
        print(f"Атака по персонажу {enemy.name}")
        print('_'*15)
        enemy.get_damage(self.damage)
    def get_damage(self,damage):
        abs_damage = damage*self.defence/100
        final_damage = damage - abs_damage
        self.health -= final_damage
        print(f'По герою {self.name} получил {final_damage} урона')
        print('_'*15)
        
hero_1 = Hero('Артур', 100, 20, 5)
hero_2 = Hero('Валера', 80, 30, 4)
hero_1.get_status()
hero_2.get_status()
hero_1.increase_defense()
hero_2.increase_defense()
hero_1.make_damage(hero_2)
hero_2.make_damage(hero_1)