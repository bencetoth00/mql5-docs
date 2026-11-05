# RenderBegin


Prepares a graphic context for rendering a new frame.

```cpp
virtual bool  RenderBegin(
   uint  flags,                  // combination of flags
   uint  background_color=0      // background color
   );
```

Parameters

flags

[in]   Combination of flags that sets the rendering mode. Possible values:  
DX\_CLEAR\_COLOR – clear the image buffer using background\_color.  
DX\_CLEAR\_DEPTH – clear the depth buffer.

background\_color=0

[in]  3D scene background color.

Return Value

true – if successful, false - if failed to update shader inputs.