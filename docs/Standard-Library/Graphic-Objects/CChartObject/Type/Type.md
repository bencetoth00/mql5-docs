# Type

Type

Gets the graphical object type ID.

|  |
| --- |
| virtual int  Type() const |

Return Value

Object type ID (0x8888 for [CChartObject](../CChartObject.md)).

Example:

|  |
| --- |
| //--- example for CChartObject::Type     #include <ChartObjects\ChartObject.mqh>     //---     void OnStart()       {        CChartObject object;     //--- get object type        int type=object.Type();       } |
