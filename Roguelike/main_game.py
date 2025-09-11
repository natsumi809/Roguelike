# --- ゲームの実行部分 ---


import random
import time

from player import Player
from enemy import Enemy
from soul import Warrior, Mage, Assassin
from utility import create_hp_bar



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

# プレイヤーと敵のインスタンス生成
player = Player(player_name, initial_job)
enemy_job = random.choice(jobs)
enemy = Enemy("敵の" + enemy_job.name, enemy_job)

print(f"\n{player.name}の魂は{player.body.name}の亡骸に憑依した！")
print(f"ステータス: HP {player.hp}, 攻撃力 {player.attack}, 素早さ: {player.speed}")
time.sleep(2)
print()
print()
print()
print()
print()
print()
print()
print(f"敵が現れた！{enemy.name} (HP: {enemy.hp}, 攻撃力: {enemy.attack}, 素早さ: {enemy.speed})")
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
print(f"{player.name}HP: \n"
      f"{create_hp_bar(player.hp, player.body.base_hp)}")
print(f"{enemy.name}HP: \n"
      f"{create_hp_bar(enemy.hp, enemy.body.base_hp, filled_symbol='💙', empty_symbol=' ♡')}")
print()
print()
print()
print()
print()
print()

time.sleep(3)

# 新しい戦闘ループ
turn = 1
is_ran_away = False

while player.hp > 0 and enemy.hp > 0 and not is_ran_away:
    print()
    print(f"---- ターン{turn} ---------------------------------")
    print()
    print()
    time.sleep(2)

    # プレイヤーの行動選択を最優先
    action = input("どうしますか？ (1:攻撃, 2:逃走)\n"
                   '🟥 ')
    print()
    print()
    
    # 素早さに基づいて行動順を決定
    combatants = [player, enemy]
    if player.speed == enemy.speed:
        random.shuffle(combatants)
    else:
        combatants = sorted(combatants, key=lambda c: c.speed, reverse=True) 

    # 決定された行動順でターンを実行
    for current_turn_character in combatants:
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
            if not is_ran_away and enemy.hp > 0:  # プレイヤーが逃走に成功しておらず、敵が生きている場合のみ
                print(f"----   {enemy.name}のターン   ----")
                print()
                time.sleep(2.5)
                enemy.attack_player(player)

        # HPバーを更新して表示
        print()
        print()
        print()
        time.sleep(3)

        # どちらかが倒れたら、または逃走に成功したらループを抜ける
        if player.hp <= 0 or enemy.hp <= 0 or is_ran_away:
            break
            
    turn += 1

print("---- 戦闘終了 ---------------------------------")
print()
print()
time.sleep(2.5)

# 勝敗判定と結果の表示
print()
print()
print()
if is_ran_away:
    print(f"【{player.name}はフロアを脱出した！】")
    print(f"残りHP {create_hp_bar(player.hp, player.body.base_hp)}")
elif player.hp > 0:
    print(f"【{player.name}の勝利！】")
    time.sleep(1.8)
    print(f"【{enemy.name}を打ち破った！】")
    print(f"残りHP {create_hp_bar(player.hp, player.body.base_hp)}")

else:
    print(f"【{player.name}は敗北した… 】")
    time.sleep(2)
    print(f"【{player.name}の魂は消滅した。亡骸はダンジョンに眠る… 】")
    print(f"残りHP {create_hp_bar(player.hp, player.body.base_hp)}")

print()
print()
print()
print()
print()