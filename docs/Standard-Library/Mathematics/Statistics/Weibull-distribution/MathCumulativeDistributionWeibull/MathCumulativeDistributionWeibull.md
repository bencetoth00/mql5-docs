# MathCumulativeDistributionWeibull

MathCumulativeDistributionWeibull

Calculates the value of the Weibull distribution function with the a and b parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionWeibull(     const double  x,             // value of random variable     const double  a,             // parameter of the distribution (shape)     const double  b,             // parameter of the distribution (scale)     const bool    tail,          // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,      // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     int&          error\_code     // variable to store the error code     ); |

Calculates the value of the Weibull distribution function with the a and b parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionWeibull(     const double  x,             // value of random variable     const double  a,             // parameter of the distribution (shape)     const double  b,             // parameter of the distribution (scale)     int&          error\_code     // variable to store the error code     ); |

Calculates the value of the Weibull distribution function with the a and b parameters for an array of random variables x[]. In case of error it returns false. Analog of the [pweibull()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Weibull.html) in R.

|  |
| --- |
| bool  MathCumulativeDistributionWeibull(     const double& x[],            // array with the values of random variable     const double  a,              // parameter of the distribution (shape)     const double  b,              // parameter of the distribution (scale)     const bool    tail,           // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     double&       result[]        // array for values of the probability function     ); |

Calculates the value of the Weibull distribution function with the a and b parameters for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathCumulativeDistributionWeibull(     const double& x[],            // array with the values of random variable     const double  a,              // parameter of the distribution (shape)     const double  b,              // parameter of the distribution (scale)     double&       result[]        // array for values of the probability function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

a

[in]  Parameter of the distribution (scale).

b

[in]  Parameter of the distribution (shape).

tail

[in]  Flag of calculation. If true, then the probability of random variable not exceeding x is calculated.

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability is calculated.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability function.
