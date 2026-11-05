# SetSymbolPeriod


Changes symbol and period of the chart assigned to the class instance.

```cpp
bool  SetSymbolPeriod(
   const string     symbol_name,     // symbol
   ENUM_TIMEFRAMES  timeframe        // period
   )
```

Parameters

symbol\_name

[in]  New chart symbol. [NULL](../../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) means the symbol of the current chart (to which an expert is attached).

timeframe

[in]  New chart timeframe (from [ENUM\_TIMEFRAMES](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration). 0 means the current chart timeframe.

Return Value

true - successful, false - cannot change the property.