# SetDouble

SetDouble

Provides simplified access to the functions of API MQL5 [ObjectSetDouble()](../../../../Object-Functions/ObjectSetDouble/ObjectSetDouble.md) to change double properties (of float and double types) of a graphical object bound to a class instance. There are two versions of a function call:

Setting a property value that does not require a modifier

|  |
| --- |
| bool  SetDouble(     ENUM\_OBJECT\_PROPERTY\_DOUBLE   prop\_id,     // double property ID     double                        value        // value     ) |

Parameters

prop\_id

[in]  ID of a graphical object double property.

value

[in]  New value of a changed double property.

Setting a property value indicating the modifier

|  |
| --- |
| bool  SetDouble(     ENUM\_OBJECT\_PROPERTY\_DOUBLE   prop\_id,      // double property ID     int                           modifier,     // modifier      double                        value         // value     ) |

Parameters

prop\_id

[in]  ID of a graphical object double property.

modifier

[in]  Modifier (index) of a double property.

value

[in]  New value of a changed double property.

Return Value

true - success, false - cannot change the double feature.

Example:

|  |
| --- |
| //--- example for CChartObject::SetDouble    #include <ChartObjects\ChartObject.mqh>    //---    void OnStart()      {       CChartObject object;    //---     for(int i=0;i<object.LevelsCount();i++)         {          //--- set level value of chart object          if(!object.SetDouble(OBJPROP\_LEVELVALUE,i,0.1\*i))            {             printf("Set double property error %d",GetLastError());             return;            }         }      } |
