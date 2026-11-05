# PriceMax


Gets window maximal price.

```cpp
double  PriceMax(
   int  num      // subwindow
   ) const
```

Parameters

num

[in]  Subwindow number (0 means main window).

Return Value

Window maximal price value of the chart assigned to the class instance. If there is not chart assigned, it returns [EMPTY\_VALUE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).