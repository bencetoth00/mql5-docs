# TextAlign

# TextAlign (Get method)

Gets the value of "TextAlign" property ([text alignment mode)](../../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_align_mode).

```cpp
ENUM_ALIGN_MODE  TextAlign() const
```

Return Value

Value of "TextAlign" property of the object assigned to the class instance.

 

# TextAlign (Set method)

Sets the value of "TextAlign" property ([text aligment mode)](../../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_align_mode).

```cpp
bool  TextAlign(
   ENUM_ALIGN_MODE  align      // property value
   )
```

Parameters

align

[in]  New value of "TextAlign" property.

Return Value

true - success, false - cannot change the property.