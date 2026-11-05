# MathQuantileNoncentralT

MathQuantileNoncentralT

For the specified probability, the function calculates the value of inverse noncentral Student's t-distribution function with the nu and delta parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathQuantileNoncentralT(     const double  probability,    // probability value of random variable occurrence     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     const bool    tail,           // flag of calculation, if lower\_tail=false, then calculation is performed for 1.0-probability     const bool    log\_mode,       // flag of calculation, if log\_mode=true, calculation is performed for Exp(probability)     int&          error\_code      // variable to store the error code     ); |

For the specified probability, the function calculates the value of inverse noncentral Student's t-distribution function with the nu and delta parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

|  |
| --- |
| double  MathQuantileNoncentralT(     const double  probability,    // probability value of random variable occurrence     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     int&          error\_code      // variable to store the error code     ); |

For the specified probability[] array of probability values, the function calculates the value of inverse noncentral Student's t-distribution function with the nu and delta parameters. In case of error it returns false. Analog of the [qt()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/TDist.html) in R.

|  |
| --- |
| double  MathQuantileNoncentralT(     const double& probability[],  // array with probability values of random variable     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     const bool    tail,           // flag of calculation, if lower\_tail=false, then calculation is performed for 1.0-probability     const bool    log\_mode,       // flag of calculation, if log\_mode=true, calculation is performed for Exp(probability)     double&       result[]        // array with values of quantiles     ); |

For the specified probability[] array of probability values, the function calculates the value of inverse noncentral Student's t-distribution function with the nu and delta parameters. In case of error it returns false.

|  |
| --- |
| bool  MathQuantileNoncentralT(     const double& probability[],  // array with probability values of random variable     const double  nu,             // parameter of distribution (number of degrees of freedom)     const double  delta,          // noncentrality parameter     double&       result[]        // array with values of quantiles     ); |

Parameters

probability

[in]  Probability value of random variable.

probability[]

[in]  Array with probability values of random variable.

nu

[in]  Parameter of distribution (number of degrees of freedom).

delta

[in]  Noncentrality parameter.

tail

[in]  Flag of calculation, if false, then calculation is performed for 1.0-probability.

log\_mode

[in]  Flag of calculation, if log\_mode=true, calculation is performed for Exp(probability).

error\_code

[out]  Variable to get the error code.

result[]

[out]  Array with values of quantiles.
