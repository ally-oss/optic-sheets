#!/usr/bin/env python3
"""
Create Portfolio Dashboard in Google Sheets
Uses only native GOOGLEFINANCE formulas - no external APIs
"""

import gspread
from google.oauth2.credentials import Credentials
import json
from pathlib import Path

CREDS_DIR = Path(__file__).parent.parent.parent / "credentials"

def get_client():
    """Get authenticated gspread client"""
    with open(CREDS_DIR / "google_tokens.json") as f:
        tokens = json.load(f)
    with open(CREDS_DIR / "google_oauth_client.json") as f:
        client_config = json.load(f)["installed"]
    
    creds = Credentials(
        token=tokens["access_token"],
        refresh_token=tokens["refresh_token"],
        token_uri=client_config["token_uri"],
        client_id=client_config["client_id"],
        client_secret=client_config["client_secret"],
        scopes=["https://www.googleapis.com/auth/spreadsheets", 
                "https://www.googleapis.com/auth/drive"]
    )
    return gspread.authorize(creds)


def create_portfolio_dashboard(name="Portfolio Dashboard"):
    """Create a portfolio tracking spreadsheet"""
    gc = get_client()
    
    # Create spreadsheet
    sh = gc.create(name)
    ws = sh.sheet1
    ws.update_title("Holdings")
    
    # Headers
    headers = [
        "Ticker", "Shares", "Avg Cost", "Cost Basis",
        "Price", "Market Value", "P&L $", "P&L %", 
        "Day Change %", "Weight %"
    ]
    ws.update('A1:J1', [headers])
    
    # Example row with formulas (row 2)
    ws.update('A2', "AAPL")
    ws.update('B2', "100")
    ws.update('C2', "150.00")
    
    # Formula columns
    formulas = [
        ('D2', '=B2*C2'),                                    # Cost Basis
        ('E2', '=GOOGLEFINANCE(A2,"price")'),                # Price
        ('F2', '=B2*E2'),                                    # Market Value
        ('G2', '=F2-D2'),                                    # P&L $
        ('H2', '=G2/D2'),                                    # P&L %
        ('I2', '=GOOGLEFINANCE(A2,"changepct")/100'),        # Day Change
        ('J2', '=F2/SUM($F$2:$F$100)'),                      # Weight
    ]
    
    for cell, formula in formulas:
        ws.update(cell, formula, value_input_option='USER_ENTERED')
    
    # Format percentages
    ws.format('H2:J100', {'numberFormat': {'type': 'PERCENT', 'pattern': '0.00%'}})
    ws.format('D2:G100', {'numberFormat': {'type': 'CURRENCY', 'pattern': '$#,##0.00'}})
    
    # Summary section
    ws.update('L1:M1', [['Metric', 'Value']])
    ws.update('L2:L5', [['Total Cost'], ['Total Value'], ['Total P&L'], ['Total P&L %']])
    
    summary_formulas = [
        ('M2', '=SUM(D2:D100)'),
        ('M3', '=SUM(F2:F100)'),
        ('M4', '=M3-M2'),
        ('M5', '=M4/M2'),
    ]
    
    for cell, formula in summary_formulas:
        ws.update(cell, formula, value_input_option='USER_ENTERED')
    
    # Make link shareable
    sh.share('', perm_type='anyone', role='writer')
    
    return sh.url


if __name__ == "__main__":
    url = create_portfolio_dashboard()
    print(f"✅ Created: {url}")
