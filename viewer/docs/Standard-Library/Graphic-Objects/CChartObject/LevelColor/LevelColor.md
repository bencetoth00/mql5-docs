# LevelColor

# LevelColor (Get Method)

Gets the line color of the specified level of a graphical object.

```cpp
color  LevelColor(
   int  level      // level number
   ) const
```

Parameters

level

[in]  Number of graphical object level.

Return Value

Line color of the specified level of the graphical object attached to the instance of the class. If there is no attached object or the object does not have the specified level, it returns CLR\_NONE.

# LevelColor (Set Method)

Sets the line color of the specified level of the graphical object.

```cpp
bool  LevelColor(
   int    level,         // level number
   color  new_color      // new color
   )
```

Parameters

level

[in]  Number of graphical object level.

new\_color

[in]  New line color of the specified level of a graphical object.

Return Value

true - success, false - cannot change the color.

Example:

```cpp
//--- example for CChartObject::LevelColor
#include <ChartObjects\ChartObject.mqh>
//---
void OnStart()
  {
   CChartObject object;
   //---
   for(int i=0;i<object.LevelsCount();i++)
     {
      //--- get level color of chart object
      color level_color=object.LevelColor(i);
      if(level_color!=clrRed)
        {
         //--- set level color of chart object
         object.LevelColor(i,clrRed);
        }
     }
  }
```