# Create


Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

```cpp
bool  Create(
   string           symbol,            // symbol
   ENUM_TIMEFRAMES  period,            // period
   int              tenkan_sen,        // period of TenkanSen
   int              kijun_sen,         // period of KijunSen
   int              senkou_span_b      // period of SenkouSpanB
   )
```

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

tenkan\_sen

[in]  Period of TenkanSen.

kijun\_sen

[in]  Period of KijunSen.

senkou\_span\_b

[in]  Period of SenkouSpanB.

Return Value

true - successful, false - cannot create the indicator.