# SetInteger

SetInteger

Provides simplified access to the functions of API MQL5 [ObjectSetInteger()](../../../../Object-Functions/ObjectSetInteger/ObjectSetInteger.md) to change integer properties (of type bool, char, uchar, short, ushort, int, uint, long, ulong, datetime, color types) of a graphical object bound to class instance. There are two versions of the function call:

Setting a property value that does not require a modifier

|  |
| --- |
| bool  SetInteger(     ENUM\_OBJECT\_PROPERTY\_INTEGER   prop\_id,     // integer property ID     long                           value        // value     ) |

Parameters

prop\_id

[in]  ID of a graphical object integer property.

value

[in]  New value of a changed integer property.

Setting a property value indicating the modifier

|  |
| --- |
| bool  SetInteger(     ENUM\_OBJECT\_PROPERTY\_INTEGER   prop\_id,      // integer property ID     int                            modifier,     // modifier      long                           value         // value     ) |

Parameters

prop\_id

[in]  ID of a graphical object integer property.

modifier

[in]  Modifier (index) of an integer property.

value

[in]  New value of an integer property.

Return Value

true - success, false - cannot change the integer property.

Example:

|  |
| --- |
| //--- example for CChartObject::SetInteger    #include <ChartObjects\ChartObject.mqh>    //---    void OnStart()      {       CChartObject object;       //--- set new color of chart object        if(!object.SetInteger(OBJPROP\_COLOR,clrRed))         {          printf("Set integer property error %d",GetLastError());          return;         }       for(int i=0;i<object.LevelsCount();i++)         {          //--- set levels width          if(!object.SetInteger(OBJPROP\_LEVELWIDTH,i,i))            {             printf("Set integer property error %d",GetLastError());             return;            }         }      } |
