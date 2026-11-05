# Chart Properties

Chart Properties

Identifiers of ENUM\_CHART\_PROPERTY enumerations are used as parameters of [functions for working with charts](../../../Chart-Operations/Chart-Operations.md). The abbreviation of r/o in the "Property Type" column means that this property is read-only and cannot be changed. The w/o abbreviation in the "Property Type" column means that this property is write-only and it cannot be received. When accessing certain properties, it's necessary to specify an additional parameter-modifier (modifier), which serves to indicate the number of chart subwindows. 0 means the main window.

The functions defining the chart properties are actually used for sending change commands to the chart. If these functions are executed successfully, the command is included in the common queue of the chart events. The changes are implemented to the chart when handling the queue of the chart events.

Thus, do not expect an immediate visual update of the chart after calling these functions. Generally, the chart is updated automatically by the terminal following the change events - a new quote arrival, resizing the chart window, etc. Use [ChartRedraw()](../../../Chart-Operations/ChartRedraw/ChartRedraw.md) function to forcefully update the chart.

For functions [ChartSetInteger()](../../../Chart-Operations/ChartSetInteger/ChartSetInteger.md) and [ChartGetInteger()](../../../Chart-Operations/ChartGetInteger/ChartGetInteger.md)

ENUM\_CHART\_PROPERTY\_INTEGER

| ID | Description | Property Type |
| --- | --- | --- |
| CHART\_SHOW | Price chart drawing. If false, drawing any price chart attributes is disabled and all chart border indents are eliminated, including time and price scales, quick navigation bar, Calendar event labels, trade labels, indicator and bar tooltips, indicator subwindows, volume histograms, etc.  Disabling the drawing is a perfect solution for creating a custom program interface using the graphical [resources](../../../MQL5-programs/Resources/Resources.md).  The [graphical objects](../../../Object-Functions/Object-Functions.md) are always drawn regardless of the CHART\_SHOW property value. | bool |
| [CHART\_IS\_OBJECT](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_is_object) | Identifying "Chart" ([OBJ\_CHART)](../../Objects-Constants/Object-Types/Object-Types.md) object – returns true for a graphical object. Returns false for a real chart | bool   r/o |
| [CHART\_BRING\_TO\_TOP](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_bring_to_top) | Show chart on top of other charts | bool |
| CHART\_CONTEXT\_MENU | Enabling/disabling access to the context menu using the right click.  When CHART\_CONTEXT\_MENU=false, only the chart context menu is disabled. The context menu of objects on the chart remains available. | bool  (default is true) |
| CHART\_CROSSHAIR\_TOOL | Enabling/disabling access to the Crosshair tool using the middle click. | bool  (default is true) |
| [CHART\_MOUSE\_SCROLL](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_mouse_scroll) | Scrolling the chart horizontally using the left mouse button. Vertical scrolling is also available if the value of any following properties is set to true: CHART\_SCALEFIX, CHART\_SCALEFIX\_11 or CHART\_SCALE\_PT\_PER\_BAR  When CHART\_MOUSE\_SCROLL=false, chart scrolling with the mouse wheel is unavailable | bool |
| CHART\_EVENT\_MOUSE\_WHEEL | Sending messages about mouse wheel events ([CHARTEVENT\_MOUSE\_WHEEL](../Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5 programs on a chart | bool  (default is true) |
| [CHART\_EVENT\_MOUSE\_MOVE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_event_mouse_move) | Send notifications of mouse move and mouse click events ([CHARTEVENT\_MOUSE\_MOVE](../Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5 programs on a chart | bool |
| [CHART\_EVENT\_OBJECT\_CREATE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_event_object_create) | Send a notification of an event of new object creation ([CHARTEVENT\_OBJECT\_CREATE](../Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5-programs on a chart | bool |
| [CHART\_EVENT\_OBJECT\_DELETE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_event_object_delete) | Send a notification of an event of object deletion ([CHARTEVENT\_OBJECT\_DELETE](../Types-of-Chart-Events/Types-of-Chart-Events.md)) to all mql5-programs on a chart | bool |
| [CHART\_MODE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_mode) | Chart type (candlesticks, bars or line) | enum     [ENUM\_CHART\_MODE](../Chart-Representation/Chart-Representation.md#enum_chart_mode) |
| [CHART\_FOREGROUND](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_foreground) | Price chart in the foreground | bool |
| [CHART\_SHIFT](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_shift) | Mode of price chart indent from the right border | bool |
| [CHART\_AUTOSCROLL](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_autoscroll) | Mode of automatic moving to the right border of the chart | bool |
| CHART\_KEYBOARD\_CONTROL | Allow managing the chart using a keyboard ("Home", "End", "PageUp", "+", "-", "Up arrow", etc.). Setting CHART\_KEYBOARD\_CONTROL to false disables chart scrolling and scaling while leaving intact the ability to receive the keys pressing events in [OnChartEvent()](../../../Event-Handling/OnChartEvent/OnChartEvent.md). | bool |
| CHART\_QUICK\_NAVIGATION | Allow the chart to intercept Space and Enter key strokes to activate the quick navigation bar. The quick navigation bar automatically appears at the bottom of the chart after double-clicking the mouse or pressing Space/Enter. It allows you to quickly change a symbol, timeframe and first visible bar date. | bool |
| [CHART\_SCALE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scale) | Scale | int        from 0 to 5 |
| [CHART\_SCALEFIX](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scalefix) | Fixed scale mode | bool |
| [CHART\_SCALEFIX\_11](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scalefix_11) | Scale 1:1 mode | bool |
| [CHART\_SCALE\_PT\_PER\_BAR](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_scale_pt_per_bar) | Scale to be specified in points per bar | bool |
| CHART\_SHOW\_TICKER | Display a symbol ticker in the upper left corner. Setting CHART\_SHOW\_TICKER to 'false' also sets [CHART\_SHOW\_OHLC](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_ohlc) to 'false' and disables OHLC | bool |
| [CHART\_SHOW\_OHLC](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_ohlc) | Display OHLC values in the upper left corner. Setting CHART\_SHOW\_OHLC to 'true' also sets CHART\_SHOW\_TICKER to 'true' and enables the ticker | bool |
| [CHART\_SHOW\_BID\_LINE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_bid_line) | Display Bid values as a horizontal line in a chart | bool |
| [CHART\_SHOW\_ASK\_LINE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_ask_line) | Display Ask values as a horizontal line in a chart | bool |
| [CHART\_SHOW\_LAST\_LINE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_last_line) | Display Last values as a horizontal line in a chart | bool |
| [CHART\_SHOW\_PERIOD\_SEP](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_period_sep) | Display vertical separators between adjacent periods | bool |
| [CHART\_SHOW\_GRID](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_grid) | Display grid in the chart | bool |
| [CHART\_SHOW\_VOLUMES](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_volumes) | Display volume in the chart | enum     [ENUM\_CHART\_VOLUME\_MODE](../Chart-Representation/Chart-Representation.md#enum_chart_volume_mode) |
| [CHART\_SHOW\_OBJECT\_DESCR](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_object_descr) | Display textual descriptions of objects (not available for all objects) | bool |
| CHART\_SHOW\_TRADE\_HISTORY | Display trades from the trading history as entry/exit arrows on a chart. See the "[Show trading history](https://www.metatrader5.com/en/terminal/help/trading/performing_deals#position_showonchart)" option descriptions in the platform settings. | bool |
| [CHART\_VISIBLE\_BARS](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_visible_bars) | The number of bars on the chart that can be displayed | int r/o |
| [CHART\_WINDOWS\_TOTAL](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_windows_total) | The total number of chart windows, including indicator subwindows | int r/o |
| [CHART\_WINDOW\_IS\_VISIBLE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_window_is_visible) | Visibility of subwindows | bool r/o   modifier - subwindow number |
| [CHART\_WINDOW\_HANDLE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_window_handle) | Chart window handle (HWND) | int r/o |
| [CHART\_WINDOW\_YDISTANCE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_window_ydistance) | The distance between the upper frame of the indicator subwindow and the upper frame of the main chart window, along the vertical Y axis, in pixels. In case of a mouse event, the cursor coordinates are passed in terms of the coordinates of the main chart window, while the coordinates of graphical objects in an indicator subwindow are set relative to the upper left corner of the subwindow.  The value is required for converting the absolute coordinates of the main chart to the local coordinates of a subwindow for correct work with the graphical objects, whose coordinates are set relative to  the upper left corner of the subwindow frame. | int r/o     modifier - subwindow number |
| [CHART\_FIRST\_VISIBLE\_BAR](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_first_visible_bar) | Number of the first visible bar in the chart. Indexing of bars is the same as for [timeseries](../../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md). | int r/o |
| [CHART\_WIDTH\_IN\_BARS](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_width_in_bars) | Chart width in bars | int r/o |
| [CHART\_WIDTH\_IN\_PIXELS](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_width_in_pixels) | Chart width in pixels | int r/o |
| [CHART\_HEIGHT\_IN\_PIXELS](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_height_in_pixels) | Chart height in pixels | int      modifier - subwindow number |
| [CHART\_COLOR\_BACKGROUND](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_background) | Chart background color | color |
| [CHART\_COLOR\_FOREGROUND](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_foreground) | Color of axes, scales and OHLC line | color |
| [CHART\_COLOR\_GRID](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_grid) | Grid color | color |
| [CHART\_COLOR\_VOLUME](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_volume) | Color of volumes and position opening levels | color |
| [CHART\_COLOR\_CHART\_UP](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_chart_up) | Color for the up bar, shadows and body borders of bull candlesticks | color |
| [CHART\_COLOR\_CHART\_DOWN](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_chart_down) | Color for the down bar, shadows and body borders of bear candlesticks | color |
| [CHART\_COLOR\_CHART\_LINE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_chart_line) | Line chart color and color of "Doji" Japanese candlesticks | color |
| [CHART\_COLOR\_CANDLE\_BULL](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_candle_bull) | Body color of a bull candlestick | color |
| [CHART\_COLOR\_CANDLE\_BEAR](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_candle_bear) | Body color of a bear candlestick | color |
| [CHART\_COLOR\_BID](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_bid) | Bid price level color | color |
| [CHART\_COLOR\_ASK](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_ask) | Ask price level color | color |
| [CHART\_COLOR\_LAST](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_last) | Line color of the last executed deal price (Last) | color |
| [CHART\_COLOR\_STOP\_LEVEL](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_color_stop_level) | Color of stop order levels (Stop Loss and Take Profit) | color |
| [CHART\_SHOW\_TRADE\_LEVELS](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_trade_levels) | Displaying trade levels in the chart (levels of open positions, Stop Loss, Take Profit and pending orders) | bool |
| [CHART\_DRAG\_TRADE\_LEVELS](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_drag_trade_levels) | Permission to drag trading levels on a chart with a mouse. The drag mode is enabled by default (true value) | bool |
| [CHART\_SHOW\_DATE\_SCALE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_date_scale) | Showing the time scale on a chart | bool |
| [CHART\_SHOW\_PRICE\_SCALE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_price_scale) | Showing the price scale on a chart | bool |
| [CHART\_SHOW\_ONE\_CLICK](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_show_one_click) | Showing the ["One click trading"](https://www.metatrader5.com/en/terminal/help/startworking/settings "\"One click trading\"") panel on a chart | bool |
| [CHART\_IS\_MAXIMIZED](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_is_maximized) | Chart window is maximized | bool  r/o |
| [CHART\_IS\_MINIMIZED](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_is_minimized) | Chart window is minimized | bool  r/o |
| CHART\_IS\_DOCKED | The chart window is docked. If set to [false](../../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), the chart can be dragged outside the terminal area | bool |
| CHART\_FLOAT\_LEFT | The left coordinate of the undocked chart window relative to the virtual screen | int |
| CHART\_FLOAT\_TOP | The top coordinate of the undocked chart window relative to the virtual screen | int |
| CHART\_FLOAT\_RIGHT | The right coordinate of the undocked chart window relative to the virtual screen | int |
| CHART\_FLOAT\_BOTTOM | The bottom coordinate of the undocked chart window relative to the virtual screen | int |

For functions [ChartSetDouble()](../../../Chart-Operations/ChartSetDouble/ChartSetDouble.md) and [ChartGetDouble()](../../../Chart-Operations/ChartGetDouble/ChartGetDouble.md)

ENUM\_CHART\_PROPERTY\_DOUBLE

| ID | Description | Property Type |
| --- | --- | --- |
| [CHART\_SHIFT\_SIZE](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_shift_size) | The size of the zero bar indent from the right border in percents | double  (from 10 to 50 percents) |
| [CHART\_FIXED\_POSITION](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_fixed_position) | Chart fixed position from the left border in percent value. Chart fixed position is marked by a small gray triangle on the horizontal time axis. It is displayed only if the automatic chart scrolling to the right on tick incoming is disabled (see CHART\_AUTOSCROLL property). The bar on a fixed position remains in the same place when zooming in and out. | double |
| [CHART\_FIXED\_MAX](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_fixed_max) | Fixed  chart maximum | double |
| [CHART\_FIXED\_MIN](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_fixed_min) | Fixed  chart minimum | double |
| [CHART\_POINTS\_PER\_BAR](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_points_per_bar) | Scale in points per bar | double |
| [CHART\_PRICE\_MIN](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_price_min) | Chart minimum | double r/o   modifier - subwindow number |
| [CHART\_PRICE\_MAX](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_price_max) | Chart maximum | double r/o   modifier - subwindow number |

For functions [ChartSetString()](../../../Chart-Operations/ChartSetString/ChartSetString.md) and [ChartGetString()](../../../Chart-Operations/ChartGetString/ChartGetString.md)

ENUM\_CHART\_PROPERTY\_STRING

| ID | Description | Property Type |
| --- | --- | --- |
| [CHART\_COMMENT](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md#chart_comment) | Text of a comment in a chart | string |
| CHART\_EXPERT\_NAME | The name of the Expert Advisor running on the chart with the specified chart\_id | string r/o |
| CHART\_SCRIPT\_NAME | The name of the script running on the chart with the specified chart\_id | string r/o |

Example:

|  |
| --- |
| int chartMode=ChartGetInteger(0,CHART\_MODE);     switch(chartMode)       {        case(CHART\_BARS):    Print("CHART\_BARS");   break;        case(CHART\_CANDLES): Print("CHART\_CANDLES");break;        default:Print("CHART\_LINE");       }     bool shifted=ChartGetInteger(0,CHART\_SHIFT);     if(shifted) Print("CHART\_SHIFT = true");     else Print("CHART\_SHIFT = false");     bool autoscroll=ChartGetInteger(0,CHART\_AUTOSCROLL);     if(autoscroll) Print("CHART\_AUTOSCROLL = true");     else Print("CHART\_AUTOSCROLL = false");     int chartHandle=ChartGetInteger(0,CHART\_WINDOW\_HANDLE);     Print("CHART\_WINDOW\_HANDLE = ",chartHandle);     int windows=ChartGetInteger(0,CHART\_WINDOWS\_TOTAL);     Print("CHART\_WINDOWS\_TOTAL = ",windows);     if(windows>1)       {        for(int i=0;i<windows;i++)          {           int height=ChartGetInteger(0,CHART\_HEIGHT\_IN\_PIXELS,i);           double priceMin=ChartGetDouble(0,CHART\_PRICE\_MIN,i);           double priceMax=ChartGetDouble(0,CHART\_PRICE\_MAX,i);           Print(i+": CHART\_HEIGHT\_IN\_PIXELS = ",height," pixels");           Print(i+": CHART\_PRICE\_MIN = ",priceMin);           Print(i+": CHART\_PRICE\_MAX = ",priceMax);          }       } |

See also

[Examples of Working with the Chart](../Examples-of-Working-with-the-Chart/Examples-of-Working-with-the-Chart.md)
