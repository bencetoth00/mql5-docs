# ChartGetDouble

ChartGetDouble

Returns the value of a corresponding property of the specified chart. Chart property must be of double type. There are 2 variants of the function calls.

1. Returns the property value directly.

|  |
| --- |
| double  ChartGetDouble(     long                         chart\_id,          // Chart ID     ENUM\_CHART\_PROPERTY\_DOUBLE   prop\_id,           // Property ID     int                          sub\_window=0       // subwindow number, if necessary     ); |

2. Returns true or false, depending on the success of a function. If successful, the value of the property is placed in a target variable double\_var passed by reference.

|  |
| --- |
| bool  ChartGetDouble(     long                         chart\_id,          // Chart ID     ENUM\_CHART\_PROPERTY\_DOUBLE   prop\_id,           // Property ID     int                          sub\_window,      // Subwindow number     double&                      double\_var       // Target variable for the chart property     ); |

Parameters

chart\_id

[in]  Chart ID. 0 means the current chart.

prop\_id

[in]  Chart property ID. This value can be one of the [ENUM\_CHART\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_double) values.

sub\_window

[in]  Number of the chart subwindow. For the first case, the default value is 0 (main chart window). The most of the properties do not require a subwindow number.

double\_var

[out]  Target variable of double type for the requested property.

Return Value

The value of double type.

For the second call case it returns true if the specified property is available and its value has been placed into double\_var variable, otherwise returns false. To get an additional information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), it is necessary to call the function [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Note

The function is synchronous, which means that it waits for the execution of all the commands that have been added to the chart queue prior to its call.

Example:

|  |
| --- |
| void OnStart()    {     double priceMin=ChartGetDouble(0,CHART\_PRICE\_MIN,0);     double priceMax=ChartGetDouble(0,CHART\_PRICE\_MAX,0);     Print("CHART\_PRICE\_MIN =",priceMin);     Print("CHART\_PRICE\_MAX =",priceMax);    } |
