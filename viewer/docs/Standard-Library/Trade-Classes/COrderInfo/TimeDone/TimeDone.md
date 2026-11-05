# TimeDone


Gets the time of order execution or cancellation.

```cpp
datetime  TimeDone() const
```

Return Value

Time of order execution or cancellation.

Note

The order should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.