from User import User
from Blockchain import Blockchain



class EventStream:
    def __init__(self):
        self.blockchain = Blockchain()

    def add_users(self):
        for i in range(10):
            user = User(i)
            self.blockchain._add_user_(user)

    def create_transactions(self):
        for i in range(8):
            self.blockchain.create_transaction()