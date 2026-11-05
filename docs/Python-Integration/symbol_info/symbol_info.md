# symbol_info

symbol\_info

Get data on the specified financial instrument.

|  |
| --- |
| symbol\_info(     symbol      // financial instrument name  ) |

symbol

[in]  Financial instrument name. Required unnamed parameter.

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using [last\_error()](../last_error/last_error.md).

Note

The function returns all data that can be obtained using [SymbolInfoInteger](../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoDouble](../../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) and [SymbolInfoString](../../Market-Info/SymbolInfoString/SymbolInfoString.md) in one call.

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # attempt to enable the display of the EURJPY symbol in MarketWatch  selected=mt5.symbol\_select("EURJPY",True)  if not selected:      print("Failed to select EURJPY")      mt5.shutdown()      quit()     # display EURJPY symbol properties  symbol\_info=mt5.symbol\_info("EURJPY")  if symbol\_info!=None:      # display the terminal data 'as is'          print(symbol\_info)      print("EURJPY: spread =",symbol\_info.spread,"  digits =",symbol\_info.digits)      # display symbol properties as a list      print("Show symbol\_info(\"EURJPY\").\_asdict():")      symbol\_info\_dict = mt5.symbol\_info("EURJPY").\_asdict()      for prop in symbol\_info\_dict:          print("  {}={}".format(prop, symbol\_info\_dict[prop]))     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown()        Result:  MetaTrader5 package author:  MetaQuotes Software Corp.  MetaTrader5 package version:  5.0.29  SymbolInfo(custom=False, chart\_mode=0, select=True, visible=True, session\_deals=0, session\_buy\_orders=0, session\_sell\_orders=0, ...  EURJPY: spread = 17   digits = 3  Show symbol\_info().\_asdict():    custom=False    chart\_mode=0    select=True    visible=True    session\_deals=0    session\_buy\_orders=0    session\_sell\_orders=0    volume=0    volumehigh=0    volumelow=0    time=1585069682    digits=3    spread=17    spread\_float=True    ticks\_bookdepth=10    trade\_calc\_mode=0    trade\_mode=4    start\_time=0    expiration\_time=0    trade\_stops\_level=0    trade\_freeze\_level=0    trade\_exemode=1    swap\_mode=1    swap\_rollover3days=3    margin\_hedged\_use\_leg=False    expiration\_mode=7    filling\_mode=1    order\_mode=127    order\_gtc\_mode=0    option\_mode=0    option\_right=0    bid=120.024    bidhigh=120.506    bidlow=118.798    ask=120.041    askhigh=120.526    asklow=118.828    last=0.0    lasthigh=0.0    lastlow=0.0    volume\_real=0.0    volumehigh\_real=0.0    volumelow\_real=0.0    option\_strike=0.0    point=0.001    trade\_tick\_value=0.8977708350166538    trade\_tick\_value\_profit=0.8977708350166538    trade\_tick\_value\_loss=0.8978272580355541    trade\_tick\_size=0.001    trade\_contract\_size=100000.0    trade\_accrued\_interest=0.0    trade\_face\_value=0.0    trade\_liquidity\_rate=0.0    volume\_min=0.01    volume\_max=500.0    volume\_step=0.01    volume\_limit=0.0    swap\_long=-0.2    swap\_short=-1.2    margin\_initial=0.0    margin\_maintenance=0.0    session\_volume=0.0    session\_turnover=0.0    session\_interest=0.0    session\_buy\_orders\_volume=0.0    session\_sell\_orders\_volume=0.0    session\_open=0.0    session\_close=0.0    session\_aw=0.0    session\_price\_settlement=0.0    session\_price\_limit\_min=0.0    session\_price\_limit\_max=0.0    margin\_hedged=100000.0    price\_change=0.0    price\_volatility=0.0    price\_theoretical=0.0    price\_greeks\_delta=0.0    price\_greeks\_theta=0.0    price\_greeks\_gamma=0.0    price\_greeks\_vega=0.0    price\_greeks\_rho=0.0    price\_greeks\_omega=0.0    price\_sensitivity=0.0    basis=    category=    currency\_base=EUR    currency\_profit=JPY    currency\_margin=EUR    bank=    description=Euro vs Japanese Yen    exchange=    formula=    isin=    name=EURJPY    page=http://www.google.com/finance?q=EURJPY    path=Forex\EURJPY |

See also

[account\_info](../account_info/account_info.md), [terminal\_info](../terminal_info/terminal_info.md)
