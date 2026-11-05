# CheckOpenShort


Gets trade volume for a short position.

```cpp
virtual double  CheckOpenShort(
   double  price,     // price
   double  sl         // Stop Loss price
   )
```

Parameters

price

[in]  Estimated open price.

sl

[in]  Estimated Stop Loss price.

Return Value

Trade volume for a short position.

Note

The function returns trade volume for a short position with a predefined fixed margin. The margin is defined by Percent parameter of [CExpertMoney](../../../Base-classes-for-Expert-Advisors/CExpertMoney/CExpertMoney.md) base class.