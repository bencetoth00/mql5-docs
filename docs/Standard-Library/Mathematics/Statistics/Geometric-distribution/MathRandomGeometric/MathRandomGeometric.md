# MathRandomGeometric

MathRandomGeometric

Generates a pseudorandom variable distributed according to the law of geometric distribution with the p parameter. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathRandomGeometric(     const double  p,              // parameter of the distribution (probability of event occurrence in one test)     int&          error\_code      // variable to store the error code     ); |

Generates pseudorandom variables distributed according to the law of geometric distribution with the p parameter. In case of error it returns false. Analog of the [rgeom()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Geometric.html) in R.

|  |
| --- |
| bool  MathRandomGeometric(     const double  p,              // parameter of the distribution (probability of event occurrence in one test)     const int     data\_count,     // amount of required data     double&       result[]        // array with values of pseudorandom variables     ); |

Parameters

p

[in]  Parameter of the distribution (probability of event occurrence in one test).  

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.
