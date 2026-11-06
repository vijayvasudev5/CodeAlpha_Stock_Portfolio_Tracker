
# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("================================")
print("       STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        print(f"{quantity} shares of {stock_name} added successfully!")

    except ValueError:
        print("Please enter a valid whole number.")

print("\n================================")
print("         YOUR PORTFOLIO")
print("================================")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} | Quantity: {quantity} | Price: ${price} | Total: ${investment}")

print("--------------------------------")
print(f"Total Investment: ${total_investment}")
print("================================")
print("Thank you for using Stock Tracker!")
