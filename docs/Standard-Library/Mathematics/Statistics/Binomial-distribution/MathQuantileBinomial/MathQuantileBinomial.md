# MathQuantileBinomial

MathQuantileBinomial

For the specified probability, the function calculates the inverse value of distribution function for binomial law with the n and p parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathQuantileBinomial(     const double  probability,    // probability value of random variable occurrence     const double  n,              // parameter of the distribution (number of tests)     const double  p,              // parameter of the distribution (probability of event occurrence in one test)     const bool    tail,           // flag of calculation, if false, then calculation is performed for 1.0-probability     const bool    log\_mode,       // flag of calculation, if log\_mode=true, calculation is performed for Exp(probability)     int&          error\_code      // variable to store the error code     ); |

For the specified probability, the function calculates the inverse value of distribution function for binomial law with the n and p parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathQuantileBinomial(     const double  probability,    // probability value of random variable occurrence     const double  n,              // parameter of the distribution (number of tests)     const double  p,              // parameter of the distribution (probability of event occurrence in one test)     int&          error\_code      // variable to store the error code     ); |

For the specified probability[] array of probability values, the function calculates the inverse value of distribution function for binomial law with the n and p parameters. In case of error it returns false. Analog of the [qbinom()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Binomial.html) in R.

|  |
| --- |
| double  MathQuantileBinomial(     const double& probability[],  // array with probability values of random variable     const double  n,              // parameter of the distribution (number of tests)     const double  p,              // parameter of the distribution (probability of event occurrence in one test)     const bool    tail,           // flag of calculation, if false, then calculation is performed for 1.0-probability     const bool    log\_mode,       // flag of calculation, if log\_mode=true, calculation is performed for Exp(probability)     double&       result[]        // array with values of quantiles     ); |

For the specified probability[] array of probability values, the function calculates the inverse value of distribution function for binomial law with the n and p parameters. In case of error it returns false.

|  |
| --- |
| bool  MathQuantileBinomial(     const double& probability[],  // array with probability values of random variable     const double  n,              // parameter of the distribution (number of tests)     const double  p,              // parameter of the distribution (probability of event occurrence in one test)     double&       result[]        // array with values of quantiles     ); |

Parameters

probability

[in]  Probability value of random variable.

probability[]

[in]  Array with probability values of random variable.

n

[in]  Parameter of the distribution (number of tests).

p

[in]  Parameter of the distribution (probability of event occurrence in one test).

tail

[in]  Flag of calculation, if false, then calculation is performed for 1.0-probability.

log\_mode

[in]  Flag of calculation, if log\_mode=true, calculation is performed for Exp(probability).

error\_code

[out]  Variable to get the error code.

result[]

[out]  Array with values of quantiles.
