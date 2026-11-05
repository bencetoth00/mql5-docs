# Create


Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

```cpp
bool  Create(
   string           symbol,          // symbol
   ENUM_TIMEFRAMES  period,          // period
   int              Kperiod,         // %K period
   int              Dperiod,         // %D period
   int              slowing,         // slowing period
   ENUM_MA_METHOD   ma_method,       // averaging method
   ENUM_STO_PRICE   price_field      // application
   )
```

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

Kperiod

[in]  Averaging period of %K indicator.

Dperiod

[in]  Averaging period of %D indicator.

slowing

[in]  Slowing period.

ma\_method

[in]  Averaging method ([ENUM\_MA\_METHOD](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) enumeration value).

price\_field

[in]  Object (Low/High or Close/Close) to apply ([ENUM\_STO\_PRICE](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md) enumeration value).

Return Value

true - successful, false - cannot create the indicator.