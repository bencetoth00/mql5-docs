# RenderEnd


Bemásolja a renderelt képkockát a belső pufferbe, és szükség esetén frissíti a diagram képét.

```cpp
virtual bool  RenderEnd(
   bool  redraw=false      // update flag
   );
```

Paraméterek

redraw=false

[in]  Jelző, amely meghatározza, szükséges-e a diagram újrarajzolása.

Visszatérési érték

Siker esetén true, egyébként false.
