# MathCumulativeDistributionExponential

MathCumulativeDistributionExponential

Calculates the exponential distribution function of probabilities with the mu parameter for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionExponential(     const double  x,             // value of random variable     const double  mu,            // parameter of the distribution (expected value)     const bool    tail,          // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,      // calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is returned     int&          error\_code     // variable to store the error code     ); |

Calculates the exponential distribution function of probabilities with the mu parameter for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionExponential(     const double  x,             // value of random variable     const double  mu,            // parameter of the distribution (expected value)     int&          error\_code     // variable to store the error code     ); |

Calculates the exponential distribution function of probabilities with the mu parameter for an array of random variables x[]. In case of error it returns false. Analog of the [pexp()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Exponential.html) in R.

|  |
| --- |
| bool  MathCumulativeDistributionExponential(     const double& x[],            // array with the values of random variable     const double  mu,             // parameter of the distribution (expected value)     const bool    tail,           // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     double&       result[]        // array for values of the probability function     ); |

Calculates the exponential distribution function of probabilities with the mu parameter for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathCumulativeDistributionExponential(     const double& x[],            // array with the values of random variable     const double  mu,             // parameter of the distribution (expected value)     double&       result[]        // array for values of the probability function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

mu

[in]  Parameter of the distribution (expected value).

tail

[in]  Flag of calculation. If true, then the probability of random variable not exceeding x is calculated.

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability is calculated.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability function.
