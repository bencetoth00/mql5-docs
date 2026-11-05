# Chart Operations


Functions for setting chart properties ([ChartSetInteger](ChartSetInteger/ChartSetInteger.md), [ChartSetDouble](ChartSetDouble/ChartSetDouble.md), [ChartSetString](ChartSetString/ChartSetString.md)) are asynchronous and are used for sending update commands to a chart. If these functions are executed successfully, the command is included in the common queue of the chart events. Chart property changes are implemented along with handling of the events queue of this chart.

Thus, do not expect an immediate update of the chart after calling asynchronous functions. Use the [ChartRedraw()](ChartRedraw/ChartRedraw.md) function to forcedly update the chart appearance and properties.

| Function | Action |
| --- | --- |
| [ChartApplyTemplate](ChartApplyTemplate/ChartApplyTemplate.md) | Applies a specific template from a specified file to the chart |
| [ChartSaveTemplate](ChartSaveTemplate/ChartSaveTemplate.md) | Saves current chart settings in a template with a specified name |
| [ChartWindowFind](ChartWindowFind/ChartWindowFind.md) | Returns the number of a subwindow where an indicator is drawn |
| [ChartTimePriceToXY](ChartTimePriceToXY/ChartTimePriceToXY.md) | Converts the coordinates of a chart from the time/price representation to the X and Y coordinates |
| [ChartXYToTimePrice](ChartXYToTimePrice/ChartXYToTimePrice.md) | Converts the X and Y coordinates on a chart to the time and price values |
| [ChartOpen](ChartOpen/ChartOpen.md) | Opens a new chart with the specified symbol and period |
| [ChartClose](ChartClose/ChartClose.md) | Closes the specified chart |
| [ChartFirst](ChartFirst/ChartFirst.md) | Returns the ID of the first chart of the client terminal |
| [ChartNext](ChartNext/ChartNext.md) | Returns the chart ID of the chart next to the specified one |
| [ChartSymbol](ChartSymbol/ChartSymbol.md) | Returns the symbol name of the specified chart |
| [ChartPeriod](ChartPeriod/ChartPeriod.md) | Returns the period value of the specified chart |
| [ChartRedraw](ChartRedraw/ChartRedraw.md) | Calls a forced redrawing of a specified chart |
| [ChartSetDouble](ChartSetDouble/ChartSetDouble.md) | Sets the double value for a corresponding property of the specified chart |
| [ChartSetInteger](ChartSetInteger/ChartSetInteger.md) | Sets the integer value (datetime, int, color, bool or char) for a corresponding property of the specified chart |
| [ChartSetString](ChartSetString/ChartSetString.md) | Sets the string value for a corresponding property of the specified chart |
| [ChartGetDouble](ChartGetDouble/ChartGetDouble.md) | Returns the double value property of the specified chart |
| [ChartGetInteger](ChartGetInteger/ChartGetInteger.md) | Returns the integer value property of the specified chart |
| [ChartGetString](ChartGetString/ChartGetString.md) | Returns the string value property of the specified chart |
| [ChartNavigate](ChartNavigate/ChartNavigate.md) | Performs shift of the specified chart by the specified number of bars relative to the specified position in the chart |
| [ChartID](ChartID/ChartID.md) | Returns the ID of the current chart |
| [ChartIndicatorAdd](ChartIndicatorAdd/ChartIndicatorAdd.md) | Adds an indicator with the specified handle into a specified chart window |
| [ChartIndicatorDelete](ChartIndicatorDelete/ChartIndicatorDelete.md) | Removes an indicator with a specified name from the specified chart window |
| [ChartIndicatorGet](ChartIndicatorGet/ChartIndicatorGet.md) | Returns the handle of the indicator with the specified short name in the specified chart window |
| [ChartIndicatorName](ChartIndicatorName/ChartIndicatorName.md) | Returns the short name of the indicator by the number in the indicators list on the specified chart window |
| [ChartIndicatorsTotal](ChartIndicatorsTotal/ChartIndicatorsTotal.md) | Returns the number of all indicators applied to the specified chart window. |
| [ChartWindowOnDropped](ChartWindowOnDropped/ChartWindowOnDropped.md) | Returns the number (index) of the chart subwindow the Expert Advisor or script has been dropped to |
| [ChartPriceOnDropped](ChartPriceOnDropped/ChartPriceOnDropped.md) | Returns the price coordinate of the chart point the Expert Advisor or script has been dropped to |
| [ChartTimeOnDropped](ChartTimeOnDropped/ChartTimeOnDropped.md) | Returns the time coordinate of the chart point the Expert Advisor or script has been dropped to |
| [ChartXOnDropped](ChartXOnDropped/ChartXOnDropped.md) | Returns the X coordinate of the chart point the Expert Advisor or script has been dropped to |
| [ChartYOnDropped](ChartYOnDropped/ChartYOnDropped.md) | Returns the Y coordinate of the chart point the Expert Advisor or script has been dropped to |
| [ChartSetSymbolPeriod](ChartSetSymbolPeriod/ChartSetSymbolPeriod.md) | Changes the symbol value and a period of the specified chart |
| [ChartScreenShot](ChartScreenShot/ChartScreenShot.md) | Provides a screenshot of the chart of its current state in a GIF, PNG or BMP format depending on specified extension |
