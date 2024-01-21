import pandas as pd
'''
CREATE SQL TABLE OF ALL THIS CRAB FOR database
financial_metrics = [
    "period End", DATE might have to reformat
    "Outstand Sh", bal_sheet[1]
    "Revenues", income_stmt[45]
    "Revs Avg3", average of current and previous two revs (total of 3) minimum window = 1
    "Turnover Avg3", probably should add column for turnover without average but Turnover = $net revenue income_stmt[45] - income_stmt[44]/ $total assets bal_sheet[40] | average of current and previous two turnovers (total of 3) minimum window = 1
    "Gross Inc / TO", If Turnover>1 Gross profit [43] / Turnover if Turnover<1 Gross profit * Turnover
    "cfEBIT adj / TO", CFEBITDA = Cash Flow cash_flow[0]+ Taxes cash_flow[46] + Interest Expense income_stmt[11]+ Depreciation & Amortization cash_flow[49] / Turnover
    "ROIC Avg3", ROIC = NOPAT / Invested Capital | NOPAT=Net operating profit after tax || average of current and previous two ROIC (total of 3) minimum window = 1
    "CROSIC Abg3", #UNKNOWN I really dont remember man
    "Revs /sh", Revenues divided by shares income_stmt[45] / bal_sheet[1]
    "Assets", bal_sheet[40]
    "Assets /sh", Assets divided by shares bal_sheet[40] / bal_sheet[1]
    "Net Excess Cash", Excess Cash = Cash & Equivalents bal_sheet[70] + Long-Term Investments bal_sheet[44] - Current Liabilities bal_sheet[28]
    "Net Common Overhang", Net Common Overhang = LT liabilities bal_sheet[19] + ST debt bal_sheet[32] - Excess Cash & ST Investments bal_sheet[69]
    "Book /sh", Book Value per Share = (total assets bal_sheet[40] - its total liabilities bal_sheet[18]) / Outstanding shares bal_sheet[1]
    "Tang Book /sh", equal to total assets bal_sheet[40] - total liabilities bal_sheet[18] - Intangibles bal_sheet[46]  / Outstanding shares bal_sheet[1]
    "ROE", = Net Profit * Turnover * Financial Leverage
    "bm roe", = roe * book to market
    "bm ROE 3yr%", average of current and previous two bm roe (total of 3) minimum window = 1
    "bm ROE 5yr%", average of current and previous 4 bm roe (total of 5) minimum window = 1
    "tbm roe", = roe * tangible book to market
    "tbm ROE 3yr%", average of current and previous two tbm roe (total of 3) minimum window = 1
    "tbm ROE 5yr%", average of current and previous 4 tbm roe (total of 5) minimum window = 1
    "Div /sh", = Dividends paid / outstanding shares
    "bm EPS Avg3yr", #UNKNOWN
    "Ebitda /sh", = EBITDA = Net Income + Taxes + Interest Expense + Depreciation & Amortization) / outstanding shares
    "Ebitda avg3 ;sh", average of current and previous two EBITDA / sh (total of 3) minimum window = 1
    "Ebitda avg7 /sh", average of current and previous 6 EBITDA / sh (total of 7) minimum window = 1
    "Common EPS", = "NetIncomeFromContinuingOperationNetMinorityInterest" / outstanding shares
    "Net inc avg3 /sh", average of current and previous two Common EPS (total of 3) minimum window = 1
    "Net Inc avg7 /sh", average of current and previous 6 Common EPS (total of 7) minimum window = 1
    "Discount EPS", #UKNOWN
    "CFO /sh", = (Operating Cash Flow = Operating Income + Depreciation – Taxes + Change in Working Capital) / outstanding shares
        =((VLOOKUP("NetIncomeFromContinuingOperations", $BB$61:$CJ$176, 5, false)) 
        + IFNA((VLOOKUP("Depreciation", $BB$61:$CJ$176, 5, false)), 
        VLOOKUP("DepreciationAndAmortization", $BB$61:$CJ$176, 5, false)) 
        - IFNA(VLOOKUP("DeferredTax", $BB$61:$CJ$158, 5, false), 0) 
        + ((VLOOKUP("CurrentAssets", $A$60:$AD$185, 4, false)
        -VLOOKUP("CurrentLiabilities", $A$60:$AN$167, 4, false))
        -(VLOOKUP("CurrentAssets", $A$60:$AD$185, 5, false)
        -VLOOKUP("CurrentLiabilities", $A$60:$AN$167, 5, false))))
        /Y7



    "CFO Avg3 /sh", average of current and previous two CFO / sh (total of 3) minimum window = 1
    "CFO Avg7 /sh", average of current and previous SIX CFO / sh (total of 7) minimum window = 1
    "SFCF /sh", SFCF = net income + depreciation and amortization - capital expenditures = 
        (VLOOKUP("NetIncomeFromContinuingOperationNetMinorityInterest", $DB$61:$ER$173, 5, false) 
        + VLOOKUP("DepreciationAndAmortization", $BB$61:$CJ$176, 5, false) 
        - VLOOKUP("CapitalExpenditure", $BB$61:$CJ$176, 5, false))/Y7
    "SFCF Avg3 /sh", average of current and previous two SFCF / sh (total of 3) minimum window = 1
    "SFCF abg7 /sh", average of current and previous six SFCF / sh (total of 7) minimum window = 1
    "Net ACGS /sh", UNKNOWN
    "NCF /sh", = Freecashflow / sharecount =(VLOOKUP("FreeCashFlow", $BB$61:$CJ$176, 5, false))/Y7
    "NCF avg3 /sh", average of current and previous two NCF / sh (total of 3) minimum window = 1
    "NCF Avg7 /sh", average of current and previous 6 NCF / sh (total of 7) minimum window = 1
    "FIn leverage", Financial Leverage = Average Assets / Average Equity (Common Stock Equity) =((VLOOKUP("TotalAssets", A60:AL155, 4, false) + VLOOKUP("TotalAssets", A60:AL155, 5, false))/2)
        /((VLOOKUP("CommonStockEquity", A60:AL155, 4, false) + VLOOKUP("CommonStockEquity", A60:AL155, 5, false))/2)
    "Net Profit Margin", = Net Income / Revenue  =VLOOKUP("NetIncome", DB61:EN121, 5, false)/Y8
    "ROIC"
        ROIC = NOPAT / Invested Capital

        NOPAT= Net operating profit after tax = (operating profit) x (1 – effective tax rate)
        ​
        effective tax rate is  divide the income tax expense by the earnings (or income earned) before taxes.

        invested capital is to obtain the working capital figure by subtracting current liabilities from current assets. 
        Next, you obtain non-cash working capital by subtracting cash from the working capital value you just calculated. 
        Finally, non-cash working capital is added to a company's fixed assets.

        =((1 - (VLOOKUP("TaxProvision", $DB$61:$ER$173, 5, false)
        /VLOOKUP("PreTaxIncome", $DB$61:$ER$173, 5, false)))
        *VLOOKUP("NetIncomeFromContinuingOperationNetMinorityInterest", $DB$61:$EQ$178, 5, false))
        /((Y16-VLOOKUP("CurrentLiabilities", $A$60:$AN$167, 4, false))
        -VLOOKUP("CashAndCashEquivalents", $A$60:$AN$167, 4, false) 
        + VLOOKUP("NetPPE", $A$60:$AN$167, 4, false))
    Turnover = Revs / average assets (this year + last /2) = =(AA8/((VLOOKUP("TotalAssets", A60:AL157, 2, false)+VLOOKUP("TotalAssets", A60:AL157, 3,  false))/2))
    Book value = Total Assets - TotalLiabilitiesNetMinorityInterest =(AA16-VLOOKUP("TotalLiabilitiesNetMinorityInterest", A60:AL149, 2, FALSE))
    Book to market = =AF7/$AE$6
    Tangible book value = =AF7-VLOOKUP("GoodwillAndOtherIntangibleAssets", A60:AL149, 2, FALSE)
    Tangible book to market = =AH7/$AE$6
    af7 = book value
    ]

'''
'''

msft.income_stmt
msft.balance_sheet
msft.cashflow
'''
import yfinance as yf
msft = yf.Ticker("MSFT")
#print(msft.balance_sheet.iloc[0]) #shares
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(msft.cashflow)