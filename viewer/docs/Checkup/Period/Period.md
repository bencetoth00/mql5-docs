# Period


Returns the current chart timeframe.

```cpp
ENUM_TIMEFRAMES  Period();
```

Return Value

The contents of the [\_Period](../../Predefined-Variables/_Period/_Period.md) variable that contains the value of the current chart timeframe. The value can be one of the values of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration.

Note

Unlike Expert Advisors, indicators and scripts, services are not bound to a specific chart. Therefore, [Period()](Period.md) returns 0 for a service.

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- get the timeframe value of the current chart and its description
   ENUM_TIMEFRAMES period    = Period();
   string          timeframe = StringSubstr(EnumToString(period), 7);
//--- send the obtained data to the journal
   PrintFormat("Current chart timeframe: %s\nTimeframe value: %s (%d)",
               timeframe, EnumToString(period), period);
   /*
   result:
   Current chart timeframe: H4
   Timeframe value: PERIOD_H4 (16388)
   */
  }
```

See also

[PeriodSeconds](../../Common-Functions/PeriodSeconds/PeriodSeconds.md), [Chart timeframes](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md), [Date and Time](../../Date-and-Time/Date-and-Time.md), [Visibility of objects](../../Constants,-Enumerations-and-Structures/Objects-Constants/Visibility-of-Objects/Visibility-of-Objects.md)