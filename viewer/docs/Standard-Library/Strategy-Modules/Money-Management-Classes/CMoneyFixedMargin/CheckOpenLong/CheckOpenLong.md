# CheckOpenLong


Gets trade volume for a long position.

```cpp
virtual double  CheckOpenLong(
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

Trade volume for a long position.

Note

The function returns trade volume for a long position with a fixed predefined margin. The margin is defined by Percent parameter of [CExpertMoney](../../../Base-classes-for-Expert-Advisors/CExpertMoney/CExpertMoney.md) base class.