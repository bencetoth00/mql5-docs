# Data Structures

Data Structures

MQL5 Language offers 12 predefined [structures](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md):

- [MqlDateTime](Date-Type-Structure/Date-Type-Structure.md) is intended for working with [date and time](../../Date-and-Time/Date-and-Time.md);

- [MqlParam](Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) can send input parameters when creating a handle of the indicator using the [IndicatorCreate()](../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) function;

- [MqlRates](History-Data-Structure/History-Data-Structure.md) is intended for manipulating the [historical data](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md), it contains information about the price, volume and spread;
- [MqlBookInfo](Order-Book-Structure/Order-Book-Structure.md) is intended for obtaining information about the [Depth of Market](../../Market-Info/Market-Info.md);
- [MqlTradeRequest](Trade-Request-Structure/Trade-Request-Structure.md) is used for creating a trade request for [trade operations](../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md);

- [MqlTradeCheckResult](Request-Check-Result-Structure/Request-Check-Result-Structure.md) is intended for [checking](../../Trade-Functions/OrderCheck/OrderCheck.md) the prepared [trade request](Trade-Request-Structure/Trade-Request-Structure.md) before [sending](../../Trade-Functions/OrderSend/OrderSend.md) it;

- [MqlTradeResult](Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) contains a trade server reply to a [trade request](Trade-Request-Structure/Trade-Request-Structure.md), sent by [OrderSend()](../../Trade-Functions/OrderSend/OrderSend.md) function;

- [MqlTradeTransaction](Trade-Transaction-Structure/Trade-Transaction-Structure.md) contains description of a trade transaction;

- [MqlTick](Price-Data-Structure/Price-Data-Structure.md) is designed for fast retrieval of the most requested information about current prices.

- [Economic calendar structures](Economic-alendar-structures/Economic-alendar-structures.md) are used to obtain data on the economic calendar events sent to the MetaTrader 5 platform in real time. [Economic calendar functions](../../Economic-Calendar/Economic-Calendar.md) allow analyzing macroeconomic parameters immediately after new reports are released, since relevant values are broadcast directly from the source with no delay.
