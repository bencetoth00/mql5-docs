# SeriesInfoInteger

SeriesInfoInteger

Returns information about the state of historical data. There are 2 variants of function calls.

Directly returns the property value.

|  |
| --- |
| long  SeriesInfoInteger(     string                     symbol\_name,     // symbol name     ENUM\_TIMEFRAMES            timeframe,       // period     ENUM\_SERIES\_INFO\_INTEGER   prop\_id,         // property identifier     ); |

Returns true or false depending on the success of the function run.

|  |
| --- |
| bool  SeriesInfoInteger(     string                     symbol\_name,     // symbol name     ENUM\_TIMEFRAMES            timeframe,       // period     ENUM\_SERIES\_INFO\_INTEGER   prop\_id,         // property ID     long&                      long\_var         // variable for getting info     ); |

Parameters

symbol\_name

[in]  Symbol name.

timeframe

[in]  Period.

prop\_id

[in]  Identifier of the requested property, value of the [ENUM\_SERIES\_INFO\_INTEGER](../../Constants,-Enumerations-and-Structures/Trade-Constants/History-Database-Properties/History-Database-Properties.md) enumeration.

long\_var

[out]  Variable to which the value of the requested property is placed.

Return Value

In the first case, it returns value of the long type.

For the second case,  it returns true, if the specified property is available and its value has been placed into long\_var variable, otherwise it returns false. For more details about an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example:

|  |
| --- |
| void OnStart()    {  //---     Print("Total number of bars for the symbol-period at this moment = ",           SeriesInfoInteger(Symbol(),Period(),SERIES\_BARS\_COUNT));        Print("The first date for the symbol-period at this moment = ",           (datetime)SeriesInfoInteger(Symbol(),Period(),SERIES\_FIRSTDATE));        Print("The first date in the history for the symbol-period on the server = ",           (datetime)SeriesInfoInteger(Symbol(),Period(),SERIES\_SERVER\_FIRSTDATE));        Print("Symbol data are synchronized = ",           (bool)SeriesInfoInteger(Symbol(),Period(),SERIES\_SYNCHRONIZED));    } |
