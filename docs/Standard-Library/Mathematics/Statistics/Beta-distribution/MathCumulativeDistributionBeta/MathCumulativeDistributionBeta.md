# MathCumulativeDistributionBeta

MathCumulativeDistributionBeta

Calculates the probability distribution function of beta distribution with the a and b parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionBeta(     const double  x,             // value of random variable     const double  a,             // the first parameter of beta distribution (shape1)     const double  b,             // the second parameter of beta distribution (shape2)     const bool    tail,          // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,      // calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is returned     int&          error\_code     // variable to store the error code     ); |

Calculates the probability distribution function of beta distribution with the a and b parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionBeta(     const double  x,             // value of random variable     const double  a,             // the first parameter of beta distribution (shape1)     const double  b,             // the second parameter of beta distribution (shape2)     int&          error\_code     // variable to store the error code     ); |

Calculates the probability distribution function of beta distribution with the a and b parameters for an array of random variables x[]. In case of error it returns false. Analog of the [pbeta()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Beta.html) in R.

|  |
| --- |
| bool  MathCumulativeDistributionBeta(     const double& x[],            // array with the values of random variable     const double  a,              // the first parameter of beta distribution (shape1)     const double  b,              // the second parameter of beta distribution (shape2)     const bool    tail,           // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     double&       result[]        // array for values of the probability function     ); |

<t0>Calculates the probability distribution function of beta distribution with the a and b parameters for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathCumulativeDistributionBeta(     const double& x[],            // array with the values of random variable     const double  a,              // the first parameter of beta distribution (shape1)     const double  b,              // the second parameter of beta distribution (shape2)     double&       result[]        // array for values of the probability function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

a

[in]  The first parameter of beta distribution (shape 1).

b

[in]  The second parameter of beta distribution (shape 2)

tail

[in]  Flag of calculation, if true, then the probability of random variable not exceeding x is calculated.  

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability is calculated.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability function.
