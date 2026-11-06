# Type


Visszaadja a grafikus objektum típusazonosítóját.

```cpp
virtual int  Type() const
```

Visszatérési érték

Az objektum típusazonosítója (például OBJ\_ARROW a [CChartObjectArrow](../CChartObjectArrow.md) esetén).

Példa:

```cpp
//--- example for CChartObjectArrow::Type
#include <ChartObjects\ChartObjectsArrows.mqh>
//---
void OnStart()
  {
   CChartObjectArrow arrow;
   //--- get arrow type
   int type=arrow.Type();
  }
```
