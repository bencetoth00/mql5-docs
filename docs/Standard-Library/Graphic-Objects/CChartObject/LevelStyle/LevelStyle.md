# LevelStyle

LevelStyle (Get Method)

Gets the line style of the specified level of a graphical object.

|  |
| --- |
| ENUM\_LINE\_STYLE  LevelStyle(     int  level      // level number     ) const |

Parameters

level

[in]  Number of graphical object level.

Return Value

Line style of the specified level of the graphical object attached to an instance of the class. If there is no attached object or the object does not have the specified level, it returns WRONG\_VALUE.

LevelStyle (Set Method)

Sets the line style of the specified level of the graphic object.

|  |
| --- |
| int  LevelStyle(     int              level,     // level number     ENUM\_LINE\_STYLE  style      // line style     ) |

Parameters

level

[in]  Number of graphical object level.

style

[in]  New line style of the specified level of a graphical object.

Return Value

true - success, false - cannot change the style.

Example:

|  |
| --- |
| //--- example for CChartObject::LevelStyle   #include <ChartObjects\ChartObject.mqh>   //---   void OnStart()     {      CChartObject object;      //---      for(int i=0;i<object.LevelsCount();i++)        {         //--- get level style of chart object          ENUM\_LINE\_STYLE level\_style=object.LevelStyle(i);         if(level\_style!=STYLE\_SOLID)           {            //--- set level style of chart object            object.LevelStyle(i,STYLE\_SOLID);           }        }     } |
