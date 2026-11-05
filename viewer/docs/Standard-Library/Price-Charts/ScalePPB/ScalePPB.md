# ScalePPB

# ScalePPB (Get Method)

Gets the value of "ScalePPB" property (scale is "point per bar" or not).

```cpp
bool  ScalePPB() const
```

Return Value

Value of "ScalePPB" property of the chart assigned to the class instance. If there is no chart assigned, it returns false.

# ScalePPB (Set Method)

Sets new value for "ScalePPB" property.

```cpp
bool  ScalePPB(
   bool  scale_ppb      // flag value
   )
```

Parameters

scale\_ppb

[in]  New value for "ScalePPB" property.

Return Value

true - successful, false - cannot change the property.