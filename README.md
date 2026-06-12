# Stock Portfolio Tracker
> CodeAlpha Python Programming Internship | Task 2

---

## 📌 Goal
A simple stock tracker that calculates total investment value based on manually defined stock prices.

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
  2. View portfolio
  3. Save portfolio to CSV
  4. Exit
```

1. Choose option 1 to add a stock — enter symbol and quantity
2. Choose option 2 to view your full portfolio with total investment
3. Choose option 3 to save results to a `.csv` file
4. Choose option 4 to exit

---

## 📈 Available Stocks

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
  ==================================================
  PORTFOLIO SUMMARY
  ==================================================
  Symbol       Price    Qty        Value
  --------------------------------------------------
  AAPL          $180     10        $1,800
  TSLA          $250      5        $1,250
  NVDA          $875      2        $1,750
  --------------------------------------------------
  TOTAL INVESTMENT               $4,800
  ==================================================
```

---

## 💡 Key Concepts Used

- `dictionary` — hardcoded stock prices
- `input/output` — user enters stock symbol and quantity
- `basic arithmetic` — price × quantity = total value
- `file handling` — saves portfolio to `.csv` file