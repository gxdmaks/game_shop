from database import db

def get_all_game(name, description, quantity, prices, link):
    get_games = db.session.query(name=name, description=description, quantity=quantity, prices=prices, link=link).all()
    db.session.get(get_games)
    db.session.commit()
    return get_games
