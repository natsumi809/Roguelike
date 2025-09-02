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
        print(f"{self.name}は{enemy.body.name}に{damage}のダメージを与えた！")
        
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
        print(f"{self.name}は{player.name}に{damage}のダメージを与えた！")

# --- ゲームの実行部分 ---
print()
print()
print("魂よ、目覚めよ。")
print()
player_name = input("あなたの名前を入力してください: ")
print() # ここに空白行を追加
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
time.sleep(1.1)
job_choice = input('--------------番号を入力してください:')
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
print()
print()
print() 
print() 
print() 
print() 
time.sleep(2.7)
print(f"敵が現れた！{enemy.name} (HP: {enemy.hp}, 攻撃力: {enemy.attack})")
print()
time.sleep(2.3)
print("----------- 戦闘開始！ -----------")
print()
print() 
time.sleep(3)

# 新しい戦闘ループ
combatants = [player, enemy]
random.shuffle(combatants) 

while player.hp > 0 and enemy.hp > 0:
    for current_turn_character in combatants:
        if current_turn_character == player:
            player.attack_enemy(enemy)
        else:
            enemy.attack_player(player)

        # 1秒待機
        time.sleep(1.7)

        # どちらかが倒れたらループを抜ける
        if player.hp <= 0 or enemy.hp <= 0:
            break
            
print()
print()
print("------------ 戦闘終了 ------------")
print()
print()
print()
print()
print()
time.sleep(2.5)

# 勝敗判定と結果の表示
if player.hp > 0:
    print(f"【{player.name}の勝利！】")
    time.sleep(1.8)
    print(f"【{enemy.name}を打ち破った！】")
else:
    print(f"【{player.name}は敗北した… 】")
    time.sleep(2)
    print(f"【{player_name}の魂は消滅した。亡骸はダンジョンで眠るだろう… 】")