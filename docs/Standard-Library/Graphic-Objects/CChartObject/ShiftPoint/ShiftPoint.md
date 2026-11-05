# ShiftPoint

ShiftPoint

Shifts a specified anchor point of the graphical object.

|  |
| --- |
| bool  ShiftPoint(     int       point,       // point number     datetime  d\_time,      // increment of time coordinate     double    d\_price      // increment of price coordinate     ) |

Parameters

point

[in]  Number of a graphical object anchor point.

d\_time

[in]  Increment of the time coordinate of the specified point.

d\_price

[in]  Increment of the price coordinate of the specified point.

Return Value

true - success, false - cannot shift the point.

Example:

|  |
| --- |
| //--- example for CChartObject::ShiftPoint    #include <ChartObjects\ChartObject.mqh>    //---    void OnStart()      {       CChartObject object;       datetime     d\_time;       double       d\_price;       //---       if(object.NumPoints()>0)         {          //--- shift point of chart object          object.ShiftPoint(0,d\_time,d\_price);         }      } |
