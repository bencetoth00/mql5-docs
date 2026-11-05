# Type

Type

Returns graphical object type identifier.

|  |
| --- |
| virtual int  Type() const |

Return Value

Object type identifier (for example, OBJ\_ARROW for [CChartObjectArrow](../CChartObjectArrow.md))

Example:

|  |
| --- |
| //--- example for CChartObjectArrow::Type     #include <ChartObjects\ChartObjectsArrows.mqh>     //---     void OnStart()       {        CChartObjectArrow arrow;        //--- get arrow type        int type=arrow.Type();       } |
