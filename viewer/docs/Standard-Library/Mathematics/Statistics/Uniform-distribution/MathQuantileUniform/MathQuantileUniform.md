# MathQuantileUniform


For the specified probability, the function calculates the value of inverse uniform distribution function with the a and b parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathQuantileUniform(
   const double  probability,    // probability value of random variable occurrence
   const double  a,              // distribution parameter a (lower bound)
   const double  b,              // distribution parameter b (upper bound)
   const bool    tail,           // flag of calculation, if false, then calculation is performed for 1.0-probability
   const bool    log_mode,       // flag of calculation, if log_mode=true, calculation is performed for Exp(probability)
   int&          error_code      // variable to store the error code
   );
```

For the specified probability, the function calculates the value of inverse uniform distribution function with the a and b parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathQuantileUniform(
   const double  probability,    // probability value of random variable occurrence
   const double  a,              // distribution parameter a (lower bound)
   const double  b,              // distribution parameter b (upper bound)
   int&          error_code      // variable to store the error code
   );
```

For the specified probability[] array of probability values, the function calculates the value of inverse uniform distribution function with the a and b parameters. In case of error it returns false. Analog of the [qcauschy()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Cauchy.html) in R.

```cpp
double  MathQuantileUniform(
   const double& probability[],  // array with probability values of random variable
   const double  a,              // distribution parameter a (lower bound)
   const double  b,              // distribution parameter b (upper bound)
   const bool    tail,           // flag of calculation, if false, then calculation is performed for 1.0-probability
   const bool    log_mode,       // flag of calculation, if log_mode=true, calculation is performed for Exp(probability)
   double&       result[]        // array with values of quantiles
   );
```

For the specified probability[] array of probability values, the function calculates the value of inverse uniform distribution function with the a and b parameters. In case of error it returns false.

```cpp
bool  MathQuantileUniform(
   const double& probability[],  // array with probability values of random variable
   const double  a,              // distribution parameter a (lower bound)
   const double  b,              // distribution parameter b (upper bound)
   double&       result[]        // array with values of quantiles
   );
```

Parameters

probability

[in]  Probability value of random variable.

probability[]

[in]  Array with probability values of random variable.

a

[in]  Distribution parameter a (lower bound).

b

[in]  Distribution parameter b (upper bound).

tail

[in]  Flag of calculation, if false, then calculation is performed for 1.0-probability.

log\_mode

[in]  Flag of calculation, if log\_mode=true, calculation is performed for Exp(probability).

error\_code

[out]  Variable to get the error code.

result[]

[out]  Array with values of quantiles.