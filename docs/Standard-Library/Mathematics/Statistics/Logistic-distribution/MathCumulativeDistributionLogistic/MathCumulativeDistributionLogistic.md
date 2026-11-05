# MathCumulativeDistributionLogistic

MathCumulativeDistributionLogistic

Calculates the logistic distribution function of probabilities with the mu and sigma parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionLogistic(     const double  x,             // value of random variable     const double  mu,            // mean parameter of the distribution     const double  sigma,         // scale parameter of the distribution     const bool    tail,          // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,      // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     int&          error\_code     // variable to store the error code     ); |

Calculates the logistic distribution function of probabilities with the mu and sigma parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionLogistic(     const double  x,             // value of random variable     const double  mu,            // mean parameter of the distribution     const double  sigma,         // scale parameter of the distribution     int&          error\_code     // variable to store the error code     ); |

Calculates the logistic distribution function of probabilities with the mu and sigma parameters for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathCumulativeDistributionLogistic(     const double& x[],            // array with the values of random variable     const double  mu,             // mean parameter of the distribution     const double  sigma,          // scale parameter of the distribution     const bool    tail,           // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     double&       result[]        // array for values of the probability function     ); |

Calculates the logistic distribution function of probabilities with the mu and sigma parameters for an array of random variables x[]. In case of error it returns false. Analog of the [plogis()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Logistic.html) in R.

|  |
| --- |
| bool  MathCumulativeDistributionLogistic(     const double& x[],            // array with the values of random variable     const double  mu,             // mean parameter of the distribution     const double  sigma,          // scale parameter of the distribution     double&       result[]        // array for values of the probability function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

mu

[in]  mean parameter of the distribution.

sigma

[in]  scale parameter of the distribution.

tail

[in]  Flag of calculation. If true, then the probability of random variable not exceeding x is calculated.

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability is calculated.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability function.
