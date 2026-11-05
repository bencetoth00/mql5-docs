# ChartWindowOnDropped


Returns the number (index) of the chart subwindow the Expert Advisor or script has been dropped to. 0 means the main chart window.

```cpp
int  ChartWindowOnDropped();
```

Return Value

Value of [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Example:

```cpp
   int myWindow=ChartWindowOnDropped();
   int windowsTotal=ChartGetInteger(0,CHART_WINDOWS_TOTAL);
   Print("Script is running on the window #"+myWindow+
         ". Total windows on the chart "+ChartSymbol()+":",windowsTotal);
```

See also

[ChartPriceOnDropped](../ChartPriceOnDropped/ChartPriceOnDropped.md), [ChartTimeOnDropped](../ChartTimeOnDropped/ChartTimeOnDropped.md), [ChartXOnDropped](../ChartXOnDropped/ChartXOnDropped.md), [ChartYOnDropped](../ChartYOnDropped/ChartYOnDropped.md)