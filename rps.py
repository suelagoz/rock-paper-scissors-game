from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'rps_game_secret'


options = ['Rock', 'Paper', 'Scissors']

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return "congrats you win"
    else:
        return "computer wins :("

@app.route('/', methods=['GET', 'POST'])
def index():
  
    if 'user_score' not in session:
        session['user_score'] = 0
        session['comp_score'] = 0

    player_choice = None
    comp_choice = None
    result = None
    game_over = False

    if request.method == 'POST':
      
        player_choice = request.form.get('choice')
      
        comp_choice = random.choice(options)
      
        result = determine_winner(player_choice, comp_choice)

       
        if "congrats you win" in result:
            session['user_score'] += 1
        elif "computer wins :(" in result:
            session['comp_score'] += 1

        
        if session['user_score'] == 3 or session['comp_score'] == 3:
            game_over = True

    return render_template('index.html',
                           player_choice=player_choice,
                           comp_choice=comp_choice,
                           result=result,
                           user_score=session['user_score'],
                           comp_score=session['comp_score'],
                           game_over=game_over)


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
