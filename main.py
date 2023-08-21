from flask import Flask, render_template, request, redirect, session
from forms import add_game, login
from database.add_game_service import add_games
from database import db
from database.models import Games
app = Flask(__name__)

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'Game_Shop'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:909411216MAx@localhost/game_shop'

db.init_app(app)




current_user_email = None

@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')

@app.route('/add-game', methods=['GET','POST'])
def add():
    form = add_game()
    name = form.game_name.data
    desc = form.game_description.data
    quantity = form.quantity.data
    price = form.game_prices.data
    link = form.game_link.data
    if request.method == 'POST':
        adds = add_games(name, desc, quantity, price, link)
        print(adds)
    return render_template('add-game.html', form=form)


@app.route('/login')
def loginm():
    global current_user_email
    if current_user_email:
        login_form = login()
        return render_template('index.html', login=login_form)

    elif not current_user_email:
        login_form = login()

        if request.method == 'POST':
            user_password = session.get(login_form.email.data)
            if user_password == login_form.password.data:
                current_user_email = login_form.email.data

                return redirect('/')

        return render_template('authorize.html', login_form=login_form)



@app.route('/register', methods=['POST'])
def register_user():
    user_data = login()
    email = user_data.email.data
    password = user_data.password.data

    session[email] = password

    return render_template('index.html', register_form=user_data)

@app.route('/all-game', methods=['GET'])
def all_game():
    game = Games.query.all()
    return render_template('all-game.html', game=game)


with app.app_context():
    db.create_all()

app.run(debug=True)


