# CheckTrailingStopLong


Checks Trailing Stop conditions of a long position.

```cpp
virtual bool  CheckTrailingStopLong(
   CPositionInfo*  position,     // pointer
   double&         sl,           // reference
   double&         tp            // reference
   )
```

Parameters

position

[in]  Pointer to [CPositionInfo](../../../../Trade-Classes/CPositionInfo/CPositionInfo.md) object.

sl

[in][out]  Reference to variable for Stop Loss price.

tp

[in][out]  Reference to variable for Take Profit price.

Return Value

true - conditions are satisfied, otherwise - false.

Note

The function always returns false.