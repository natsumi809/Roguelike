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