from app import app, db
from models import Message

with app.app_context():
    db.drop_all()
    db.create_all()

    m1 = Message(body="Hello 👋", username="Liza")
    m2 = Message(body="Hi there!", username="Mike")
    m3 = Message(body="Howdy!", username="Jake")

    db.session.add_all([m1, m2, m3])
    db.session.commit()

    print("Seeded database.")
