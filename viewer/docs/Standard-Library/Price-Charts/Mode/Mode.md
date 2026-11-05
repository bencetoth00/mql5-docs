# Mode

# Mode (Get Method)

Gets the value of "Mode" property (bars, candles, or line).

```cpp
ENUM_CHART_MODE  Mode() const
```

Return Value

Value of "Mode" property of the object assigned to the class instance. If there is no chart assigned, it returns [WRONG\_VALUE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# Mode (Set Method)

Sets new value for "Mode" property (bars, candles, or line).

```cpp
bool  Mode(
   ENUM_CHART_MODE  mode      // chart mode
   )
```

Parameters

mode

[in]  Chart mode (candles, bars or line) of [ENUM\_CHART\_MODE](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Representation/Chart-Representation.md#enum_chart_mode) enumeration.

Return Value

true - successful, false - cannot change the mode.