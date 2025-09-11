import curses

def main(stdscr):
    # 画面の初期設定
    stdscr.nodelay(True)  # キー入力を待機しない設定
    stdscr.clear()       # 画面をクリア

    # 画面の最大サイズを取得
    sh, sw = stdscr.getmaxyx()

    player_x = 1         # プレイヤーのX座標（レーン）
    player_y = sh - 3    # プレイヤーのY座標を画面の底から3行目に設定

    while True:
        # 画面描画
        stdscr.clear()
        stdscr.addstr(player_y, player_x * 4, "P") # Pはプレイヤー

        # レーンの描画
        for i in range(3):
            # レーンの終点を画面の最大高さより1つ上に設定
            stdscr.addstr(0, i * 4 + 2, "|")
            stdscr.addstr(sh - 1, i * 4 + 2, "|") # sh-1で最終行に描画

        stdscr.refresh()

        # キー入力
        try:
            key = stdscr.getch()
        except curses.error:
            # 入力がない場合はスキップ
            key = -1 
        
        if key == curses.KEY_LEFT and player_x > 0:
            player_x -= 1
        elif key == curses.KEY_RIGHT and player_x < 2:
            player_x += 1
        elif key == ord('q'):
            break

        # ゲームの進行を一時停止
        curses.napms(100) # 100ミリ秒待機

curses.wrapper(main)