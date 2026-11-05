# MathProbabilityDensityT

MathProbabilityDensityT

Calculates the value of the probability density function of Student's t-distribution with the nu parameter for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathProbabilityDensityT(     const double  x,             // value of random variable     const double  nu,            // parameter of distribution (number of degrees of freedom)     const bool    log\_mode,      // calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability density is calculated     int&          error\_code     // variable to store the error code     ); |

Calculates the value of the probability density function of Student's t-distribution with the nu parameter for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathProbabilityDensityT(     const double  x,             // value of random variable     const double  nu,            // parameter of distribution (number of degrees of freedom)     int&          error\_code     // variable to store the error code     ); |

Calculates the value of the probability density function of Student's t-distribution with the nu parameter for an array of random variables x[]. In case of error it returns false. Analog of the [dt()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/TDist.html) in R.

|  |
| --- |
| bool  MathProbabilityDensityT(     const double& x[],            // array with the values of random variable     const double  nu,             // parameter of distribution (number of degrees of freedom)     const bool    log\_mode,       // flag to calculate the logarithm of the value, if log\_mode=true, then the natural logarithm of the probability density is calculated     double&       result[]        // array for values of the probability density function     ); |

Calculates the value of the probability density function of Student's t-distribution with the nu parameter for an array of random variables x[]. In case of error it returns false.

|  |
| --- |
| bool  MathProbabilityDensityT(     const double& x[],            // array with the values of random variable     const double  nu,             // parameter of distribution (number of degrees of freedom)     double&       result[]        // array for values of the probability density function     ); |

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

nu

[in]  Parameter of distribution (number of degrees of freedom).

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability density is returned.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability density function.
