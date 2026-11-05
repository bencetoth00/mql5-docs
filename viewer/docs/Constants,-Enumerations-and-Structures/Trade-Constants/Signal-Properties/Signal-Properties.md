# Signal Properties


The following enumerations are used when working with trading signals and signal copy settings.

Enumeration of [double](../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type properties of the trading signal:

ENUM\_SIGNAL\_BASE\_DOUBLE

| ID | Description |
| --- | --- |
| SIGNAL\_BASE\_BALANCE | Account balance |
| SIGNAL\_BASE\_EQUITY | Account equity |
| SIGNAL\_BASE\_GAIN | Account gain |
| SIGNAL\_BASE\_MAX\_DRAWDOWN | Account maximum drawdown |
| SIGNAL\_BASE\_PRICE | Signal subscription price |
| SIGNAL\_BASE\_ROI | Return on Investment (%) |

Enumeration of [integer](../../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type properties of the trading signal:

ENUM\_SIGNAL\_BASE\_INTEGER

| ID | Description |
| --- | --- |
| SIGNAL\_BASE\_DATE\_PUBLISHED | Publication date (date when it become available for subscription) |
| SIGNAL\_BASE\_DATE\_STARTED | Monitoring starting date |
| SIGNAL\_BASE\_DATE\_UPDATED | The date of the last update of the signal's trading statistics |
| SIGNAL\_BASE\_ID | Signal ID |
| SIGNAL\_BASE\_LEVERAGE | Account leverage |
| SIGNAL\_BASE\_PIPS | Profit in pips |
| SIGNAL\_BASE\_RATING | Position in rating |
| SIGNAL\_BASE\_SUBSCRIBERS | Number of subscribers |
| SIGNAL\_BASE\_TRADES | Number of trades |
| SIGNAL\_BASE\_TRADE\_MODE | Account type (0-real, 1-demo, 2-contest) |

Enumeration of [string](../../../Language-Basics/Data-Types/String-Type/String-Type.md) type properties of the trading signal:

ENUM\_SIGNAL\_BASE\_STRING

| ID | Description |
| --- | --- |
| SIGNAL\_BASE\_AUTHOR\_LOGIN | Author login |
| SIGNAL\_BASE\_BROKER | Broker name (company) |
| SIGNAL\_BASE\_BROKER\_SERVER | Broker server |
| SIGNAL\_BASE\_NAME | Signal name |
| SIGNAL\_BASE\_CURRENCY | Signal base currency |

Enumeration of [double](../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type properties of the signal copy settings:

ENUM\_SIGNAL\_INFO\_DOUBLE

| ID | Description |
| --- | --- |
| SIGNAL\_INFO\_EQUITY\_LIMIT | Equity limit |
| SIGNAL\_INFO\_SLIPPAGE | Slippage (used when placing market orders in synchronization of positions and copying of trades) |
| SIGNAL\_INFO\_VOLUME\_PERCENT | Maximum percent of deposit used (%), r/o |

Enumeration of [integer](../../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type properties of the signal copy settings:

ENUM\_SIGNAL\_INFO\_INTEGER

| ID | Description |
| --- | --- |
| SIGNAL\_INFO\_CONFIRMATIONS\_DISABLED | The flag enables synchronization without confirmation dialog |
| SIGNAL\_INFO\_COPY\_SLTP | Copy Stop Loss and Take Profit flag |
| SIGNAL\_INFO\_DEPOSIT\_PERCENT | Deposit percent (%) |
| SIGNAL\_INFO\_ID | Signal id, r/o |
| SIGNAL\_INFO\_SUBSCRIPTION\_ENABLED | "Copy trades by subscription" permission flag |
| SIGNAL\_INFO\_TERMS\_AGREE | "Agree to terms of use of Signals service" flag, r/o |

Enumeration of [string](../../../Language-Basics/Data-Types/String-Type/String-Type.md) type properties of the signal copy settings:

ENUM\_SIGNAL\_INFO\_STRING

| ID | Description |
| --- | --- |
| SIGNAL\_INFO\_NAME | Signal name, r/o |

See also

[Trade signals](../../../Trade-Signals/Trade-Signals.md)
