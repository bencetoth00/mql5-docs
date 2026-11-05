# HasNan


Return the number of [NaN](../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) values in a matrix/vector.

```cpp
ulong vector::HasNan();
ulong matrix::HasNan();
```

Return Value

The number of matrix/vector elements that contain a NaN value.

 

Note

When comparing the appropriate pair of elements having NaN values, the [Compare](../Compare/Compare.md) and [CompareByDigits](../CompareByDigits/CompareByDigits.md) methods consider these elements equal, while in case of a usual comparison of floating-point numbers NaN != NaN.

 

Example:

```cpp
void OnStart(void)
  {
   double x=sqrt(-1);
   Print("single: ",x==x);
   vector<double> v1={x};
   vector<double> v2={x};
   Print("vector: ", v1.Compare(v2,0)==0);
  }
/* Result:
 single: false
 vector: true
*/
```

 

See also

[MathClassify](../../../Math-Functions/MathClassify/MathClassify.md), [Compare](../Compare/Compare.md), [CompareByDigits](../CompareByDigits/CompareByDigits.md)