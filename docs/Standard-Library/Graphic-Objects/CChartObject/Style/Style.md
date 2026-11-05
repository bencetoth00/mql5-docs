# Style

Style (Get Method)

Gets the line style of the graphical object.

|  |
| --- |
| ENUM\_LINE\_STYLE  Style() const |

Return Value

Line style of the graphical object attached to the class instance. If there is no attached object, it returns WRONG\_VALUE.

Style (Set Method)

Sets the line style of the graphical object.

|  |
| --- |
| bool  Style(     ENUM\_LINE\_STYLE  new\_style      // style     ) |

Parameters

new\_style

[in]  New value of the graphical object line style.

Return Value

true - success, false - cannot change the style.

Example:

|  |
| --- |
| //--- example for CChartObject::Style    #include <ChartObjects\ChartObject.mqh>    //---    void OnStart()      {       CChartObject object;       //--- get style of chart object        ENUM\_LINE\_STYLE style=object.Style();       if(style!=STYLE\_SOLID)         {          //--- set style of chart object          object.Style(STYLE\_SOLID);         }      } |
