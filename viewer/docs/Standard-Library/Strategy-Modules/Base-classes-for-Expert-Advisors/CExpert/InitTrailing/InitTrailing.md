# InitTrailing


Initializes trailing stop object.

```cpp
virtual bool  InitTrailing(
   CExpertTrailing*     trailing=NULL,        // pointer
   )
```

Parameters

trailing

[in]  Pointer to [CExpertTrailing](../../CExpertTrailing/CExpertTrailing.md) class object (or its descendant).

Return Value

true - successful, otherwise - false.

Note

If trailing is NULL, the [ExpertTrailing](../../CExpertTrailing/CExpertTrailing.md) class will be used for initialization (it does nothing).