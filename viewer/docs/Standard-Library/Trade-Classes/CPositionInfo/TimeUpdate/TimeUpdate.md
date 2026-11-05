# TimeUpdate


Receives the time of position changing in seconds since 01.01.1970.

```cpp
datetime  TimeUpdate() const
```

Return Value

Time of position changing in seconds since 01.01.1970.

Note

Position should be preliminarily selected for access using [Select](../Select/Select.md) (by symbol) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) method.