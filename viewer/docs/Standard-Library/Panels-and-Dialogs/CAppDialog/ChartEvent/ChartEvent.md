# ChartEvent


Virtual handler of the control events.

```cpp
virtual bool  ChartEvent(
   const int      id,         // ID
   const long&    lparam,     // parameter
   const double&  dparam,     // parameter
   const string&  sparam      // parameter
   )
```

Parameters

id

[in]  Event ID.

lparam

[in]  Event parameter of [long](../../../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#long) type passed by reference.

dparam

[in]  Event parameter of [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type passed by reference.

sparam

[in]  Event parameter of [string](../../../../Language-Basics/Data-Types/String-Type/String-Type.md) type passed by reference.

Return Value

true - event processed, otherwise - false.