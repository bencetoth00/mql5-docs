# AmbientColorGet


Gets the color and intensity of the ambient all-round lighting.

```cpp
void  AmbientColorGet(
   DXColor  &ambient_color      // all-round lighting color and intensity
   );
```

Parameters

&ambient\_color

[out]  All-round lighting color.

Return Value

No

Note

Intensity is stored in the alpha channel of the DXColor structure.