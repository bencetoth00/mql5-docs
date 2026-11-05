# ChartXOnDropped

ChartXOnDropped

Returns the X coordinate of the chart point the Expert Advisor or script has been dropped to.

|  |
| --- |
| int  ChartXOnDropped(); |

Return Value

The X coordinate value.

Note

X axis direction from left to right.

Example:

|  |
| --- |
| int X=ChartXOnDropped();     int Y=ChartYOnDropped();     Print("(X,Y) = ("+X+","+Y+")"); |

See also

[ChartWindowOnDropped](../ChartWindowOnDropped/ChartWindowOnDropped.md), [ChartPriceOnDropped](../ChartPriceOnDropped/ChartPriceOnDropped.md), [ChartTimeOnDropped](../ChartTimeOnDropped/ChartTimeOnDropped.md)
