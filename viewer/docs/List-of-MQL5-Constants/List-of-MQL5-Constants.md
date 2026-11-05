# List of MQL5 Constants


All MQL5 constants in alphabetical order.

| Constant | Description | Usage |
| --- | --- | --- |
| \_\_DATE\_\_ | File compilation date without time (hours, minutes and seconds are equal to 0) | [Print](../Common-Functions/Print/Print.md) |
| \_\_DATETIME\_\_ | File compilation date and time | [Print](../Common-Functions/Print/Print.md) |
| \_\_FILE\_\_ | Name of the currently compiled file | [Print](../Common-Functions/Print/Print.md) |
| \_\_FUNCSIG\_\_ | Signature of the function in whose body the macro is located. Logging of the full description of functions can be useful in the identification of [overloaded functions](../Language-Basics/Functions/Function-Overloading/Function-Overloading.md) | [Print](../Common-Functions/Print/Print.md) |
| \_\_FUNCTION\_\_ | Name of the function, in whose body the macro is located | [Print](../Common-Functions/Print/Print.md) |
| \_\_LINE\_\_ | Line number in the source code, in which the macro is located | [Print](../Common-Functions/Print/Print.md) |
| \_\_MQLBUILD\_\_, \_\_MQL5BUILD\_\_ | Compiler build number | [Print](../Common-Functions/Print/Print.md) |
| \_\_PATH\_\_ | An absolute path to the file that is currently being compiled | [Print](../Common-Functions/Print/Print.md) |
| ACCOUNT\_ASSETS | The current assets of an account | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_BALANCE | Account balance in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_COMMISSION\_BLOCKED | The current blocked commission amount on an account | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_COMPANY | Name of a company that serves the account | [AccountInfoString](../Account-Information/AccountInfoString/AccountInfoString.md) |
| ACCOUNT\_CREDIT | Account credit in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_CURRENCY | Account currency | [AccountInfoString](../Account-Information/AccountInfoString/AccountInfoString.md) |
| ACCOUNT\_EQUITY | Account equity in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_LEVERAGE | Account leverage | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_LIABILITIES | The current liabilities on an account | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_LIMIT\_ORDERS | Maximum allowed number of active pending orders | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_LOGIN | Account number | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_MARGIN | Account margin used in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_MARGIN\_FREE | Free margin of an account in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_MARGIN\_INITIAL | Initial margin. The amount reserved on an account to cover the margin of all pending orders | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_MARGIN\_LEVEL | Account margin level in percents | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_MARGIN\_MAINTENANCE | Maintenance margin. The minimum equity reserved on an account to cover the minimum amount of all open positions | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_MARGIN\_SO\_CALL | Margin call level. Depending on the set ACCOUNT\_MARGIN\_SO\_MODE is expressed in percents or in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_MARGIN\_SO\_MODE | Mode for setting the minimal allowed margin | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_MARGIN\_SO\_SO | Margin stop out level. Depending on the set ACCOUNT\_MARGIN\_SO\_MODE is expressed in percents or in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_NAME | Client name | [AccountInfoString](../Account-Information/AccountInfoString/AccountInfoString.md) |
| ACCOUNT\_PROFIT | Current profit of an account in the deposit currency | [AccountInfoDouble](../Account-Information/AccountInfoDouble/AccountInfoDouble.md) |
| ACCOUNT\_SERVER | Trade server name | [AccountInfoString](../Account-Information/AccountInfoString/AccountInfoString.md) |
| ACCOUNT\_STOPOUT\_MODE\_MONEY | Account stop out mode in money | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_STOPOUT\_MODE\_PERCENT | Account stop out mode in percents | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_TRADE\_ALLOWED | [Allowed trade](../MQL5-programs/Trade-Permission/Trade-Permission.md) for the current account | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_TRADE\_EXPERT | [Allowed trade](../MQL5-programs/Trade-Permission/Trade-Permission.md) for an Expert Advisor | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_TRADE\_MODE | Account trade mode | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_TRADE\_MODE\_CONTEST | Contest account | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_TRADE\_MODE\_DEMO | Demo account | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ACCOUNT\_TRADE\_MODE\_REAL | Real account | [AccountInfoInteger](../Account-Information/AccountInfoInteger/AccountInfoInteger.md) |
| ALIGN\_CENTER | Centered (only for the Edit object) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md), [ChartScreenShot](../Custom-Indicators/Custom-Indicators.md) |
| ALIGN\_LEFT | Left alignment | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md), [ChartScreenShot](../Custom-Indicators/Custom-Indicators.md) |
| ALIGN\_RIGHT | Right alignment | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md), [ChartScreenShot](../Custom-Indicators/Custom-Indicators.md) |
| ANCHOR\_CENTER | Anchor point strictly in the center of the object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_LEFT | Anchor point to the left in the center | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_LEFT\_LOWER | Anchor point at the lower left corner | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_LEFT\_UPPER | Anchor point at the upper left corner | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_LOWER | Anchor point below in the center | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_RIGHT | Anchor point to the right in the center | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_RIGHT\_LOWER | Anchor point at the lower right corner | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_RIGHT\_UPPER | Anchor point at the upper right corner | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ANCHOR\_UPPER | Anchor point above in the center | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| BASE\_LINE | Main line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| BOOK\_TYPE\_BUY | Buy order (Bid) | [MqlBookInfo](../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) |
| BOOK\_TYPE\_BUY\_MARKET | Buy order by Market | [MqlBookInfo](../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) |
| BOOK\_TYPE\_SELL | Sell order (Offer) | [MqlBookInfo](../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) |
| BOOK\_TYPE\_SELL\_MARKET | Sell order by Market | [MqlBookInfo](../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) |
| BORDER\_FLAT | Flat form | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| BORDER\_RAISED | Prominent form | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| BORDER\_SUNKEN | Concave form | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| CHAR\_MAX | Maximal value, which can be represented by char type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| CHAR\_MIN | Minimal value, which can be represented by char type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| [CHART\_AUTOSCROLL](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_autoscroll) | Mode of automatic moving to the right border of the chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| CHART\_BARS | Display as a sequence of bars | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md) |
| CHART\_BEGIN | Chart beginning (the oldest prices) | [ChartNavigate](../Chart-Operations/ChartNavigate/ChartNavigate.md) |
| [CHART\_BRING\_TO\_TOP](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_bring_to_top) | Show chart on top of other charts | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| CHART\_CANDLES | Display as Japanese candlesticks | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md) |
| [CHART\_COLOR\_ASK](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_ask) | Ask price level color | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_BACKGROUND](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_background) | Chart background color | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_BID](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_bid) | Bid price level color | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_CANDLE\_BEAR](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_candle_bear) | Body color of a bear candlestick | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_CANDLE\_BULL](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_candle_bull) | Body color of a bull candlestick | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_CHART\_DOWN](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_chart_down) | Color for the down bar, shadows and body borders of bear candlesticks | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_CHART\_LINE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_chart_line) | Line chart color and color of "Doji" Japanese candlesticks | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_CHART\_UP](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_chart_up) | Color for the up bar, shadows and body borders of bull candlesticks | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_FOREGROUND](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_foreground) | Color of axes, scales and OHLC line | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_GRID](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_grid) | Grid color | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_LAST](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_last) | Line color of the last executed deal price (Last) | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_STOP\_LEVEL](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_stop_level) | Color of stop order levels (Stop Loss and Take Profit) | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COLOR\_VOLUME](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_volume) | Color of volumes and position opening levels | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_COMMENT](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_comment) | Text of a comment in a chart | [ChartSetString](../Chart-Operations/ChartSetString/ChartSetString.md), [ChartGetString](../Chart-Operations/ChartGetString/ChartGetString.md) |
| CHART\_CURRENT\_POS | Current position | [ChartNavigate](../Chart-Operations/ChartNavigate/ChartNavigate.md) |
| [CHART\_DRAG\_TRADE\_LEVELS](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_drag_trade_levels) | Permission to drag trading levels on a chart with a mouse. The drag mode is enabled by default (true value) | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_EVENT\_MOUSE\_MOVE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_event_mouse_move) | Send notifications of mouse move and mouse click events ([CHARTEVENT\_MOUSE\_MOVE](../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5 programs on a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_EVENT\_OBJECT\_CREATE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_event_object_create) | Send a notification of an event of new object creation ([CHARTEVENT\_OBJECT\_CREATE](../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5-programs on a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_EVENT\_OBJECT\_DELETE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_event_object_delete) | Send a notification of an event of object deletion ([CHARTEVENT\_OBJECT\_DELETE](../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5-programs on a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_FIRST\_VISIBLE\_BAR](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_first_visible_bar) | Number of the first visible bar in the chart. Indexing of bars is the same as for [timeseries](../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md). | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_FIXED\_MAX](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_fixed_max) | Fixed  chart maximum | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_FIXED\_MIN](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_fixed_min) | Fixed  chart minimum | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_FIXED\_POSITION](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_fixed_position) | Chart fixed position from the left border in percent value. Chart fixed position is marked by a small gray triangle on the horizontal time axis. It is displayed only if the automatic chart scrolling to the right on tick incoming is disabled (see CHART\_AUTOSCROLL property). The bar on a fixed position remains in the same place when zooming in and out. | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_FOREGROUND](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_foreground) | Price chart in the foreground | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_HEIGHT\_IN\_PIXELS](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_height_in_pixels) | Chart height in pixels | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_IS\_OBJECT](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_is_object) | Identifying "Chart" ([OBJ\_CHART)](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) object – returns true for a graphical object. Returns false for a real chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| CHART\_LINE | Display as a line drawn by Close prices | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md) |
| [CHART\_MODE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_mode) | Chart type (candlesticks, bars or line) | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_MOUSE\_SCROLL](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_mouse_scroll) | Scrolling the chart horizontally using the left mouse button. Vertical scrolling is also available if the value of any following properties is set to true: CHART\_SCALEFIX, CHART\_SCALEFIX\_11 or CHART\_SCALE\_PT\_PER\_BAR | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_POINTS\_PER\_BAR](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_points_per_bar) | Scale in points per bar | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_PRICE\_MAX](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_price_max) | Chart maximum | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_PRICE\_MIN](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_price_min) | Chart minimum | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_SCALE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scale) | Scale | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SCALE\_PT\_PER\_BAR](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scale_pt_per_bar) | Scale to be specified in points per bar | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SCALEFIX](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scalefix) | Fixed scale mode | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SCALEFIX\_11](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scalefix_11) | Scale 1:1 mode | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHIFT](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_shift) | Mode of price chart indent from the right border | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHIFT\_SIZE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_shift_size) | The size of the zero bar indent from the right border in percents | [ChartSetDouble](../Chart-Operations/ChartSetDouble/ChartSetDouble.md), [ChartGetDouble](../Chart-Operations/ChartGetDouble/ChartGetDouble.md) |
| [CHART\_SHOW\_ASK\_LINE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_ask_line) | Display Ask values as a horizontal line in a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_BID\_LINE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_bid_line) | Display Bid values as a horizontal line in a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_DATE\_SCALE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_date_scale) | Showing the time scale on a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_GRID](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_grid) | Display grid in the chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_LAST\_LINE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_last_line) | Display Last values as a horizontal line in a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_OBJECT\_DESCR](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_object_descr) | Pop-up descriptions of graphical objects | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_OHLC](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_ohlc) | Show OHLC values in the upper left corner | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_ONE\_CLICK](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_one_click) | Showing the ["One click trading"](https://www.metatrader5.com/en/terminal/help/startworking/settings "\"One click trading\"") panel on a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_PERIOD\_SEP](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_period_sep) | Display vertical separators between adjacent periods | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_PRICE\_SCALE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_price_scale) | Showing the price scale on a chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_TRADE\_LEVELS](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_trade_levels) | Displaying trade levels in the chart (levels of open positions, Stop Loss, Take Profit and pending orders) | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_SHOW\_VOLUMES](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_volumes) | Display volume in the chart | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_VISIBLE\_BARS](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_visible_bars) | The number of bars on the chart that can be displayed | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| CHART\_VOLUME\_HIDE | Volumes are not shown | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md) |
| CHART\_VOLUME\_REAL | Trade volumes | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md) |
| CHART\_VOLUME\_TICK | Tick volumes | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md) |
| [CHART\_WIDTH\_IN\_BARS](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_width_in_bars) | Chart width in bars | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_WIDTH\_IN\_PIXELS](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_width_in_pixels) | Chart width in pixels | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_WINDOW\_HANDLE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_window_handle) | Chart window handle (HWND) | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_WINDOW\_IS\_VISIBLE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_window_is_visible) | Visibility of subwindows | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_WINDOW\_YDISTANCE](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_window_ydistance) | The distance between the upper frame of the indicator subwindow and the upper frame of the main chart window, along the vertical Y axis, in pixels. In case of a mouse event, the cursor coordinates are passed in terms of the coordinates of the main chart window, while the coordinates of graphical objects in an indicator subwindow are set relative to the upper left corner of the subwindow.  The value is required for converting the absolute coordinates of the main chart to the local coordinates of a subwindow for correct work with the graphical objects, whose coordinates are set relative to  the upper left corner of the subwindow frame. | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| [CHART\_WINDOWS\_TOTAL](../Constants,-Enumerations-and-Structures/Chart-Constants/Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_windows_total) | The total number of chart windows, including indicator subwindows | [ChartSetInteger](../Chart-Operations/ChartSetInteger/ChartSetInteger.md), [ChartGetInteger](../Chart-Operations/ChartGetInteger/ChartGetInteger.md) |
| CHARTEVENT\_CHART\_CHANGE | Change of the chart size or modification of chart properties through the Properties dialog | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_CLICK | Clicking on a chart | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_CUSTOM | Initial number of an event from a range of custom events | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_CUSTOM\_LAST | The final number of an event from a range of custom events | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_KEYDOWN | Keystrokes | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_MOUSE\_MOVE | Mouse move, mouse clicks (if [CHART\_EVENT\_MOUSE\_MOVE](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer)=true is set for the chart) | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_OBJECT\_CHANGE | [Graphical object](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) property changed via the properties dialog | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_OBJECT\_CLICK | Clicking on a [graphical object](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_OBJECT\_CREATE | [Graphical object](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) created (if [CHART\_EVENT\_OBJECT\_CREATE](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer)=true is set for the chart) | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_OBJECT\_DELETE | [Graphical object](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) deleted (if [CHART\_EVENT\_OBJECT\_DELETE](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer)=true is set for the chart) | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_OBJECT\_DRAG | Drag and drop of a [graphical object](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTEVENT\_OBJECT\_ENDEDIT | End of text editing in the graphical object Edit | [OnChartEvent](../Event-Handling/OnChartEvent/OnChartEvent.md) |
| CHARTS\_MAX | The maximum possible number of simultaneously open charts in the terminal | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| CHIKOUSPAN\_LINE | Chikou Span line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| clrAliceBlue | Alice Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrAntiqueWhite | Antique White | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrAqua | Aqua | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrAquamarine | Aquamarine | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBeige | Beige | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBisque | Bisque | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBlack | Black | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBlanchedAlmond | Blanched Almond | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBlue | Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBlueViolet | Blue Violet | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBrown | Brown | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrBurlyWood | Burly Wood | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrCadetBlue | Cadet Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrChartreuse | Chartreuse | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrChocolate | Chocolate | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrCoral | Coral | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrCornflowerBlue | Cornflower Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrCornsilk | Cornsilk | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrCrimson | Crimson | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkBlue | Dark Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkGoldenrod | Dark Goldenrod | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkGray | Dark Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkGreen | Dark Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkKhaki | Dark Khaki | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkOliveGreen | Dark Olive Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkOrange | Dark Orange | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkOrchid | Dark Orchid | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkSalmon | Dark Salmon | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkSeaGreen | Dark Sea Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkSlateBlue | Dark Slate Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkSlateGray | Dark Slate Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkTurquoise | Dark Turquoise | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDarkViolet | Dark Violet | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDeepPink | Deep Pink | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDeepSkyBlue | Deep Sky Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDimGray | Dim Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrDodgerBlue | Dodger Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrFireBrick | Fire Brick | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrForestGreen | Forest Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrGainsboro | Gainsboro | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrGold | Gold | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrGoldenrod | Goldenrod | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrGray | Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrGreen | Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrGreenYellow | Green Yellow | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrHoneydew | Honeydew | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrHotPink | Hot Pink | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrIndianRed | Indian Red | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrIndigo | Indigo | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrIvory | Ivory | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrKhaki | Khaki | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLavender | Lavender | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLavenderBlush | Lavender Blush | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLawnGreen | Lawn Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLemonChiffon | Lemon Chiffon | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightBlue | Light Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightCoral | Light Coral | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightCyan | Light Cyan | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightGoldenrod | Light Goldenrod | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightGray | Light Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightGreen | Light Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightPink | Light Pink | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightSalmon | Light Salmon | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightSeaGreen | Light Sea Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightSkyBlue | Light Sky Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightSlateGray | Light Slate Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightSteelBlue | Light Steel Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLightYellow | Light Yellow | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLime | Lime | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLimeGreen | Lime Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrLinen | Linen | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMagenta | Magenta | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMaroon | Maroon | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumAquamarine | Medium Aquamarine | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumBlue | Medium Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumOrchid | Medium Orchid | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumPurple | Medium Purple | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumSeaGreen | Medium Sea Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumSlateBlue | Medium Slate Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumSpringGreen | Medium Spring Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumTurquoise | Medium Turquoise | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMediumVioletRed | Medium Violet Red | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMidnightBlue | Midnight Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMintCream | Mint Cream | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMistyRose | Misty Rose | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrMoccasin | Moccasin | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrNavajoWhite | Navajo White | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrNavy | Navy | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrNONE | Absence of color | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| clrOldLace | Old Lace | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrOlive | Olive | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrOliveDrab | Olive Drab | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrOrange | Orange | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrOrangeRed | Orange Red | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrOrchid | Orchid | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPaleGoldenrod | Pale Goldenrod | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPaleGreen | Pale Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPaleTurquoise | Pale Turquoise | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPaleVioletRed | Pale Violet Red | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPapayaWhip | Papaya Whip | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPeachPuff | Peach Puff | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPeru | Peru | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPink | Pink | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPlum | Plum | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPowderBlue | Powder Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrPurple | Purple | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrRed | Red | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrRosyBrown | Rosy Brown | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrRoyalBlue | Royal Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSaddleBrown | Saddle Brown | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSalmon | Salmon | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSandyBrown | Sandy Brown | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSeaGreen | Sea Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSeashell | Seashell | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSienna | Sienna | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSilver | Silver | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSkyBlue | Sky Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSlateBlue | Slate Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSlateGray | Slate Gray | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSnow | Snow | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSpringGreen | Spring Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrSteelBlue | Steel Blue | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrTan | Tan | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrTeal | Teal | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrThistle | Thistle | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrTomato | Tomato | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrTurquoise | Turquoise | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrViolet | Violet | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrWheat | Wheat | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrWhite | White | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrWhiteSmoke | White Smoke | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrYellow | Yellow | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| clrYellowGreen | Yellow Green | [Web Colors](../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) |
| CORNER\_LEFT\_LOWER | Center of coordinates is in the lower left corner of the chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| CORNER\_LEFT\_UPPER | Center of coordinates is in the upper left corner of the chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| CORNER\_RIGHT\_LOWER | Center of coordinates is in the lower right corner of the chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| CORNER\_RIGHT\_UPPER | Center of coordinates is in the upper right corner of the chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| CP\_ACP | The current Windows ANSI code page. | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CP\_MACCP | The current system Macintosh code page.  Note: This value is mostly used in earlier created program codes and is of no use now, since modern Macintosh computers use Unicode for encoding. | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CP\_OEMCP | The current system OEM code page. | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CP\_SYMBOL | Symbol code page | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CP\_THREAD\_ACP | The Windows ANSI code page for the current thread. | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CP\_UTF7 | UTF-7 code page. | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CP\_UTF8 | UTF-8 code page. | [CharArrayToString](../Conversion-Functions/CharArrayToString/CharArrayToString.md), [StringToCharArray](../Conversion-Functions/StringToCharArray/StringToCharArray.md), [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| CRYPT\_AES128 | AES encryption with 128 bit key (16 bytes) | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_AES256 | AES encryption with 256 bit key (32 bytes) | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_ARCH\_ZIP | ZIP archives | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_BASE64 | BASE64 | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_DES | DES encryption with 56 bit key (7 bytes) | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_HASH\_MD5 | MD5 HASH calculation | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_HASH\_SHA1 | SHA1 HASH calculation | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| CRYPT\_HASH\_SHA256 | SHA256 HASH calculation | [CryptEncode](../Common-Functions/CryptEncode/CryptEncode.md), [CryptDecode](../Common-Functions/CryptDecode/CryptDecode.md) |
| DBL\_DIG | Number of significant decimal digits for double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_EPSILON | Minimal value, which satisfies the condition:  1.0+DBL\_EPSILON != 1.0 (for double type) | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MANT\_DIG | Bits count in a mantissa for double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MAX | Maximal value, which can be represented by double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MAX\_10\_EXP | Maximal decimal value of exponent degree for double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MAX\_EXP | Maximal binary value of exponent degree for double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MIN | Minimal positive value, which can be represented by double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MIN\_10\_EXP | Minimal decimal value of exponent degree for double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DBL\_MIN\_EXP | Minimal binary value of exponent degree for double type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| DEAL\_COMMENT | Deal comment | [HistoryDealGetString](../Trade-Functions/HistoryDealGetString/HistoryDealGetString.md) |
| DEAL\_COMMISSION | Deal commission | [HistoryDealGetDouble](../Trade-Functions/HistoryDealGetDouble/HistoryDealGetDouble.md) |
| DEAL\_ENTRY | Deal entry - entry in, entry out, reverse | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_ENTRY\_IN | Entry in | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_ENTRY\_INOUT | Reverse | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_ENTRY\_OUT | Entry out | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_MAGIC | Deal magic number (see [ORDER\_MAGIC](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)) | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_ORDER | Deal [order number](../Trade-Functions/HistoryOrderGetTicket/HistoryOrderGetTicket.md) | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_POSITION\_ID | [Identifier of a position](../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer), in the opening, modification or change of which this deal took part. Each position has a unique identifier that is assigned to all deals executed for the symbol during the entire lifetime of the position. | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_PRICE | Deal price | [HistoryDealGetDouble](../Trade-Functions/HistoryDealGetDouble/HistoryDealGetDouble.md) |
| DEAL\_PROFIT | Deal profit | [HistoryDealGetDouble](../Trade-Functions/HistoryDealGetDouble/HistoryDealGetDouble.md) |
| DEAL\_SWAP | Cumulative swap on close | [HistoryDealGetDouble](../Trade-Functions/HistoryDealGetDouble/HistoryDealGetDouble.md) |
| DEAL\_SYMBOL | Deal symbol | [HistoryDealGetString](../Trade-Functions/HistoryDealGetString/HistoryDealGetString.md) |
| DEAL\_TIME | Deal time | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TIME\_MSC | The time of a deal execution in milliseconds since 01.01.1970 | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE | Deal type | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_BALANCE | Balance | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_BONUS | Bonus | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_BUY | Buy | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_BUY\_CANCELED | Canceled buy deal. There can be a situation when a previously executed buy deal is canceled. In this case, the type of the previously executed deal (DEAL\_TYPE\_BUY) is changed to DEAL\_TYPE\_BUY\_CANCELED, and its profit/loss is zeroized. Previously obtained profit/loss is charged/withdrawn using a separated balance operation | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_CHARGE | Additional charge | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_COMMISSION | Additional commission | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_COMMISSION\_AGENT\_DAILY | Daily agent commission | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_COMMISSION\_AGENT\_MONTHLY | Monthly agent commission | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_COMMISSION\_DAILY | Daily commission | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_COMMISSION\_MONTHLY | Monthly commission | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_CORRECTION | Correction | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_CREDIT | Credit | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_INTEREST | Interest rate | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_SELL | Sell | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_TYPE\_SELL\_CANCELED | Canceled sell deal. There can be a situation when a previously executed sell deal is canceled. In this case, the type of the previously executed deal (DEAL\_TYPE\_SELL) is changed to DEAL\_TYPE\_SELL\_CANCELED, and its profit/loss is zeroized. Previously obtained profit/loss is charged/withdrawn using a separated balance operation | [HistoryDealGetInteger](../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) |
| DEAL\_VOLUME | Deal volume | [HistoryDealGetDouble](../Trade-Functions/HistoryDealGetDouble/HistoryDealGetDouble.md) |
| [DRAW\_ARROW](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_ARROW/DRAW_ARROW.md) | Drawing arrows | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_BARS](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_BARS/DRAW_BARS.md) | Display as a sequence of bars | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_CANDLES](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_CANDLES/DRAW_CANDLES.md) | Display as a sequence of candlesticks | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_ARROW](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_ARROW/DRAW_COLOR_ARROW.md) | Drawing multicolored arrows | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_BARS](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_BARS/DRAW_COLOR_BARS.md) | Multicolored bars | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_CANDLES](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_CANDLES/DRAW_COLOR_CANDLES.md) | Multicolored candlesticks | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_HISTOGRAM](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_HISTOGRAM/DRAW_COLOR_HISTOGRAM.md) | Multicolored histogram from the zero line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_HISTOGRAM2](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_HISTOGRAM2/DRAW_COLOR_HISTOGRAM2.md) | Multicolored histogram of the two indicator buffers | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_LINE](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_LINE/DRAW_COLOR_LINE.md) | Multicolored line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_SECTION](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_SECTION/DRAW_COLOR_SECTION.md) | Multicolored section | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_COLOR\_ZIGZAG](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_ZIGZAG/DRAW_COLOR_ZIGZAG.md) | Multicolored ZigZag | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_FILLING](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_FILLING/DRAW_FILLING.md) | Color fill between the two levels | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_HISTOGRAM](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_HISTOGRAM/DRAW_HISTOGRAM.md) | Histogram from the zero line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_HISTOGRAM2](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_HISTOGRAM2/DRAW_HISTOGRAM2.md) | Histogram of the two indicator buffers | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_LINE](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_LINE/DRAW_LINE.md) | Line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_NONE](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_NONE/DRAW_NONE.md) | Not drawn | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_SECTION](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_SECTION/DRAW_SECTION.md) | Section | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| [DRAW\_ZIGZAG](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_ZIGZAG/DRAW_ZIGZAG.md) | Style Zigzag allows vertical section on the bar | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) |
| ELLIOTT\_CYCLE | Cycle | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_GRAND\_SUPERCYCLE | Grand Supercycle | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_INTERMEDIATE | Intermediate | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_MINOR | Minor | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_MINUETTE | Minuette | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_MINUTE | Minute | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_PRIMARY | Primary | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_SUBMINUETTE | Subminuette | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ELLIOTT\_SUPERCYCLE | Supercycle | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| EMPTY\_VALUE | Empty value in an indicator buffer | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| ERR\_ACCOUNT\_WRONG\_PROPERTY | Wrong account property ID | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_ARRAY\_BAD\_SIZE | Requested array size exceeds 2 GB | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_ARRAY\_RESIZE\_ERROR | Not enough memory for the relocation of an array, or an attempt to change the size of a static array | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_BOOKS\_CANNOT\_ADD | Depth Of Market can not be added | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_BOOKS\_CANNOT\_DELETE | Depth Of Market can not be removed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_BOOKS\_CANNOT\_GET | The data from Depth Of Market can not be obtained | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_BOOKS\_CANNOT\_SUBSCRIBE | Error in subscribing to receive new data from Depth Of Market | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_BUFFERS\_NO\_MEMORY | Not enough memory for the distribution of indicator buffers | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_BUFFERS\_WRONG\_INDEX | Wrong indicator buffer index | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CANNOT\_CLEAN\_DIRECTORY | Failed to clear the directory (probably one or more files are blocked and removal operation failed) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CANNOT\_DELETE\_DIRECTORY | The directory cannot be removed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CANNOT\_DELETE\_FILE | File deleting error | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CANNOT\_OPEN\_FILE | File opening error | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHAR\_ARRAY\_ONLY | Must be an array of type char | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_CANNOT\_CHANGE | Failed to change chart symbol and period | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_CANNOT\_CREATE\_TIMER | Failed to create timer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_CANNOT\_OPEN | Chart opening error | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_INDICATOR\_CANNOT\_ADD | Error adding an indicator to chart | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_INDICATOR\_CANNOT\_DEL | Error deleting an indicator from the chart | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_INDICATOR\_NOT\_FOUND | Indicator not found on the specified chart | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_NAVIGATE\_FAILED | Error navigating through chart | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_NO\_EXPERT | No Expert Advisor in the chart that could handle the event | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_NO\_REPLY | Chart does not respond | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_NOT\_FOUND | Chart not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_SCREENSHOT\_FAILED | Error creating screenshots | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_TEMPLATE\_FAILED | Error applying template | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_WINDOW\_NOT\_FOUND | Subwindow containing the indicator was not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_WRONG\_ID | Wrong chart ID | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_WRONG\_PARAMETER | Error value of the parameter for the [function of working with charts](../Chart-Operations/Chart-Operations.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CHART\_WRONG\_PROPERTY | Wrong chart property ID | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_CUSTOM\_WRONG\_PROPERTY | Wrong ID of the custom indicator property | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_DIRECTORY\_NOT\_EXIST | Directory does not exist | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_DOUBLE\_ARRAY\_ONLY | Must be an array of type double | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_BINSTRINGSIZE | String size must be specified, because the file is opened as binary | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_CACHEBUFFER\_ERROR | Not enough memory for cache to read | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_CANNOT\_REWRITE | File can not be rewritten | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_IS\_DIRECTORY | This is not a file, this is a directory | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_ISNOT\_DIRECTORY | This is a file, not a directory | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOT\_EXIST | File does not exist | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOTBIN | The file must be opened as a binary one | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOTCSV | The file must be opened as CSV | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOTTOREAD | The file must be opened for reading | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOTTOWRITE | The file must be opened for writing | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOTTXT | The file must be opened as a text | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_NOTTXTORCSV | The file must be opened as a text or CSV | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_READERROR | File reading error | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FILE\_WRITEERROR | Failed to write a resource to a file | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FLOAT\_ARRAY\_ONLY | Must be an array of type float | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FTP\_SEND\_FAILED | File sending via ftp failed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_FUNCTION\_NOT\_ALLOWED | Function is not allowed for call | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_GLOBALVARIABLE\_EXISTS | Global variable of the client terminal with the same name already exists | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_GLOBALVARIABLE\_NOT\_FOUND | Global variable of the client terminal is not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_HISTORY\_NOT\_FOUND | Requested history not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_HISTORY\_WRONG\_PROPERTY | Wrong ID of the history property | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INCOMPATIBLE\_ARRAYS | Copying incompatible arrays. String array can be copied only to a string array, and a numeric array - in numeric array only | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INCOMPATIBLE\_FILE | A text file must be for string arrays, for other arrays - binary | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_CANNOT\_ADD | Error applying an indicator to chart | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_CANNOT\_APPLY | The indicator cannot be applied to another indicator | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_CANNOT\_CREATE | Indicator cannot be created | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_CUSTOM\_NAME | The first parameter in the array must be the name of the custom indicator | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_DATA\_NOT\_FOUND | Requested data not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_NO\_MEMORY | Not enough memory to add the indicator | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_PARAMETER\_TYPE | Invalid parameter type in the array when creating an indicator | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_PARAMETERS\_MISSING | No parameters when creating an indicator | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_UNKNOWN\_SYMBOL | Unknown symbol | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_WRONG\_HANDLE | Wrong indicator handle | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_WRONG\_INDEX | Wrong index of the requested indicator buffer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INDICATOR\_WRONG\_PARAMETERS | Wrong number of parameters when creating an indicator | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INT\_ARRAY\_ONLY | Must be an array of type int | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INTERNAL\_ERROR | Unexpected internal error | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INVALID\_ARRAY | Array of a wrong type, wrong size, or a damaged object of a dynamic array | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INVALID\_DATETIME | Invalid date and/or time | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INVALID\_FILEHANDLE | A file with this handle was closed, or was not opening at all | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INVALID\_PARAMETER | Wrong parameter when calling the system function | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INVALID\_POINTER | Wrong pointer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_INVALID\_POINTER\_TYPE | Wrong type of pointer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_LONG\_ARRAY\_ONLY | Must be an array of type long | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MAIL\_SEND\_FAILED | Email sending failed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MARKET\_LASTTIME\_UNKNOWN | Time of the last tick is not known (no ticks) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MARKET\_NOT\_SELECTED | Symbol is not selected in MarketWatch | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MARKET\_SELECT\_ERROR | Error adding or deleting a symbol in MarketWatch | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MARKET\_UNKNOWN\_SYMBOL | Unknown symbol | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MARKET\_WRONG\_PROPERTY | Wrong identifier of a symbol property | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_MQL5\_WRONG\_PROPERTY | Wrong identifier of the program property | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NO\_STRING\_DATE | No date in the string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NOT\_ENOUGH\_MEMORY | Not enough memory to perform the system function | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NOTIFICATION\_SEND\_FAILED | Failed to send a [notification](../Network-Functions/SendNotification/SendNotification.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NOTIFICATION\_TOO\_FREQUENT | Too frequent sending of notifications | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NOTIFICATION\_WRONG\_PARAMETER | Invalid parameter for sending a notification – an empty string or [NULL](../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) has been passed to the [SendNotification()](../Network-Functions/SendNotification/SendNotification.md) function | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NOTIFICATION\_WRONG\_SETTINGS | Wrong settings of notifications in the terminal (ID is not specified or permission is not set) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NOTINITIALIZED\_STRING | Not initialized string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_NUMBER\_ARRAYS\_ONLY | Must be a numeric array | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OBJECT\_ERROR | Error working with a graphical object | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OBJECT\_GETDATE\_FAILED | Unable to get date corresponding to the value | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OBJECT\_GETVALUE\_FAILED | Unable to get value corresponding to the date | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OBJECT\_NOT\_FOUND | Graphical object was not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OBJECT\_WRONG\_PROPERTY | Wrong ID of a graphical object property | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_ONEDIM\_ARRAYS\_ONLY | Must be a one-dimensional array | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_BUFFER\_CREATE | Failed to create an [OpenCL buffer](../Working-with-OpenCL/CLBufferCreate/CLBufferCreate.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_CONTEXT\_CREATE | Error creating the [OpenCL context](../Working-with-OpenCL/CLContextCreate/CLContextCreate.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_EXECUTE | [OpenCL program](../Working-with-OpenCL/CLExecute/CLExecute.md) runtime error | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_INTERNAL | Internal error occurred when [running OpenCL](../Working-with-OpenCL/CLExecute/CLExecute.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_INVALID\_HANDLE | Invalid [OpenCL handle](../Working-with-OpenCL/CLProgramCreate/CLProgramCreate.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_KERNEL\_CREATE | Error creating an [OpenCL kernel](../Working-with-OpenCL/CLKernelCreate/CLKernelCreate.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_NOT\_SUPPORTED | [OpenCL functions](../Working-with-OpenCL/Working-with-OpenCL.md) are not supported on this computer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_PROGRAM\_CREATE | Error occurred when [compiling an OpenCL program](../Working-with-OpenCL/CLProgramCreate/CLProgramCreate.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_QUEUE\_CREATE | Failed to create a run queue in OpenCL | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_SET\_KERNEL\_PARAMETER | Error occurred when [setting parameters](../Working-with-OpenCL/CLSetKernelArg/CLSetKernelArg.md) for the OpenCL kernel | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_TOO\_LONG\_KERNEL\_NAME | Too long kernel name [(OpenCL kernel)](../Working-with-OpenCL/CLKernelCreate/CLKernelCreate.md) | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_WRONG\_BUFFER\_OFFSET | Invalid offset in the OpenCL buffer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_OPENCL\_WRONG\_BUFFER\_SIZE | Invalid size of the OpenCL buffer | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_PLAY\_SOUND\_FAILED | Sound playing failed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_RESOURCE\_NAME\_DUPLICATED | The names of the [dynamic](../Common-Functions/ResourceCreate/ResourceCreate.md) and the [static](../MQL5-programs/Resources/Resources.md) resource match | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_RESOURCE\_NAME\_IS\_TOO\_LONG | The resource name exceeds 63 characters | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_RESOURCE\_NOT\_FOUND | Resource with this name has not been found in EX5 | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_RESOURCE\_UNSUPPORTED\_TYPE | Unsupported resource type or its size exceeds 16 Mb | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_SERIES\_ARRAY | Timeseries cannot be used | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_SHORT\_ARRAY\_ONLY | Must be an array of type short | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_SMALL\_ARRAY | Too small array, the starting position is outside the array | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_SMALL\_ASSERIES\_ARRAY | The receiving array is declared as AS\_SERIES, and it is of insufficient size | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_OUT\_OF\_MEMORY | Not enough memory for the string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_RESIZE\_ERROR | Not enough memory for the relocation of string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_SMALL\_LEN | The string length is less than expected | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_TIME\_ERROR | Error converting string to date | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_TOO\_BIGNUMBER | Too large number, more than ULONG\_MAX | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_UNKNOWNTYPE | Unknown data type when converting to a string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRING\_ZEROADDED | 0 added to the string end, a useless operation | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRINGPOS\_OUTOFRANGE | Position outside the string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_STRUCT\_WITHOBJECTS\_ORCLASS | The structure contains objects of strings and/or dynamic arrays and/or structure of such objects and/or classes | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_SUCCESS | The operation completed successfully | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TERMINAL\_WRONG\_PROPERTY | Wrong identifier of the terminal property | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TOO\_LONG\_FILENAME | Too long file name | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TOO\_MANY\_FILES | More than 64 files cannot be opened at the same time | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TOO\_MANY\_FORMATTERS | Amount of format specifiers more than the parameters | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TOO\_MANY\_PARAMETERS | Amount of parameters more than the format specifiers | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TRADE\_DEAL\_NOT\_FOUND | Deal not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TRADE\_DISABLED | Trading by Expert Advisors prohibited | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TRADE\_ORDER\_NOT\_FOUND | Order not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TRADE\_POSITION\_NOT\_FOUND | Position not found | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TRADE\_SEND\_FAILED | Trade request sending failed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_TRADE\_WRONG\_PROPERTY | Wrong trade property ID | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_USER\_ERROR\_FIRST | [User defined](../Common-Functions/SetUserError/SetUserError.md) errors start with this code | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WEBREQUEST\_CONNECT\_FAILED | Failed to connect to specified URL | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WEBREQUEST\_INVALID\_ADDRESS | Invalid URL | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WEBREQUEST\_REQUEST\_FAILED | HTTP request failed | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WEBREQUEST\_TIMEOUT | Timeout exceeded | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_DIRECTORYNAME | Wrong directory name | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_FILEHANDLE | Wrong file handle | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_FILENAME | Invalid file name | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_FORMATSTRING | Invalid format string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_INTERNAL\_PARAMETER | Wrong parameter in the inner call of the client terminal function | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_STRING\_DATE | Wrong date in the string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_STRING\_OBJECT | Damaged string object | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_STRING\_PARAMETER | Damaged parameter of string type | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_WRONG\_STRING\_TIME | Wrong time in the string | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| ERR\_ZEROSIZE\_ARRAY | An array of zero length | [GetLastError](../Checkup/GetLastError/GetLastError.md) |
| FILE\_ACCESS\_DATE | Date of the last access to the file | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_ANSI | Strings of ANSI type (one byte symbols). Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_BIN | Binary read/write mode (without string to string conversion). Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_COMMON | The file path in the common folder of all client terminals \Terminal\Common\Files. Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md), [FileCopy()](../File-Functions/FileCopy/FileCopy.md), [FileMove()](../File-Functions/FileMove/FileMove.md) and in [FileIsExist()](../File-Functions/FileIsExist/FileIsExist.md) functions. | [FileOpen](../File-Functions/FileOpen/FileOpen.md), [FileCopy](../File-Functions/FileCopy/FileCopy.md), [FileMove](../File-Functions/FileMove/FileMove.md), [FileIsExist](../File-Functions/FileIsExist/FileIsExist.md) |
| FILE\_CREATE\_DATE | Date of creation | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_CSV | CSV file (all its elements are converted to strings of the appropriate type, Unicode or ANSI, and separated by separator). Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_END | Get the end of file sign | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_EXISTS | Check the existence | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_ANSI | The file is opened as ANSI (see [FILE\_ANSI](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_BINARY | The file is opened as a binary file (see [FILE\_BIN](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_COMMON | The file is opened in a shared folder of all terminals (see [FILE\_COMMON](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_CSV | The file is opened as CSV (see [FILE\_CSV](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_READABLE | The opened file is readable (see [FILE\_READ](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_TEXT | The file is opened as a text file (see [FILE\_TXT](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_IS\_WRITABLE | The opened file is writable (see [FILE\_WRITE](../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)) | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_LINE\_END | Get the end of line sign | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_MODIFY\_DATE | Date of the last modification | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_POSITION | Position of a pointer in the file | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_READ | File is opened for reading. Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). When opening a file specification of FILE\_WRITE and/or FILE\_READ is required. | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_REWRITE | Possibility for the file rewrite using functions [FileCopy()](../File-Functions/FileCopy/FileCopy.md) and [FileMove()](../File-Functions/FileMove/FileMove.md). The file should exist or should be opened for writing, otherwise the file will not be opened. | [FileCopy](../File-Functions/FileCopy/FileCopy.md), [FileMove](../File-Functions/FileMove/FileMove.md) |
| FILE\_SHARE\_READ | Shared access for reading from several programs. Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md), but it does not replace the necessity to indicate FILE\_WRITE and/or the FILE\_READ flag when opening a file. | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_SHARE\_WRITE | Shared access for writing from several programs. Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md), but it does not replace the necessity to indicate FILE\_WRITE and/or the FILE\_READ flag when opening a file. | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_SIZE | File size in bytes | [FileGetInteger](../File-Functions/FileGetInteger/FileGetInteger.md) |
| FILE\_TXT | Simple text file (the same as csv file, but without taking into account the separators). Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_UNICODE | Strings of UNICODE type (two byte symbols). Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FILE\_WRITE | File is opened for writing. Flag is used in [FileOpen()](../File-Functions/FileOpen/FileOpen.md). When opening a file specification of FILE\_WRITE and/or FILE\_READ is required. | [FileOpen](../File-Functions/FileOpen/FileOpen.md) |
| FLT\_DIG | Number of significant decimal digits for float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_EPSILON | Minimal value, which satisfies the condition:  1.0+DBL\_EPSILON != 1.0 (for float type) | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MANT\_DIG | Bits count in a mantissa for float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MAX | Maximal value, which can be represented by float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MAX\_10\_EXP | Maximal decimal value of exponent degree for float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MAX\_EXP | Maximal binary value of exponent degree for float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MIN | Minimal positive value, which can be represented by float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MIN\_10\_EXP | Minimal decimal value of exponent degree for float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FLT\_MIN\_EXP | Minimal binary value of exponent degree for float type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| FRIDAY | Friday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| GANN\_DOWN\_TREND | Line corresponding to the downward trend | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| GANN\_UP\_TREND | Line corresponding to the uptrend line | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| GATORJAW\_LINE | Jaw line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| GATORLIPS\_LINE | Lips line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| GATORTEETH\_LINE | Teeth line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| IDABORT | "Abort" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDCANCEL | "Cancel" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDCONTINUE | "Continue" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDIGNORE | "Ignore" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDNO | "No" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDOK | "OK" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDRETRY | "Retry" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDTRYAGAIN | "Try Again" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IDYES | "Yes" button has been pressed | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| IND\_AC | Accelerator Oscillator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_AD | Accumulation/Distribution | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_ADX | Average Directional Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_ADXW | ADX by Welles Wilder | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_ALLIGATOR | Alligator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_AMA | Adaptive Moving Average | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_AO | Awesome Oscillator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_ATR | Average True Range | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_BANDS | Bollinger Bands® | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_BEARS | Bears Power | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_BULLS | Bulls Power | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_BWMFI | Market Facilitation Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_CCI | Commodity Channel Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_CHAIKIN | Chaikin Oscillator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_CUSTOM | Custom indicator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_DEMA | Double Exponential Moving Average | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_DEMARKER | DeMarker | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_ENVELOPES | Envelopes | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_FORCE | Force Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_FRACTALS | Fractals | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_FRAMA | Fractal Adaptive Moving Average | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_GATOR | Gator Oscillator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_ICHIMOKU | Ichimoku Kinko Hyo | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_MA | Moving Average | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_MACD | MACD | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_MFI | Money Flow Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_MOMENTUM | Momentum | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_OBV | On Balance Volume | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_OSMA | OsMA | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_RSI | Relative Strength Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_RVI | Relative Vigor Index | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_SAR | Parabolic SAR | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_STDDEV | Standard Deviation | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_STOCHASTIC | Stochastic Oscillator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_TEMA | Triple Exponential Moving Average | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_TRIX | Triple Exponential Moving Averages Oscillator | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_VIDYA | Variable Index Dynamic Average | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_VOLUMES | Volumes | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| IND\_WPR | Williams' Percent Range | [IndicatorCreate](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorParameters](../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) |
| INDICATOR\_CALCULATIONS | Auxiliary buffers for intermediate calculations | [SetIndexBuffer](../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) |
| INDICATOR\_COLOR\_INDEX | Color | [SetIndexBuffer](../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) |
| INDICATOR\_DATA | Data to draw | [SetIndexBuffer](../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) |
| INDICATOR\_DIGITS | Accuracy of drawing of indicator values | [IndicatorSetInteger](../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) |
| INDICATOR\_HEIGHT | Fixed height of the indicator's window (the preprocessor command [#property indicator\_height](../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md)) | [IndicatorSetInteger](../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) |
| INDICATOR\_LEVELCOLOR | Color of the level line | [IndicatorSetInteger](../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) |
| INDICATOR\_LEVELS | Number of levels in the indicator window | [IndicatorSetInteger](../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) |
| INDICATOR\_LEVELSTYLE | Style of the level line | [IndicatorSetInteger](../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) |
| INDICATOR\_LEVELTEXT | Level description | [IndicatorSetString](../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) |
| INDICATOR\_LEVELVALUE | Level value | [IndicatorSetDouble](../Custom-Indicators/IndicatorSetDouble/IndicatorSetDouble.md) |
| INDICATOR\_LEVELWIDTH | Thickness of the level line | [IndicatorSetInteger](../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) |
| INDICATOR\_MAXIMUM | Maximum of the indicator window | [IndicatorSetDouble](../Custom-Indicators/IndicatorSetDouble/IndicatorSetDouble.md) |
| INDICATOR\_MINIMUM | Minimum of the indicator window | [IndicatorSetDouble](../Custom-Indicators/IndicatorSetDouble/IndicatorSetDouble.md) |
| INDICATOR\_SHORTNAME | Short indicator name | [IndicatorSetString](../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) |
| INT\_MAX | Maximal value, which can be represented by int type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| INT\_MIN | Minimal value, which can be represented by int type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| INVALID\_HANDLE | Incorrect handle | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| IS\_DEBUG\_MODE | Flag that a mq5-program operates in debug mode | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| IS\_PROFILE\_MODE | Flag that a mq5-program operates in profiling mode | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| KIJUNSEN\_LINE | Kijun-sen line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| LICENSE\_DEMO | A trial version of a paid product from the Market. It works only in the strategy tester | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| LICENSE\_FREE | A free unlimited version | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| LICENSE\_FULL | A purchased licensed version allows at least 5 activations. The number of activations is specified by seller. Seller may increase the allowed number of activations | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| LICENSE\_TIME | A version with a limited term license | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| LONG\_MAX | Maximal value, which can be represented by long type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| LONG\_MIN | Minimal value, which can be represented by long type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| LOWER\_BAND | Lower limit | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| LOWER\_HISTOGRAM | Bottom histogram | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| LOWER\_LINE | Bottom line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| M\_1\_PI | 1/pi | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_2\_PI | 2/pi | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_2\_SQRTPI | 2/sqrt(pi) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_E | e | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_LN10 | ln(10) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_LN2 | ln(2) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_LOG10E | log10(e) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_LOG2E | log2(e) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_PI | pi | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_PI\_2 | pi/2 | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_PI\_4 | pi/4 | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_SQRT1\_2 | 1/sqrt(2) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| M\_SQRT2 | sqrt(2) | [Mathematical Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Mathematical-Constants/Mathematical-Constants.md) |
| MAIN\_LINE | Main line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| MB\_ABORTRETRYIGNORE | Message window contains three buttons: Abort, Retry and Ignore | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_CANCELTRYCONTINUE | Message window contains three buttons: Cancel, Try Again, Continue | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_DEFBUTTON1 | The first button MB\_DEFBUTTON1 - is default, if the other buttons MB\_DEFBUTTON2, MB\_DEFBUTTON3, or MB\_DEFBUTTON4 are not specified | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_DEFBUTTON2 | The second button is default | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_DEFBUTTON3 | The third button is default | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_DEFBUTTON4 | The fourth button is default | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_ICONEXCLAMATION,  MB\_ICONWARNING | The exclamation/warning sign icon | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_ICONINFORMATION,  MB\_ICONASTERISK | The encircled i sign | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_ICONQUESTION | The question sign icon | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_ICONSTOP,  MB\_ICONERROR,  MB\_ICONHAND | The STOP sign icon | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_OK | Message window contains only one button: OK. Default | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_OKCANCEL | Message window contains two buttons: OK and Cancel | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_RETRYCANCEL | Message window contains two buttons: Retry and Cancel | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_YESNO | Message window contains two buttons: Yes and No | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MB\_YESNOCANCEL | Message window contains three buttons: Yes, No and Cancel | [MessageBox](../Common-Functions/MessageBox/MessageBox.md) |
| MINUSDI\_LINE | Line –DI | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| MODE\_EMA | Exponential averaging | [Smoothing Methods](../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) |
| MODE\_LWMA | Linear-weighted averaging | [Smoothing Methods](../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) |
| MODE\_SMA | Simple averaging | [Smoothing Methods](../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) |
| MODE\_SMMA | Smoothed averaging | [Smoothing Methods](../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) |
| MONDAY | Monday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| MQL\_DEBUG | The flag, that indicates the debug mode | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_DLLS\_ALLOWED | The permission to use DLL for the given executed program | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_FRAME\_MODE | The flag, that indicates the Expert Advisor operating in [gathering optimization result frames mode](../Event-Handling/OnTesterPass/OnTesterPass.md) | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_LICENSE\_TYPE | Type of license of the EX5 module. The license refers to the EX5 module, from which a request is made using MQLInfoInteger(MQL\_LICENSE\_TYPE). | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_MEMORY\_LIMIT | Maximum possible amount of dynamic memory for MQL5 program in MB | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_MEMORY\_USED | The memory size used by MQL5 program in MB | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_OPTIMIZATION | The flag, that indicates the optimization process | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_PROFILER | The flag, that indicates the program operating in the code profiling mode | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_PROGRAM\_NAME | Name of the mql5-program executed | [MQLInfoString](../Checkup/MQLInfoString/MQLInfoString.md) |
| MQL\_PROGRAM\_PATH | Path for the given executed program | [MQLInfoString](../Checkup/MQLInfoString/MQLInfoString.md) |
| MQL\_PROGRAM\_TYPE | Type of the mql5 program | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_SIGNALS\_ALLOWED | The permission to modify the Signals for the given executed program | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_TESTER | The flag, that indicates the tester process | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_TRADE\_ALLOWED | The [permission to trade](../MQL5-programs/Trade-Permission/Trade-Permission.md) for the given executed program | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| MQL\_VISUAL\_MODE | The flag, that indicates the visual tester process | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| NULL | Zero for any types | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| OBJ\_ALL\_PERIODS | The object is drawn in all timeframes | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| [OBJ\_ARROW](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW/OBJ_ARROW.md) | Arrow | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_BUY](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_BUY/OBJ_ARROW_BUY.md) | Buy Sign | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_CHECK](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_CHECK/OBJ_ARROW_CHECK.md) | Check Sign | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_DOWN](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_DOWN/OBJ_ARROW_DOWN.md) | Arrow Down | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_LEFT\_PRICE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_LEFT_PRICE/OBJ_ARROW_LEFT_PRICE.md) | Left Price Label | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_RIGHT\_PRICE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_RIGHT_PRICE/OBJ_ARROW_RIGHT_PRICE.md) | Right Price Label | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_SELL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_SELL/OBJ_ARROW_SELL.md) | Sell Sign | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_STOP](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_STOP/OBJ_ARROW_STOP.md) | Stop Sign | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_THUMB\_DOWN](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_THUMB_DOWN/OBJ_ARROW_THUMB_DOWN.md) | Thumbs Down | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_THUMB\_UP](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_THUMB_UP/OBJ_ARROW_THUMB_UP.md) | Thumbs Up | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROW\_UP](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_UP/OBJ_ARROW_UP.md) | Arrow Up | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ARROWED\_LINE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROWED_LINE/OBJ_ARROWED_LINE.md) | Arrowed Line | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_BITMAP](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP/OBJ_BITMAP.md) | Bitmap | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_BITMAP\_LABEL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) | Bitmap Label | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_BUTTON](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BUTTON/OBJ_BUTTON.md) | Button | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_CHANNEL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_CHANNEL/OBJ_CHANNEL.md) | Equidistant Channel | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_CHART](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_CHART/OBJ_CHART.md) | Chart | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_CYCLES](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_CYCLES/OBJ_CYCLES.md) | Cycle Lines | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_EDIT](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_EDIT/OBJ_EDIT.md) | Edit | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ELLIOTWAVE3](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ELLIOTWAVE3/OBJ_ELLIOTWAVE3.md) | Elliott Correction Wave | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ELLIOTWAVE5](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ELLIOTWAVE5/OBJ_ELLIOTWAVE5.md) | Elliott Motive Wave | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_ELLIPSE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ELLIPSE/OBJ_ELLIPSE.md) | Ellipse | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_EVENT](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_EVENT/OBJ_EVENT.md) | The "Event" object corresponding to an event in the economic calendar | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_EXPANSION](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_EXPANSION/OBJ_EXPANSION.md) | Fibonacci Expansion | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_FIBO](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBO/OBJ_FIBO.md) | Fibonacci Retracement | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_FIBOARC](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOARC/OBJ_FIBOARC.md) | Fibonacci Arcs | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_FIBOCHANNEL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOCHANNEL/OBJ_FIBOCHANNEL.md) | Fibonacci Channel | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_FIBOFAN](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOFAN/OBJ_FIBOFAN.md) | Fibonacci Fan | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_FIBOTIMES](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOTIMES/OBJ_FIBOTIMES.md) | Fibonacci Time Zones | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_GANNFAN](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_GANNFAN/OBJ_GANNFAN.md) | Gann Fan | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_GANNGRID](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_GANNGRID/OBJ_GANNGRID.md) | Gann Grid | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_GANNLINE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_GANNLINE/OBJ_GANNLINE.md) | Gann Line | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_HLINE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_HLINE/OBJ_HLINE.md) | Horizontal Line | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_LABEL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_LABEL/OBJ_LABEL.md) | Label | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| OBJ\_NO\_PERIODS | The object is not drawn in all timeframes | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_D1 | The object is drawn in day charts | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H1 | The object is drawn in 1-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H12 | The object is drawn in 12-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H2 | The object is drawn in 2-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H3 | The object is drawn in 3-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H4 | The object is drawn in 4-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H6 | The object is drawn in 6-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_H8 | The object is drawn in 8-hour chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M1 | The object is drawn in 1-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M10 | The object is drawn in 10-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M12 | The object is drawn in 12-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M15 | The object is drawn in 15-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M2 | The object is drawn in 2-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M20 | The object is drawn in 20-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M3 | The object is drawn in 3-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M30 | The object is drawn in 30-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M4 | The object is drawn in 4-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M5 | The object is drawn in 5-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_M6 | The object is drawn in 6-minute chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_MN1 | The object is drawn in month charts | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJ\_PERIOD\_W1 | The object is drawn in week charts | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| [OBJ\_PITCHFORK](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_PITCHFORK/OBJ_PITCHFORK.md) | Andrews’ Pitchfork | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_RECTANGLE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_RECTANGLE/OBJ_RECTANGLE.md) | Rectangle | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_RECTANGLE\_LABEL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_RECTANGLE_LABEL/OBJ_RECTANGLE_LABEL.md) | The "Rectangle label" object for creating and designing the custom graphical interface. | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_REGRESSION](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_REGRESSION/OBJ_REGRESSION.md) | Linear Regression Channel | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_STDDEVCHANNEL](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_STDDEVCHANNEL/OBJ_STDDEVCHANNEL.md) | Standard Deviation Channel | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_TEXT](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TEXT/OBJ_TEXT.md) | Text | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_TREND](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TREND/OBJ_TREND.md) | Trend Line | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_TRENDBYANGLE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TRENDBYANGLE/OBJ_TRENDBYANGLE.md) | Trend Line By Angle | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_TRIANGLE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TRIANGLE/OBJ_TRIANGLE.md) | Triangle | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| [OBJ\_VLINE](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_VLINE/OBJ_VLINE.md) | Vertical Line | [Object Types](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) |
| OBJPROP\_ALIGN | Horizontal text alignment in the "Edit" object (OBJ\_EDIT) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_ANCHOR | Location of the anchor point of a graphical object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_ANGLE | Angle.  For the objects with no angle specified, created from a program, the value is equal to [EMPTY\_VALUE](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) | [ObjectSetDouble](../Object-Functions/ObjectSetDouble/ObjectSetDouble.md), [ObjectGetDouble](../Object-Functions/ObjectGetDouble/ObjectGetDouble.md) |
| OBJPROP\_ARROWCODE | Arrow code for the Arrow object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_BACK | Object in the background | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_BGCOLOR | The background color for  OBJ\_EDIT, OBJ\_BUTTON, OBJ\_RECTANGLE\_LABEL | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_BMPFILE | The name of BMP-file for Bitmap Label. See also [Resources](../MQL5-programs/Resources/Resources.md) | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_BORDER\_COLOR | Border color for the OBJ\_EDIT and OBJ\_BUTTON objects | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_BORDER\_TYPE | Border type for the "Rectangle label" object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_CHART\_ID | ID of the "Chart" object ([OBJ\_CHART](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md)). It allows working with the properties of this object like with a normal chart using the functions described in [Chart Operations](../Chart-Operations/Chart-Operations.md), but there some [exceptions](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#objprop_chart_id_exception). | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_CHART\_SCALE | The scale for the Chart object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_COLOR | Color | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_CORNER | The corner of the chart to link a graphical object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_CREATETIME | Time of object creation | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_DATE\_SCALE | Displaying the time scale for the Chart object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_DEGREE | Level of the Elliott Wave Marking | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_DEVIATION | Deviation for the Standard Deviation Channel | [ObjectSetDouble](../Object-Functions/ObjectSetDouble/ObjectSetDouble.md), [ObjectGetDouble](../Object-Functions/ObjectGetDouble/ObjectGetDouble.md) |
| OBJPROP\_DIRECTION | Trend of the Gann object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_DRAWLINES | Displaying lines for marking the Elliott Wave | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_ELLIPSE | Showing the full ellipse of the Fibonacci Arc object ([OBJ\_FIBOARC](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md)) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_FILL | Fill an object with color (for OBJ\_RECTANGLE, OBJ\_TRIANGLE, OBJ\_ELLIPSE, OBJ\_CHANNEL, OBJ\_STDDEVCHANNEL, OBJ\_REGRESSION) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_FONT | Font | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_FONTSIZE | Font size | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_HIDDEN | Prohibit showing of the name of a graphical object in the list of objects from the terminal menu "Charts" - "Objects" - "List of objects". The true value allows to hide an object from the list. By default, true is set to the objects that display calendar events, trading history and to the objects [created from MQL5 programs](../Object-Functions/ObjectCreate/ObjectCreate.md). To see such [graphical objects](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) and access their properties, click on the "All" button in the "List of objects" window. | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_LEVELCOLOR | Color of the line-level | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_LEVELS | Number of levels | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_LEVELSTYLE | Style of the line-level | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_LEVELTEXT | Level description | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_LEVELVALUE | Level value | [ObjectSetDouble](../Object-Functions/ObjectSetDouble/ObjectSetDouble.md), [ObjectGetDouble](../Object-Functions/ObjectGetDouble/ObjectGetDouble.md) |
| OBJPROP\_LEVELWIDTH | Thickness of the line-level | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_NAME | Object name | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_PERIOD | Timeframe for the Chart object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_PRICE | Price coordinate | [ObjectSetDouble](../Object-Functions/ObjectSetDouble/ObjectSetDouble.md), [ObjectGetDouble](../Object-Functions/ObjectGetDouble/ObjectGetDouble.md) |
| OBJPROP\_PRICE\_SCALE | Displaying the price scale for the Chart object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_RAY | A vertical line goes through all the windows of a chart | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_RAY\_LEFT | Ray goes to the left | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_RAY\_RIGHT | Ray goes to the right | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_READONLY | Ability to edit text in the Edit object | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_SCALE | Scale (properties of Gann objects and Fibonacci Arcs) | [ObjectSetDouble](../Object-Functions/ObjectSetDouble/ObjectSetDouble.md), [ObjectGetDouble](../Object-Functions/ObjectGetDouble/ObjectGetDouble.md) |
| OBJPROP\_SELECTABLE | Object availability | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_SELECTED | Object is selected | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_STATE | Button state (pressed / depressed) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_STYLE | Style | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_SYMBOL | Symbol for the Chart object | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_TEXT | Description of the object (the text contained in the object) | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_TIME | Time coordinate | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_TIMEFRAMES | Visibility of an object at timeframes | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_TOOLTIP | The text of a tooltip. If the property is not set, then the tooltip generated automatically by the terminal is shown. A tooltip can be disabled by setting the "\n" (line feed) value to it | [ObjectSetString](../Object-Functions/ObjectSetString/ObjectSetString.md), [ObjectGetString](../Object-Functions/ObjectGetString/ObjectGetString.md) |
| OBJPROP\_TYPE | Object type | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_WIDTH | Line thickness | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_XDISTANCE | The distance in pixels along the X axis from the binding corner (see [note](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#distance_fixedsize)) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_XOFFSET | The X coordinate of the upper left corner of the [rectangular visible area](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#visual_rectangle) in the graphical objects "Bitmap Label" and "Bitmap" (OBJ\_BITMAP\_LABEL and OBJ\_BITMAP). The value is set in pixels relative to the upper left corner of the original image. | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_XSIZE | The object's width along the X axis in pixels. Specified for  OBJ\_LABEL (read only), OBJ\_BUTTON, OBJ\_CHART, OBJ\_BITMAP, OBJ\_BITMAP\_LABEL, OBJ\_EDIT, OBJ\_RECTANGLE\_LABEL objects. | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_YDISTANCE | The distance in pixels along the Y axis from the binding corner (see [note](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#distance_fixedsize)) | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_YOFFSET | The Y coordinate of the upper left corner of the [rectangular visible area](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#visual_rectangle) in the graphical objects "Bitmap Label" and "Bitmap" (OBJ\_BITMAP\_LABEL and OBJ\_BITMAP). The value is set in pixels relative to the upper left corner of the original image. | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_YSIZE | The object's height along the Y axis in pixels. Specified for  OBJ\_LABEL (read only), OBJ\_BUTTON, OBJ\_CHART, OBJ\_BITMAP, OBJ\_BITMAP\_LABEL, OBJ\_EDIT, OBJ\_RECTANGLE\_LABEL objects. | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| OBJPROP\_ZORDER | Priority of a graphical object for receiving events of clicking on a chart ([CHARTEVENT\_CLICK](../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md)). The default zero value is set when creating an object; the priority can be increased if necessary. When applying objects one over another, only one of them with the highest priority will receive the CHARTEVENT\_CLICK event. | [ObjectSetInteger](../Object-Functions/ObjectSetInteger/ObjectSetInteger.md), [ObjectGetInteger](../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) |
| ORDER\_COMMENT | Order comment | [OrderGetString](../Trade-Functions/OrderGetString/OrderGetString.md), [HistoryOrderGetString](../Trade-Functions/HistoryOrderGetString/HistoryOrderGetString.md) |
| ORDER\_FILLING\_FOK | This filling policy means that an order can be filled only in the specified amount. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The required volume can be filled using several offers available on the market at the moment. | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_FILLING\_IOC | This mode means that a trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. In case the the entire volume of an order cannot be filled, the available volume of it will be filled, and the remaining volume will be canceled. | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_FILLING\_RETURN | This policy is used only for market orders (ORDER\_TYPE\_BUY and ORDER\_TYPE\_SELL), limit and stop limit orders (ORDER\_TYPE\_BUY\_LIMIT, ORDER\_TYPE\_SELL\_LIMIT, ORDER\_TYPE\_BUY\_STOP\_LIMIT and ORDER\_TYPE\_SELL\_STOP\_LIMIT ) and only for the symbols with Market or Exchange [execution](../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_trade_execution). In case of partial filling a market or limit order with remaining volume is not canceled but processed further.  For the activation of the ORDER\_TYPE\_BUY\_STOP\_LIMIT and ORDER\_TYPE\_SELL\_STOP\_LIMIT orders, a corresponding limit order ORDER\_TYPE\_BUY\_LIMIT/ORDER\_TYPE\_SELL\_LIMIT with the ORDER\_FILLING\_RETURN execution type is created. | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_MAGIC | ID of an Expert Advisor that has placed the order (designed to ensure that each Expert Advisor places its own unique number) | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_POSITION\_ID | [Position identifier](../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer) that is set to an order as soon as it is executed. Each executed order results in a [deal](../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md) that opens or modifies an already existing position. The identifier of exactly this position is set to the executed order at this moment. | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_PRICE\_CURRENT | The current price of the order symbol | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| ORDER\_PRICE\_OPEN | Price specified in the order | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| ORDER\_PRICE\_STOPLIMIT | The Limit order price for the StopLimit order | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| ORDER\_SL | Stop Loss value | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| ORDER\_STATE | Order state | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_CANCELED | Order canceled by client | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_EXPIRED | Order expired | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_FILLED | Order fully executed | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_PARTIAL | Order partially executed | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_PLACED | Order accepted | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_REJECTED | Order rejected | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_REQUEST\_ADD | Order is being registered (placing to the trading system) | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_REQUEST\_CANCEL | Order is being deleted (deleting from the trading system) | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_REQUEST\_MODIFY | Order is being modified (changing its parameters) | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_STATE\_STARTED | Order checked, but not yet accepted by broker | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_SYMBOL | Symbol of the order | [OrderGetString](../Trade-Functions/OrderGetString/OrderGetString.md), [HistoryOrderGetString](../Trade-Functions/HistoryOrderGetString/HistoryOrderGetString.md) |
| ORDER\_TIME\_DAY | Good till current trade day order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_DONE | Order execution or cancellation time | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_DONE\_MSC | Order execution/cancellation time in milliseconds since 01.01.1970 | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_EXPIRATION | Order expiration time | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_GTC | Good till cancel order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_SETUP | Order setup time | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_SETUP\_MSC | The time of placing an order for execution in milliseconds since 01.01.1970 | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_SPECIFIED | Good till expired order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TIME\_SPECIFIED\_DAY | The order will be effective till 23:59:59 of the specified day. If this time is outside a trading session, the order expires in the nearest trading time. | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TP | Take Profit value | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| ORDER\_TYPE | Order type | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_BUY | Market Buy order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_BUY\_LIMIT | Buy Limit pending order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_BUY\_STOP | Buy Stop pending order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_BUY\_STOP\_LIMIT | Upon reaching the order price, a pending Buy Limit order is placed at the StopLimit price | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_FILLING | Order filling type | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_SELL | Market Sell order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_SELL\_LIMIT | Sell Limit pending order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_SELL\_STOP | Sell Stop pending order | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_SELL\_STOP\_LIMIT | Upon reaching the order price, a pending Sell Limit order is placed at the StopLimit price | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_TYPE\_TIME | Order lifetime | [OrderGetInteger](../Trade-Functions/OrderGetInteger/OrderGetInteger.md), [HistoryOrderGetInteger](../Trade-Functions/HistoryOrderGetInteger/HistoryOrderGetInteger.md) |
| ORDER\_VOLUME\_CURRENT | Order current volume | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| ORDER\_VOLUME\_INITIAL | Order initial volume | [OrderGetDouble](../Trade-Functions/OrderGetDouble/OrderGetDouble.md), [HistoryOrderGetDouble](../Trade-Functions/HistoryOrderGetDouble/HistoryOrderGetDouble.md) |
| PERIOD\_CURRENT | Current timeframe | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_D1 | 1 day | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H1 | 1 hour | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H12 | 12 hours | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H2 | 2 hours | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H3 | 3 hours | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H4 | 4 hours | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H6 | 6 hours | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_H8 | 8 hours | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M1 | 1 minute | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M10 | 10 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M12 | 12 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M15 | 15 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M2 | 2 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M20 | 20 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M3 | 3 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M30 | 30 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M4 | 4 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M5 | 5 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_M6 | 6 minutes | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_MN1 | 1 month | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PERIOD\_W1 | 1 week | [Chart Timeframes](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| PLOT\_ARROW | Arrow code for style DRAW\_ARROW | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_ARROW\_SHIFT | Vertical shift of arrows for style DRAW\_ARROW | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_COLOR\_INDEXES | The number of colors | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_DRAW\_BEGIN | Number of initial bars without drawing and values in the DataWindow | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_DRAW\_TYPE | Type of graphical construction | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_EMPTY\_VALUE | An empty value for plotting, for which there is no drawing | [PlotIndexSetDouble](../Custom-Indicators/PlotIndexSetDouble/PlotIndexSetDouble.md) |
| PLOT\_LABEL | The name of the indicator graphical series to display in the DataWindow. When working with complex graphical styles requiring several indicator buffers for display, the names for each buffer can be specified using ";" as a separator. Sample code is shown in [DRAW\_CANDLES](../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_CANDLES/DRAW_CANDLES.md) | [PlotIndexSetString](../Custom-Indicators/PlotIndexSetString/PlotIndexSetString.md) |
| PLOT\_LINE\_COLOR | The index of a buffer containing the drawing color | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_LINE\_STYLE | Drawing line style | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_LINE\_WIDTH | The thickness of the drawing line | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_SHIFT | Shift of indicator plotting along the time axis in bars | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLOT\_SHOW\_DATA | Sign of display of construction values in the DataWindow | [PlotIndexSetInteger](../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md), [PlotIndexGetInteger](../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md) |
| PLUSDI\_LINE | Line +DI | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| POINTER\_AUTOMATIC | Pointer of any objects created automatically (not using new()) | [CheckPointer](../Common-Functions/CheckPointer/CheckPointer.md) |
| POINTER\_DYNAMIC | Pointer of the object created by the [new()](../Language-Basics/Operators/Object-Create-Operator-new/Object-Create-Operator-new.md) operator | [CheckPointer](../Common-Functions/CheckPointer/CheckPointer.md) |
| POINTER\_INVALID | Incorrect pointer | [CheckPointer](../Common-Functions/CheckPointer/CheckPointer.md) |
| POSITION\_COMMENT | Position comment | [PositionGetString](../Trade-Functions/PositionGetString/PositionGetString.md) |
| POSITION\_COMMISSION | Commission | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_IDENTIFIER | Position identifier is a unique number that is assigned to every newly opened position and doesn't change during the entire lifetime of the position. Position turnover doesn't change its identifier. | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_MAGIC | Position magic number (see [ORDER\_MAGIC](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)) | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_PRICE\_CURRENT | Current price of the position symbol | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_PRICE\_OPEN | Position open price | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_PROFIT | Current profit | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_SL | Stop Loss level of opened position | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_SWAP | Cumulative swap | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_SYMBOL | Symbol of the position | [PositionGetString](../Trade-Functions/PositionGetString/PositionGetString.md) |
| POSITION\_TIME | Position open time | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_TIME\_MSC | Position opening time in milliseconds since 01.01.1970 | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_TIME\_UPDATE | Position changing time in seconds since 01.01.1970 | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_TIME\_UPDATE\_MSC | Position changing time in milliseconds since 01.01.1970 | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_TP | Take Profit level of opened position | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| POSITION\_TYPE | Position type | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_TYPE\_BUY | Buy | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_TYPE\_SELL | Sell | [PositionGetInteger](../Trade-Functions/PositionGetInteger/PositionGetInteger.md) |
| POSITION\_VOLUME | Position volume | [PositionGetDouble](../Trade-Functions/PositionGetDouble/PositionGetDouble.md) |
| PRICE\_CLOSE | Close price | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PRICE\_HIGH | The maximum price for the period | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PRICE\_LOW | The minimum price for the period | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PRICE\_MEDIAN | Median price, (high + low)/2 | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PRICE\_OPEN | Open price | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PRICE\_TYPICAL | Typical price, (high + low + close)/3 | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PRICE\_WEIGHTED | Average price, (high + low + close + close)/4 | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| PROGRAM\_EXPERT | Expert | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| PROGRAM\_INDICATOR | Indicator | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| PROGRAM\_SCRIPT | Script | [MQLInfoInteger](../Checkup/MQLInfoInteger/MQLInfoInteger.md) |
| REASON\_ACCOUNT | Another account has been activated or reconnection to the trade server has occurred due to changes in the account settings | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_CHARTCHANGE | Symbol or chart period has been changed | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_CHARTCLOSE | Chart has been closed | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_CLOSE | Terminal has been closed | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_INITFAILED | This value means that [OnInit()](../Event-Handling/OnInit/OnInit.md) handler has returned a nonzero value | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_PARAMETERS | Input parameters have been changed by a user | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_PROGRAM | Expert Advisor terminated its operation by calling the [ExpertRemove()](../Common-Functions/ExpertRemove/ExpertRemove.md) function | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_RECOMPILE | Program has been recompiled | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_REMOVE | Program has been deleted from the chart | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| REASON\_TEMPLATE | A new template has been applied | [UninitializeReason](../Checkup/UninitializeReason/UninitializeReason.md), [OnDeinit](../Event-Handling/OnDeinit/OnDeinit.md) |
| SATURDAY | Saturday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| SEEK\_CUR | Current position of a file pointer | [FileSeek](../File-Functions/FileSeek/FileSeek.md) |
| SEEK\_END | File end | [FileSeek](../File-Functions/FileSeek/FileSeek.md) |
| SEEK\_SET | File beginning | [FileSeek](../File-Functions/FileSeek/FileSeek.md) |
| SENKOUSPANA\_LINE | Senkou Span A line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| SENKOUSPANB\_LINE | Senkou Span B line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| SERIES\_BARS\_COUNT | Bars count for the symbol-period for the current moment | [SeriesInfoInteger](../Timeseries-and-Indicators-Access/SeriesInfoInteger/SeriesInfoInteger.md) |
| SERIES\_FIRSTDATE | The very first date for the symbol-period for the current moment | [SeriesInfoInteger](../Timeseries-and-Indicators-Access/SeriesInfoInteger/SeriesInfoInteger.md) |
| SERIES\_LASTBAR\_DATE | Open time of the last bar of the symbol-period | [SeriesInfoInteger](../Timeseries-and-Indicators-Access/SeriesInfoInteger/SeriesInfoInteger.md) |
| SERIES\_SERVER\_FIRSTDATE | The very first date in the history of the symbol on the server regardless of the timeframe | [SeriesInfoInteger](../Timeseries-and-Indicators-Access/SeriesInfoInteger/SeriesInfoInteger.md) |
| SERIES\_SYNCHRONIZED | Symbol/period data synchronization flag for the current moment | [SeriesInfoInteger](../Timeseries-and-Indicators-Access/SeriesInfoInteger/SeriesInfoInteger.md) |
| SERIES\_TERMINAL\_FIRSTDATE | The very first date in the history of the symbol in the client terminal, regardless of the timeframe | [SeriesInfoInteger](../Timeseries-and-Indicators-Access/SeriesInfoInteger/SeriesInfoInteger.md) |
| SHORT\_MAX | Maximal value, which can be represented by short type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| SHORT\_MIN | Minimal value, which can be represented by short type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| SIGNAL\_BASE\_AUTHOR\_LOGIN | Author login | [SignalBaseGetString](../Trade-Signals/SignalBaseGetString/SignalBaseGetString.md) |
| SIGNAL\_BASE\_BALANCE | Account balance | [SignalBaseGetDouble](../Trade-Signals/SignalBaseGetDouble/SignalBaseGetDouble.md) |
| SIGNAL\_BASE\_BROKER | Broker name (company) | [SignalBaseGetString](../Trade-Signals/SignalBaseGetString/SignalBaseGetString.md) |
| SIGNAL\_BASE\_BROKER\_SERVER | Broker server | [SignalBaseGetString](../Trade-Signals/SignalBaseGetString/SignalBaseGetString.md) |
| SIGNAL\_BASE\_CURRENCY | Signal base currency | [SignalBaseGetString](../Trade-Signals/SignalBaseGetString/SignalBaseGetString.md) |
| SIGNAL\_BASE\_DATE\_PUBLISHED | Publication date (date when it become available for subscription) | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_DATE\_STARTED | Monitoring starting date | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_EQUITY | Account equity | [SignalBaseGetDouble](../Trade-Signals/SignalBaseGetDouble/SignalBaseGetDouble.md) |
| SIGNAL\_BASE\_GAIN | Account gain | [SignalBaseGetDouble](../Trade-Signals/SignalBaseGetDouble/SignalBaseGetDouble.md) |
| SIGNAL\_BASE\_ID | Signal ID | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_LEVERAGE | Account leverage | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_MAX\_DRAWDOWN | Account maximum drawdown | [SignalBaseGetDouble](../Trade-Signals/SignalBaseGetDouble/SignalBaseGetDouble.md) |
| SIGNAL\_BASE\_NAME | Signal name | [SignalBaseGetString](../Trade-Signals/SignalBaseGetString/SignalBaseGetString.md) |
| SIGNAL\_BASE\_PIPS | Profit in pips | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_PRICE | Signal subscription price | [SignalBaseGetDouble](../Trade-Signals/SignalBaseGetDouble/SignalBaseGetDouble.md) |
| SIGNAL\_BASE\_RATING | Position in rating | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_ROI | Return on Investment (%) | [SignalBaseGetDouble](../Trade-Signals/SignalBaseGetDouble/SignalBaseGetDouble.md) |
| SIGNAL\_BASE\_SUBSCRIBERS | Number of subscribers | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_TRADE\_MODE | Account type (0-real, 1-demo, 2-contest) | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_BASE\_TRADES | Number of trades | [SignalBaseGetInteger](../Trade-Signals/SignalBaseGetInteger/SignalBaseGetInteger.md) |
| SIGNAL\_INFO\_CONFIRMATIONS\_DISABLED | The flag enables synchronization without confirmation dialog | [SignalInfoGetInteger](../Trade-Signals/SignalInfoGetInteger/SignalInfoGetInteger.md), [SignalInfoSetInteger](../Trade-Signals/SignalInfoSetInteger/SignalInfoSetInteger.md) |
| SIGNAL\_INFO\_COPY\_SLTP | Copy Stop Loss and Take Profit flag | [SignalInfoGetInteger](../Trade-Signals/SignalInfoGetInteger/SignalInfoGetInteger.md), [SignalInfoSetInteger](../Trade-Signals/SignalInfoSetInteger/SignalInfoSetInteger.md) |
| SIGNAL\_INFO\_DEPOSIT\_PERCENT | Deposit percent (%) | [SignalInfoGetInteger](../Trade-Signals/SignalInfoGetInteger/SignalInfoGetInteger.md), [SignalInfoSetInteger](../Trade-Signals/SignalInfoSetInteger/SignalInfoSetInteger.md) |
| SIGNAL\_INFO\_EQUITY\_LIMIT | Equity limit | [SignalInfoGetDouble](../Trade-Signals/SignalInfoGetDouble/SignalInfoGetDouble.md), [SignalInfoSetDouble](../Trade-Signals/SignalInfoSetDouble/SignalInfoSetDouble.md) |
| SIGNAL\_INFO\_ID | Signal id, r/o | [SignalInfoGetInteger](../Trade-Signals/SignalInfoGetInteger/SignalInfoGetInteger.md), [SignalInfoSetInteger](../Trade-Signals/SignalInfoSetInteger/SignalInfoSetInteger.md) |
| SIGNAL\_INFO\_NAME | Signal name, r/o | [SignalInfoGetString](../Trade-Signals/SignalInfoGetString/SignalInfoGetString.md) |
| SIGNAL\_INFO\_SLIPPAGE | Slippage (used when placing market orders in synchronization of positions and copying of trades) | [SignalInfoGetDouble](../Trade-Signals/SignalInfoGetDouble/SignalInfoGetDouble.md), [SignalInfoSetDouble](../Trade-Signals/SignalInfoSetDouble/SignalInfoSetDouble.md) |
| SIGNAL\_INFO\_SUBSCRIPTION\_ENABLED | "Copy trades by subscription" permission flag | [SignalInfoGetInteger](../Trade-Signals/SignalInfoGetInteger/SignalInfoGetInteger.md), [SignalInfoSetInteger](../Trade-Signals/SignalInfoSetInteger/SignalInfoSetInteger.md) |
| SIGNAL\_INFO\_TERMS\_AGREE | "Agree to terms of use of Signals service" flag, r/o | [SignalInfoGetInteger](../Trade-Signals/SignalInfoGetInteger/SignalInfoGetInteger.md), [SignalInfoSetInteger](../Trade-Signals/SignalInfoSetInteger/SignalInfoSetInteger.md) |
| SIGNAL\_INFO\_VOLUME\_PERCENT | Maximum percent of deposit used (%), r/o | [SignalInfoGetDouble](../Trade-Signals/SignalInfoGetDouble/SignalInfoGetDouble.md), [SignalInfoSetDouble](../Trade-Signals/SignalInfoSetDouble/SignalInfoSetDouble.md) |
| SIGNAL\_LINE | Signal line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| STAT\_BALANCE\_DD | Maximum balance drawdown in monetary terms. In the process of trading, a balance may have numerous drawdowns; here the largest value is taken | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_BALANCE\_DD\_RELATIVE | Balance drawdown in monetary terms that was recorded at the moment of the maximum balance drawdown as a percentage (STAT\_BALANCE\_DDREL\_PERCENT). | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_BALANCE\_DDREL\_PERCENT | Maximum balance drawdown as a percentage. In the process of trading, a balance may have numerous drawdowns, for each of which the relative drawdown value in percents is calculated. The greatest value is returned | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_BALANCEDD\_PERCENT | Balance drawdown as a percentage that was recorded at the moment of the maximum balance drawdown in monetary terms (STAT\_BALANCE\_DD). | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_BALANCEMIN | Minimum balance value | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_CONLOSSMAX | Maximum loss in a series of losing trades. The value is less than or equal to zero | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_CONLOSSMAX\_TRADES | The number of trades that have formed STAT\_CONLOSSMAX (maximum loss in a series of losing trades) | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_CONPROFITMAX | Maximum profit in a series of profitable trades. The value is greater than or equal to zero | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_CONPROFITMAX\_TRADES | The number of trades that have formed STAT\_CONPROFITMAX (maximum profit in a series of profitable trades) | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_CUSTOM\_ONTESTER | The value of the calculated custom optimization criterion returned by the [OnTester()](../Event-Handling/OnTester/OnTester.md) function | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_DEALS | The number of deals | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_EQUITY\_DD | Maximum equity drawdown in monetary terms. In the process of trading, numerous drawdowns may appear on the equity; here the largest value is taken | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_EQUITY\_DD\_RELATIVE | Equity drawdown in monetary terms that was recorded at the moment of the maximum equity drawdown in percent (STAT\_EQUITY\_DDREL\_PERCENT). | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_EQUITY\_DDREL\_PERCENT | Maximum equity drawdown as a percentage. In the process of trading, an equity may have numerous drawdowns, for each of which the relative drawdown value in percents is calculated. The greatest value is returned | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_EQUITYDD\_PERCENT | Drawdown in percent that was recorded at the moment of the maximum equity drawdown in monetary terms (STAT\_EQUITY\_DD). | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_EQUITYMIN | Minimum equity value | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_EXPECTED\_PAYOFF | Expected payoff | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_GROSS\_LOSS | Total loss, the sum of all negative trades. The value is less than or equal to zero | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_GROSS\_PROFIT | Total profit, the sum of all profitable (positive) trades. The value is greater than or equal to zero | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_INITIAL\_DEPOSIT | The value of the initial deposit | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_LONG\_TRADES | Long trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_LOSS\_TRADES | Losing trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_LOSSTRADES\_AVGCON | Average length of a losing series of trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MAX\_CONLOSS\_TRADES | The number of trades in the longest series of losing trades STAT\_MAX\_CONLOSSES | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MAX\_CONLOSSES | The total loss of the longest series of losing trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MAX\_CONPROFIT\_TRADES | The number of trades in the longest series of profitable trades STAT\_MAX\_CONWINS | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MAX\_CONWINS | The total profit of the longest series of profitable trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MAX\_LOSSTRADE | Maximum loss – the lowest value of all losing trades. The value is less than or equal to zero | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MAX\_PROFITTRADE | Maximum profit – the largest value of all profitable trades. The value is greater than or equal to zero | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_MIN\_MARGINLEVEL | Minimum value of the margin level | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_PROFIT | Net profit after testing, the sum of STAT\_GROSS\_PROFIT and STAT\_GROSS\_LOSS (STAT\_GROSS\_LOSS is always less than or equal to zero) | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_PROFIT\_FACTOR | Profit factor, equal to  the ratio of STAT\_GROSS\_PROFIT/STAT\_GROSS\_LOSS. If STAT\_GROSS\_LOSS=0, the profit factor is equal to [DBL\_MAX](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_PROFIT\_LONGTRADES | Profitable long trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_PROFIT\_SHORTTRADES | Profitable short trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_PROFIT\_TRADES | Profitable trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_PROFITTRADES\_AVGCON | Average length of a profitable series of trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_RECOVERY\_FACTOR | Recovery factor, equal to the ratio of STAT\_PROFIT/STAT\_BALANCE\_DD | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_SHARPE\_RATIO | Sharpe ratio | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_SHORT\_TRADES | Short trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_TRADES | The number of trades | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STAT\_WITHDRAWAL | Money withdrawn from an account | [TesterStatistics](../Common-Functions/TesterStatistics/TesterStatistics.md) |
| STO\_CLOSECLOSE | Calculation is based on Close/Close prices | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| STO\_LOWHIGH | Calculation is based on Low/High prices | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| STYLE\_DASH | Broken line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) |
| STYLE\_DASHDOT | Dash-dot line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) |
| STYLE\_DASHDOTDOT | Dash - two points | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) |
| STYLE\_DOT | Dotted line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) |
| STYLE\_SOLID | Solid line | [Drawing Styles](../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) |
| SUNDAY | Sunday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| SYMBOL\_ASK | Ask - best buy offer | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_ASKHIGH | Maximal Ask of the day | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_ASKLOW | Minimal Ask of the day | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_BANK | Feeder of the current quote | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_BASIS | The underlying asset of a derivative | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_BID | Bid - best sell offer | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_BIDHIGH | Maximal Bid of the day | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_BIDLOW | Minimal Bid of the day | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_CALC\_MODE\_CFD | CFD mode - calculation of margin and profit for CFD | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_CFDINDEX | CFD index mode - calculation of margin and profit for CFD by indexes | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_CFDLEVERAGE | CFD Leverage mode - calculation of margin and profit for CFD at leverage trading | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_EXCH\_FUTURES | Futures mode –  calculation of margin and profit for trading futures contracts on a stock exchange | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_EXCH\_FUTURES\_FORTS | FORTS Futures mode –  calculation of margin and profit for trading futures contracts on FORTS. | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_EXCH\_STOCKS | Exchange mode – calculation of margin and profit for trading securities on a stock exchange | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_FOREX | Forex mode - calculation of profit and margin for Forex | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_FUTURES | Futures mode - calculation of margin and profit for futures | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CALC\_MODE\_SERV\_COLLATERAL | Collateral mode - a symbol is used as a non-tradable asset on a trading account. | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_CURRENCY\_BASE | Basic currency of a symbol | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_CURRENCY\_MARGIN | Margin currency | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_CURRENCY\_PROFIT | Profit currency | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_DESCRIPTION | Symbol description | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_DIGITS | Digits after a decimal point | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_EXPIRATION\_DAY | The order is valid till the end of the day | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_EXPIRATION\_GTC | The order is valid during the unlimited time period, until it is explicitly canceled | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_EXPIRATION\_MODE | Flags of allowed order [expiration modes](../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_expiration_mode) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_EXPIRATION\_SPECIFIED | The expiration time is specified in the order | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_EXPIRATION\_SPECIFIED\_DAY | The expiration date is specified in the order | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_EXPIRATION\_TIME | Date of the symbol trade end (usually used for futures) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_FILLING\_FOK | This policy means that a deal can be executed only with the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The required volume can be filled using several offers available on the market at the moment. | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_FILLING\_IOC | In this case a trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. In case the order cannot be filled completely, the available volume of the order will be filled, and the remaining volume will be canceled. The possibility of using IOC orders is determined at the trade server. | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_FILLING\_MODE | Flags of allowed order [filling modes](../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_filling_mode) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ISIN | The name of a symbol in the ISIN system (International Securities Identification Number). The International Securities Identification Number is a 12-digit alphanumeric code that uniquely identifies a security. The presence of this symbol property is determined on the side of a trade server. | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_LAST | Price of the last deal | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_LASTHIGH | Maximal Last of the day | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_LASTLOW | Minimal Last of the day | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_MARGIN\_INITIAL | Initial margin means the amount in the margin currency required for opening a position with the volume of one lot. It is used for checking a client's assets when he or she enters the market. | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_MARGIN\_MAINTENANCE | The maintenance margin. If it is set, it sets the margin amount in the margin currency of the symbol, charged from one lot. It is used for checking a client's assets when his/her account state changes. If the maintenance margin is equal to 0, the initial margin is used. | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_OPTION\_MODE | Option type | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_OPTION\_MODE\_EUROPEAN | European option may only be exercised on a specified date (expiration, execution date, delivery date) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_OPTION\_MODE\_AMERICAN | American option may be exercised on any trading day on or before expiry. The period within which a buyer can exercise the option is specified for it | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_OPTION\_RIGHT | Option right (Call/Put) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_OPTION\_RIGHT\_CALL | A call option gives you the right to buy an asset at a specified price | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_OPTION\_RIGHT\_PUT | A put option gives you the right to sell an asset at a specified price | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_OPTION\_STRIKE | The strike price of an option. The price at which an option buyer can buy (in a Call option) or sell (in a Put option) the underlying asset, and the option seller is obliged to sell or buy the appropriate amount of the underlying asset. | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_ORDER\_LIMIT | Limit orders are allowed (Buy Limit and Sell Limit) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ORDER\_MARKET | Market orders are allowed (Buy and Sell) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ORDER\_MODE | Flags of allowed [order types](../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_order_mode) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ORDER\_SL | Stop Loss is allowed | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ORDER\_STOP | Stop orders are allowed (Buy Stop and Sell Stop) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ORDER\_STOP\_LIMIT | Stop-limit orders are allowed (Buy Stop Limit and Sell Stop Limit) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_ORDER\_TP | Take Profit is allowed | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_PATH | Path in the symbol tree | [SymbolInfoString](../Market-Info/SymbolInfoString/SymbolInfoString.md) |
| SYMBOL\_POINT | Symbol point value | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SELECT | Symbol is selected in Market Watch | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SESSION\_AW | Average weighted price of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_BUY\_ORDERS | Number of Buy orders at the moment | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SESSION\_BUY\_ORDERS\_VOLUME | Current volume of Buy orders | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_CLOSE | Close price of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_DEALS | Number of deals in the current session | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SESSION\_INTEREST | Summary open interest | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_OPEN | Open price of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_PRICE\_LIMIT\_MAX | Maximal price of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_PRICE\_LIMIT\_MIN | Minimal price of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_PRICE\_SETTLEMENT | Settlement price of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_SELL\_ORDERS | Number of Sell orders at the moment | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SESSION\_SELL\_ORDERS\_VOLUME | Current volume of Sell orders | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_TURNOVER | Summary turnover of the current session | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SESSION\_VOLUME | Summary volume of current session deals | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SPREAD | Spread value in points | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SPREAD\_FLOAT | Indication of a floating spread | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_START\_TIME | Date of the symbol trade beginning (usually used for futures) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_LONG | Long swap value | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_SWAP\_MODE | Swap calculation model | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_DEPOSIT | Swaps are charged in money, in client deposit currency | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_MARGIN | Swaps are charged in money in margin currency of the symbol | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_CURRENCY\_SYMBOL | Swaps are charged in money in base currency of the symbol | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_DISABLED | Swaps disabled (no swaps) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_INTEREST\_CURRENT | Swaps are charged as the specified annual interest from the instrument price at calculation of swap (standard bank year is 360 days) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_INTEREST\_OPEN | Swaps are charged as the specified annual interest from the open price of position (standard bank year is 360 days) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_POINTS | Swaps are charged in points | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_REOPEN\_BID | Swaps are charged by reopening positions. At the end of a trading day the position is closed. Next day it is reopened by the current Bid price +/- specified number of points (parameters SYMBOL\_SWAP\_LONG and SYMBOL\_SWAP\_SHORT) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_MODE\_REOPEN\_CURRENT | Swaps are charged by reopening positions. At the end of a trading day the position is closed. Next day it is reopened by the close price +/- specified number of points (parameters SYMBOL\_SWAP\_LONG and SYMBOL\_SWAP\_SHORT) | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_ROLLOVER3DAYS | Day of week to charge 3 days swap rollover | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_SWAP\_SHORT | Short swap value | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_TICKS\_BOOKDEPTH | Maximal number of requests shown in [Depth of Market](../Market-Info/MarketBookGet/MarketBookGet.md). For symbols that have no queue of requests, the value is equal to zero. | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TIME | Time of the last quote | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_CALC\_MODE | Contract price calculation mode | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_CONTRACT\_SIZE | Trade contract size | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_TRADE\_EXECUTION\_EXCHANGE | Exchange execution | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_EXECUTION\_INSTANT | Instant execution | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_EXECUTION\_MARKET | Market execution | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_EXECUTION\_REQUEST | Execution by request | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_EXEMODE | Deal execution mode | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_FREEZE\_LEVEL | Distance to freeze trade operations in points | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_MODE | Order execution type | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_MODE\_CLOSEONLY | Allowed only position close operations | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_MODE\_DISABLED | Trade is disabled for the symbol | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_MODE\_FULL | No trade restrictions | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_MODE\_LONGONLY | Allowed only long positions | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_MODE\_SHORTONLY | Allowed only short positions | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_STOPS\_LEVEL | Minimal indention in points from the current close price to place Stop orders | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_TRADE\_TICK\_SIZE | Minimal price change | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_TRADE\_TICK\_VALUE | Value of SYMBOL\_TRADE\_TICK\_VALUE\_PROFIT | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_TRADE\_TICK\_VALUE\_LOSS | Calculated tick price for a losing position | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_TRADE\_TICK\_VALUE\_PROFIT | Calculated tick price for a profitable position | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_VOLUME | Volume of the last deal | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_VOLUME\_LIMIT | Maximum allowed aggregate volume of an open position and pending orders in one direction (buy or sell) for the symbol. For example, with the limitation of 5 lots, you can have an open buy position with the volume of 5 lots and place a pending order Sell Limit with the volume of 5 lots. But in this case you cannot place a Buy Limit pending order (since the total volume in one direction will exceed the limitation) or place Sell Limit with the volume more than 5 lots. | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_VOLUME\_MAX | Maximal volume for a deal | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_VOLUME\_MIN | Minimal volume for a deal | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_VOLUME\_STEP | Minimal volume change step for deal execution | [SymbolInfoDouble](../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md) |
| SYMBOL\_VOLUMEHIGH | Maximal day volume | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| SYMBOL\_VOLUMELOW | Minimal day volume | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md) |
| TENKANSEN\_LINE | Tenkan-sen line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| TERMINAL\_BUILD | The client terminal build number | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_CODEPAGE | Number of [the code page of the language](../Constants,-Enumerations-and-Structures/Input-Output-Constants/Use-of-a-Codepage/Use-of-a-Codepage.md) installed in the client terminal | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_COMMONDATA\_PATH | Common path for all of the terminals installed on a computer | [TerminalInfoString](../Checkup/TerminalInfoString/TerminalInfoString.md) |
| TERMINAL\_COMMUNITY\_ACCOUNT | The flag indicates the presence of MQL5.community authorization data in the terminal | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_COMMUNITY\_BALANCE | Balance in MQL5.community | [TerminalInfoDouble](../Checkup/TerminalInfoDouble/TerminalInfoDouble.md) |
| TERMINAL\_COMMUNITY\_CONNECTION | Connection to MQL5.community | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_COMPANY | Company name | [TerminalInfoString](../Checkup/TerminalInfoString/TerminalInfoString.md) |
| TERMINAL\_CONNECTED | Connection to a trade server | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_CPU\_CORES | The number of CPU cores in the system | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_DATA\_PATH | Folder in which terminal data are stored | [TerminalInfoString](../Checkup/TerminalInfoString/TerminalInfoString.md) |
| TERMINAL\_DISK\_SPACE | Free disk space for the MQL5\Files folder of the terminal (agent), MB | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_DLLS\_ALLOWED | Permission to use DLL | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_EMAIL\_ENABLED | Permission to send e-mails using SMTP-server and login, specified in the terminal settings | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_FTP\_ENABLED | Permission to send reports using FTP-server and login, specified in the terminal settings | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_LANGUAGE | Language of the terminal | [TerminalInfoString](../Checkup/TerminalInfoString/TerminalInfoString.md) |
| TERMINAL\_MAXBARS | The maximal bars count on the chart | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_MEMORY\_AVAILABLE | Free memory of the terminal (agent) process, MB | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_MEMORY\_PHYSICAL | Physical memory in the system, MB | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_MEMORY\_TOTAL | Memory available to the process of the terminal (agent), MB | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_MEMORY\_USED | Memory used by the terminal (agent), MB | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_MQID | The flag indicates the presence of MetaQuotes ID data for [Push notifications](../Network-Functions/SendNotification/SendNotification.md) | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_NAME | Terminal name | [TerminalInfoString](../Checkup/TerminalInfoString/TerminalInfoString.md) |
| TERMINAL\_NOTIFICATIONS\_ENABLED | Permission to send notifications to smartphone | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_OPENCL\_SUPPORT | The version of the supported OpenCL in the format of 0x00010002 = 1.2.  "0" means that OpenCL is not supported | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_PATH | Folder from which the terminal is started | [TerminalInfoString](../Checkup/TerminalInfoString/TerminalInfoString.md) |
| TERMINAL\_PING\_LAST | The last known value of a ping to a trade server in microseconds. One second comprises of one million microseconds | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_SCREEN\_DPI | The resolution of information display on the screen is measured as number of Dots in a line per Inch (DPI). | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_TRADE\_ALLOWED | [Permission to trade](../MQL5-programs/Trade-Permission/Trade-Permission.md) | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| TERMINAL\_X64 | Indication of the "64-bit terminal" | [TerminalInfoInteger](../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) |
| THURSDAY | Thursday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| TRADE\_ACTION\_DEAL | Place a trade order for an immediate execution with the specified parameters (market order) | [MqlTradeRequest](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) |
| TRADE\_ACTION\_MODIFY | Modify the parameters of the order placed previously | [MqlTradeRequest](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) |
| TRADE\_ACTION\_PENDING | Place a trade order for the execution under specified conditions (pending order) | [MqlTradeRequest](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) |
| TRADE\_ACTION\_REMOVE | Delete the pending order placed previously | [MqlTradeRequest](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) |
| TRADE\_ACTION\_SLTP | Modify Stop Loss and Take Profit values of an opened position | [MqlTradeRequest](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) |
| TRADE\_RETCODE\_CANCEL | Request canceled by trader | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_CLIENT\_DISABLES\_AT | Autotrading disabled by client terminal | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_CONNECTION | No connection with the trade server | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_DONE | Request completed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_DONE\_PARTIAL | Only part of the request was completed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_ERROR | Request processing error | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_FROZEN | Order or position frozen | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID | Invalid request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID\_EXPIRATION | Invalid order expiration date in the request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID\_FILL | Invalid [order filling type](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID\_ORDER | Incorrect or prohibited [order type](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID\_PRICE | Invalid price in the request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID\_STOPS | Invalid stops in the request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_INVALID\_VOLUME | Invalid volume in the request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_LIMIT\_ORDERS | The number of pending orders has reached the limit | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_LIMIT\_VOLUME | The volume of orders and positions for the symbol has reached the limit | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_LOCKED | Request locked for processing | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_MARKET\_CLOSED | Market is closed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_NO\_CHANGES | No changes in request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_NO\_MONEY | There is not enough money to complete the request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_ONLY\_REAL | Operation is allowed only for live accounts | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_ORDER\_CHANGED | Order state changed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_PLACED | Order placed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_POSITION\_CLOSED | Position with the specified [POSITION\_IDENTIFIER](../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer) has already been closed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_PRICE\_CHANGED | Prices changed | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_PRICE\_OFF | There are no quotes to process the request | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_REJECT | Request rejected | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_REQUOTE | Requote | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_SERVER\_DISABLES\_AT | Autotrading disabled by server | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_TIMEOUT | Request canceled by timeout | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_TOO\_MANY\_REQUESTS | Too frequent requests | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_RETCODE\_TRADE\_DISABLED | Trade is disabled | [MqlTradeResult](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) |
| TRADE\_TRANSACTION\_DEAL\_ADD | Adding a deal to the history. The action is performed as a result of an order execution or performing operations with an account balance. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_DEAL\_DELETE | Deleting a deal from the history. There may be cases when a previously executed deal is deleted from a server. For example, a deal has been deleted in an external trading system (exchange) where it was previously transferred by a broker. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_DEAL\_UPDATE | Updating a deal in the history. There may be cases when a previously executed deal is changed on a server. For example, a deal has been changed in an external trading system (exchange) where it was previously transferred by a broker. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_HISTORY\_ADD | Adding an order to the history as a result of execution or cancellation. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_HISTORY\_DELETE | Deleting an order from the orders history. This type is provided for enhancing functionality on a trade server side. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_HISTORY\_UPDATE | Changing an order located in the orders history. This type is provided for enhancing functionality on a trade server side. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_ORDER\_ADD | Adding a new open order. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_ORDER\_DELETE | Removing an order from the list of the open ones. An order can be deleted from the open ones as a result of setting an appropriate request or execution (filling) and moving to the history. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_ORDER\_UPDATE | Updating an open order. The updates include not only evident changes from the client terminal or a trade server sides but also changes of an order state when setting it (for example, transition from [ORDER\_STATE\_STARTED](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_state) to [ORDER\_STATE\_PLACED](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_state) or from [ORDER\_STATE\_PLACED](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_state) to [ORDER\_STATE\_PARTIAL](../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_state), etc.). | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_POSITION | Changing a position not related to a deal execution. This type of transaction shows that a position has been changed on a trade server side. Position volume, open price, Stop Loss and Take Profit levels can be changed. Data on changes are submitted in [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) structure via OnTradeTransaction handler. Position change (adding, changing or closing), as a result of a deal execution, does not lead to the occurrence of TRADE\_TRANSACTION\_POSITION transaction. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TRADE\_TRANSACTION\_REQUEST | Notification of the fact that a trade request has been processed by a server and processing result has been received. Only type field (trade transaction type) must be analyzed for such transactions in [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) structure. The second and third parameters of [OnTradeTransaction](../Event-Handling/OnTradeTransaction/OnTradeTransaction.md) (request and result) must be analyzed for additional data. | [MqlTradeTransaction](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Transaction-Structure/Trade-Transaction-Structure.md) |
| TUESDAY | Tuesday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| TYPE\_BOOL | bool | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_CHAR | char | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_COLOR | color | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_DATETIME | datetime | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_DOUBLE | double | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_FLOAT | float | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_INT | int | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_LONG | long | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_SHORT | short | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_STRING | string | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_UCHAR | uchar | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_UINT | uint | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_ULONG | ulong | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| TYPE\_USHORT | ushort | [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) |
| UCHAR\_MAX | Maximal value, which can be represented by uchar type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| UINT\_MAX | Maximal value, which can be represented by uint type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| ULONG\_MAX | Maximal value, which can be represented by ulong type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| UPPER\_BAND | Upper limit | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| UPPER\_HISTOGRAM | Upper histogram | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| UPPER\_LINE | Upper line | [Indicators Lines](../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicators-Lines/Indicators-Lines.md) |
| USHORT\_MAX | Maximal value, which can be represented by ushort type | [Numerical Type Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md) |
| VOLUME\_REAL | Trade volume | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| VOLUME\_TICK | Tick volume | [Price Constants](../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) |
| WEDNESDAY | Wednesday | [SymbolInfoInteger](../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [SymbolInfoSessionQuote](../Market-Info/SymbolInfoSessionQuote/SymbolInfoSessionQuote.md), [SymbolInfoSessionTrade](../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) |
| WHOLE\_ARRAY | Means the number of items remaining until the end of the array, i.e., the entire array will be processed | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
| WRONG\_VALUE | The constant can be implicitly [cast](../Language-Basics/Data-Types/Typecasting/Typecasting.md) to any [enumeration](../Language-Basics/Data-Types/Integer-Types/Enumerations/Enumerations.md) type | [Other Constants](../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) |
