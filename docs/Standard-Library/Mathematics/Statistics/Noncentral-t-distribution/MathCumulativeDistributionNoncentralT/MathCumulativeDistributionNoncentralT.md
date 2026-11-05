# MathCumulativeDistributionNoncentralT

MathCumulativeDistributionNoncentralT

Calculates the probability distribution function of noncentral Student's t-distribution with the nu and delta parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionNoncentralT(     const double  x,             // value of random variable     const double  nu,            // parameter of distribution (number of degrees of freedom)     const double  delta,         // noncentrality parameter     const bool    tail,          // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,      // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     int&          error\_code     // variable to store the error code     ); |

Calculates the probability distribution function of noncentral Student's t-distribution with the nu and delta parameters for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathCumulativeDistributionNoncentralT(     const double  x,             // value of random variable     const double  nu,            // parameter of distribution (number of degrees of freedom)     const double  delta,         // noncentrality parameter     int&          error\_code     // variable to store the error code     ); |

Calculates the probability distribution function of noncentral Student's t-distribution with the nu and delta parameters for an array of random variables x[]. In case of error it returns false. Analog of the [pt()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/TDist.html) in R.

|  |
| --- |
| bool  MathCumulativeDistributionNoncentralT(     const double& x[],            // array with the values of random variable     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     const bool    tail,           // flag of calculation, if true, then the probability of random variable not exceeding x is calculated     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability is calculated     double&       result[]        // array for values of the probability function     ); |

Calculates the probability distribution function of noncentral Student's t-distribution with the nu and delta parameters for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathCumulativeDistributionNoncentralT(     const double& x[],            // array with the values of random variable     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     double&       result[]        // array for values of the probability function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

nu

[in]  Parameter of distribution (number of degrees of freedom).

delta

[in]  Noncentrality parameter.

tail

[in]  Flag of calculation. If true, then the probability of random variable not exceeding x is calculated.

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability is calculated.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability function.
