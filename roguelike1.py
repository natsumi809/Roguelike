# 段階1: ゲームシステム作成（『魂』『職業』システム）

import sys
import random
import time

# --- クラスの定義 ---
class Job:
    """職業の基本クラス。"""
    def __init__(self, name, base_hp, base_attack):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack

class Warrior(Job):
    """戦士クラス：Jobクラスを継承。"""
    def __init__(self):
        super().__init__("戦士", 150, 40)

class Mage(Job):
    """魔法使いクラス：Jobクラスを継承。"""
    def __init__(self):
        super().__init__("魔法使い", 80, 50)

class Assassin(Job):
    """暗殺者クラス：Jobクラスを継承。"""
    def __init__(self):
        super().__init__("暗殺者", 100, 30)

class Player:
    """プレイヤー（魂）のクラス。乗り移った体のジョブを持つ。"""
    def __init__(self, name, body_job):
        self.name = name
        self.body = body_job
        self.hp = self.body.base_hp
        self.attack = self.body.base_attack

    def attack_enemy(self, enemy):
        """敵を攻撃するメソッド。"""
        damage = self.attack
        enemy.hp -= damage
        print(f"{self.name}の攻撃！  -{damage}")
        
class Enemy:
    """敵（過去の冒険者）のクラス。"""
    def __init__(self, name, job):
        self.name = name
        self.body = job
        self.hp = self.body.base_hp
        self.attack = self.body.base_attack
        
    def attack_player(self, player):
        """プレイヤーを攻撃するメソッド。"""
        damage = self.attack
        player.hp -= damage
        print(f"{self.name}の攻撃！  -{damage}")

# --- ユーティリティ関数 ---
def create_hp_bar(current_hp, max_hp, bar_length=10):
    """HPバー文字列を生成する関数。"""
    # HPの割合を計算し、バーに変換
    filled_blocks = int(current_hp / max_hp * bar_length)
    empty_blocks = bar_length - filled_blocks
    
    # ♥ と ♡ でHPバーを生成
    hp_bar = "♥" * filled_blocks + "♡" * empty_blocks
    return f"[{hp_bar}] {current_hp}/{max_hp}"

# --- ゲームの実行部分 ---
print()
print()
print("汝、目覚めよ。")
print()
player_name = input("- あなたの名前を入力してください - \n" 
                    '□ ')
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
print("どの亡骸に乗り移りますか？")
time.sleep(1.1)
print()
for i, job in enumerate(jobs, 1):
    print(f"{i}: {job.name}（HP: {job.base_hp}, 攻撃力: {job.base_attack}）")

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
    print("無効な選択です。戦士としてゲームを開始します。")
    initial_job = Warrior()

# プレイヤーと敵のインスタンス生成
player = Player(player_name, initial_job)
enemy_job = random.choice(jobs)
enemy = Enemy("敵の" + enemy_job.name, enemy_job)

print(f"\n魂は{player.body.name}の体に乗り移った！")
print(f"ステータス: HP {player.hp}, 攻撃力 {player.attack}")
time.sleep(2)
print()
print()
print()
print()
print()
print()
print()
print(f"敵が現れた！{enemy.name} (HP: {enemy.hp}, 攻撃力: {enemy.attack})")
print()
print()
print()
print()
print()
print()
print()
time.sleep(2)
print("--- 戦闘開始！ ---")
print()

# HPバーの初期表示
print(f"プレイヤーHP: {create_hp_bar(player.hp, player.body.base_hp)}")
print(f"敵HP: {create_hp_bar(enemy.hp, enemy.body.base_hp)}")
print()
print()
print()
print()
print()

time.sleep(3)

# 新しい戦闘ループ
combatants = [player, enemy]
random.shuffle(combatants) 
turn = 1

while player.hp > 0 and enemy.hp > 0:
    print(f"---------------- ターン{turn} ----------------")
    print()
    print()
    print()
    time.sleep(2)

    for current_turn_character in combatants:
        if current_turn_character == player:
            print(f"----   {player_name}のターン   ----")
            player.attack_enemy(enemy)
        else:
            print(f"----   {enemy.name}のターン   ----")
            enemy.attack_player(player)

        # HPバーを更新して表示
        print(f"プレイヤーHP: {create_hp_bar(player.hp, player.body.base_hp)}")
        print(f"敵HP: {create_hp_bar(enemy.hp, enemy.body.base_hp)}")
        print()
        print()
        print()
        time.sleep(3.5)

        # どちらかが倒れたらループを抜ける
        if player.hp <= 0 or enemy.hp <= 0:
            break
            
    turn += 1


print("---------------- 戦闘終了 ----------------")
print()
print()
time.sleep(2.5)

# 勝敗判定と結果の表示
print()
print()
print()
if player.hp > 0:
    print(f"【{player.name}の勝利！】")
    time.sleep(1.8)
    print(f"【{enemy.name}を打ち破った！】")
    print(f"最終HP: {create_hp_bar(player.hp, player.body.base_hp)}")
else:
    print(f"【{player.name}は敗北した… 】")
    time.sleep(2)
    print(f"【{player_name}の魂は消滅した。亡骸はダンジョンに眠る… 】")
    print(f"残りHP: {create_hp_bar(player.hp, player.body.base_hp)}")

print()
print()
print()
print()
print()