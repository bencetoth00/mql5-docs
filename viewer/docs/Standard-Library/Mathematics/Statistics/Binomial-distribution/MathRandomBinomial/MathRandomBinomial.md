# MathRandomBinomial


Generates a pseudorandom variable distributed according to the law of binomial distribution with the n and p parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathRandomBinomial(
   const double  n,              // parameter of the distribution (number of tests)
   const double  p,              // parameter of the distribution (probability of event occurrence in one test)
   int&          error_code      // variable to store the error code
   );
```

Generates pseudorandom variables distributed according to the law of binomial distribution with the n and p parameters. In case of error it returns false. Analog of the [rweibull()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Weibull.html) in R.

```cpp
bool  MathRandomBinomial(
   const double  n,              // parameter of the distribution (number of tests)
   const double  p,              // parameter of the distribution (probability of event occurrence in one test)
   const int     data_count,     // amount of required data
   double&       result[]        // array with values of pseudorandom variables
   );
```

Parameters

n

[in]  Parameter of the distribution (number of tests).

p

[in]  Parameter of the distribution (probability of event occurrence in one test).

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.