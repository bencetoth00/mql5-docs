# MathRandomNoncentralChiSquare

MathRandomNoncentralChiSquare

Generates a pseudorandom variable distributed according to the law of noncentral chi-squared distribution with the nu and sigma parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathRandomNoncentralChiSquare(     const double  nu,            // parameter of distribution (number of degrees of freedom)     const double  sigma,         // noncentrality parameter     int&          error\_code     // variable to store the error code     ); |

Generates pseudorandom variables distributed according to the law of noncentral chi-squared distribution with the nu and sigma parameters. In case of error it returns false. Analog of the [rchisq()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Chisquare.html) in R.

|  |
| --- |
| bool  MathRandomNoncentralChiSquare(     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  sigma,          // noncentrality parameter     const int     data\_count,     // amount of required data     double&       result[]        // array with values of pseudorandom variables     ); |

Parameters

nu

[in]  Parameter of distribution (number of degrees of freedom).

sigma

[in]  Noncentrality parameter.

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.
