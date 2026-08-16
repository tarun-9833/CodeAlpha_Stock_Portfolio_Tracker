
# Stock Portfolio Tracker
# CodeAlpha - Python Programming Internship

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you have finished adding stocks.")

while True:
    stock = input("\nEnter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available. Please choose AAPL or TSLA.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity

        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        total_investment += investment

        print(f"✅ {stock}: {quantity} shares added.")
        print(f"Investment: ${investment:,.2f}")

    except ValueError:
        print("❌ Please enter a valid number.")

print("\n" + "=" * 45)
print("             PORTFOLIO SUMMARY")
print("=" * 45)

if portfolio:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity

        print(f"{stock}: {quantity} shares × ${price} = ${value:,.2f}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total_investment:,.2f}")
else:
    print("No stocks were added.")

print("=" * 45)
print("Thank you for using Stock Portfolio Tracker!")