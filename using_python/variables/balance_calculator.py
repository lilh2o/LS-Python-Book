def balance_calc(balance, years):
    for i in range(years):
        balance = 1.05 * balance
    return balance

balance = balance_calc(1000, 5)
print(f'${balance}')

balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05

print(f'augmented ${balance}')