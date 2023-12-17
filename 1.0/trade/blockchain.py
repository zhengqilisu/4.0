import json
import time
import random
import string
'''
'Block'类表示区块链中的一个区块。它包含一个用来进行计算，以及一个'compute_hash'方法用来计算区块内容的哈希值。哈希值唯一的表示一个区块，一旦区块的内容改变，哈希值将会变动。

'compute_hash'方法通过调用'random_string'方法返回一个随机字符串表示区块的哈希值。

'Blockchain'类表示一个完整的区块链。区块链的第一个区块叫做'genesis_block'，即创世区块，并通过'create_genesis_block'方法生成。调用'add_block'方法可以添加一个新的区块到区块链中。

在这个代码中，通过'proof_of_work'进行工作量证明(POW）的计算，来获取得到的符合难度要求的哈希值。'is_valid_proof'方法用来验证一个区块的哈希值是否满足POW的条件。

'add_new_transaction'方法用于添加新的交易到待处理交易的列表，然后通过'mine'方法将待处理的交易添加到新的区块中，最后将新区块添加到区块链中。

'check_chain_validity'方法用于校验整个区块链的正确性，它会遍历整个区块链，对每个区块进行工作量证明的验证，确保每个区块的哈希值一致且前后区块链接正确。
'''
class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):#初始化一个新的区块，设置索引、交易、时间戳、前一个区块的哈希值和工作量证明
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        print(
            f"使用索引初始化新区块: {index}, 交易: {transactions}, 时间戳: {timestamp}, 上一个哈希值: {previous_hash}, 随机数: {nonce}")

    def compute_hash(self):#通过调用'random_string'方法返回一个随机字符串表示区块的哈希值。
        """
        返回区块内容哈希值的函数
        """
        print("计算区块哈希值...")
        return self.random_string()


    def random_string(self, starts_with='00', stringLength=8):#生成一个随机字符串，用于简化的哈希计算。
        letters = string.ascii_lowercase
        return starts_with  + ''.join(random.choice(letters) for i in range(stringLength))



class Blockchain:
    # PoW算法的难度
    difficulty = 2

    def __init__(self):#初始化区块链，创建创世区块。
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):#创始区块
        """
        生成创世区块并将其附加到链条。
        该块的索引为 0，previous_hash为 0，
        并且有效的哈希值。
        """
        genesis_block = Block(0, [], 0, "0")
        genesis_block.hash = genesis_block.compute_hash()
        print(genesis_block.hash)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        验证后将区块添加到链中的函数。
        验证包括：
        * 检查证明是否有效。
        * 区块中引用的previous_hash和最新区块的哈希值
          在链式比赛中。
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    @staticmethod
    def proof_of_work(block):
        """
        尝试不同随机数值以获取符合我们
        难度标准的哈希值的函数
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def get_unconfirmed_transactions(self):
        return self.unconfirmed_transactions

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        """
        检查block_hash是否为有效的区块哈希值并满足难度标准。
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            # 删除哈希字段以再次重新计算哈希
            # 使用“compute_hash”方法。
            delattr(block, "hash")

            if not cls.is_valid_proof(block, block_hash) or \
                    previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return result

    def mine(self):
        """
        此功能用作通过将待处理交易添加到区块并找出工作量证明来将待处理交易添加到区块链的接口。
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []

        return True

