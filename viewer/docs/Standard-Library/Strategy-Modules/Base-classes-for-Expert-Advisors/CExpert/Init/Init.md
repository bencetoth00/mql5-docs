# Init


Class instance initialization method.

```cpp
bool  Init(
   string             symbol,        // symbol
   ENUM_TIMEFRAMES    period,        // timeframe
   bool               every_tick,    // flag
   ulong              magic          // Expert Advisor identifier
   )
```

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe from [ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration.

every\_tick

[in]  Flag.

magic

[in]  Expert Advisor ID (Magic number).

Return Value

None.

Note

If every\_tick is set to true, the [Processing()](../Processing/Processing.md) method is called at each tick of the working symbol. otherwise, the [Processing()](../Processing/Processing.md) is called only when a new bar is formed on the working timeframe of the EA's working symbol.