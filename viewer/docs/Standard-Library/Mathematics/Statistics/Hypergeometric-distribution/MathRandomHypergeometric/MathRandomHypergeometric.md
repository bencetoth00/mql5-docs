# MathRandomHypergeometric


Generates a pseudorandom variable distributed according to the law of hypergeometric distribution with the m, n and k parameters. In case of error it returns [NaN](../../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

```cpp
double  MathRandomHypergeometric(
   const double  m,              // total number of objects (integer)
   const double  k,              // number of objects with the desired characteristic (integer)
   const double  n,              // number of object draws (integer)
   int&          error_code      // variable to store the error code
   );
```

Generates pseudorandom variables distributed according to the law of hypergeometric distribution with the m, n and k parameters. In case of error it returns false. Analog of the [rgeom()](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/Geometric.html) in R.

```cpp
bool  MathRandomHypergeometric(
   const double  m,              // total number of objects (integer)
   const double  k,              // number of objects with the desired characteristic (integer)
   const double  n,              // number of object draws (integer)
   const int     data_count,     // amount of required data
   double&       result[]        // array with values of pseudorandom variables
   );
```

Parameters

m

[in]  Total number of objects (integer).

k

[in]  Number of objects with the desired characteristic (integer).

n

[in]  Number of object draws (integer).

error\_code

[out]  Variable to store the error code.

data\_count

[out]  Amount of required data.

result[]

[out]  Array to obtain the values of pseudorandom variables.