# TimeSetupMsc


Receives the time of placing an order for execution in milliseconds since 01.01.1970.

```cpp
ulong  TimeSetupMsc() const
```

Return Value

The time of placing an order for execution in milliseconds since 01.01.1970.

Note

Order should be preliminarily selected for access using [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) method.