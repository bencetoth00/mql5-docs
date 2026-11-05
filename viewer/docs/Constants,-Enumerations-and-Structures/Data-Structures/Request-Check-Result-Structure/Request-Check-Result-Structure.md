# Request Check Result Structure

# The Structure of Results of a Trade Request Check (MqlTradeCheckResult)

Before [sending](../../../Trade-Functions/OrderSend/OrderSend.md) a [request](../Trade-Request-Structure/Trade-Request-Structure.md) for a [trade operation](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md) to a trade server, it is recommended to check it. The check is performed using the [OrderCheck()](../../../Trade-Functions/OrderCheck/OrderCheck.md) function, to which the checked request and a variable of the MqlTradeCheckResult structure type are passed. The check result will be written to this variable.

```cpp
struct MqlTradeCheckResult
  {
   uint         retcode;             // Reply code
   double       balance;             // Balance after the execution of the deal
   double       equity;              // Equity after the execution of the deal
   double       profit;              // Floating profit
   double       margin;              // Margin requirements
   double       margin_free;         // Free margin
   double       margin_level;        // Margin level
   string       comment;             // Comment to the reply code (description of the error)
  };
```

Description of Fields

| Field | Description |
| --- | --- |
| retcode | [Return code](../../Codes-of-Errors-and-Warnings/Trade-Server-Return-Codes/Trade-Server-Return-Codes.md) |
| balance | Balance value that will be after the execution of the trade operation |
| equity | Equity value that will be after the execution of the trade operation |
| profit | Value of the floating profit that will be after the execution of the trade operation |
| margin | Margin required for the trade operation |
| margin\_free | Free margin that will be left after the execution of the trade operation |
| margin\_level | Margin level that will be set after the execution of the trade operation |
| comment | Comment to the reply code, error description |

See also

[Trade Request Structure](../Trade-Request-Structure/Trade-Request-Structure.md), [Structure for Current Prices](../Price-Data-Structure/Price-Data-Structure.md), [OrderSend](../../../Trade-Functions/OrderSend/OrderSend.md), [OrderCheck](../../../Trade-Functions/OrderCheck/OrderCheck.md)