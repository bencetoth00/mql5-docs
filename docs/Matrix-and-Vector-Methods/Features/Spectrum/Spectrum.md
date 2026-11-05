# Spectrum

Spectrum

Compute spectrum of a matrix as the set of its eigenvalues from the product AT\*A.

|  |
| --- |
| vector matrix::Spectrum() |

Return Value

Spectrum of a matrix as a vector of matrix eigenvalues.

 

Example

|  |
| --- |
| double MatrixCondSpectral(matrix& a)    {     double norm=0.0;     vector v=a.Spectrum();        if(v.Size()>0)       {        double max\_norm=v[0];        double min\_norm=v[0];        for(ulong i=1; i<v.Size(); i++)          {           double real=MathAbs(v[i]);           if(max\_norm<real)              max\_norm=real;           if(min\_norm>real)              min\_norm=real;          }        max\_norm=MathSqrt(max\_norm);        min\_norm=MathSqrt(min\_norm);        if(min\_norm>0.0)           norm=max\_norm/min\_norm;       }        return(norm);    } |
