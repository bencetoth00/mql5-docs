# iBars


Returns the number of bars of a corresponding symbol and period, available in history.

```cpp
int  iBars(
   const string           symbol,          // Symbol
   ENUM_TIMEFRAMES        timeframe        // Period
   );
```

Parameters

symbol

[in]  The symbol name of the financial instrument. [NULL](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) means the current symbol.

timeframe

[in]  Period. It can be one of the values of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration. 0 means the current chart period.

Return Value

The number of bars of a corresponding symbol and period, available in history, but no more than allowed by the "Max bars in chart" parameter in platform settings.

Example:

```cpp
  Print("Bar count on the 'EURUSD,H1' is ",iBars("EURUSD",PERIOD_H1));
```

See also

[Bars](../Bars/Bars.md)