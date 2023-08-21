from database.models import Games
from database import db
from datetime import datetime

def add_games(name, description, prices, quantity, link):
    game = Games(name=name, description=description, quantity=quantity, prices=prices, link=link)
    db.session.add(game)
    db.session.commit()
    return game.name,game.description,game.quantity,game.prices,game.link

