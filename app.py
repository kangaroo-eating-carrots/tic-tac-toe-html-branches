from flask import Flask, render_template, request, redirect, url_for
import game_logic as gl

app = Flask(__name__)

# Initialise game board and current player
# board = [' '] * 9
# current_player = 'X'

BOARD_WIDTH = 3
WINNING_LINE = 3
game = gl.Game_Play(BOARD_WIDTH, WINNING_LINE)


# NOTE: you cannot use this answer in Portfolio Part 2
# def check_winner():
#     # Winning combinations
#     return None
# def check_draw():
#     return ' ' not in board
# @app.route('/')
# def index():
#     winner = check_winner()
#     draw = check_draw()
#     return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)

@app.route('/')
def index():
    winner = game.check_winner()
    draw = game.check_draw()
    current_player = game.current_player.mark
    board = game.setting.board
    return render_template('index.html', board=board, current_player=current_player, winner=winner, draw=draw)

# @app.route('/play/<int:cell>')
# def play(cell):
#     # breakpoint()
#     global current_player
#     if board[cell] == ' ':
#         board[cell] = current_player
#         if not check_winner():
#             current_player = 'O' if current_player == 'X' else 'X'
#     return redirect(url_for('index'))

@app.route('/play/<int:cell>')
def play(cell):
    # breakpoint()

    if game.do_continue() == False:
        return redirect(url_for('index'))

    if game.setting.board[cell] == ' ':
        game.setting.board[cell] = game.current_player.mark
        game.current_player.make_choice(cell, game.setting.board_width)
        game.current_player = game.player1 if game.current_player == game.player2 else game.player2
    return redirect(url_for('index'))


# @app.route('/reset')
# def reset():
#     global board, current_player
#     board = [' '] * 9
#     current_player = 'X'
#     return redirect(url_for('index'))

@app.route('/reset')
def reset():
    game.setting.board = [' '] * 9
    game.current_player = game.player1
    game.put_counter = 0
    game.player1.choices = []
    game.player2.choices = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
