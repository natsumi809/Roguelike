# --- ユーティリティ関数 ---

def create_hp_bar(current_hp, max_hp, filled_symbol='❤️ ', empty_symbol=' ♡'):
    """HPバー文字列を生成する関数。体力10につき1つのシンボル。"""
    filled_hearts = int(current_hp / 10)
    max_hearts = int(max_hp / 10)
    empty_hearts = max_hearts - filled_hearts
    
    hp_bar = filled_symbol * filled_hearts + empty_symbol * empty_hearts
    return f"[ {hp_bar} ] {current_hp}/{max_hp}"