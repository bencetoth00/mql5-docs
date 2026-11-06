# Delete


Eltávolítja a diagramhoz csatolt grafikus objektumot.

```cpp
bool  Delete()
```

Visszatérési érték

true, ha sikerült; false, ha az objektum nem távolítható el.

Példa:

```cpp
//--- example for CChartObject::Delete
#include <ChartObjects\ChartObject.mqh>
//---
void OnStart()
  {
   CChartObject object;
   //--- detach chart object
   if(!object.Delete())
     {
      printf("Object delete error");
      return;
     }
  }
```
