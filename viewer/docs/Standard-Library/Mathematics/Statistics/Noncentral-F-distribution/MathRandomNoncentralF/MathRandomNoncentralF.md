# MathRandomNoncentralF


Generates a pseudorandom variable distributed according to the law of noncentral Fisher's F-distribution with the nu1, nu2 and sigma parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathRandomNoncentralF(
   const double  nu1,            // the first parameter of distribution (number of degrees of freedom)
   const double  nu2,            // the second parameter of distribution (number of degrees of freedom)
   const double  sigma,          // noncentrality parameter
   int&          error_code      // variable to store the error code
   );
```

Generates pseudorandom variables distributed according to the law of noncentral Fisher's F-distribution with the nu1, nu2 and sigma parameters. In case of error it returns false. Analog of the [rf()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Fdist.html) in R.

```cpp
bool  MathRandomNoncentralF(
   const double  nu1,            // the first parameter of distribution (number of degrees of freedom)
   const double  nu2,            // the second parameter of distribution (number of degrees of freedom)
   const double  sigma,          // noncentrality parameter
   const int     data_count,     // amount of required data
   double&       result[]        // array with values of pseudorandom variables
   );
```

Parameters

nu1

[in]  The first parameter of distribution (number of degrees of freedom).

nu2

[in]  The second parameter of distribution (number of degrees of freedom).

sigma

[in]  Noncentrality parameter.

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.