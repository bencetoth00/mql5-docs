# Style

# Style (Get Method)

Gets the line style of the graphical object.

```cpp
ENUM_LINE_STYLE  Style() const
```

Return Value

Line style of the graphical object attached to the class instance. If there is no attached object, it returns WRONG\_VALUE.

# Style (Set Method)

Sets the line style of the graphical object.

```cpp
bool  Style(
   ENUM_LINE_STYLE  new_style      // style
   )
```

Parameters

new\_style

[in]  New value of the graphical object line style.

Return Value

true - success, false - cannot change the style.

Example:

```cpp
//--- example for CChartObject::Style
#include <ChartObjects\ChartObject.mqh>
//---
void OnStart()
  {
   CChartObject object;
   //--- get style of chart object
   ENUM_LINE_STYLE style=object.Style();
   if(style!=STYLE_SOLID)
     {
      //--- set style of chart object
      object.Style(STYLE_SOLID);
     }
  }
```