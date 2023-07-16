import math
import argparse
import logging

balance = 0
transactions = []

# Настройки логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='banking_system.log',
                    filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def deposit(amount):
    global balance
    global transactions
    if amount % 50 != 0:
        logging.error("Сумма должна быть кратна 50")
        return
    balance += amount
    transactions.append(("Пополнение", amount))
    if len(transactions) % 3 == 0:
        interest = balance * 0.03
        balance += interest
        transactions.append(("Проценты", interest))
    logging.info(f"Пополнение успешно. Баланс: {balance}")

def withdraw(amount):
    global balance
    global transactions
    if amount % 50 != 0:
        logging.error("Сумма должна быть кратна 50")
        return
    if amount > balance:
        logging.error("Недостаточно средств на счете")
        return
    if balance >= 5000000:
        tax = balance * 0.1
        balance -= tax
        transactions.append(("Налог на богатство", tax))
    fee = max(amount * 0.015, 30)
    fee = min(fee, 600)
    balance -= amount + fee
    transactions.append(("Снятие", amount))
    if len(transactions) % 3 == 0:
        interest = balance * 0.03
        balance += interest
        transactions.append(("Проценты", interest))
    logging.info(f"Снятие успешно. Баланс: {balance}")

def print_balance():
    global balance
    logging.info(f"Текущий баланс: {balance}")

def print_transactions():
    global transactions
    for transaction in transactions:
        logging.info(f"{transaction[0]}: {transaction[1]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Banking System")
    parser.add_argument("--amount", type=int, help="Amount for deposit or withdrawal")
    parser.add_argument("--action", choices=["deposit", "withdraw", "print_balance", "print_transactions"],
                        help="Action to perform")
    args = parser.parse_args()

    if args.action == "deposit":
        if args.amount is None:
            logging.error("Для операции 'пополнить' необходимо указать сумму (--amount)")
        else:
            deposit(args.amount)
    elif args.action == "withdraw":
        if args.amount is None:
            logging.error("Для операции 'снять' необходимо указать сумму (--amount)")
        else:
            withdraw(args.amount)
    elif args.action == "print_balance":
        print_balance()
    elif args.action == "print_transactions":
        print_transactions()
    else:
        logging.error("Неверная команда")


# Теперь можно запустить программу из командной строки с использованием аргументов для
# указания действия и суммы. Например:

# Для пополнения на 1000: python banking_system.py --action deposit --amount 1000
# Для снятия 500: python banking_system.py --action withdraw --amount 500
# Для вывода текущего баланса: python banking_system.py --action print_balance
# Для вывода списка транзакций: python banking_system.py --action print_transactions