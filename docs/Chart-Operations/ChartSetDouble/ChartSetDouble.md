# ChartSetDouble

ChartSetDouble

Sets a value for a corresponding property of the specified chart. Chart property should be of a [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type. The command is added to chart messages queue and will be executed after processing of all previous commands.

|  |
| --- |
| bool  ChartSetDouble(     long                           chart\_id,     // Chart ID     ENUM\_CHART\_PROPERTY\_DOUBLE     prop\_id,      // Property ID     double                         value         // Value     ); |

Parameters

chart\_id

[in]  Chart ID. 0 means the current chart.

prop\_id

[in]  Chart property ID. Can be one of the [ENUM\_CHART\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_double) values (except the read-only properties).

value

[in] Property value.

Return Value

Returns true if the command has been added to chart queue, otherwise false. To get an information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

The function is asynchronous, which means that the function does not wait for the execution of the command, which has been successfully added to the queue of specified the chart. Instead, it immediately returns control. The property will only change after the handling of the appropriate command from the chart queue. To immediately execute commands from the chart queue, call the [ChartRedraw](../ChartRedraw/ChartRedraw.md) function.

If you want to immediately change several chart properties at once, then the corresponding functions ([ChartSetString](../ChartSetString/ChartSetString.md), [ChartSetDouble](ChartSetDouble.md), [ChartSetString](../ChartSetString/ChartSetString.md)) should be executed in one code block, after which you should call [ChartRedraw](../ChartRedraw/ChartRedraw.md) once.

To check the command execution result, you can use a function, which requests the specified chart property ([ChartGetInteger](../ChartGetInteger/ChartGetInteger.md), [ChartGetDouble](../ChartGetDouble/ChartGetDouble.md), [ChartSetString](../ChartSetString/ChartSetString.md)). However, note that these functions are synchronous and wait for execution results.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the current chart ID     long chart\_id = ChartID();       //--- save the initial offset of the zero bar from the right edge in percentage and the auto scroll flag     double shift = ChartGetDouble(chart\_id, CHART\_SHIFT\_SIZE);     bool   scroll= ChartGetInteger(chart\_id,CHART\_AUTOSCROLL);       //--- reset the auto scroll chart flag     ChartSetInteger(chart\_id, CHART\_AUTOSCROLL, true);     PrintFormat("Initial chart shift size: %.2f", shift);     //--- in the loop from 2.0% to 50.0% with the step of 0.5%     for(int i=20; i<=500; i+=5)       {        //--- set the shift size as i / 10 and print the specified value in the journal        ChartSetDouble(chart\_id, CHART\_SHIFT\_SIZE, i/10.0);        PrintFormat("Set chart shift size to %.1f%%", i/10.0);                //--- keep the chart zero bar at the specified shift distance        ChartNavigate(chart\_id, CHART\_END, 0);                //--- wait a bit        Sleep(16);       }     //--- set the initial chart shift and auto scroll     Print("Set the chart shift size to the initial value of ", shift);     ChartSetDouble(ChartID(), CHART\_SHIFT\_SIZE, shift);     ChartSetInteger(chart\_id, CHART\_AUTOSCROLL, scroll);    } |
