from flask import Flask, render_template, request, redirect, url_for
import game_play as gp

app = Flask(__name__)

BOARD_WIDTH = 3
WINNING_LINE = 3
game = gp.Game_Play(BOARD_WIDTH, WINNING_LINE)

@app.route('/')
def index():
    winner = game.check_winner()
    draw = game.check_draw()
    current_player = game.current_player.mark
    board = game.setting.board
    scores = {'Player 1': game.player1.score, 'Player 2': game.player2.score}

    return render_template('index.html',
                           board=board,
                           current_player=current_player,
                           winner=winner,
                           draw=draw,
                           scores=scores)

@app.route('/play/<int:cell>')
def play(cell):
    if game.do_continue() == False:
        return redirect(url_for('index'))

    if game.setting.board[cell] == ' ':
        game.setting.board[cell] = game.current_player.mark
        game.current_player.make_choice(cell, game.setting.board_width)
        game.current_player = game.player1 if game.current_player == game.player2 else game.player2
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    game.setting.board = [' '] * 9
    game.current_player = game.player1
    game.put_counter = 0
    game.player1.choices = []
    game.player2.choices = []
    game.is_there_winner = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
