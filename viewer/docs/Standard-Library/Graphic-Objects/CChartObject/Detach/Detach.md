# Detach


Detaches the graphical object.

```cpp
void  Detach()
```

Return Value

None.

Example:

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