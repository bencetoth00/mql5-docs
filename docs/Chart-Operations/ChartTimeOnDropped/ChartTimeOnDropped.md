# ChartTimeOnDropped

ChartTimeOnDropped

Returns the time coordinate corresponding to the chart point the Expert Advisor or script has been dropped to.

|  |
| --- |
| datetime  ChartTimeOnDropped(); |

Return Value

Value of [datetime](../../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) type.

Example:

|  |
| --- |
| datetime t=ChartTimeOnDropped();     Print("Script was dropped on the "+t); |

See also

[ChartXOnDropped](../ChartXOnDropped/ChartXOnDropped.md), [ChartYOnDropped](../ChartYOnDropped/ChartYOnDropped.md)
