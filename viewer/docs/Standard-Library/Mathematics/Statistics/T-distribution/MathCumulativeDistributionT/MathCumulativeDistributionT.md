# MathCumulativeDistributionT


Calculates the value of the Student's t-distribution function with the nu parameter for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathCumulativeDistributionT(
   const double  x,             // value of random variable
   const double  nu,            // parameter of distribution (number of degrees of freedom)
   const bool    tail,          // flag of calculation, if true, then the probability of random variable not exceeding x is calculated
   const bool    log_mode,      // flag to calculate the logarithm of the value, if log_mode=true, then the natural logarithm of the probability is calculated
   int&          error_code     // variable to store the error code
   );
```

Calculates the value of the Student's t-distribution function with the nu parameter for a random variable x. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathCumulativeDistributionT(
   const double  x,             // value of random variable
   const double  nu,            // parameter of distribution (number of degrees of freedom)
   int&          error_code     // variable to store the error code
   );
```

Calculates the value of the Student's t-distribution function with the nu parameter for an array of random variables x[]. In case of error it returns false. Analog of the [pt()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/TDist.html) in R.

```cpp
bool  MathCumulativeDistributionT(
   const double& x[],            // array with the values of random variable
   const double  nu,             // parameter of distribution (number of degrees of freedom)
   const bool    tail,           // flag of calculation, if true, then the probability of random variable not exceeding x is calculated
   const bool    log_mode,       // flag to calculate the logarithm of the value, if log_mode=true, then the natural logarithm of the probability is calculated
   double&       result[]        // array for values of the probability function
   );
```

Calculates the value of the Student's t-distribution function with the nu parameter for an array of random variables x[]. In case of error it returns false.

```cpp
bool  MathCumulativeDistributionT(
   const double& x[],            // array with the values of random variable
   const double  nu,             // parameter of distribution (number of degrees of freedom)
   double&       result[]        // array for values of the probability function
   );
```

Parameters

x

[in]  Value of random variable.

x[]

[in]  Array with the values of random variable.

nu

[in]  Parameter of distribution (number of degrees of freedom).

tail

[in]  Flag of calculation. If true, then the probability of random variable not exceeding x is calculated.

log\_mode

[in]  Flag to calculate the logarithm of the value. If log\_mode=true, then the natural logarithm of the probability is calculated.

error\_code

[out]  Variable to store the error code.

result[]

[out]  Array for values of the probability function.