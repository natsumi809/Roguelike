import curses
import random
import time

def main(stdscr):
    # 画面の初期設定
    stdscr.nodelay(True)
    stdscr.clear()

    # 画面の最大サイズを取得
    sh, sw = stdscr.getmaxyx()

    # 敵のパターンを定義
    enemy_patterns = [
        {"interval": 0.01},  # パターン1: 一定間隔で進む
        {"interval": 0.005},  # パターン2: 少し速い
    ]
    # NOTE: 複数の敵が動くようにするため、ダブルや超高速タイプは
    # 現状のコードでは単一の敵しか扱えないため今回は含めていません。
    # 今後の改善で追加していきましょう。

    # プレイヤー情報
    player_x = 1
    player_y = sh // 2

    # 現在画面に表示されている敵を管理するリスト
    active_enemies = []
    
    # 敵の出現を制御する変数
    last_spawn_time = time.time()
    spawn_interval = 0.8 # 0.8秒ごとに新しい敵の出現を試みる

    while True:
        # 現在時刻を取得
        current_time = time.time()
        
        # 新しい敵をスポーンさせるかチェック
        if current_time - last_spawn_time >= spawn_interval:
            new_enemy_pattern = random.choice(enemy_patterns)
            new_enemy_x = random.randint(0, 2)
            active_enemies.append({
                "x": new_enemy_x,
                "y": 0,
                "interval": new_enemy_pattern["interval"],
                "last_move_time": current_time
            })
            last_spawn_time = current_time

        # 敵の移動と描画、衝突判定
        enemies_to_remove = []
        for enemy in active_enemies:
            # 敵の移動を時間で制御
            if current_time - enemy["last_move_time"] >= enemy["interval"]:
                enemy["y"] += 1
                enemy["last_move_time"] = current_time
            
            # 敵の描画
            stdscr.addstr(enemy["y"], enemy["x"] * 4, "E")

            # 衝突判定
            if player_x == enemy["x"] and player_y == enemy["y"]:
                stdscr.addstr(sh // 2, sw // 2 - len("GAME OVER") // 2, "GAME OVER")
                stdscr.refresh()
                curses.napms(2000)
                return

            # 画面外に出た敵は削除リストに追加
            if enemy["y"] > sh // 2:
                enemies_to_remove.append(enemy)

        # 画面外に出た敵をリストから削除
        for enemy in enemies_to_remove:
            active_enemies.remove(enemy)
        
        # 画面描画
        stdscr.clear()
        stdscr.addstr(player_y, player_x * 4, "P")

        # レーンの描画
        for y in range(sh // 2):
            for i in range(3):
                stdscr.addstr(y, i * 4, "|")
        
        # ここで敵を描画する
        for enemy in active_enemies:
            stdscr.addstr(enemy["y"], enemy["x"] * 4, "E")

        stdscr.refresh()

        # キー入力
        try:
            key = stdscr.getch()
        except curses.error:
            key = -1 
        
        if key == curses.KEY_LEFT and player_x > 0:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < 2:
            player_x += 1
        elif key == ord('q'):
            break

        curses.napms(6)

curses.wrapper(main)