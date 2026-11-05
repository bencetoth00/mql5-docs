# ShiftObject

ShiftObject

Shifts a graphical object.

|  |
| --- |
| bool  ShiftObject(     datetime  d\_time,      // increment of time coordinate     double    d\_price      // increment of price coordinate     ) |

Parameters

d\_time

[in]  Increment of the time coordinate of all anchor points.

d\_price

[in]  Increment of the price coordinate of all anchor points.

Return Value

true - success, false - cannot shift the object.

Example:

|  |
| --- |
| //--- example for CChartObject::ShiftObject    #include <ChartObjects\ChartObject.mqh>    //---    void OnStart()      {       CChartObject object;       datetime     d\_time;       double       d\_price;       //--- shift chart object       object.ShiftObject(d\_time,d\_price);      } |
