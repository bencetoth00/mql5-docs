# ChartPriceOnDropped


Returns the price coordinate corresponding to the chart point the Expert Advisor or script has been dropped to.

```cpp
double  ChartPriceOnDropped();
```

Return Value

Value of [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type.

Example:

```cpp
   double p=ChartPriceOnDropped();
   Print("ChartPriceOnDropped() = ",p);
```

See also

[ChartXOnDropped](../ChartXOnDropped/ChartXOnDropped.md), [ChartYOnDropped](../ChartYOnDropped/ChartYOnDropped.md)