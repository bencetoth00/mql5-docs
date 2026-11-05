# ObjectSetString

ObjectSetString

The function sets the value of the corresponding object property. The object property must be of the [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type. There are 2 variants of the function.

Setting property value, without modifier

|  |
| --- |
| bool  ObjectSetString(     long                            chart\_id,          // chart identifier     string                          name,              // object name     ENUM\_OBJECT\_PROPERTY\_STRING     prop\_id,           // property     string                          prop\_value         // value     ); |

Setting a property value indicating the modifier

|  |
| --- |
| bool  ObjectSetString(     long                            chart\_id,          // chart identifier     string                          name,              // object name     ENUM\_OBJECT\_PROPERTY\_STRING     prop\_id,           // property     int                             prop\_modifier,     // modifier     string                          prop\_value         // value     ); |

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object.

prop\_id

[in]  ID of the object property. The value can be one of the values of the [ENUM\_OBJECT\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_string) enumeration.

prop\_modifier

[in]  Modifier of the specified property.  It denotes the number of the level in [Fibonacci tools](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) and in the graphical object Andrew's pitchfork. The numeration of levels starts from zero.

prop\_value

[in]  The value of the property.

Return Value

The function returns true only if the command to change properties of a graphical object has been sent to a chart successfully. Otherwise it returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Note

The function uses an asynchronous call, which means that the function does not wait for the execution of the command that has been added to the queue of the specified chart. Instead, it immediately returns control.

To check the command execution result, you can use a function that requests the specified object property. However, you should keep in mind that such functions are added to the end of the queue of that chart, and they wait for the execution result, and can therefore be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

When an object is renamed, two events are formed simultaneously. These events can be handled in an Expert Advisor or indicator by the [OnChartEvent()](../../Event-Handling/OnChartEvent/OnChartEvent.md) function:

- an event of deletion of an object with the old name;
- an event of creation of an object with a new name.

 

Example:

|  |
| --- |
| #property copyright "Copyright 2025, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   OBJ\_NAME   "TestObjectSetString"   // Object name     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- current chart ID and symbol, flag for displaying object descriptions     long   chart\_id= ChartID();     string symbol  = ChartSymbol(chart\_id);     bool   descript= ChartGetInteger(chart\_id, CHART\_SHOW\_OBJECT\_DESCR);        //--- set the display of object descriptions on the chart     ChartSetInteger(chart\_id, CHART\_SHOW\_OBJECT\_DESCR, true);     //--- get the current Bid price     double bid=0;;     ResetLastError();     if(!SymbolInfoDouble(symbol, SYMBOL\_BID, bid))       {        Print("SymbolInfoDouble() failed. Error ", GetLastError());        return;       }         //--- create the "Horizontal line" graphical object on the current Bid price     if(!ObjectCreate(chart\_id, OBJ\_NAME, OBJ\_HLINE, 0, 0, bid))       {        Print("ObjectCreate() failed. Error ", GetLastError());        return;       }  //--- enter the object name+"Description" into the object description     if(!ObjectSetString(chart\_id, OBJ\_NAME, OBJPROP\_TEXT, "Bid: "+DoubleToString(bid, (int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS))))       {        Print("ObjectSetString() failed. Error ", GetLastError());        return;       }  //--- update the chart to immediately reflect the changes     ChartRedraw(chart\_id);       //--- get the object description     string string\_var="";     if(!ObjectGetString(chart\_id, OBJ\_NAME, OBJPROP\_TEXT, 0, string\_var))       {        Print("ObjectGetInteger() failed. Error ", GetLastError());        return;       }  //--- get the object name     string obj\_name=ObjectGetString(chart\_id, OBJ\_NAME, OBJPROP\_NAME);       //--- get the object type     ENUM\_OBJECT object\_type=(ENUM\_OBJECT)ObjectGetInteger(chart\_id, OBJ\_NAME, OBJPROP\_TYPE);       //--- display the object type, its name and description in the journal     PrintFormat("The %s object named \"%s\" has the description \"%s\"",EnumToString(object\_type), obj\_name, string\_var);       //--- wait two seconds and delete the created object     Sleep(2000);     ObjectDelete(chart\_id, OBJ\_NAME);       //--- return the initial flag for displaying descriptions of objects for the chart     ChartSetInteger(chart\_id, CHART\_SHOW\_OBJECT\_DESCR, descript);     ChartRedraw(chart\_id);     /\*     result:     The OBJ\_HLINE object named "TestObjectSetString" has the description "Bid: 0.62096"     \*/    } |
