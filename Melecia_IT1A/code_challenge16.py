
def create_account(name, initial_amount = 0):
    account_name = name
    amount = initial_amount
    print(f"ACCOUNT CREATED FOR {account_name} WITH AN INITIAL AMOUNT OF {amount}. ")

def get_denomintaion(amount):
    one_thousand = amount // 1000
    l_sukli = amount % 1000

    five_h = l_sukli // 500
    fh_sukli = l_sukli % 500

    two_h = fh_sukli // 200
    th_sukli = fh_sukli % 200

    one_h = th_sukli // 100
    oh_sukli = th_sukli % 100

    fifty = oh_sukli // 50
    f_sukli = oh_sukli % 50

    bente = f_sukli // 20
    b_sukli = f_sukli % 20

    ten = b_sukli // 10
    t_sukli = b_sukli % 10

    five = t_sukli // 5
    lima = t_sukli % 5

    piso = lima // 1

    print(f"{one_thousand} = 1000")
    print(f"{five_h} = 500")
    print(f"{two_h} = 200")
    print(f"{one_h} = 100")
    print(f"{fifty} = 50")
    print(f"{bente} = 20")
    print(f"{ten} = 10")
    print(f"{five} = 5")
    print(f"{piso} = 1")

name = input("Please enter your name: ")
amount = input("Please enter the amount you want to deposit: ")

