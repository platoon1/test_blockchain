from User import User
from Blockchain import Blockchain

blockchain = Blockchain()

for i in range(10):
    user = User(i)
    blockchain._add_user_(user)

for i in range(8):
    blockchain.create_transaction()