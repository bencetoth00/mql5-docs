# SeriesInfoInteger


Returns information about the state of historical data. There are 2 variants of function calls.

Directly returns the property value.

```cpp
long  SeriesInfoInteger(
   string                     symbol_name,     // symbol name
   ENUM_TIMEFRAMES            timeframe,       // period
   ENUM_SERIES_INFO_INTEGER   prop_id,         // property identifier
   );
```

Returns true or false depending on the success of the function run.

```cpp
bool  SeriesInfoInteger(
   string                     symbol_name,     // symbol name
   ENUM_TIMEFRAMES            timeframe,       // period
   ENUM_SERIES_INFO_INTEGER   prop_id,         // property ID
   long&                      long_var         // variable for getting info
   );
```

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

```cpp
void OnStart()
  {
//---
   Print("Total number of bars for the symbol-period at this moment = ",
         SeriesInfoInteger(Symbol(),Period(),SERIES_BARS_COUNT));
   Print("The first date for the symbol-period at this moment = ",
         (datetime)SeriesInfoInteger(Symbol(),Period(),SERIES_FIRSTDATE));
   Print("The first date in the history for the symbol-period on the server = ",
         (datetime)SeriesInfoInteger(Symbol(),Period(),SERIES_SERVER_FIRSTDATE));
   Print("Symbol data are synchronized = ",
         (bool)SeriesInfoInteger(Symbol(),Period(),SERIES_SYNCHRONIZED));
  }
```