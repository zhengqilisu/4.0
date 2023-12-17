from datetime import datetime

class SmartContract:
    idCounter = 1

    def __init__(self): #初始化智能合约，生成唯一ID，设置客户和车主的余额。
        self.id = SmartContract.idCounter
        SmartContract.idCounter += 1
        self.client_balance = 0
        self.owner_balance = 0
        self.booking_details = BookingDetails

    def retrieve_balance(self):#检索合约中的余额。
        return self.client_balance 

    def withdraw_earnings(self):#提取车主的收益。
        return self.owner_balance

    def client_deposit(self, ether):#客户向合约存款。
        self.client_balance += ether

    def owner_deposit(self, ether):#车主向合约存款。
        self.owner_balance += ether

    def allow_car_usage(self):#允许汽车使用。
        self.booking_details.get_car().allow_to_use()

    def add_booking_details(self, booking_details):#添加预订细节。
        self.booking_details = booking_details

    def get_booking_details(self):#获取预订细节。
        return self.booking_details

    def end_car_rental(self):# 结束汽车租赁，并处理费用。
        self.booking_details.get_car().end_rental()
        self.client_balance -= self.booking_details.get_summed_cost()
        self.owner_balance += self.booking_details.get_summed_cost()
    
    def get_car(self):
        return self.booking_details.get_car()


class BookingDetails:#初始化预订细节，如汽车信息、租赁价格等。
    def __init__(self, car, price_per_day):
        self.car = car
        self.price_per_day = price_per_day
        self.no_of_days = 0
        self.rental_date = datetime.now()

    def request(self, no_of_days):
        self.no_of_days = no_of_days

    def get_summed_cost(self):
        return self.price_per_day * self.no_of_days

    def get_car(self):
        return self.car


