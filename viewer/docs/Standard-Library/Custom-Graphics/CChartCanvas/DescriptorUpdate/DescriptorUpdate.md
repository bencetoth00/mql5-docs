# DescriptorUpdate


Updates the value of the series descriptor (at the specified position).

```cpp
 bool  DescriptorUpdate(
   const uint    pos,    // index
   const string  descr,  // value
   )
```

Parameters

pos

[in] Index of the series — the serial number of its addition, starting with 0.

descr

[in] Descriptor value.

Return Value

true if successful, otherwise — false.