from blockchain import Blockchain
from car_sharing import Owner, Car, Customer

def show_balance(cust_balance, owner_balance):# 显示客户和车主的余额。
    print("客户余额: %s" % (cust_balance,))
    print("车主余额: %s" % (owner_balance,))

def show_rental_cost(cost):# 显示交易金额。
    print("交易金额: ", cost)

def start():    #启动整个汽车共享服务的流程，包括部署智能合约、预订汽车、添加汽车到市场等。
    blockchain = Blockchain()
    customer = Customer(50000)
    owner = Owner(0)
    eth = 50

    show_balance(customer.balance, owner.balance)

    #1 部署合约
    owner.deploy(eth, blockchain)

    #2 订车
    customer.request_book(eth, blockchain)

    #3 填加汽车以交易
    options = {'label0': 'BMJSER_alfa-romero giulia', 'value0': 13495,
                  'label1': 'YEORFT_audi 100 ls', 'value1': 13950,
                  'label2': 'FWIBH1_bmw 320i', 'value2': 16430,
                  'label3': 'KWMFOR_chevrolet impala', 'value3': 5155,
                  'label4': 'L3YIVX_dodge rampage', 'value4': 5572,
                  'label5': 'VO35Q7_honda civic', 'value5': 6475,
                  'label6': 'KAS1Q7_isuzu MU-X', 'value6': 6784,
                  'label7': 'ST9XPG_jaguar xj', 'value7': 3228,
                  'label8': 'JOMZA0_maxda rx3', 'value8': 5198}
    # car = "Ferrari"
    days_no = 1
    owner.add_car_to_rent(options['value2'], options['label2'])
    customer.pass_number_of_days(days_no)
    # 这里不需要区块链交易，除非汽车添加过程涉及金钱交易

    #4 加密并存储详细信息
    owner.encrypt_and_store_details(blockchain)
    owner.allow_car_usage()

    #5 Access Car
    customer.access_car()
    # 这里不需要区块链交易，除非汽车添加过程涉及金钱交易

    #6 End Car Rental
    customer.end_car_rental()

    #7 提取收入并取回余额
    owner.withdraw_earnings()
    customer.retrieve_balance()

    show_rental_cost(options['value2']*days_no)
    show_balance(customer.balance, owner.balance)

if __name__ == '__main__':
    start()
