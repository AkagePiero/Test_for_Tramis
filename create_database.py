from models.database import create_db, Session
from models.model import Test, Cont

# здесь создаётся наше БД
def create_database():
    create_db()
