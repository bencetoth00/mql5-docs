# ScaleFix

# ScaleFix (Get Method)

Gets the value of "ScaleFix" property (fixed chart scale or not).

```cpp
bool  ScaleFix() const
```

Return Value

Value of "ScaleFix" property of the chart assigned to the class instance. If there is no chart assigned, it returns false.

# ScaleFix (Set Method)

Sets new value for "ScaleFix" property.

```cpp
bool  ScaleFix(
   bool  scale_fix      // property value
   )
```

Parameters

scale\_fix

[in]  New value for "ScaleFix" property.

Return Value

true - successful, false - cannot change the property.