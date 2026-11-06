# Type


Lekéri a grafikus objektum típusazonosítóját.

```cpp
virtual int  Type() const
```

Visszatérési érték

Az objektum típusazonosítója (0x8888 a [CChartObject](../CChartObject.md) esetén).

Példa:

```cpp
//--- example for CChartObject::Type
#include <ChartObjects\ChartObject.mqh>
//---
void OnStart()
  {
   CChartObject object;
   //--- get object type
   int type=object.Type();
  }
```
