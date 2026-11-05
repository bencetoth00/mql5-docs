# MathRandomExponential

MathRandomExponential

Generates a pseudorandom variable distributed according to the law of exponential distribution with the mu parameter. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathRandomExponential(     const double  mu,            // parameter of the distribution (expected value)     int&          error\_code     // variable to store the error code     ); |

Generates pseudorandom variables distributed according to the law of exponential distribution with the mu parameter. In case of error it returns false. Analog of the [rexp()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Exponential.html) in R.

|  |
| --- |
| bool  MathRandomExponential(     const double  mu,             // parameter of the distribution (expected value)     const int     data\_count,     // amount of required data     double&       result[]        // array with values of pseudorandom variables     ); |

Parameters

mu

[in]  Parameter of the distribution (expected value).

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.
