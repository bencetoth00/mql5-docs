# CheckTrailingStopLong


Checks conditions to modify parameters of a long position.

```cpp
virtual bool  CheckTrailingStopLong(
   CPositionInfo*  position,     // pointer
   double&         sl,           // Stop Loss
   double&         tp            // Take Profit
   )
```

Parameters

position

[in]  Pointer to [CPositionInfo](../../../../Trade-Classes/CPositionInfo/CPositionInfo.md) class object.

sl

[in][out]  Variable for Stop Loss price, passed by reference.

tp

[in][out]  Variable for Take Profit price, passed by reference.

Return Value

true - condition is satisfied, otherwise - false.

Note

Base class method always returns false.