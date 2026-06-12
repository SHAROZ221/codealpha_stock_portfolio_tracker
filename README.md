# Stock Portfolio Tracker
> CodeAlpha Python Programming Internship | Task 2

---

## 📌 Goal
A stock tracker that calculates total investment value, current value, and **profit/loss** based on manually defined stock prices.

---

## 📁 Project Files

| File | Purpose |
|---|---|
| `main.py` | Main script — stock tracker with menu |
| `portfolio_<timestamp>.csv` | Auto-generated output file with portfolio summary |

---

## ▶️ How to Run

No external libraries needed. Uses only built-in Python modules.

```
python main.py
```

---

## 🎮 How to Use

```
==================================================
  Stock Portfolio Tracker
==================================================

  1. Add stock
  2. View portfolio (with profit/loss)
  3. Remove/sell stock
  4. Save portfolio to CSV
  5. Exit
```

1. **Add stock** — enter symbol, quantity, and your buy price (or press Enter to use the current market price). Adding more shares of an existing stock automatically calculates a weighted average buy price.
2. **View portfolio** — shows quantity, buy price, current price, invested amount, current value, and profit/loss (in $ and %) for each stock, plus an overall total.
3. **Remove/sell stock** — sell part or all of your shares of a stock.
4. **Save portfolio to CSV** — exports the full breakdown including profit/loss to a `.csv` file.
5. **Exit** — quit the program.

---

## 📈 Available Stocks (Current Market Price)

| Symbol | Price ($) |
|---|---|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 380 |
| AMZN | 185 |
| META | 490 |
| NFLX | 620 |
| NVDA | 875 |
| AMD | 165 |
| INTC | 35 |

---

## 🔍 Sample Output

```
  ================================================================================
  PORTFOLIO SUMMARY
  ================================================================================
  Symbol     Qty      Buy $      Cur $     Invested        Value          P/L    P/L %
  --------------------------------------------------------------------------------
  AAPL         5     170.00     180.00       850.00       900.00 +      50.00 +   5.88%
  TSLA         5     250.00     250.00     1,250.00     1,250.00 +       0.00 +   0.00%
  --------------------------------------------------------------------------------
  TOTAL                                    2,100.00     2,150.00 +      50.00 +   2.38%
  ================================================================================
  [+] Overall: You're up $50.00 (2.38%)
```

---

## 💡 Key Concepts Used

- `dictionary` — hardcoded current stock prices
- `input/output` — user enters stock symbol, quantity, and buy price
- `basic arithmetic` — invested amount, current value, profit/loss calculations
- `file handling` — saves portfolio summary (with P/L) to `.csv` file

---

## 🚀 Extra Features Added Beyond the Original Brief

- **Profit/Loss tracking** — compares your buy price against current market price to show gains/losses per stock and overall, in both dollar amount and percentage.
- **Weighted average buy price** — adding more shares of a stock you already own recalculates your average cost basis automatically.
- **Sell/remove option** — sell part or all of a holding directly from the menu.
- **Detailed CSV export** — saved file includes buy price, current price, invested amount, value, and P/L columns.