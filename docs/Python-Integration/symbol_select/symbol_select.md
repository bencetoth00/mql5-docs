# symbol_select

symbol\_select

Select a symbol in the [MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch) window or remove a symbol from the window.

|  |
| --- |
| symbol\_select(     symbol,      // financial instrument name     enable=None  // enable or disable  ) |

symbol

[in]  Financial instrument name. Required unnamed parameter.

enable

[in]  Switch. Optional unnamed parameter. If 'false', a symbol should be removed from the MarketWatch window. Otherwise, it should be selected in the MarketWatch window. A symbol cannot be removed if open charts with this symbol are currently present or positions are opened on it.

Return Value

True if successful, otherwise – False.

Note

The function is similar to [SymbolSelect](../../Market-Info/SymbolSelect/SymbolSelect.md).

Example:

|  |
| --- |
| import MetaTrader5 as mt5  import pandas as pd  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)  print()  # establish connection to the MetaTrader 5 terminal  if not mt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):      print("initialize() failed, error code =",mt5.last\_error())      quit()     # attempt to enable the display of the EURCAD in MarketWatch  selected=mt5.symbol\_select("EURCAD",True)  if not selected:      print("Failed to select EURCAD, error code =",mt5.last\_error())  else:      symbol\_info=mt5.symbol\_info("EURCAD")      print(symbol\_info)      print("EURCAD: currency\_base =",symbol\_info.currency\_base,"  currency\_profit =",symbol\_info.currency\_profit,"  currency\_margin =",symbol\_info.currency\_margin)      print()         # get symbol properties in the form of a dictionary      print("Show symbol\_info().\_asdict():")      symbol\_info\_dict = symbol\_info.\_asdict()      for prop in symbol\_info\_dict:          print("  {}={}".format(prop, symbol\_info\_dict[prop]))      print()         # convert the dictionary into DataFrame and print      df=pd.DataFrame(list(symbol\_info\_dict.items()),columns=['property','value'])      print("symbol\_info\_dict() as dataframe:")      print(df)     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  SymbolInfo(custom=False, chart\_mode=0, select=True, visible=True, session\_deals=0, session\_buy\_orders=0, session\_sell\_orders=0, volume=0, volumehigh=0, ....  EURCAD: currency\_base = EUR   currency\_profit = CAD   currency\_margin = EUR     Show symbol\_info().\_asdict():    custom=False    chart\_mode=0    select=True    visible=True    session\_deals=0    session\_buy\_orders=0    session\_sell\_orders=0    volume=0    volumehigh=0    volumelow=0    time=1585217595    digits=5    spread=39    spread\_float=True    ticks\_bookdepth=10    trade\_calc\_mode=0    trade\_mode=4    start\_time=0    expiration\_time=0    trade\_stops\_level=0    trade\_freeze\_level=0    trade\_exemode=1    swap\_mode=1    swap\_rollover3days=3    margin\_hedged\_use\_leg=False    expiration\_mode=7    filling\_mode=1    order\_mode=127    order\_gtc\_mode=0    option\_mode=0    option\_right=0    bid=1.55192    bidhigh=1.55842    bidlow=1.5419800000000001    ask=1.5523099999999999    askhigh=1.55915    asklow=1.5436299999999998    last=0.0    lasthigh=0.0    lastlow=0.0    volume\_real=0.0    volumehigh\_real=0.0    volumelow\_real=0.0    option\_strike=0.0    point=1e-05    trade\_tick\_value=0.7043642408362214    trade\_tick\_value\_profit=0.7043642408362214    trade\_tick\_value\_loss=0.7044535553770941    trade\_tick\_size=1e-05    trade\_contract\_size=100000.0    trade\_accrued\_interest=0.0    trade\_face\_value=0.0    trade\_liquidity\_rate=0.0    volume\_min=0.01    volume\_max=500.0    volume\_step=0.01    volume\_limit=0.0    swap\_long=-1.1    swap\_short=-0.9    margin\_initial=0.0    margin\_maintenance=0.0    session\_volume=0.0    session\_turnover=0.0    session\_interest=0.0    session\_buy\_orders\_volume=0.0    session\_sell\_orders\_volume=0.0    session\_open=0.0    session\_close=0.0    session\_aw=0.0    session\_price\_settlement=0.0    session\_price\_limit\_min=0.0    session\_price\_limit\_max=0.0    margin\_hedged=100000.0    price\_change=0.0    price\_volatility=0.0    price\_theoretical=0.0    price\_greeks\_delta=0.0    price\_greeks\_theta=0.0    price\_greeks\_gamma=0.0    price\_greeks\_vega=0.0    price\_greeks\_rho=0.0    price\_greeks\_omega=0.0    price\_sensitivity=0.0    basis=    category=    currency\_base=EUR    currency\_profit=CAD    currency\_margin=EUR    bank=    description=Euro vs Canadian Dollar    exchange=    formula=    isin=    name=EURCAD    page=http://www.google.com/finance?q=EURCAD    path=Forex\EURCAD     symbol\_info\_dict() as dataframe:           property                                   value  0          custom                                   False  1      chart\_mode                                       0  2          select                                    True  3         visible                                    True  4   session\_deals                                       0  ..            ...                                     ...  91        formula                                          92           isin                                          93           name                                  EURCAD  94           page  http://www.google.com/finance?q=EURCAD  95           path                            Forex\EURCAD     [96 rows x 2 columns] |

See also

[symbol\_info](../symbol_info/symbol_info.md)
