from contract import SmartContract, BookingDetails

class Owner:  #初始化车主，设置智能合约实例和余额。
    def __init__(self, balance):
        self.contract = SmartContract
        self.balance = balance

    def add_car_to_rent(self, day_price, car_info):#车主将汽车添加到租赁服务。
        car = Car(car_info)
        self.contract.add_booking_details(BookingDetails(car, day_price))

    def deploy(self, ether, blockchain):#部署智能合约到区块链上。
        self.balance -= ether
        self.contract = SmartContract()
        self.contract.owner_deposit(ether)
        blockchain.add_new_transaction(self.contract)

    def withdraw_earnings(self):#提取从交易中赚取的收益。
        self.balance += self.contract.withdraw_earnings()

    def allow_car_usage(self):#允许客户使用汽车。
        self.contract.allow_car_usage()

    def encrypt_and_store_details(self, blockchain):# 加密并存储相关细节到区块链上。
        blockchain.mine()

class Customer:#初始化客户，设置余额和智能合约实例。
    def __init__(self, balance):
        self.balance = balance
        self.contract = SmartContract

    def request_book(self, ether, blockchain):#客户请求预订汽车。
        self.contract = blockchain.get_unconfirmed_transactions()[0]
        self.contract.client_deposit(ether)
        self.balance -= ether

    def pass_number_of_days(self, days_no):
        self.contract.get_booking_details().request(days_no)

    def retrieve_balance(self):
        self.balance += self.contract.retrieve_balance()

    def end_car_rental(self):
        self.contract.end_car_rental()

    def access_car(self):
        self.contract.get_car().access()


class Car:
    def __init__(self, car_info, **kwargs):
        self.car_info = car_info
        self.additional = kwargs
        self.is_rented = False
        self.allowed_to_use = False

    def access(self):
        print("汽车已经获取")
        self.is_rented = True

    def end_rental(self):
        self.is_rented = False

    def allow_to_use(self):
        self.allowed_to_use = True





