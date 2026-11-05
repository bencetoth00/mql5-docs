# MathRandomF


Generates a pseudorandom variable distributed according to the law of Fisher's F-distribution with the nu1 and nu2 parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathRandomF(
   const double  nu1,            // the first parameter of distribution (number of degrees of freedom)
   const double  nu2,            // the second parameter of distribution (number of degrees of freedom)
   int&          error_code     // variable to store the error code
   );
```

Generates pseudorandom variables distributed according to the law of Fisher's F-distribution with the nu1 and nu2 parameters. In case of error it returns false. Analog of the [rf()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Fdist.html) in R.

```cpp
bool  MathRandomF(
   const double  nu1,            // the first parameter of distribution (number of degrees of freedom)
   const double  nu2,            // the second parameter of distribution (number of degrees of freedom)
   const int     data_count,     // amount of required data
   double&       result[]        // array with values of pseudorandom variables
   );
```

Parameters

nu1

[in]  The first parameter of distribution (number of degrees of freedom).

nu2

[in]  The second parameter of distribution (number of degrees of freedom).

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.