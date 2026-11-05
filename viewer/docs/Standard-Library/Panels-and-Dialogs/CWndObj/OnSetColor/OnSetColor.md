# OnSetColor


The virtual handler of control "SetColor" (change of the [OBJPROP\_COLOR](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) property) event.

```cpp
virtual bool  OnSetColor()
```

Return Value

true - event processed, otherwise - false.

Note

The base class method does nothing and always returns true.