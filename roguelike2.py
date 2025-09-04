# 段階5: ローグライク要素（階層の概念と連戦）の追加

import sys
import random
import time

# --- クラスの定義 ---

# 職業（亡骸）の基本クラス
class Job:
    def __init__(self, name, base_hp, base_attack, base_speed, weakness):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_speed = base_speed
        self.weakness = weakness

"""戦士クラス：Jobクラスを継承。"""
class Warrior(Job):
    def __init__(self):
        super().__init__("戦士", 130, 40, 10, "魔法使い")

"""魔法使いクラス：Jobクラスを継承。"""
class Mage(Job):
    def __init__(self):
        super().__init__("魔法使い", 90, 45, 15, "暗殺者")

"""暗殺者クラス：Jobクラスを継承。"""
class Assassin(Job):
    def __init__(self):
        super().__init__("暗殺者", 110, 30, 25, "戦士")

# プレイヤー（魂）のクラス
# 憑依した亡骸のジョブを持つ
class Player:
    def __init__(self, name, body_job):
        self.name = (f"🟥{name}")
        self.body = body_job
        self.hp = self.body.base_hp
        self.attack = self.body.base_attack
        self.speed = self.body.base_speed

    # 攻撃コマンドメソッド
    def attack_enemy(self, enemy):
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
        
# 敵（過去の冒険者）のクラス
class Enemy:
    def __init__(self, name, job):
        self.name = (f"🟦{name}")
        self.body = job
        self.hp = self.body.base_hp
        self.attack = self.body.base_attack
        self.speed = self.body.base_speed

    # プレイヤー攻撃メソッド    
    def attack_player(self, player):
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

# --- ユーティリティ関数 ---

def create_hp_bar(current_hp, max_hp, filled_symbol='❤️ ', empty_symbol=' ♡'):
    """HPバー文字列を生成する関数。体力10につき1つのシンボル。"""
    if current_hp < 0:
        current_hp = 0
        
    filled_hearts = int(current_hp / 10)
    max_hearts = int(max_hp / 10)
    empty_hearts = max_hearts - filled_hearts
    
    hp_bar = filled_symbol * filled_hearts + empty_symbol * empty_hearts
    return f"[ {hp_bar} ] {current_hp}/{max_hp}"

# --- ゲームの実行部分 ---

print()
print()
print("汝、目覚めよ。")
print()
player_name = input("- あなたの名前を入力してください - \n" 
                    '🟥 ')
print()
print()
print()
print()
print()

# ジョブの選択肢をリストにまとめる
jobs = [Warrior(), Mage(), Assassin()]

print('--------------------------------------')
print()
print()
print("どの亡骸に憑依しますか？")
time.sleep(1.1)
print()
for i, job in enumerate(jobs, 1):
    print(f"{i}: {job.name}（HP: {job.base_hp}, 攻撃力: {job.base_attack}, 素早さ: {job.base_speed}）")

print()
print()
time.sleep(1.8)
job_choice = input('--------------番号を入力してください:')
print()
print()
print()
print()
print()
print()

# 選択されたジョブを反映
try:
    initial_job = jobs[int(job_choice) - 1]
except (ValueError, IndexError):
    print("無効な選択です。気分で亡骸に憑依します。")
    initial_job = random.choice(jobs)

# プレイヤーのインスタンスを生成（一度だけ）
player = Player(player_name, initial_job)

print(f"\n魂は{player.body.name}の亡骸に憑依した！")
print(f"ステータス: HP {player.hp}, 攻撃力 {player.attack}, 素早さ: {player.speed}")
time.sleep(2)

# ローグライクのメインループ
floor = 1
while player.hp > 0:
    print("\n" * 5)
    print(f"--- 第{floor}階層 ---")
    time.sleep(2)
    print()

    # 新しい敵を生成
    enemy_job = random.choice(jobs)
    enemy = Enemy("敵の" + enemy_job.name, enemy_job)

    print(f"敵が現れた！{enemy.name} (HP: {enemy.hp}, 攻撃力: {enemy.attack}, 素早さ: {enemy.speed})")
    time.sleep(2)
    print("--- 戦闘開始！ ---")
    print()

    # HPバーの初期表示
    print(f"{player.name}HP: \n"
          f"{create_hp_bar(player.hp, player.body.base_hp)}")
    print(f"{enemy.name}HP: \n"
          f"{create_hp_bar(enemy.hp, enemy.body.base_hp, filled_symbol='💙', empty_symbol=' ♡')}")
    print()
    time.sleep(3)

    # 1対1の戦闘ループ
    turn = 1
    is_ran_away = False
    
    while player.hp > 0 and enemy.hp > 0 and not is_ran_away:
        print()
        print(f"---- ターン{turn} ---------------------------------")
        print()
        time.sleep(2)

        # プレイヤーの行動選択を最優先
        action = input("どうしますか？ (1:攻撃, 2:逃走)\n"
                       '□ ')
        print()
        
        # 素早さに基づいて行動順を決定
        combatants = [player, enemy]
        if player.speed == enemy.speed:
            random.shuffle(combatants)
        else:
            combatants = sorted(combatants, key=lambda c: c.speed, reverse=True) 

        # 決定された行動順でターンを実行
        for current_turn_character in combatants:
            if player.hp <= 0 or enemy.hp <= 0 or is_ran_away:
                break
            
            # プレイヤーの行動
            if current_turn_character == player:
                print(f"----   {player.name}のターン   ----")
                print()
                time.sleep(2.5)
                if action == "1":
                    player.attack_enemy(enemy)
                elif action == "2":
                    is_ran_away = player.run_away()
                else:
                    print("無効な選択です。プレイヤーは何もできなかった！")
            
            # 敵の行動
            else:
                if not is_ran_away and enemy.hp > 0:
                    print(f"----   {enemy.name}のターン   ----")
                    print()
                    time.sleep(2.5)
                    enemy.attack_player(player)

            # HPバーを更新して表示
            print()
            print()
            print()
            print(f"{player.name}HP: \n"
                  f"{create_hp_bar(player.hp, player.body.base_hp)}")
            print(f"{enemy.name}HP: \n"
                  f"{create_hp_bar(enemy.hp, enemy.body.base_hp, filled_symbol='💙', empty_symbol=' ♡')}")
            print()
            print()
            time.sleep(3)
        
        turn += 1

    print("\n" * 5)
    print("---- 戦闘終了 ---------------------------------")
    time.sleep(2.5)
    
    # 勝敗判定と次の階層へ進むかどうかの処理
    if is_ran_away:
        print(f"【{player_name}はフロアを脱出した！】")
        print(f"次のフロアで再挑戦！")
        continue # 同じ階層で再戦
    elif player.hp > 0:
        print(f"【{player_name}の勝利！】")
        time.sleep(1.8)
        print(f"【{enemy.name}を打ち破った！】")
        print()
        print(f"残りHP: {player.hp} / {player.body.base_hp}")
        time.sleep(2.5)
        floor += 1
        continue  # 次の階層へ
    else:
        # プレイヤー敗北
        break

# ゲーム終了時のメッセージ
print("\n" * 5)
print("---- ゲーム終了 ---------------------------------")
print()
if player.hp <= 0:
    print(f"【{player_name}は敗北した… 】")
    time.sleep(2)
    print(f"【{player_name}の魂は消滅した。亡骸はダンジョンに眠る… 】")
    print()
    print(f"到達階層: 第{floor}階層")
else: # 逃走に成功した場合
    print(f"【{player_name}は無事にダンジョンから脱出した！】")
    print(f"到達階層: 第{floor}階層")

print()
print()
print()
print()
print()