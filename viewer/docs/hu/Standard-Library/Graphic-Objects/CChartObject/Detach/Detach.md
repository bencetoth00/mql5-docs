# Detach


Leválasztja a grafikus objektumot.

```cpp
void  Detach()
```

Visszatérési érték

Nincs.

Példa:

```cpp
//--- example for CChartObject::Detach
#include <ChartObjects\ChartObject.mqh>
//---
void OnStart()
  {
   CChartObject object;
   //--- detach chart object
   object.Detach();
  }
```
