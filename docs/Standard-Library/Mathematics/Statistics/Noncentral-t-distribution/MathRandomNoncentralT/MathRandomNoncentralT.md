# MathRandomNoncentralT

MathRandomNoncentralT

Generates a pseudorandom variable distributed according to the law of noncentral Student's t-distribution with the nu and delta parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathRandomNoncentralT(     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     int&          error\_code      // variable to store the error code     ); |

Generates pseudorandom variables distributed according to the law of noncentral Student's t-distribution with the nu and delta parameters. In case of error it returns false. Analog of the [rt()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/TDist.html) in R.

|  |
| --- |
| bool  MathRandomNoncentralT(     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     const int     data\_count,     // amount of required data     double&       result[]        // array with values of pseudorandom variables     ); |

Parameters

nu

[in] Parameter of distribution (number of degrees of freedom).

delta

[in]  Noncentrality parameter.

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.
