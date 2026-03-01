# Google Sheets Design Guide

> Principles for clean, readable, professional spreadsheets

---

## 1. Color Palette (Keep it minimal)

| Use | Color | Hex |
|-----|-------|-----|
| Headers | Dark blue/gray | `#1a1a2e` or `#2d3436` |
| Positive values | Green | `#00b894` |
| Negative values | Red | `#d63031` |
| Alternating rows | Light gray | `#f5f6fa` |
| Highlights/Totals | Light blue | `#74b9ff` |
| Background | White | `#ffffff` |

**Rule:** Max 3-4 colors per sheet. Less is more.

---

## 2. Typography

| Element | Style |
|---------|-------|
| Headers | **Bold**, slightly larger (11-12pt) |
| Data | Regular, 10pt |
| Titles | **Bold**, 14pt |
| Numbers | Right-aligned |
| Text | Left-aligned |
| Dates | Center-aligned |

**Font choices:**
- Clean: `Inter`, `Roboto`, `Arial`
- Finance-y: `IBM Plex Sans`, `Helvetica`
- Avoid: Comic Sans, decorative fonts

---

## 3. Layout Principles

### Spacing
```
┌─────────────────────────────────────────┐
│  [Title]                    [Date]      │  ← Row 1: Title section
│                                         │  ← Row 2: Empty spacer
│  Header │ Header │ Header │ Header      │  ← Row 3: Column headers
│─────────┼────────┼────────┼─────────    │
│  Data   │ Data   │ Data   │ Data        │  ← Data rows
│  Data   │ Data   │ Data   │ Data        │
│                                         │  ← Empty spacer before totals
│  TOTAL  │        │        │ $X,XXX      │  ← Summary row (highlighted)
└─────────────────────────────────────────┘
```

### Column Widths
- **Ticker/Symbol:** 60-80px
- **Numbers:** 80-100px
- **Currency:** 100-120px
- **Descriptions:** 150-250px
- **Dates:** 90-100px

### Freeze Panes
- Always freeze header row: `View → Freeze → 1 row`
- Freeze ticker column if scrolling: `View → Freeze → 1 column`

---

## 4. Conditional Formatting

### P&L Colors
```
Green if > 0:  Custom formula: =G2>0  → Background #d4edda
Red if < 0:    Custom formula: =G2<0  → Background #f8d7da
```

### Heat Maps (for allocation)
```
Color scale: White → Green
Min: 0%
Max: 25% (or max weight)
```

### Status Indicators
```
🟢 Good    =IF(A1>0,"🟢","🔴")
🟡 Warning
🔴 Bad
```

---

## 5. Number Formatting

| Type | Format | Example |
|------|--------|---------|
| Currency | `$#,##0.00` | $1,234.56 |
| Percentage | `0.00%` | 12.34% |
| Shares | `#,##0` | 1,234 |
| Large numbers | `$#,##0.0,,"M"` | $1.2M |
| Negative in red | `$#,##0.00;[Red]($#,##0.00)` | ($1,234.56) |

---

## 6. Dashboard Layout

### The "F-Pattern"
Users scan in an F shape - put important stuff top-left:

```
┌────────────────────────────────────────────────┐
│ PORTFOLIO VALUE    $1,234,567    [+2.3%]       │  ← Key metric, top-left
├────────────────────────────────────────────────┤
│                                                │
│  [Holdings Table]              [Allocation     │
│   - Most important             Pie Chart]      │
│   - Full width or 2/3                          │
│                                                │
├────────────────────────────────────────────────┤
│  [Performance Chart]    [Recent Trades]        │  ← Secondary info bottom
└────────────────────────────────────────────────┘
```

### Card Pattern
Group related metrics in "cards":

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Total Value │  │ Day P&L     │  │ Total P&L   │
│ $1,234,567  │  │ +$12,345    │  │ +$234,567   │
│             │  │ +0.98%      │  │ +23.4%      │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## 7. Pro Tips

### Borders
- Use sparingly - white space is better than boxes
- If needed: light gray `#e0e0e0`, thin lines only
- Bold bottom border under headers

### Alignment
- Numbers: RIGHT (always)
- Text: LEFT
- Headers: Match data below
- Currency: RIGHT with consistent decimals

### Grouping
- Use `Data → Group rows/columns` to hide detail
- Keeps sheet clean, expandable when needed

### Named Ranges
- Name key cells: `Settings!B2` → `TaxRate`
- Use in formulas: `=A2*(1-TaxRate)`
- Easier to read and maintain

### Sparklines
```
=SPARKLINE(A1:A30, {"charttype","line"; "color","#00b894"})
```
Mini charts in cells - great for trends without taking space.

---

## 8. Template Structure

### Sheet Order
1. **Dashboard** - Summary view, KPIs
2. **Holdings** - Current positions
3. **Transactions** - Trade log
4. **Settings** - Config, tax rates, etc.
5. **Data** - Raw data (hide if needed)

### Naming
- Clear sheet names: "Dashboard", not "Sheet1"
- No spaces in named ranges: `TotalValue`, not `Total Value`

---

## 9. Don't Do This ❌

- Rainbow colors
- Merged cells (breaks sorting/filtering)
- Tiny fonts (<9pt)
- All caps everywhere
- Borders on every cell
- Multiple fonts
- Center-aligned numbers
- Hidden data people need

---

## 10. Quick Wins

1. **Freeze top row** - Always
2. **Alternate row colors** - Format → Alternating colors
3. **Auto-resize columns** - Double-click column border
4. **Conditional P&L colors** - Green/red based on value
5. **Add a dashboard tab** - Summary of everything

---

*Good design = less cognitive load = better decisions*
