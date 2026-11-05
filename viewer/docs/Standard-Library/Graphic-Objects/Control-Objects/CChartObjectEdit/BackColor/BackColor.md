# BackColor

# BackColor (Get Method)

Gets the value of "BackColor" property.

```cpp
color  BackColor() const
```

Return Value

Value of "BackColor" property of the object assigned to the class instance. If there is no object assigned, it returns CLR\_NONE.

# BackColor (Set Method)

Sets the value for "BackColor" property.

```cpp
bool  BackColor(
   color  new_color      // property value
   )
```

Parameters

new\_color

[in]  New value for "BackColor" property.

Return Value

true - success, false - cannot change the property.