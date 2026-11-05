# ObjectGetInteger

ObjectGetInteger

The function returns the value of the corresponding object property. The object property must be of the [datetime, int, color, bool or char](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| long  ObjectGetInteger(     long                             chart\_id,          // chart identifier     string                           name,              // object name     ENUM\_OBJECT\_PROPERTY\_INTEGER     prop\_id,           // property identifier     int                              prop\_modifier=0    // property modifier, if required     ); |

2. Returns true or false, depending on the success of the function. If successful, the property value is placed to a receiving variable passed by reference by the last parameter.

|  |
| --- |
| bool  ObjectGetInteger(     long                             chart\_id,          // chart identifier     string                           name,              // object name     ENUM\_OBJECT\_PROPERTY\_INTEGER     prop\_id,           // property identifier     int                              prop\_modifier,     // property modifier     long&                            long\_var           // here we accept the property value     ); |

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object.

prop\_id

[in]  ID of the object property. The value can be one of the values of the [ENUM\_OBJECT\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) enumeration.

prop\_modifier

[in]  Modifier of the specified property. For the first variant, the default modifier value is equal to 0. Most properties do not require a modifier.  It denotes the number of the level in [Fibonacci tools](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) and in the graphical object Andrew's pitchfork. The numeration of levels starts from zero.

long\_var

[out]  Variable of the long type that receives the value of the requested property.

Return Value

The long value for the first calling variant.

For the second variant the function returns true, if this property is maintained and the value has been placed into the long\_var variable, otherwise returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Note

The function uses a synchronous call, which means that the function waits for the execution of all commands that have been enqueued for this chart prior to its call, that is why this function can be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

 

Example:

|  |
| --- |
| #property copyright "Copyright 2025, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   OBJ\_NAME   "TestObjectGetInteger"  // Object name     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- current chart ID     long chart\_id=ChartID();     //--- create a "Vertical Line" graphical object at the current known server time     if(!ObjectCreate(chart\_id, OBJ\_NAME, OBJ\_VLINE, 0, TimeCurrent(), 0))       {        Print("ObjectCreate() failed. Error ", GetLastError());        return;       }  //--- update the chart to immediately reflect the changes     ChartRedraw(chart\_id);       //--- get the object creation time     long long\_var=0;     if(!ObjectGetInteger(chart\_id, OBJ\_NAME, OBJPROP\_CREATETIME, 0, long\_var))       {        Print("ObjectGetInteger() failed. Error ", GetLastError());        return;       }  //--- string representation of the object creation time     string create\_time=TimeToString((datetime)long\_var, TIME\_DATE|TIME\_MINUTES|TIME\_SECONDS);       //--- get the time set in the object     if(!ObjectGetInteger(chart\_id, OBJ\_NAME, OBJPROP\_TIME, 0, long\_var))       {        Print("ObjectGetInteger() failed. Error ", GetLastError());        return;       }  //--- string representation of the object location time     string obj\_time=TimeToString((datetime)long\_var, TIME\_DATE|TIME\_MINUTES|TIME\_SECONDS);       //--- get the object type     ENUM\_OBJECT object\_type=(ENUM\_OBJECT)ObjectGetInteger(chart\_id, OBJ\_NAME, OBJPROP\_TYPE);       //--- output to the journal the type of object, the time of its creation and the time on the chart the graphical object is located on     PrintFormat("%s object created at %s at chart point with time %s",EnumToString(object\_type), create\_time, obj\_time);       //--- wait two seconds and delete the created object     Sleep(2000);     ObjectDelete(chart\_id, OBJ\_NAME);     ChartRedraw(chart\_id);     /\*     result:     OBJ\_VLINE object created at 2025.02.01 12:15:37 at chart point with time 2025.01.31 23:54:59     \*/    } |
