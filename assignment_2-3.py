money=int(input("Input amount of money: "))
apple=int(input("Input price of apple: "))

amount1=money//apple
amount2=money%apple

print(f"You can buy: {amount1} amount of apples")
print(f"Your change is: {amount2}")

