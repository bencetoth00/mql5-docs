# TimeDoneMsc


Receives order execution or cancellation time in milliseconds since 01.01.1970.

```cpp
ulong  TimeDoneMsc() const
```

Return Value

Order execution or cancellation time in milliseconds since 01.01.1970.

Note

Order should be preliminarily selected for access using [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) method.