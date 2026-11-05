# Symbol Properties


To obtain the current market information there are several functions: [SymbolInfoInteger()](../../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoDouble()](../../../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) and [SymbolInfoString()](../../../Market-Info/SymbolInfoString/SymbolInfoString.md). The first parameter is the symbol name, the values of the second function parameter can be one of the identifiers of ENUM\_SYMBOL\_INFO\_INTEGER, ENUM\_SYMBOL\_INFO\_DOUBLE and ENUM\_SYMBOL\_INFO\_STRING.

For function [SymbolInfoInteger()](../../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md)

ENUM\_SYMBOL\_INFO\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| SYMBOL\_SUBSCRIPTION\_DELAY | Symbol data arrives with a delay. The property can be requested only for symbols selected in MarketWatch (SYMBOL\_SELECT = true). The [ERR\_MARKET\_NOT\_SELECTED](../../Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) (4302) error is generated for other symbols | bool |
| SYMBOL\_SECTOR | The sector of the economy to which the asset belongs | [ENUM\_SYMBOL\_SECTOR](Symbol-Properties.md#enum_symbol_sector) |
| SYMBOL\_INDUSTRY | The industry or the economy branch to which the symbol belongs | [ENUM\_SYMBOL\_INDUSTRY](Symbol-Properties.md#enum_symbol_industry) |
| SYMBOL\_CUSTOM | It is a custom symbol – the symbol has been created synthetically based on other symbols from the Market Watch and/or external data sources | bool |
| SYMBOL\_BACKGROUND\_COLOR | The color of the background used for the symbol in Market Watch | color |
| SYMBOL\_CHART\_MODE | The price type used for generating symbols bars, i.e. Bid or Last | [ENUM\_SYMBOL\_CHART\_MODE](Symbol-Properties.md#enum_symbol_chart_mode) |
| SYMBOL\_EXIST | Symbol with this name exists | bool |
| SYMBOL\_SELECT | Symbol is selected in Market Watch | bool |
| SYMBOL\_VISIBLE | Symbol is visible in Market Watch.     Some symbols (mostly, these are cross rates required for calculation of margin requirements or profits in deposit currency) are selected automatically, but may not be visible in Market Watch. To be displayed such symbols have to be explicitly selected. | bool |
| SYMBOL\_SESSION\_DEALS | Number of deals in the current session | long |
| SYMBOL\_SESSION\_BUY\_ORDERS | Number of Buy orders at the moment | long |
| SYMBOL\_SESSION\_SELL\_ORDERS | Number of Sell orders at the moment | long |
| SYMBOL\_VOLUME | Volume of the last deal | long |
| SYMBOL\_VOLUMEHIGH | Maximal day volume | long |
| SYMBOL\_VOLUMELOW | Minimal day volume | long |
| SYMBOL\_TIME | Time of the last quote | datetime |
| SYMBOL\_TIME\_MSC | Time of the last quote in milliseconds since 1970.01.01 | long |
| SYMBOL\_DIGITS | Digits after a decimal point | int |
| SYMBOL\_SPREAD\_FLOAT | Indication of a floating spread | bool |
| SYMBOL\_SPREAD | Spread value in points | int |
| SYMBOL\_TICKS\_BOOKDEPTH | Maximal number of requests shown in [Depth of Market](../../../Market-Info/MarketBookGet/MarketBookGet.md). For symbols that have no queue of requests, the value is equal to zero. | int |
| SYMBOL\_TRADE\_CALC\_MODE | Contract price calculation mode | [ENUM\_SYMBOL\_CALC\_MODE](Symbol-Properties.md#enum_symbol_calc_mode) |
| SYMBOL\_TRADE\_MODE | Order execution type | [ENUM\_SYMBOL\_TRADE\_MODE](Symbol-Properties.md#enum_symbol_trade_mode) |
| SYMBOL\_START\_TIME | Date of the symbol trade beginning (usually used for futures) | datetime |
| SYMBOL\_EXPIRATION\_TIME | Date of the symbol trade end (usually used for futures) | datetime |
| SYMBOL\_TRADE\_STOPS\_LEVEL | Minimal indention in points from the current close price to place Stop orders | int |
| SYMBOL\_TRADE\_FREEZE\_LEVEL | Distance to freeze trade operations in points | int |
| SYMBOL\_TRADE\_EXEMODE | Deal execution mode | [ENUM\_SYMBOL\_TRADE\_EXECUTION](Symbol-Properties.md#enum_symbol_trade_execution) |
| SYMBOL\_SWAP\_MODE | Swap calculation model | [ENUM\_SYMBOL\_SWAP\_MODE](Symbol-Properties.md#enum_symbol_swap_mode) |
| SYMBOL\_SWAP\_ROLLOVER3DAYS | The day of week to charge 3-day swap rollover | [ENUM\_DAY\_OF\_WEEK](Symbol-Properties.md#enum_day_of_week) |
| SYMBOL\_MARGIN\_HEDGED\_USE\_LEG | Calculating hedging margin using the larger leg (Buy or Sell) | bool |
| SYMBOL\_EXPIRATION\_MODE | Flags of allowed order [expiration modes](Symbol-Properties.md#symbol_expiration_mode) | int |
| SYMBOL\_FILLING\_MODE | Flags of allowed order [filling modes](Symbol-Properties.md#symbol_filling_mode) | int |
| SYMBOL\_ORDER\_MODE | Flags of allowed [order types](Symbol-Properties.md#symbol_order_mode) | int |
| SYMBOL\_ORDER\_GTC\_MODE | Expiration of Stop Loss and Take Profit orders, if SYMBOL\_EXPIRATION\_MODE=[SYMBOL\_EXPIRATION\_GTC](Symbol-Properties.md#symbol_expiration_mode) (Good till canceled) | [ENUM\_SYMBOL\_ORDER\_GTC\_MODE](Symbol-Properties.md#enum_symbol_order_gtc_mode) |
| SYMBOL\_OPTION\_MODE | Option type | [ENUM\_SYMBOL\_OPTION\_MODE](Symbol-Properties.md#enum_symbol_option_mode) |
| SYMBOL\_OPTION\_RIGHT | Option right (Call/Put) | [ENUM\_SYMBOL\_OPTION\_RIGHT](Symbol-Properties.md#enum_symbol_option_right) |

For function [SymbolInfoDouble()](../../../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md)

ENUM\_SYMBOL\_INFO\_DOUBLE

| Identifier | Description | Type |
| --- | --- | --- |
| SYMBOL\_BID | Bid - best sell offer | double |
| SYMBOL\_BIDHIGH | Maximal Bid of the day | double |
| SYMBOL\_BIDLOW | Minimal Bid of the day | double |
| SYMBOL\_ASK | Ask - best buy offer | double |
| SYMBOL\_ASKHIGH | Maximal Ask of the day | double |
| SYMBOL\_ASKLOW | Minimal Ask of the day | double |
| SYMBOL\_LAST | Price of the last deal | double |
| SYMBOL\_LASTHIGH | Maximal Last of the day | double |
| SYMBOL\_LASTLOW | Minimal Last of the day | double |
| SYMBOL\_VOLUME\_REAL | Volume of the last deal | double |
| SYMBOL\_VOLUMEHIGH\_REAL | Maximum Volume of the day | double |
| SYMBOL\_VOLUMELOW\_REAL | Minimum Volume of the day | double |
| SYMBOL\_OPTION\_STRIKE | The strike price of an option. The price at which an option buyer can buy (in a Call option) or sell (in a Put option) the underlying asset, and the option seller is obliged to sell or buy the appropriate amount of the underlying asset. | double |
| SYMBOL\_POINT | Symbol point value | double |
| SYMBOL\_TRADE\_TICK\_VALUE | Value of SYMBOL\_TRADE\_TICK\_VALUE\_PROFIT | double |
| SYMBOL\_TRADE\_TICK\_VALUE\_PROFIT | Calculated tick price for a profitable position | double |
| SYMBOL\_TRADE\_TICK\_VALUE\_LOSS | Calculated tick price for a losing position | double |
| SYMBOL\_TRADE\_TICK\_SIZE | Minimal price change | double |
| SYMBOL\_TRADE\_CONTRACT\_SIZE | Trade contract size | double |
| SYMBOL\_TRADE\_ACCRUED\_INTEREST | [Accrued interest](https://www.metatrader5.com/en/terminal/help/trading/market_watch "https://www.metatrader5.com/en/terminal/help/trading/market_watch") – accumulated coupon interest, i.e. part of the coupon interest calculated in proportion to the number of days since the coupon bond issuance or the last coupon interest payment | double |
| SYMBOL\_TRADE\_FACE\_VALUE | [Face value](https://www.metatrader5.com/en/terminal/help/trading/market_watch) – initial bond value set by the issuer | double |
| SYMBOL\_TRADE\_LIQUIDITY\_RATE | Liquidity Rate is the share of the asset that can be used for the margin. | double |
| SYMBOL\_VOLUME\_MIN | Minimal volume for a deal | double |
| SYMBOL\_VOLUME\_MAX | Maximal volume for a deal | double |
| SYMBOL\_VOLUME\_STEP | Minimal volume change step for deal execution | double |
| SYMBOL\_VOLUME\_LIMIT | Maximum allowed aggregate volume of an open position and pending orders in one direction (buy or sell) for the symbol. For example, with the limitation of 5 lots, you can have an open buy position with the volume of 5 lots and place a pending order Sell Limit with the volume of 5 lots. But in this case you cannot place a Buy Limit pending order (since the total volume in one direction will exceed the limitation) or place Sell Limit with the volume more than 5 lots. | double |
| SYMBOL\_SWAP\_LONG | Long swap value | double |
| SYMBOL\_SWAP\_SHORT | Short swap value | double |
| SYMBOL\_SWAP\_SUNDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from SUNDAY to the next day. There following values are supported:   - 0 – no swap is charged - 1 – single swap - 3 – triple swap | double |
| SYMBOL\_SWAP\_MONDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from Monday to Tuesday | double |
| SYMBOL\_SWAP\_TUESDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from Tuesday to Wednesday | double |
| SYMBOL\_SWAP\_WEDNESDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from Wednesday to Thursday | double |
| SYMBOL\_SWAP\_THURSDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from Thursday to Friday | double |
| SYMBOL\_SWAP\_FRIDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from Friday to Saturday | double |
| SYMBOL\_SWAP\_SATURDAY | Swap calculation ratio (SYMBOL\_SWAP\_LONG or SYMBOL\_SWAP\_SHORT) for overnight positions rolled over from Saturday to Sunday | double |
| SYMBOL\_MARGIN\_INITIAL | Initial margin means the amount in the margin currency required for opening a position with the volume of one lot. It is used for checking a client's assets when he or she enters the market.     The [SymbolInfoMarginRate()](../../../Market-Info/SymbolInfoMarginRate/SymbolInfoMarginRate.md) function provides data on the amount of charged margin depending on the order type and direction. | double |
| SYMBOL\_MARGIN\_MAINTENANCE | The maintenance margin. If it is set, it sets the margin amount in the margin currency of the symbol, charged from one lot. It is used for checking a client's assets when his/her account state changes. If the maintenance margin is equal to 0, the initial margin is used.     The [SymbolInfoMarginRate()](../../../Market-Info/SymbolInfoMarginRate/SymbolInfoMarginRate.md) function provides data on the amount of charged margin depending on the order type and direction. | double |
| SYMBOL\_SESSION\_VOLUME | Summary volume of current session deals | double |
| SYMBOL\_SESSION\_TURNOVER | Summary turnover of the current session | double |
| SYMBOL\_SESSION\_INTEREST | Summary open interest | double |
| SYMBOL\_SESSION\_BUY\_ORDERS\_VOLUME | Current volume of Buy orders | double |
| SYMBOL\_SESSION\_SELL\_ORDERS\_VOLUME | Current volume of Sell orders | double |
| SYMBOL\_SESSION\_OPEN | Open price of the current session | double |
| SYMBOL\_SESSION\_CLOSE | Close price of the current session | double |
| SYMBOL\_SESSION\_AW | Average weighted price of the current session | double |
| SYMBOL\_SESSION\_PRICE\_SETTLEMENT | Settlement price of the current session | double |
| SYMBOL\_SESSION\_PRICE\_LIMIT\_MIN | Minimal price of the current session | double |
| SYMBOL\_SESSION\_PRICE\_LIMIT\_MAX | Maximal price of the current session | double |
| SYMBOL\_MARGIN\_HEDGED | Contract size or margin value per one lot of hedged positions (oppositely directed positions of one symbol). Two margin calculation methods are possible for hedged positions. The calculation method is defined by the broker.     Basic calculation:   - If the initial margin (SYMBOL\_MARGIN\_INITIAL) is specified for a symbol, the hedged margin is specified as an absolute value (in monetary terms). - If the initial margin is not specified (equal to 0), SYMBOL\_MARGIN\_HEDGED is equal to the size of the contract, that will be used to calculate the margin by the appropriate formula in accordance with the type of the financial instrument ([SYMBOL\_TRADE\_CALC\_MODE](Symbol-Properties.md#enum_symbol_calc_mode)).      Calculation for the largest position:   - The SYMBOL\_MARGIN\_HEDGED value is not taken into account. - The volume of all short and all long positions of a symbol is calculated. - For each direction, a weighted average open price and a weighted average rate of conversion to the deposit currency is calculated. - Next, using the appropriate formula chosen in accordance with the symbol type ([SYMBOL\_TRADE\_CALC\_MODE](Symbol-Properties.md#enum_symbol_calc_mode)) the margin is calculated for the short and the long part. - The largest one of the values is used as the margin. | double |
| SYMBOL\_PRICE\_CHANGE | Change of the current price relative to the end of the previous trading day in % | double |
| SYMBOL\_PRICE\_VOLATILITY | Price volatility in % | double |
| SYMBOL\_PRICE\_THEORETICAL | Theoretical option price | double |
| SYMBOL\_PRICE\_DELTA | Option/warrant delta shows the value the option price changes by, when the underlying asset price changes by 1 | double |
| SYMBOL\_PRICE\_THETA | Option/warrant theta shows the number of points the option price is to lose every day due to a temporary breakup, i.e. when the expiration date approaches | double |
| SYMBOL\_PRICE\_GAMMA | Option/warrant gamma shows the change rate of delta – how quickly or slowly the option premium changes | double |
| SYMBOL\_PRICE\_VEGA | Option/warrant vega shows the number of points the option price changes by when the volatility changes by 1% | double |
| SYMBOL\_PRICE\_RHO | Option/warrant rho reflects the sensitivity of the theoretical option price to the interest rate changing by 1% | double |
| SYMBOL\_PRICE\_OMEGA | Option/warrant omega. Option elasticity shows a relative percentage change of the option price by the percentage change of the underlying asset price | double |
| SYMBOL\_PRICE\_SENSITIVITY | Option/warrant sensitivity shows by how many points the price of the option's underlying asset should change so that the price of the option changes by one point | double |

For function [SymbolInfoString()](../../../Market-Info/SymbolInfoString/SymbolInfoString.md)

ENUM\_SYMBOL\_INFO\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| SYMBOL\_BASIS | The underlying asset of a derivative | string |
| SYMBOL\_CATEGORY | The name of the sector or category to which the financial symbol belongs | string |
| SYMBOL\_COUNTRY | The country to which the financial symbol belongs | string |
| SYMBOL\_SECTOR\_NAME | The sector of the economy to which the financial symbol belongs | string |
| SYMBOL\_INDUSTRY\_NAME | The industry branch or the industry to which the financial symbol belongs | string |
| SYMBOL\_CURRENCY\_BASE | Basic currency of a symbol | string |
| SYMBOL\_CURRENCY\_PROFIT | Profit currency | string |
| SYMBOL\_CURRENCY\_MARGIN | Margin currency | string |
| SYMBOL\_BANK | Feeder of the current quote | string |
| SYMBOL\_DESCRIPTION | Symbol description | string |
| SYMBOL\_EXCHANGE | The name of the exchange in which the financial symbol is traded | string |
| SYMBOL\_FORMULA | The formula used for the custom symbol pricing. If the name of a financial symbol used in the formula starts with a digit or contains a special character (">" ", ".", "-", "&", "#" and so on) quotation marks should be used around this symbol name.   - Synthetic symbol: "@ESU19"/EURCAD - Calendar spread: "Si-9.13"-"Si-6.13" - Euro index: 34.38805726 \* pow(EURUSD,0.3155) \* pow(EURGBP,0.3056) \* pow(EURJPY,0.1891) \* pow(EURCHF,0.1113) \* pow(EURSEK,0.0785) | string |
| SYMBOL\_ISIN | The name of a symbol in the ISIN system (International Securities Identification Number). The International Securities Identification Number is a 12-digit alphanumeric code that uniquely identifies a security. The presence of this symbol property is determined on the side of a trade server. | string |
| SYMBOL\_PAGE | The address of the web page containing symbol information. This address will be displayed as a link when viewing symbol properties in the terminal | string |
| SYMBOL\_PATH | Path in the symbol tree | string |

 

A symbol price chart can be based on Bid or Last prices. The price selected for symbol charts also affects the generation and display of bars in the terminal. Possible values of the SYMBOL\_CHART\_MODE property are described in ENUM\_SYMBOL\_CHART\_MODE

ENUM\_SYMBOL\_CHART\_MODE

| Identifier | Description |
| --- | --- |
| SYMBOL\_CHART\_MODE\_BID | Bars are based on Bid prices |
| SYMBOL\_CHART\_MODE\_LAST | Bars are based on Last prices |

 

For each symbol several expiration modes of pending orders can be specified. A flag is matched to each mode. Flags can be combined using the operation of logical OR (|), for example, SYMBOL\_EXPIRATION\_GTC|SYMBOL\_EXPIRATION\_SPECIFIED. In order to check whether a certain mode is allowed for the symbol, the result of the logical AND (&) should be compared to the mode flag.

If flag SYMBOL\_EXPIRATION\_SPECIFIED is specified for a symbol, then while sending a pending order, you may specify the moment this pending order is valid till.

| Identifier | Value | Description |
| --- | --- | --- |
| SYMBOL\_EXPIRATION\_GTC | 1 | The order is valid during the unlimited time period, until it is explicitly canceled |
| SYMBOL\_EXPIRATION\_DAY | 2 | The order is valid till the end of the day |
| SYMBOL\_EXPIRATION\_SPECIFIED | 4 | The expiration time is specified in the order |
| SYMBOL\_EXPIRATION\_SPECIFIED\_DAY | 8 | The expiration date is specified in the order |

Example:

```cpp
//+------------------------------------------------------------------+
//| Checks if the specified expiration mode is allowed               |
//+------------------------------------------------------------------+
bool IsExpirationTypeAllowed(string symbol,int exp_type)
  {
//--- Obtain the value of the property that describes allowed expiration modes
   int expiration=(int)SymbolInfoInteger(symbol,SYMBOL_EXPIRATION_MODE);
//--- Return true, if mode exp_type is allowed
   return((expiration&exp_type)==exp_type);
  }
```

 

If the SYMBOL\_EXPIRATION\_MODE property is set to SYMBOL\_EXPIRATION\_GTC (good till canceled), the expiration of pending orders, as well as of Stop Loss/Take Profit orders should be additionally set using the ENUM\_SYMBOL\_ORDER\_GTC\_MODE enumeration.

ENUM\_SYMBOL\_ORDER\_GTC\_MODE

| Identifier | Description |
| --- | --- |
| SYMBOL\_ORDERS\_GTC | Pending orders and Stop Loss/Take Profit levels are valid for an unlimited period until their explicit cancellation |
| SYMBOL\_ORDERS\_DAILY | Orders are valid during one trading day. At the end of the day, all Stop Loss and Take Profit levels, as well as pending orders are deleted. |
| SYMBOL\_ORDERS\_DAILY\_EXCLUDING\_STOPS | When a trade day changes, only pending orders are deleted, while Stop Loss and Take Profit levels are preserved. |

 

When sending an order, we can specify the filling policy of a volume set in the order. The possible volume-based order execution options for each symbol are specified in the table. It is possible to set several modes for each instrument via a combination of flags. The combination of flags is expressed by the logical OR (|) operation, for example SYMBOL\_FILLING\_FOK|SYMBOL\_FILLING\_IOC.  To check if a specific mode is allowed for an instrument, compare the logical AND (&) result with the mode flag - [example](Symbol-Properties.md#filling_example).

| Fill policy | ID | Value | Description |
| --- | --- | --- | --- |
| Fill or Kill | SYMBOL\_FILLING\_FOK | 1 | An order can be executed in the specified volume only.     If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The desired volume can be made up of several available offers.     When sending an order, the [ORDER\_FILLING\_FOK](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) filling type should be specified for this policy.     The possibility of using FOK orders is determined at the trade server. |
| Immediate or Cancel | SYMBOL\_FILLING\_IOC | 2 | A trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled.     When sending an order, the [ORDER\_FILLING\_IOC](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) filling type should be specified for this policy.     The possibility of using IOC orders is determined at the trade server. |
| Passive | SYMBOL\_FILLING\_BOC | 4 | The BOC (Book-or-Cancel) policy assumes that an order can only be placed in the Depth of Market and cannot be immediately executed. If the order can be executed immediately when placed, then it is canceled.     In fact, this execution policy can only be specified when the price of the placed order is to be worse than the current market. BoC orders are used to implement passive trading, so that the order is not executed immediately when placed and does not affect current liquidity.     Only limit and stop limit orders are supported, i.e. the [SYMBOL\_ORDER\_MODE](Symbol-Properties.md#symbol_order_mode) flag should contain the SYMBOL\_ORDER\_LIMIT and/or SYMBOL\_ORDER\_STOP\_LIMIT values. |
| Return | No identifier |  | In case of partial filling, a market or limit order with remaining volume is not canceled but processed further.     When sending an order, the [ORDER\_FILLING\_RETURN](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) filling type should be specified for this policy.     Return orders are not allowed in the Market Execution mode (market execution — SYMBOL\_TRADE\_EXECUTION\_MARKET). |

When sending a trade request using the [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md) function, the necessary volume execution policy can be set in the type\_filling field, namely in the special [MqlTradeRequest](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) structure. The values from the [ENUM\_ORDER\_TYPE\_FILLING](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) enumeration are available.  If no filling type is specified, ORDER\_FILLING\_RETURN is automatically set in the trade request. The ORDER\_FILLING\_RETURN filling type is enabled in any [execution mode](Symbol-Properties.md#enum_symbol_trade_execution) except for "Market execution" (SYMBOL\_TRADE\_EXECUTION\_MARKET).

While sending a trade request for execution at the current time (time in force), we should keep in mind that financial markets provide no guarantee that the entire requested volume is available for a certain financial instrument at the desired price. Therefore, trading operations in real time are regulated using the price and volume execution modes. The modes, or execution policies, define the rules for cases when the price has changed or the requested volume cannot be completely fulfilled at the moment.

| Execution mode | Description | The value in [ENUM\_SYMBOL\_TRADE\_EXECUTION](Symbol-Properties.md#symbol_filling_mode) |
| --- | --- | --- |
| Execution mode     (Request Execution) | Executing a market order at the price previously received from the broker.     Prices for a certain market order are requested from the broker before the order is sent. Upon receiving the prices, order execution at the given price can be either confirmed or rejected. | SYMBOL\_TRADE\_EXECUTION\_REQUEST |
| Instant Execution | Executing a market order at the specified price immediately.     When sending a trade request to be executed, the platform automatically adds the current prices to the order.   - If the broker accepts the price, the order is executed. - If the broker does not accept the requested price, a "Requote" is sent — the broker returns prices, at which this order can be executed. | SYMBOL\_TRADE\_EXECUTION\_INSTANT |
| Market Execution | A broker makes a decision about the order execution price without any additional discussion with the trader.     Sending the order in such a mode means advance consent to its execution at this price. | SYMBOL\_TRADE\_EXECUTION\_MARKET |
| Exchange Execution | Trade operations are executed at the prices of the current market offers. | SYMBOL\_TRADE\_EXECUTION\_EXCHANGE |

Before sending an order with the current execution time, for the correct setting of the [ORDER\_TYPE\_FILLING](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_integer) value (volume execution type), you can use the [SymbolInfoInteger()](../../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) function with each financial instrument to get the [SYMBOL\_FILLING\_MODE](Symbol-Properties.md#enum_symbol_info_integer) property value, which shows [volume execution types](Symbol-Properties.md#symbol_filling_mode) allowed for the symbol as a combination of flags. The ORDER\_FILLING\_RETURN filling type is enabled at all times except for the "Market execution" mode (SYMBOL\_TRADE\_EXECUTION\_MARKET).

The use of filling types depending on the execution mode can be shown as the following table:

| Type of Execution\Fill Policy | Fill or Kill (FOK ORDER\_FILLING\_FOK) | Immediate or Cancel (IOC ORDER\_FILLING\_IOC) | Return (Return ORDER\_FILLING\_RETURN) |
| --- | --- | --- | --- |
| Instant Execution     (SYMBOL\_TRADE\_EXECUTION\_INSTANT) | + (regardless of a symbol setting) | + (regardless of a symbol setting) | + (always) |
| Request Execution     SYMBOL\_TRADE\_EXECUTION\_REQUEST | + (regardless of a symbol setting) | + (regardless of a symbol setting) | + (always) |
| Market Execution     SYMBOL\_TRADE\_EXECUTION\_MARKET | + (set in the symbol settings) | + (set in the symbol settings) | - (disabled regardless of the symbol settings) |
| Exchange Execution     SYMBOL\_TRADE\_EXECUTION\_EXCHANGE | + (set in the symbol settings) | + (set in the symbol settings) | + (always) |

In case of pending orders, the ORDER\_FILLING\_RETURN filling type should be used regardless of an execution type ([SYMBOL\_TRADE\_EXEMODE](Symbol-Properties.md#enum_symbol_trade_execution)), since such orders are not meant for execution at the time of sending. When using pending orders, a trader agrees in advance that, when conditions for a deal on this order are met, the broker will use the filling type supported by the exchange.

Example:

```cpp
//+------------------------------------------------------------------+
//| check if a given filling mode is allowed                         |
//+------------------------------------------------------------------+
bool IsFillingTypeAllowed(string symbol,int fill_type)
  {
//--- get the value of the property describing the filling mode
   int filling=(int)SymbolInfoInteger(symbol,SYMBOL_FILLING_MODE);
//--- return 'true' if the fill_type mode is allowed
   return((filling&fill_type)==fill_type);
  }
```

 

When sending a [trade request](../../Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) using OrderSend() function, an order type from [ENUM\_ORDER\_TYPE enumeration](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) should be specified for some operations. Not all types of orders may be allowed for a specific symbol. [SYMBOL\_ORDER\_MODE](Symbol-Properties.md#enum_symbol_info_integer) property describes the flags of the allowed order types.

| Identifier | Value | Description |
| --- | --- | --- |
| SYMBOL\_ORDER\_MARKET | 1 | Market orders are allowed (Buy and Sell) |
| SYMBOL\_ORDER\_LIMIT | 2 | Limit orders are allowed (Buy Limit and Sell Limit) |
| SYMBOL\_ORDER\_STOP | 4 | Stop orders are allowed (Buy Stop and Sell Stop) |
| SYMBOL\_ORDER\_STOP\_LIMIT | 8 | Stop-limit orders are allowed (Buy Stop Limit and Sell Stop Limit) |
| SYMBOL\_ORDER\_SL | 16 | Stop Loss is allowed |
| SYMBOL\_ORDER\_TP | 32 | Take Profit is allowed |
| SYMBOL\_ORDER\_CLOSEBY | 64 | Close By operation is allowed, i.e. closing a position by another open position on the same instruments but in the opposite direction. The property is set for accounts with the hedging accounting system ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../Account-Properties/Account-Properties.md#enum_account_margin_mode)) |

Example:

```cpp
//+------------------------------------------------------------------+
//| The function prints out order types allowed for a symbol         |
//+------------------------------------------------------------------+
void Check_SYMBOL_ORDER_MODE(string symbol)
  {
//--- receive the value of the property describing allowed order types
   int symbol_order_mode=(int)SymbolInfoInteger(symbol,SYMBOL_ORDER_MODE);
//--- check for market orders (Market Execution)
   if((SYMBOL_ORDER_MARKET&symbol_order_mode)==SYMBOL_ORDER_MARKET)
      Print(symbol+": Market orders are allowed (Buy and Sell)");
//--- check for Limit orders
   if((SYMBOL_ORDER_LIMIT&symbol_order_mode)==SYMBOL_ORDER_LIMIT)
      Print(symbol+": Buy Limit and Sell Limit orders are allowed");
//--- check for Stop orders
   if((SYMBOL_ORDER_STOP&symbol_order_mode)==SYMBOL_ORDER_STOP)
      Print(symbol+": Buy Stop and Sell Stop orders are allowed");
//--- check for Stop Limit orders
   if((SYMBOL_ORDER_STOP_LIMIT&symbol_order_mode)==SYMBOL_ORDER_STOP_LIMIT)
      Print(symbol+": Buy Stop Limit and Sell Stop Limit orders are allowed");
//--- check if placing a Stop Loss orders is allowed
   if((SYMBOL_ORDER_SL&symbol_order_mode)==SYMBOL_ORDER_SL)
      Print(symbol+": Stop Loss orders are allowed");
//--- check if placing a Take Profit orders is allowed
   if((SYMBOL_ORDER_TP&symbol_order_mode)==SYMBOL_ORDER_TP)
      Print(symbol+": Take Profit orders are allowed");
//--- check if closing a position by an opposite one is allowed
   if((SYMBOL_ORDER_TP&symbol_order_mode)==SYMBOL_ORDER_CLOSEBY)
      Print(symbol+": Close by allowed");
//---
  }
```

 

The ENUM\_SYMBOL\_CALC\_MODE enumeration is used for obtaining information about how the margin requirements for a symbol are calculated.

ENUM\_SYMBOL\_CALC\_MODE

| Identifier | Description | Formula |
| --- | --- | --- |
| SYMBOL\_CALC\_MODE\_FOREX | Forex mode - calculation of profit and margin for Forex | Margin:  Lots \* [Contract\_Size](Symbol-Properties.md#enum_symbol_info_double) / [Leverage](../../../Account-Information/AccountInfoInteger/AccountInfoInteger.md) \* [Margin\_Rate](../../../Market-Info/SymbolInfoMarginRate/SymbolInfoMarginRate.md)     Profit:   (close\_price - open\_price) \* Contract\_Size\*Lots |
| SYMBOL\_CALC\_MODE\_FOREX\_NO\_LEVERAGE | Forex No Leverage mode – calculation of profit and margin for Forex symbols without taking into account the leverage | Margin:  Lots \* Contract\_Size \* Margin\_Rate     Profit:   (close\_price - open\_price) \* Contract\_Size \* Lots |
| SYMBOL\_CALC\_MODE\_FUTURES | Futures mode - calculation of margin and profit for futures | Margin: Lots \* InitialMargin \* Margin\_Rate     Profit:  (close\_price - open\_price) \* TickPrice / TickSize\*Lots |
| SYMBOL\_CALC\_MODE\_CFD | CFD mode - calculation of margin and profit for CFD | Margin: Lots \* ContractSize \* MarketPrice \* Margin\_Rate     Profit:  (close\_price - open\_price) \* Contract\_Size \* Lots |
| SYMBOL\_CALC\_MODE\_CFDINDEX | CFD index mode - calculation of margin and profit for CFD by indexes | Margin: (Lots \* ContractSize \* MarketPrice) \* TickPrice / TickSize \* Margin\_Rate     Profit:  (close\_price - open\_price) \* Contract\_Size \* Lots |
| SYMBOL\_CALC\_MODE\_CFDLEVERAGE | CFD Leverage mode - calculation of margin and profit for CFD at leverage trading | Margin: (Lots \* ContractSize \* MarketPrice) / Leverage \* Margin\_Rate     Profit:  (close\_price-open\_price) \* Contract\_Size \* Lots |
| SYMBOL\_CALC\_MODE\_EXCH\_STOCKS | Exchange mode – calculation of margin and profit for trading securities on a stock exchange | Margin: Lots \* ContractSize \* LastPrice \* Margin\_Rate     Profit:  (close\_price - open\_price) \* Contract\_Size \* Lots |
| SYMBOL\_CALC\_MODE\_EXCH\_FUTURES | Futures mode –  calculation of margin and profit for trading futures contracts on a stock exchange | Margin: Lots \* InitialMargin \* Margin\_Rate or Lots \* MaintenanceMargin \* Margin\_Rate     Profit:  (close\_price - open\_price) \* Lots \* TickPrice / TickSize |
| SYMBOL\_CALC\_MODE\_EXCH\_FUTURES\_FORTS | FORTS Futures mode –  calculation of margin and profit for trading futures contracts on FORTS. The margin may be reduced by the amount of MarginDiscount deviation according to the following rules:  1. If the price of a long position (buy order) is less than the estimated price, MarginDiscount = Lots\*((PriceSettle-PriceOrder)\*TickPrice/TickSize)  2. If the price of a short position (sell order) exceeds the estimated price, MarginDiscount = Lots\*((PriceOrder-PriceSettle)\*TickPrice/TickSize)  where:   - - PriceSettle – estimated (clearing) price of the previous session;   - PriceOrder – average weighted position price or open price set in the order (request);   - TickPrice – tick price (cost of the price change by one point)   - TickSize – tick size (minimum price change step) | Margin: Lots \* InitialMargin \* Margin\_Rate or Lots \* MaintenanceMargin \* Margin\_Rate     Profit:  (close\_price - open\_price) \* Lots \* TickPrice / TickSize |
| SYMBOL\_CALC\_MODE\_EXCH\_BONDS | Exchange Bonds mode – calculation of margin and profit for trading bonds on a stock exchange | Margin: Lots \* ContractSize \* FaceValue \* open\_price \* /100     Profit:  Lots \* close\_price \* FaceValue \* Contract\_Size  + AccruedInterest \* Lots \* ContractSize |
| SYMBOL\_CALC\_MODE\_EXCH\_STOCKS\_MOEX | Exchange MOEX Stocks mode – calculation of margin and profit for trading securities on MOEX | Margin: Lots \* ContractSize \* LastPrice \* Margin\_Rate     Profit:  (close\_price - open\_price) \* Contract\_Size \* Lots |
| SYMBOL\_CALC\_MODE\_EXCH\_BONDS\_MOEX | Exchange MOEX Bonds mode – calculation of margin and profit for trading bonds on MOEX | Margin: Lots \* ContractSize \* FaceValue \* open\_price \* /100     Profit:  Lots \* close\_price \* FaceValue \* Contract\_Size  + AccruedInterest \* Lots \* ContractSize |
| SYMBOL\_CALC\_MODE\_SERV\_COLLATERAL | Collateral mode - a symbol is used as a non-tradable asset on a trading account. The market value of an open position is calculated based on the volume, current market price, contract size and liquidity ratio. The value is included into Assets, which are added to Equity. Open positions of such symbols increase the Free Margin amount and are used as additional margin (collateral) for open positions of tradable instruments. | Margin: no  Profit:  no     Market Value: Lots\*ContractSize\*MarketPrice\*LiqudityRate |

 

There are several symbol trading modes. Information about trading modes of a certain symbol is reflected in the values of enumeration ENUM\_SYMBOL\_TRADE\_MODE.

ENUM\_SYMBOL\_TRADE\_MODE

| Identifier | Description |
| --- | --- |
| SYMBOL\_TRADE\_MODE\_DISABLED | Trade is disabled for the symbol |
| SYMBOL\_TRADE\_MODE\_LONGONLY | Allowed only long positions |
| SYMBOL\_TRADE\_MODE\_SHORTONLY | Allowed only short positions |
| SYMBOL\_TRADE\_MODE\_CLOSEONLY | Allowed only position close operations |
| SYMBOL\_TRADE\_MODE\_FULL | No trade restrictions |

 

Possible deal execution modes for a certain symbol are defined in enumeration ENUM\_SYMBOL\_TRADE\_EXECUTION.

ENUM\_SYMBOL\_TRADE\_EXECUTION

| Identifier | Description |
| --- | --- |
| SYMBOL\_TRADE\_EXECUTION\_REQUEST | Execution by request |
| SYMBOL\_TRADE\_EXECUTION\_INSTANT | Instant execution |
| SYMBOL\_TRADE\_EXECUTION\_MARKET | Market execution |
| SYMBOL\_TRADE\_EXECUTION\_EXCHANGE | Exchange execution |

 

Methods of swap calculation at position transfer are specified in enumeration ENUM\_SYMBOL\_SWAP\_MODE. The method of swap calculation determines the units of measure of the [SYMBOL\_SWAP\_LONG](Symbol-Properties.md#enum_symbol_info_double) and [SYMBOL\_SWAP\_SHORT](Symbol-Properties.md#enum_symbol_info_double) parameters. For example, if swaps are charged in the client deposit currency, then the values of those parameters are specified as an amount of money in the client deposit currency.

ENUM\_SYMBOL\_SWAP\_MODE

| Identifier | Description |
| --- | --- |
| SYMBOL\_SWAP\_MODE\_DISABLED | Swaps disabled (no swaps) |
| SYMBOL\_SWAP\_MODE\_POINTS | Swaps are charged in points |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_SYMBOL | Swaps are charged in money in base currency of the symbol |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_MARGIN | Swaps are charged in money in margin currency of the symbol |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_DEPOSIT | Swaps are charged in money, in client deposit currency |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_PROFIT | Swaps are charged in money in profit calculation currency |
| SYMBOL\_SWAP\_MODE\_INTEREST\_CURRENT | Swaps are charged as the specified annual interest from the instrument price at calculation of swap (standard bank year is 360 days) |
| SYMBOL\_SWAP\_MODE\_INTEREST\_OPEN | Swaps are charged as the specified annual interest from the open price of position (standard bank year is 360 days) |
| SYMBOL\_SWAP\_MODE\_REOPEN\_CURRENT | Swaps are charged by reopening positions. At the end of a trading day the position is closed. Next day it is reopened by the close price +/- specified number of points (parameters SYMBOL\_SWAP\_LONG and SYMBOL\_SWAP\_SHORT) |
| SYMBOL\_SWAP\_MODE\_REOPEN\_BID | Swaps are charged by reopening positions. At the end of a trading day the position is closed. Next day it is reopened by the current Bid price +/- specified number of points (parameters SYMBOL\_SWAP\_LONG and SYMBOL\_SWAP\_SHORT) |

 

Values of the ENUM\_DAY\_OF\_WEEK enumeration are used for specifying days of week.

ENUM\_DAY\_OF\_WEEK

| Identifier | Description |
| --- | --- |
| SUNDAY | Sunday |
| MONDAY | Monday |
| TUESDAY | Tuesday |
| WEDNESDAY | Wednesday |
| THURSDAY | Thursday |
| FRIDAY | Friday |
| SATURDAY | Saturday |

 

An option is a contract, which gives the right, but not the obligation, to buy or sell an underlying asset (goods, stocks, futures, etc.) at a specified price on or before a specific date. The following enumerations describe option properties, including the option type and the right arising from it.  

ENUM\_SYMBOL\_OPTION\_RIGHT

| Identifier | Description |
| --- | --- |
| SYMBOL\_OPTION\_RIGHT\_CALL | A call option gives you the right to buy an asset at a specified price |
| SYMBOL\_OPTION\_RIGHT\_PUT | A put option gives you the right to sell an asset at a specified price |

 

ENUM\_SYMBOL\_OPTION\_MODE

| Identifier | Description |
| --- | --- |
| SYMBOL\_OPTION\_MODE\_EUROPEAN | European option may only be exercised on a specified date (expiration, execution date, delivery date) |
| SYMBOL\_OPTION\_MODE\_AMERICAN | American option may be exercised on any trading day or before expiry. The period within which a buyer can exercise the option is specified for it |

 

Financial instruments are categorized by sectors of the economy. An economic sector is a part of economic activity which has specific characteristics, economic goals, functions and behavior, which allow separating this sector from other parts of the economy. ENUM\_SYMBOL\_SECTOR lists the economic sectors which a trading instruments can belong to.

ENUM\_SYMBOL\_SECTOR

| ID | Description |
| --- | --- |
| SECTOR\_UNDEFINED | Undefined |
| SECTOR\_BASIC\_MATERIALS | Basic materials |
| SECTOR\_COMMUNICATION\_SERVICES | Communication services |
| SECTOR\_CONSUMER\_CYCLICAL | Consumer cyclical |
| SECTOR\_CONSUMER\_DEFENSIVE | Consumer defensive |
| SECTOR\_CURRENCY | Currencies |
| SECTOR\_CURRENCY\_CRYPTO | Cryptocurrencies |
| SECTOR\_ENERGY | Energy |
| SECTOR\_FINANCIAL | Finance |
| SECTOR\_HEALTHCARE | Healthcare |
| SECTOR\_INDUSTRIALS | Industrials |
| SECTOR\_REAL\_ESTATE | Real estate |
| SECTOR\_TECHNOLOGY | Technology |
| SECTOR\_UTILITIES | Utilities |

 

Each financial instrument can be assigned to a specific type of industry or economy branch. An industry is a branch of an economy that produces a closely related set of raw materials, goods, or services. ENUM\_SYMBOL\_INDUSTRY lists industries which a trading instrument can belong to.

ENUM\_SYMBOL\_INDUSTRY

| ID | Description |
| --- | --- |
| INDUSTRY\_UNDEFINED | Undefined |
| Basic materials | |
| INDUSTRY\_AGRICULTURAL\_INPUTS | Agricultural inputs |
| INDUSTRY\_ALUMINIUM | Aluminium |
| INDUSTRY\_BUILDING\_MATERIALS | Building materials |
| INDUSTRY\_CHEMICALS | Chemicals |
| INDUSTRY\_COKING\_COAL | Coking coal |
| INDUSTRY\_COPPER | Copper |
| INDUSTRY\_GOLD | Gold |
| INDUSTRY\_LUMBER\_WOOD | Lumber and wood production |
| INDUSTRY\_INDUSTRIAL\_METALS | Other industrial metals and mining |
| INDUSTRY\_PRECIOUS\_METALS | Other precious metals and mining |
| INDUSTRY\_PAPER | Paper and paper products |
| INDUSTRY\_SILVER | Silver |
| INDUSTRY\_SPECIALTY\_CHEMICALS | Specialty chemicals |
| INDUSTRY\_STEEL | Steel |
| Communication services | |
| INDUSTRY\_ADVERTISING | Advertising agencies |
| INDUSTRY\_BROADCASTING | Broadcasting |
| INDUSTRY\_GAMING\_MULTIMEDIA | Electronic gaming and multimedia |
| INDUSTRY\_ENTERTAINMENT | Entertainment |
| INDUSTRY\_INTERNET\_CONTENT | Internet content and information |
| INDUSTRY\_PUBLISHING | Publishing |
| INDUSTRY\_TELECOM | Telecom services |
| Consumer cyclical | |
| INDUSTRY\_APPAREL\_MANUFACTURING | Apparel manufacturing |
| INDUSTRY\_APPAREL\_RETAIL | Apparel retail |
| INDUSTRY\_AUTO\_MANUFACTURERS | Auto manufacturers |
| INDUSTRY\_AUTO\_PARTS | Auto parts |
| INDUSTRY\_AUTO\_DEALERSHIP | Auto and truck dealerships |
| INDUSTRY\_DEPARTMENT\_STORES | Department stores |
| INDUSTRY\_FOOTWEAR\_ACCESSORIES | Footwear and accessories |
| INDUSTRY\_FURNISHINGS | Furnishing, fixtures and appliances |
| INDUSTRY\_GAMBLING | Gambling |
| INDUSTRY\_HOME\_IMPROV\_RETAIL | Home improvement retail |
| INDUSTRY\_INTERNET\_RETAIL | Internet retail |
| INDUSTRY\_LEISURE | Leisure |
| INDUSTRY\_LODGING | Lodging |
| INDUSTRY\_LUXURY\_GOODS | Luxury goods |
| INDUSTRY\_PACKAGING\_CONTAINERS | Packaging and containers |
| INDUSTRY\_PERSONAL\_SERVICES | Personal services |
| INDUSTRY\_RECREATIONAL\_VEHICLES | Recreational vehicles |
| INDUSTRY\_RESIDENT\_CONSTRUCTION | Residential construction |
| INDUSTRY\_RESORTS\_CASINOS | Resorts and casinos |
| INDUSTRY\_RESTAURANTS | Restaurants |
| INDUSTRY\_SPECIALTY\_RETAIL | Specialty retail |
| INDUSTRY\_TEXTILE\_MANUFACTURING | Textile manufacturing |
| INDUSTRY\_TRAVEL\_SERVICES | Travel services |
| Consumer defensive | |
| INDUSTRY\_BEVERAGES\_BREWERS | Beverages - Brewers |
| INDUSTRY\_BEVERAGES\_NON\_ALCO | Beverages - Non-alcoholic |
| INDUSTRY\_BEVERAGES\_WINERIES | Beverages - Wineries and distilleries |
| INDUSTRY\_CONFECTIONERS | Confectioners |
| INDUSTRY\_DISCOUNT\_STORES | Discount stores |
| INDUSTRY\_EDUCATION\_TRAINIG | Education and training services |
| INDUSTRY\_FARM\_PRODUCTS | Farm products |
| INDUSTRY\_FOOD\_DISTRIBUTION | Food distribution |
| INDUSTRY\_GROCERY\_STORES | Grocery stores |
| INDUSTRY\_HOUSEHOLD\_PRODUCTS | Household and personal products |
| INDUSTRY\_PACKAGED\_FOODS | Packaged foods |
| INDUSTRY\_TOBACCO | Tobacco |
| Energy | |
| INDUSTRY\_OIL\_GAS\_DRILLING | Oil and gas drilling |
| INDUSTRY\_OIL\_GAS\_EP | Oil and gas extraction and processing |
| INDUSTRY\_OIL\_GAS\_EQUIPMENT | Oil and gas equipment and services |
| INDUSTRY\_OIL\_GAS\_INTEGRATED | Oil and gas integrated |
| INDUSTRY\_OIL\_GAS\_MIDSTREAM | Oil and gas midstream |
| INDUSTRY\_OIL\_GAS\_REFINING | Oil and gas refining and marketing |
| INDUSTRY\_THERMAL\_COAL | Thermal coal |
| INDUSTRY\_URANIUM | Uranium |
| Finance | |
| INDUSTRY\_EXCHANGE\_TRADED\_FUND | Exchange traded fund |
| INDUSTRY\_ASSETS\_MANAGEMENT | Assets management |
| INDUSTRY\_BANKS\_DIVERSIFIED | Banks - Diversified |
| INDUSTRY\_BANKS\_REGIONAL | Banks - Regional |
| INDUSTRY\_CAPITAL\_MARKETS | Capital markets |
| INDUSTRY\_CLOSE\_END\_FUND\_DEBT | Closed-End fund - Debt |
| INDUSTRY\_CLOSE\_END\_FUND\_EQUITY | Closed-end fund - Equity |
| INDUSTRY\_CLOSE\_END\_FUND\_FOREIGN | Closed-end fund - Foreign |
| INDUSTRY\_CREDIT\_SERVICES | Credit services |
| INDUSTRY\_FINANCIAL\_CONGLOMERATE | Financial conglomerates |
| INDUSTRY\_FINANCIAL\_DATA\_EXCHANGE | Financial data and stock exchange |
| INDUSTRY\_INSURANCE\_BROKERS | Insurance brokers |
| INDUSTRY\_INSURANCE\_DIVERSIFIED | Insurance - Diversified |
| INDUSTRY\_INSURANCE\_LIFE | Insurance - Life |
| INDUSTRY\_INSURANCE\_PROPERTY | Insurance - Property and casualty |
| INDUSTRY\_INSURANCE\_REINSURANCE | Insurance - Reinsurance |
| INDUSTRY\_INSURANCE\_SPECIALTY | Insurance - Specialty |
| INDUSTRY\_MORTGAGE\_FINANCE | Mortgage finance |
| INDUSTRY\_SHELL\_COMPANIES | Shell companies |
| Healthcare | |
| INDUSTRY\_BIOTECHNOLOGY | Biotechnology |
| INDUSTRY\_DIAGNOSTICS\_RESEARCH | Diagnostics and research |
| INDUSTRY\_DRUGS\_MANUFACTURERS | Drugs manufacturers - general |
| INDUSTRY\_DRUGS\_MANUFACTURERS\_SPEC | Drugs manufacturers - Specialty and generic |
| INDUSTRY\_HEALTHCARE\_PLANS | Healthcare plans |
| INDUSTRY\_HEALTH\_INFORMATION | Health information services |
| INDUSTRY\_MEDICAL\_FACILITIES | Medical care facilities |
| INDUSTRY\_MEDICAL\_DEVICES | Medical devices |
| INDUSTRY\_MEDICAL\_DISTRIBUTION | Medical distribution |
| INDUSTRY\_MEDICAL\_INSTRUMENTS | Medical instruments and supplies |
| INDUSTRY\_PHARM\_RETAILERS | Pharmaceutical retailers |
| Industrials | |
| INDUSTRY\_AEROSPACE\_DEFENSE | Aerospace and defense |
| INDUSTRY\_AIRLINES | Airlines |
| INDUSTRY\_AIRPORTS\_SERVICES | Airports and air services |
| INDUSTRY\_BUILDING\_PRODUCTS | Building products and equipment |
| INDUSTRY\_BUSINESS\_EQUIPMENT | Business equipment and supplies |
| INDUSTRY\_CONGLOMERATES | Conglomerates |
| INDUSTRY\_CONSULTING\_SERVICES | Consulting services |
| INDUSTRY\_ELECTRICAL\_EQUIPMENT | Electrical equipment and parts |
| INDUSTRY\_ENGINEERING\_CONSTRUCTION | Engineering and construction |
| INDUSTRY\_FARM\_HEAVY\_MACHINERY | Farm and heavy construction machinery |
| INDUSTRY\_INDUSTRIAL\_DISTRIBUTION | Industrial distribution |
| INDUSTRY\_INFRASTRUCTURE\_OPERATIONS | Infrastructure operations |
| INDUSTRY\_FREIGHT\_LOGISTICS | Integrated freight and logistics |
| INDUSTRY\_MARINE\_SHIPPING | Marine shipping |
| INDUSTRY\_METAL\_FABRICATION | Metal fabrication |
| INDUSTRY\_POLLUTION\_CONTROL | Pollution and treatment controls |
| INDUSTRY\_RAILROADS | Railroads |
| INDUSTRY\_RENTAL\_LEASING | Rental and leasing services |
| INDUSTRY\_SECURITY\_PROTECTION | Security and protection services |
| INDUSTRY\_SPEALITY\_BUSINESS\_SERVICES | Specialty business services |
| INDUSTRY\_SPEALITY\_MACHINERY | Specialty industrial machinery |
| INDUSTRY\_STUFFING\_EMPLOYMENT | Stuffing and employment services |
| INDUSTRY\_TOOLS\_ACCESSORIES | Tools and accessories |
| INDUSTRY\_TRUCKING | Trucking |
| INDUSTRY\_WASTE\_MANAGEMENT | Waste management |
| Real estate | |
| INDUSTRY\_REAL\_ESTATE\_DEVELOPMENT | Real estate - Development |
| INDUSTRY\_REAL\_ESTATE\_DIVERSIFIED | Real estate - Diversified |
| INDUSTRY\_REAL\_ESTATE\_SERVICES | Real estate services |
| INDUSTRY\_REIT\_DIVERSIFIED | REIT - Diversified |
| INDUSTRY\_REIT\_HEALTCARE | REIT - Healthcase facilities |
| INDUSTRY\_REIT\_HOTEL\_MOTEL | REIT - Hotel and motel |
| INDUSTRY\_REIT\_INDUSTRIAL | REIT - Industrial |
| INDUSTRY\_REIT\_MORTAGE | REIT - Mortgage |
| INDUSTRY\_REIT\_OFFICE | REIT - Office |
| INDUSTRY\_REIT\_RESIDENTAL | REIT - Residential |
| INDUSTRY\_REIT\_RETAIL | REIT - Retail |
| INDUSTRY\_REIT\_SPECIALITY | REIT - Specialty |
| Technology | |
| INDUSTRY\_COMMUNICATION\_EQUIPMENT | Communication equipment |
| INDUSTRY\_COMPUTER\_HARDWARE | Computer hardware |
| INDUSTRY\_CONSUMER\_ELECTRONICS | Consumer electronics |
| INDUSTRY\_ELECTRONIC\_COMPONENTS | Electronic components |
| INDUSTRY\_ELECTRONIC\_DISTRIBUTION | Electronics and computer distribution |
| INDUSTRY\_IT\_SERVICES | Information technology services |
| INDUSTRY\_SCIENTIFIC\_INSTRUMENTS | Scientific and technical instruments |
| INDUSTRY\_SEMICONDUCTOR\_EQUIPMENT | Semiconductor equipment and materials |
| INDUSTRY\_SEMICONDUCTORS | Semiconductors |
| INDUSTRY\_SOFTWARE\_APPLICATION | Software - Application |
| INDUSTRY\_SOFTWARE\_INFRASTRUCTURE | Software - Infrastructure |
| INDUSTRY\_SOLAR | Solar |
| Utilities | |
| INDUSTRY\_UTILITIES\_DIVERSIFIED | Utilities - Diversified |
| INDUSTRY\_UTILITIES\_POWERPRODUCERS | Utilities - Independent power producers |
| INDUSTRY\_UTILITIES\_RENEWABLE | Utilities - Renewable |
| INDUSTRY\_UTILITIES\_REGULATED\_ELECTRIC | Utilities - Regulated electric |
| INDUSTRY\_UTILITIES\_REGULATED\_GAS | Utilities - Regulated gas |
| INDUSTRY\_UTILITIES\_REGULATED\_WATER | Utilities - Regulated water |
| INDUSTRY\_UTILITIES\_FIRST | Start of the utilities services types enumeration. Corresponds to INDUSTRY\_UTILITIES\_DIVERSIFIED. |
| INDUSTRY\_UTILITIES\_LAST | End of the utilities services types enumeration. Corresponds to INDUSTRY\_UTILITIES\_REGULATED\_WATER. |