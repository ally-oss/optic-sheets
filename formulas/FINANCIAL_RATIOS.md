# Financial Ratios - Google Sheets Formulas

> Extracted and vetted from FinanceToolkit (MIT License)
> Pure formulas only - no external code, no APIs, no risk

---

## Profitability Ratios

| Ratio | Formula | Google Sheets |
|-------|---------|---------------|
| **Gross Margin** | (Revenue - COGS) / Revenue | `=(B2-B3)/B2` |
| **Operating Margin** | Operating Income / Revenue | `=B4/B2` |
| **Net Profit Margin** | Net Income / Revenue | `=B5/B2` |
| **ROE** | Net Income / Shareholders Equity | `=B5/B10` |
| **ROA** | Net Income / Total Assets | `=B5/B8` |
| **ROIC** | NOPAT / Invested Capital | `=(B4*(1-TaxRate))/(B8-CurrentLiabilities)` |
| **Interest Coverage** | Operating Income / Interest Expense | `=B4/B6` |

## Liquidity Ratios

| Ratio | Formula | Google Sheets |
|-------|---------|---------------|
| **Current Ratio** | Current Assets / Current Liabilities | `=B11/B12` |
| **Quick Ratio** | (Current Assets - Inventory) / Current Liabilities | `=(B11-B13)/B12` |
| **Cash Ratio** | Cash / Current Liabilities | `=B14/B12` |
| **Working Capital** | Current Assets - Current Liabilities | `=B11-B12` |

## Solvency Ratios

| Ratio | Formula | Google Sheets |
|-------|---------|---------------|
| **Debt to Equity** | Total Debt / Shareholders Equity | `=B15/B10` |
| **Debt to Assets** | Total Debt / Total Assets | `=B15/B8` |
| **Equity Ratio** | Shareholders Equity / Total Assets | `=B10/B8` |
| **Debt to EBITDA** | Total Debt / EBITDA | `=B15/B16` |

## Valuation Ratios

| Ratio | Formula | Google Sheets |
|-------|---------|---------------|
| **EPS** | (Net Income - Preferred Div) / Shares Outstanding | `=(B5-B17)/B18` |
| **P/E Ratio** | Stock Price / EPS | `=B19/B20` |
| **PEG Ratio** | P/E / Earnings Growth Rate | `=B21/B22` |
| **P/B Ratio** | Stock Price / Book Value Per Share | `=B19/(B10/B18)` |
| **P/S Ratio** | Market Cap / Revenue | `=(B19*B18)/B2` |
| **EV/EBITDA** | Enterprise Value / EBITDA | `=B23/B16` |
| **Dividend Yield** | Annual Dividend / Stock Price | `=B24/B19` |

## Efficiency Ratios

| Ratio | Formula | Google Sheets |
|-------|---------|---------------|
| **Asset Turnover** | Revenue / Total Assets | `=B2/B8` |
| **Inventory Turnover** | COGS / Average Inventory | `=B3/AVERAGE(B13,C13)` |
| **Receivables Turnover** | Revenue / Average Receivables | `=B2/AVERAGE(B25,C25)` |
| **Days Sales Outstanding** | 365 / Receivables Turnover | `=365/(B2/B25)` |
| **Days Inventory** | 365 / Inventory Turnover | `=365/(B3/B13)` |

---

## GOOGLEFINANCE Quick Reference

```
=GOOGLEFINANCE("AAPL", "price")           Current price
=GOOGLEFINANCE("AAPL", "priceopen")       Opening price
=GOOGLEFINANCE("AAPL", "high")            Day high
=GOOGLEFINANCE("AAPL", "low")             Day low
=GOOGLEFINANCE("AAPL", "volume")          Volume
=GOOGLEFINANCE("AAPL", "marketcap")       Market cap
=GOOGLEFINANCE("AAPL", "pe")              P/E ratio
=GOOGLEFINANCE("AAPL", "eps")             Earnings per share
=GOOGLEFINANCE("AAPL", "shares")          Shares outstanding
=GOOGLEFINANCE("AAPL", "beta")            Beta
=GOOGLEFINANCE("AAPL", "high52")          52-week high
=GOOGLEFINANCE("AAPL", "low52")           52-week low
=GOOGLEFINANCE("AAPL", "changepct")       % change today
=GOOGLEFINANCE("AAPL", "closeyest")       Yesterday close
=GOOGLEFINANCE("AAPL", "tradetime")       Last trade time

// Historical data
=GOOGLEFINANCE("AAPL", "price", DATE(2024,1,1), DATE(2024,12,31), "DAILY")

// Currency
=GOOGLEFINANCE("CURRENCY:USDEUR")
```

---

## Portfolio Formulas

| Metric | Formula |
|--------|---------|
| **Position Value** | `=Shares * Price` |
| **Total Cost Basis** | `=Shares * Avg Cost` |
| **Unrealized P&L** | `=Position Value - Cost Basis` |
| **P&L %** | `=(Current - Cost) / Cost` |
| **Portfolio Weight** | `=Position Value / Total Portfolio` |
| **Weighted Return** | `=SUMPRODUCT(Weights, Returns)` |
| **XIRR** | `=XIRR(CashFlows, Dates)` |
| **CAGR** | `=(EndValue/StartValue)^(1/Years)-1` |

---

## Options Formulas

| Metric | Formula |
|--------|---------|
| **Intrinsic Value (Call)** | `=MAX(0, Stock - Strike)` |
| **Intrinsic Value (Put)** | `=MAX(0, Strike - Stock)` |
| **Time Value** | `=Option Price - Intrinsic Value` |
| **Breakeven (Call)** | `=Strike + Premium` |
| **Breakeven (Put)** | `=Strike - Premium` |
| **Max Profit (Long Call)** | Unlimited |
| **Max Loss (Long Call)** | `=Premium Paid` |
| **Return if Exercised** | `=(Stock - Strike - Premium) / Premium` |

---

*Source: Vetted extraction from JerBouma/FinanceToolkit (MIT License)*
*No external API calls - pure math only*
