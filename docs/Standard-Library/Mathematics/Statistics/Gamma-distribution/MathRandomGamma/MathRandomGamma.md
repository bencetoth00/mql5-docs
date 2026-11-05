# MathRandomGamma

MathRandomGamma

Generates a pseudorandom variable distributed according to the law of gamma distribution with the a and b parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathRandomGamma(     const double  a,             // the first parameter of the distribution (shape)     const double  b,             // the second parameter of the distribution (scale)     int&          error\_code     // variable to store the error code     ); |

Generates pseudorandom variables distributed according to the law of gamma distribution with the a and b parameters. In case of error it returns false. Analog of the [rgamma()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/GammaDist.html) in R.

|  |
| --- |
| bool  MathRandomGamma(     const double  a,              // the first parameter of the distribution (shape)     const double  b,              // the second parameter of the distribution (scale)     const int     data\_count,     // amount of required data     double&       result[]        // array with values of pseudorandom variables     ); |

Parameters

a

[in]  The first parameter of the distribution (shape).

b

[in]  The second parameter of the distribution (scale).

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.
