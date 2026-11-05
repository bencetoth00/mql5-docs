# ShiftSize

# ShiftSize (Get Method)

Gets the value of "ShiftSize" property (in percents).

```cpp
double  ShiftSize() const
```

Return Value

Value of "ShiftSize" property of the chart assigned to the class instance. If there is no chart assigned, it returns [EMPTY\_VALUE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ShiftSize (Set Method)

Sets new value for "Shift" property (in percents).

```cpp
bool  ShiftSize(
   double  shift_size      // property value
   )
```

Parameters

shift\_size

[in]  New value for "ShiftSize" property (in percents).

Return Value

true - successful, false - cannot change the property.