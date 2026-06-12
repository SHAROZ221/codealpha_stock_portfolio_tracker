import csv
from datetime import datetime

# HARDCODED CURRENT MARKET PRICES
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
# { "AAPL": {"qty": 10, "buy_price": 170} }
portfolio = {}


def show_available_stocks():
    print("\n  Available Stocks (Current Market Price):")
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

    try:
        buy_price_input = input(
            f"  Enter your buy price for {symbol} (press Enter to use current price ${STOCK_PRICES[symbol]}): "
        ).strip()
        if buy_price_input == "":
            buy_price = STOCK_PRICES[symbol]
        else:
            buy_price = float(buy_price_input)
            if buy_price <= 0:
                print("  [!] Buy price must be greater than 0.")
                return
    except ValueError:
        print("  [!] Invalid price. Enter a number.")
        return

    if symbol in portfolio:
        existing = portfolio[symbol]
        total_qty = existing["qty"] + qty
        # Weighted average buy price
        total_cost = (existing["qty"] * existing["buy_price"]) + (qty * buy_price)
        avg_buy_price = total_cost / total_qty
        portfolio[symbol] = {"qty": total_qty, "buy_price": avg_buy_price}
        print(f"  [+] Added {qty} more shares of {symbol}. Total: {total_qty} (avg buy price: ${avg_buy_price:.2f})")
    else:
        portfolio[symbol] = {"qty": qty, "buy_price": buy_price}
        print(f"  [+] {symbol} x{qty} added to portfolio at buy price ${buy_price:.2f}.")


def remove_stock():
    if not portfolio:
        print("\n  [!] Portfolio is empty. Nothing to remove.")
        return

    symbol = input("\n  Enter stock symbol to remove/sell: ").strip().upper()
    if symbol not in portfolio:
        print(f"  [!] '{symbol}' not found in your portfolio.")
        return

    try:
        qty = int(input(f"  Enter quantity to sell (current: {portfolio[symbol]['qty']}): ").strip())
        if qty <= 0:
            print("  [!] Quantity must be greater than 0.")
            return
    except ValueError:
        print("  [!] Invalid quantity. Enter a number.")
        return

    current_qty = portfolio[symbol]["qty"]
    if qty > current_qty:
        print(f"  [!] You only have {current_qty} shares of {symbol}.")
        return

    if qty == current_qty:
        del portfolio[symbol]
        print(f"  [-] All shares of {symbol} removed from portfolio.")
    else:
        portfolio[symbol]["qty"] -= qty
        print(f"  [-] Sold {qty} shares of {symbol}. Remaining: {portfolio[symbol]['qty']}")


def view_portfolio():
    if not portfolio:
        print("\n  [!] Portfolio is empty. Add stocks first.")
        return

    print("\n  " + "=" * 80)
    print("  PORTFOLIO SUMMARY")
    print("  " + "=" * 80)
    print(f"  {'Symbol':<8} {'Qty':>5} {'Buy $':>10} {'Cur $':>10} {'Invested':>12} {'Value':>12} {'P/L':>12} {'P/L %':>8}")
    print("  " + "-" * 80)

    total_invested = 0
    total_value = 0

    for symbol, data in portfolio.items():
        qty = data["qty"]
        buy_price = data["buy_price"]
        current_price = STOCK_PRICES[symbol]

        invested = buy_price * qty
        value = current_price * qty
        pl = value - invested
        pl_pct = (pl / invested * 100) if invested != 0 else 0

        total_invested += invested
        total_value += value

        sign = "+" if pl >= 0 else ""
        print(f"  {symbol:<8} {qty:>5} {buy_price:>10.2f} {current_price:>10.2f} "
              f"{invested:>12,.2f} {value:>12,.2f} {sign}{pl:>11,.2f} {sign}{pl_pct:>7.2f}%")

    total_pl = total_value - total_invested
    total_pl_pct = (total_pl / total_invested * 100) if total_invested != 0 else 0
    sign = "+" if total_pl >= 0 else ""

    print("  " + "-" * 80)
    print(f"  {'TOTAL':<8} {'':>5} {'':>10} {'':>10} {total_invested:>12,.2f} {total_value:>12,.2f} "
          f"{sign}{total_pl:>11,.2f} {sign}{total_pl_pct:>7.2f}%")
    print("  " + "=" * 80)

    if total_pl > 0:
        print(f"  [+] Overall: You're up ${total_pl:,.2f} ({total_pl_pct:.2f}%)")
    elif total_pl < 0:
        print(f"  [-] Overall: You're down ${abs(total_pl):,.2f} ({abs(total_pl_pct):.2f}%)")
    else:
        print("  [=] Overall: Breakeven.")


def save_portfolio():
    if not portfolio:
        print("\n  [!] Portfolio is empty. Nothing to save.")
        return

    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Buy Price ($)", "Current Price ($)",
                          "Invested ($)", "Current Value ($)", "Profit/Loss ($)", "Profit/Loss (%)"])

        total_invested = 0
        total_value = 0

        for symbol, data in portfolio.items():
            qty = data["qty"]
            buy_price = data["buy_price"]
            current_price = STOCK_PRICES[symbol]
            invested = buy_price * qty
            value = current_price * qty
            pl = value - invested
            pl_pct = (pl / invested * 100) if invested != 0 else 0

            total_invested += invested
            total_value += value

            writer.writerow([symbol, qty, round(buy_price, 2), current_price,
                              round(invested, 2), round(value, 2), round(pl, 2), round(pl_pct, 2)])

        total_pl = total_value - total_invested
        total_pl_pct = (total_pl / total_invested * 100) if total_invested != 0 else 0
        writer.writerow(["", "", "", "TOTAL", round(total_invested, 2), round(total_value, 2),
                          round(total_pl, 2), round(total_pl_pct, 2)])

    print(f"\n  [✓] Portfolio saved to: {filename}")


def main():
    print("=" * 50)
    print("  Stock Portfolio Tracker")
    print("=" * 50)

    while True:
        print("\n  1. Add stock")
        print("  2. View portfolio (with profit/loss)")
        print("  3. Remove/sell stock")
        print("  4. Save portfolio to CSV")
        print("  5. Exit")
        choice = input("\n  Choose an option: ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            remove_stock()
        elif choice == "4":
            save_portfolio()
        elif choice == "5":
            print("\n  Goodbye!")
            break
        else:
            print("  [!] Invalid option. Enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()