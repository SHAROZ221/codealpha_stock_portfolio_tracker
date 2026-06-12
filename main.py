
import csv
from datetime import datetime

# HARDCODED STOCK PRICES 
STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "MSFT":  380,
    "AMZN":  185,
    "META":  490,
    "NFLX":  620,
    "NVDA":  875,
    "AMD":   165,
    "INTC":   35,
}

# PORTFOLIO 
portfolio = {}  # { "AAPL": quantity }


def show_available_stocks():
    print("\n  Available Stocks:")
    print("  " + "-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price}")
    print("  " + "-" * 30)


def add_stock():
    show_available_stocks()
    symbol = input("\n  Enter stock symbol: ").strip().upper()

    if symbol not in STOCK_PRICES:
        print(f"  [!] '{symbol}' not found. Choose from the list above.")
        return

    try:
        qty = int(input(f"  Enter quantity for {symbol}: ").strip())
        if qty <= 0:
            print("  [!] Quantity must be greater than 0.")
            return
    except ValueError:
        print("  [!] Invalid quantity. Enter a number.")
        return

    if symbol in portfolio:
        portfolio[symbol] += qty
        print(f"  [+] Added {qty} more shares of {symbol}. Total: {portfolio[symbol]}")
    else:
        portfolio[symbol] = qty
        print(f"  [+] {symbol} x{qty} added to portfolio.")


def view_portfolio():
    if not portfolio:
        print("\n  [!] Portfolio is empty. Add stocks first.")
        return

    print("\n  " + "=" * 50)
    print("  PORTFOLIO SUMMARY")
    print("  " + "=" * 50)
    print(f"  {'Symbol':<10} {'Price':>10} {'Qty':>6} {'Value':>12}")
    print("  " + "-" * 50)

    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<10} ${price:>9} {qty:>6} ${value:>11,}")

    print("  " + "-" * 50)
    print(f"  {'TOTAL INVESTMENT':<28} ${total:>11,}")
    print("  " + "=" * 50)


def save_portfolio():
    if not portfolio:
        print("\n  [!] Portfolio is empty. Nothing to save.")
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Price ($)", "Quantity", "Total Value ($)"])
        total = 0
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            total += value
            writer.writerow([symbol, price, qty, value])
        writer.writerow(["", "", "TOTAL", total])

    print(f"\n  [✓] Portfolio saved to: {filename}")


def main():
    print("=" * 50)
    print("  Stock Portfolio Tracker")
    print("=" * 50)

    while True:
        print("\n  1. Add stock")
        print("  2. View portfolio")
        print("  3. Save portfolio to CSV")
        print("  4. Exit")
        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            save_portfolio()
        elif choice == "4":
            print("\n  Goodbye!")
            break
        else:
            print("  [!] Invalid option. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
