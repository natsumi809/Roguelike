# 敵（過去の冒険者）のクラス


import random
from utility import create_hp_bar


class Enemy:
    def __init__(self, name, job):
        self.name = (f"🟦{name}")
        self.body = job
        self.hp = self.body.base_hp
        self.attack = self.body.base_attack
        self.speed = self.body.base_speed

    # 回避判定メソッド
    def is_dodged(self):
        # 回避率を計算
        dodge_chance = 10 + self.speed
        # 1から100までの乱数と回避率を比較
        return random.randint(1, 100) <= dodge_chance

    # プレイヤー攻撃メソッド    
    def attack_player(self, player):
        # プレイヤーの回避判定
        if player.is_dodged():
            print(f"{player.name}は攻撃をうまく回避した！")
            return

        damage = self.attack
        is_critical = False
        is_advantage = False

        # ジョブ相性の判定とダメージ加算
        if player.body.weakness == self.body.name:
            damage += 15
            is_advantage = True

        # 会心の一撃の判定とダメージ加算
        critical_chance = 10 + self.speed
        if random.randint(1, 100) <= critical_chance:
            damage += 20
            is_critical = True

        player.hp -= damage
        
        print(f"{self.name}の攻撃！", end='')
        if is_advantage:
            print(" (相性ボーナス!)", end='')
        if is_critical:
            print(" (会心の一撃!)", end='')
        print(f"  -{damage}")
        print(f"{player.name}HP:{create_hp_bar(player.hp, player.body.base_hp)}")