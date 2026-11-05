# MathRandomPoisson


Generates a pseudorandom variable distributed according to the law of Poisson distribution with the lambda parameter. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathRandomPoisson(
   const double  lambda,         // parameter of the distribution (mean)
   int&          error_code      // variable to store the error code
   );
```

Generates pseudorandom variables distributed according to the law of Poisson distribution with the lambda parameter. In case of error it returns false. Analog of the [rgeom()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Geometric.html) in R.

```cpp
bool  MathRandomPoisson(
   const double  lambda,         // parameter of the distribution (mean)
   const int     data_count,     // amount of required data
   double&       result[]        // array with values of pseudorandom variables
   );
```

Parameters

lambda

[in]  Parameter of the distribution (mean).  

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.