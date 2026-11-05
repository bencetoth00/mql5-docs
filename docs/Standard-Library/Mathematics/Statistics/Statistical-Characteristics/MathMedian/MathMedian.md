# MathMedian

MathMedian

Calculates the median value of array elements. Analog of the [median()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/median.html) in R.

|  |
| --- |
| double  MathMedian(     const double&  array[]                // array with data     ); |

Parameters

array

[in]  Array with data for calculation.

start=0

[in]  Initial index for calculation.

count=WHOLE\_ARRAY

[in]  The number of elements for calculation.

Return Value

The median value of array elements. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) (not a number).
