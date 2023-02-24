from hashlib import md5
from random import randint

class User:
    def __init__(self, number):
        self.id = number
        self.computing_power = randint(100, 300)

    # hash_ - хэш нынешней транзакции который нужно подтвердить
    # transaction - список , в котором хранятся элементы транзакций
    # prev_block_last_hash - последний хэш в преб\дыдущем блоке
    def accept_first_transaction_in_blocK(self, hash_, transaction, prev_block_last_hash):
        s =  prev_block_last_hash + ''.join(transaction)
        s = md5(s.encode()).hexdigest()
        if s == hash_:
            return 0
        else:
            return 1


    # hash_ - хэш нынешней транзакции который нужно подтвердить
    # transaction - список , в котором хранятся элементы транзакций
    # block_journal - список транзакций в нынешнем блоке
    # prev_hash - последний хэш в предыдущем блоке
    def accept_transaction(self, hash_, transaction, block_journal, prev_hash):
        # эта функция с самого начала блока строит хэш , учитывая в нем весь журнал транзакций,
        # причем первую проверку осуществляет с учетом хэша предыдущего блока
        for transaction0 in block_journal:
            s = prev_hash + ''.join(transaction0[:3])
            s = md5(s.encode()).hexdigest()
            prev_hash = s
        res = prev_hash + ''.join(transaction)
        res = md5(res.encode()).hexdigest()
        if res == hash_:
            print(f'Success:: Confirmed by user {self.id}')
            return 0
        else:
            print(f'Error:: Uncomfirmed by user {self.id}')
            return 1