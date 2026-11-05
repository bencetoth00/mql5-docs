# MathProbabilityDensityCauchy

MathProbabilityDensityCauchy

Calculates the value of the probability density function of Cauchy distribution with the a and b parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathProbabilityDensityCauchy(     const double  x,             // value of random variable     const double  a,             // mean parameter of the distribution     const double  b,             // scale parameter of the distribution     const bool    log\_mode,      // calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability density is calculated     int&          error\_code     // variable to store the error code     ); |

Calculates the value of the probability density function of Cauchy distribution with the a and b parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathProbabilityDensityCauchy(     const double  x,             // value of random variable     const double  a,             // mean parameter of the distribution     const double  b,             // scale parameter of the distribution     int&          error\_code     // variable to store the error code     ); |

Calculates the value of the probability density function of Cauchy distribution with the a and b parameters for an array of random variables x[]. In case of error it returns false. Analog of the [dcauchy()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Cauchy.html) in R.

|  |
| --- |
| bool  MathProbabilityDensityCauchy(     const double& x[],            // array with the values of random variable     const double  a,              // mean parameter of the distribution     const double  b,              // scale parameter of the distribution     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability density is calculated     double&       result[]        // array for values of the probability density function     ); |

Calculates the value of the probability density function of Cauchy distribution with the a and b parameters for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathProbabilityDensityCauchy(     const double& x[],            // array with the values of random variable     const double  a,              // mean parameter of the distribution     const double  b,              // scale parameter of the distribution     double&       result[]        // array for values of the probability density function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

a

[in]  mean parameter of the distribution.

b

[in]  scale parameter of the distribution.

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability density is returned.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability density function.
