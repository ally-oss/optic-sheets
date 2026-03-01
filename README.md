# Optic Sheets

> Clean, secure financial spreadsheet toolkit for Google Sheets
> No third-party code, no APIs, no add-ons - just pure formulas

## Security Principles

- ✅ **No external code** - Only native Google Sheets formulas
- ✅ **No Apps Script** - Unless explicitly reviewed and approved
- ✅ **No add-ons** - They have full data access
- ✅ **No API keys in sheets** - Credentials stored separately
- ✅ **Audit trail** - All formulas documented and sourced

## Structure

```
optic-sheets/
├── formulas/
│   └── FINANCIAL_RATIOS.md    # All vetted formulas
├── templates/
│   ├── portfolio_dashboard/   # Holdings + P&L tracking
│   ├── trade_journal/         # Entry/exit logging
│   └── company_financials/    # P&L, Balance Sheet, Cash Flow
└── scripts/
    └── (future: vetted Apps Script if needed)
```

## Formula Sources

All formulas extracted and vetted from:
- **FinanceToolkit** (MIT License) - github.com/JerBouma/FinanceToolkit
- Pure mathematical definitions only
- No runtime dependencies

## Usage

1. Copy formulas from `formulas/FINANCIAL_RATIOS.md`
2. Use templates as starting points
3. All GOOGLEFINANCE calls are native Google functions

## License

MIT - formulas are mathematical facts, templates are original work.
