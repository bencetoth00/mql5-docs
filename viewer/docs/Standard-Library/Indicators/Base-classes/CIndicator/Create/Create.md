# Create


Creates the indicator of the specified type with the specified parameters.

```cpp
bool  Create(
   const string           symbol,         // symbol
   const ENUM_TIMEFRAMES  period,         // period
   const ENUM_INDICATOR   type,           // type
   const int              num_params,     // number of parameters
   const MqlParam&        params[]        // array of parameters
   )
```

Parameters

symbol

[in]  Indicator symbol.

period

[in]  Indicator timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration).

type

[in]  Indicator type ([ENUM\_INDICATOR](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicator-Types/Indicator-Types.md) enumeration).

num\_params

[in]  Number of indicator's parameters.

params

[in]  Reference to the parameters array for the indicator.

Return Value

true - successful, false - cannot create the indicator.