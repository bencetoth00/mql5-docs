# Navigate


Shifts the chart.

```cpp
bool  Navigate(
   ENUM_CHART_POSITION  position,     // position
   int                  shift=0       // shift
   )
```

Parameters

position

[in]  Chart position (from [ENUM\_CHART\_POSITION](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Positioning-Constants/Positioning-Constants.md) enumeration), relative to which a shift is performed.

shift=0

[in]  Number of bars to shift.

Return Value

true - successful, false - cannot shift the chart.