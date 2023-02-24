
from hashlib import md5
from User import User
from time import time
from random import randint, random

class Blockchain(object):
    def __init__(self):
        self.blocks = {}  # хэши всех транзакций во всех блоках со времени запуска блокчейна
        self.now_block = [['0x001', '0x002', '0.5432','0b83e4f71f94229141b55324c110eae5']]  # хэши транзакций в нынешнем блоке
        self.addresses = {} # балансы пользователей
        self.prev_block_last_hash = '' # хэш крайней транзакции в предыдущем блоке

        #self.addresses = dict((('0x'+md5(str(time()).encode()).hexdigest() , randint(5, 100)+random()) for i in range(10))) # здесь хранятся адреса и балансы
        self.tokenName = 'FCN'
        self.totalBalance = 100  # сколько выпущено всего валюты
        self.users = []  # объекты пользователи


        self.block_size = 5 # transactions

        for i in range(5):
            addr = '0x'+f'00{i}'
            value = randint(5, 10) + random()
            self.addresses[addr] = value
        print(self.addresses)



    def create_transaction(self):
        transaction = input("Введите транзакцию (address_from, address_to, value) : ").split()
        if len(transaction) > 3:
            print('Error:: wrong number of arguments')
            return 1
        if transaction[0] not in self.addresses.keys():
            print(f'Error:: address {transaction[0]} is unknown')
            return 1
        elif transaction[1] not in self.addresses.keys():
            print(f'Error:: address {transaction[1]} is unknown')
            return 1
        if self.addresses[transaction[0]] < float(transaction[2]):
            print('Error:: not enough balance for executing of transaction')
            return 1

        hash_ = self.make_hash(transaction)

        # здесь происходит вызов функции которая осуществялет моделирование
        # проверки целостности хэша данной транзакции путем высчитывания
        # вссех предыдущих хэшей в даном блоке результат либо 0 либо 1
        decision = self.accept_transaction(hash_, transaction)

        if decision:
            """ передвижение криптовалюты между балансами"""
            self.addresses[transaction[0]] -= float(transaction[2])
            self.addresses[transaction[1]] += float(transaction[2])
            transaction.append(hash_)

            """максимальное количество блоков не будет достигнуто, но на всякий случай проверим"""
            if len(self.now_block) < self.block_size:
                self.now_block.append(transaction)
                if len(self.now_block)== self.block_size:
                    self.blocks[len(self.blocks) + 1] = self.now_block
                    self.now_block = []
                    self.prev_block_last_hash = hash_
            print(f'self.blocks: {self.blocks}')
            print(f'self.now_block:  {self.now_block}')



            print(f'Success:: now balance of {transaction[1]} is {self.addresses[transaction[1]]} {self.tokenName}, transaction hash : {hash_}')
        else:
            print(f'Not accepted:: transaction from: {transaction[0]} to: {transaction[1]} value: {transaction[2]}')


    def make_hash(self, transaction):
        if type(transaction) is list:
            s = ''.join(transaction)
        elif type(transaction) is int or type(transaction) is float:
            s = str(transaction)
        else:
            s = transaction
        prev = self.now_block[-1][-1] if len(self.now_block)>0 else self.prev_block_last_hash
        s = prev + s
        s = md5(s.encode())
        return s.hexdigest()


    def accept_transaction(self, hash_ ,transaction):
        good = 1
        print(self.users)
        for user in self.users:
            if len(self.now_block) == 0:
                decision = user.accept_first_transaction_in_blocK(hash_, transaction,  self.prev_block_last_hash)
            else:
                decision = user.accept_transaction(hash_, transaction, self.now_block, self.prev_block_last_hash)
            if  decision:
                good = 0
                break
        if not good: return 0
        else: return 1


    def _add_user_(self, user):
        if isinstance(user, User):
            self.users.append(user)
        else:
            raise ValueError

