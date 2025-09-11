# プレイヤー（魂）のクラス
# 憑依した亡骸のジョブを持つ

class Player:
    def __init__(self, name, body_job):
        self.name = (f"🟥{name}")
        self.body = body_job
        self.hp = self.body.base_hp
        self.attack = self.body.base_attack
        self.speed = self.body.base_speed

    # 回避判定メソッド
    def is_dodged(self):
        # 回避率を計算 (例: 素早さ25の暗殺者なら 10 + 25 = 30%)
        dodge_chance = 10 + self.speed
        # 1から100までの乱数と回避率を比較
        return random.randint(1, 100) <= dodge_chance

    # 攻撃コマンドメソッド
    def attack_enemy(self, enemy):
        # 敵の回避判定
        if enemy.is_dodged():
            print(f"{enemy.name}は攻撃をうまく回避した！")
            return # 回避されたらここで処理を終了

        damage = self.attack
        is_critical = False
        is_advantage = False

        # ジョブ相性の判定とダメージ加算
        if enemy.body.weakness == self.body.name:
            damage += 15
            is_advantage = True

        # 会心の一撃の判定とダメージ加算
        critical_chance = 10 + self.speed
        if random.randint(1, 100) <= critical_chance:
            damage += 20
            is_critical = True

        enemy.hp -= damage
        
        print(f"{self.name}の攻撃！", end='')
        if is_advantage:
            print(" (相性ボーナス!)", end='')
        if is_critical:
            print(" (会心の一撃!)", end='')
        print(f"  -{damage}")
        print(f"{enemy.name}HP:{create_hp_bar(enemy.hp, enemy.body.base_hp, filled_symbol='💙', empty_symbol=' ♡')}")

    

    # 逃走コマンドメソッド
    def run_away(self):
        run_chance = 35 + self.speed
        if random.randint(1, 100) <= run_chance:
            print(f"{self.name}はうまく逃走した！")
            return True
        else:
            print(f"{self.name}は逃走に失敗した！")
            return False