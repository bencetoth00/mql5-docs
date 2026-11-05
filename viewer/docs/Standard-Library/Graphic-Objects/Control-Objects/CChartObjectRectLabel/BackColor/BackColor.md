# BackColor

# BackColor

Gets the background color property value.

```cpp
color  BackColor() const
```

Return Value

Background color property value of the object assigned to the class instance. If there is no object assigned, it returns 0.

 

BackColor

Sets the background color property value.

```cpp
bool  BackColor(
   color  new_color      // property value
   )
```

Parameters

new\_color

[in]  New background color property value.

Return Value

true - successful, false - cannot change the property.