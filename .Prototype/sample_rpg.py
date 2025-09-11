class Character:
    # コンストラクタ: オブジェクトが作られるときに呼ばれる
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        print(f"{self.name}が登場しました！\n体力: {self.health}, 攻撃力: {self.attack_power}")

    # 攻撃メソッド
    def attack(self, other):
        # 相手の体力を自分の攻撃力分減らす
        other.health -= self.attack_power
        print(f"{self.name}が{other.name}に攻撃！{self.attack_power}のダメージを与えた。")

    # 生存判定メソッド
    def is_alive(self):
        # 体力が0より多ければTrue、そうでなければFalseを返す
        return self.health > 0
    
    # --- ゲーム開始 ---

# プレイヤーとモンスターのオブジェクトを作成
# これで、Characterクラスの設計図から、実際の「モノ」が2つ作られたことになります。
player = Character("勇者", 100, 20)
monster = Character("スライム", 50, 10)

print("--- バトル開始！ ---")

# バトルループ
turn = 1
while player.is_alive() and monster.is_alive():
    print(f"\n--- ターン {turn} ---")

    # 勇者の攻撃
    player.attack(monster)
    print(f"{monster.name}の残り体力: {monster.health}")

    # モンスターが生きているかチェック
    if not monster.is_alive():
        print(f"{monster.name}は倒れた。")
        break # 倒れていたらループを抜ける

    # モンスターの攻撃
    monster.attack(player)
    print(f"{player.name}の残り体力: {player.health}")

    turn += 1

print("\n--- バトル終了 ---")

# 勝利判定
if player.is_alive():
    print(f"{player.name}の勝利！")
else:
    print(f"{monster.name}の勝利！")