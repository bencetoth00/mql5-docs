# InitSignal


Initializes trading signal object.

```cpp
virtual bool  InitSignal(
   CExpertSignal*     signal=NULL,        // pointer
   )
```

Parameters

signal

[in]  Pointer to [CExpertSignal](../../CExpertSignal/CExpertSignal.md) class object (or its descendant).

Return Value

true - successful, otherwise - false.

Note

If signal is NULL, the [CExpertSignal](../../CExpertSignal/CExpertSignal.md) class will be used for initialization (it does nothing).