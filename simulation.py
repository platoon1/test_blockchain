from User import User
from Blockchain import Blockchain
from time import sleep
from random import sample, randint, choice

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

    def create_transaction(self, trnasaction):
        self.blockchain.create_transaction(trnasaction)

    def add_user(self, user):
        self.blockchain._add_user_(user)

    def main(self):
        work = 1
        while work<10:
            work+=1
            sleep(1)
            if choice([0,1]):
                new_user = User(0)
                self.blockchain._add_user_(new_user)
            else:
                addr_from, addr_to = sample(self.blockchain.addresses.keys(), 2)
                value = randint(0, 100)
                self.blockchain.create_transaction([addr_from, addr_to, str(value)])
        self.blockchain.check_integrity()


if __name__=='__main__':
    stream  = EventStream()

    stream.main()
