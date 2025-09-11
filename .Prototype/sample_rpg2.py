# ローグライクゲームへシステム変更

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        damage = self.attack
        player.hp -= damage
        print(f"{self.name}は{player.name}に{damage}のダメージを与えた！")

# 骸骨騎士のインスタンスを作成
skeleton_knight = Enemy("骸骨騎士", 100, 35)

print(f"敵が現れた！{skeleton_knight.name} (HP: {skeleton_knight.hp}, 攻撃力: {skeleton_knight.attack})")




class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_enemy(self, enemy):
        damage = self.attack
        enemy.hp -= damage
        print(f"{self.name}は{enemy.name}に{damage}のダメージを与えた！")


# プレイヤーのインスタンスを作成
player = Player("Na", 100, 35)

print(f"プレイヤーが現れた！{player.name} (HP: {player.hp}, 攻撃力: {player.attack})")



# プレイヤーと敵のインスタンス
skeleton_knight = Enemy("骸骨騎士", 100, 35)
player = Player("Na", 100, 35)

print("--- 戦闘開始！ ---")
print(f"プレイヤー: {player.name} (HP: {player.hp})")
print(f"敵: {skeleton_knight.name} (HP: {skeleton_knight.hp})")
print("--------------------")

# 戦闘ループ
while player.hp > 0 and skeleton_knight.hp > 0:
    # プレイヤーのターン
    player.attack_enemy(skeleton_knight)
    if skeleton_knight.hp <= 0:
        print(f"{skeleton_knight.name}を倒した！")
        break
    
    # 敵のターン
    skeleton_knight.attack_player(player)
    if player.hp <= 0:
        print("プレイヤーは敗北した…")
        break

print("--- 戦闘終了 ---")