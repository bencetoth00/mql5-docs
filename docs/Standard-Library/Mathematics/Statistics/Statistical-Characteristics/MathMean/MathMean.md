# MathMean

MathMean

Calculates the mean (first moment) of array elements. Analog of the [mean()](https://stat.ethz.ch/R-manual/R-devel/library/base/html/mean.html) in R.

|  |
| --- |
| double  MathMean(     const double&  array[]                // array with data     ); |

Parameters

array

[in]  Array with data for calculation of the mean.

start=0

[in]  Initial index for calculation.

count=WHOLE\_ARRAY

[in]  The number of elements for calculation.

Return Value

The mean of array elements. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) (not a number).
