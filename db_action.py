from db import Shop,Session


def add_shop(author,text):
    with Session() as session:
        shop = Shop(author=author,text=text)
        session.add(shop)
        session.commit()
        session.refresh(shop)
        return shop.id


def get_shops():
        with Session() as session:
            return session.query(Shop).all()


def update_shop(id, author, text):
        with Session() as session:
            shop = session.query(Shop).filter_by(id=id).first()
            shop.author = author
            shop.text = text
            return "інформацію про магазин успішно оновлено"

def delete_shop(id):
        with Session() as session:
            shop = session.query(Shop).filter_by(id = id).first()
            session.delete(shop)
            session.commit()
            return "інформацію про магазин успішно видалено"