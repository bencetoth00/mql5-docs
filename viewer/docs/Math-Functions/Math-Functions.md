# Math Functions

# Mathematical Functions

A set of mathematical and trigonometric functions.

Math functions were originally designed to perform relevant operations on scalar values. From this build on, most of the functions can be applied to [matrices and vectors](../Language-Basics/Data-Types/Matrices-and-vectors/Matrices-and-vectors.md). These include MathAbs, MathArccos, MathArcsin, MathArctan, MathCeil, MathCos, MathExp, MathFloor, MathLog, MathLog10, MathMod, MathPow, MathRound, MathSin, MathSqrt, MathTan, MathExpm1, MathLog1p, MathArccosh, MathArcsinh, MathArctanh, MathCosh, MathSinh, and MathTanh. Such operations imply element-wise handling of matrices or vectors. Example:

```cpp
//---
  matrix a= {{1, 4}, {9, 16}};
  Print("matrix a=\n",a);
  a=MathSqrt(a);
  Print("MatrSqrt(a)=\n",a);
  /*
   matrix a=
   [[1,4]
    [9,16]]
   MatrSqrt(a)=
   [[1,2]
    [3,4]]
  */
```

For [MathMod](MathMod/MathMod.md) and [MathPow](MathPow/MathPow.md), the second element can be either a scalar or a matrix/vector of the appropriate size.

| Function | Action |
| --- | --- |
| [MathAbs](MathAbs/MathAbs.md) | Returns absolute value (modulus) of the specified numeric value |
| [MathArccos](MathArccos/MathArccos.md) | Returns the arc cosine of x in radians |
| [MathArcsin](MathArcsin/MathArcsin.md) | Returns the arc sine of x in radians |
| [MathArctan](MathArctan/MathArctan.md) | Returns the arc tangent of x in radians |
| [MathArctan2](MathArctan2/MathArctan2.md) | Return the angle (in radians) whose tangent is the quotient of two specified numbers |
| [MathClassify](MathClassify/MathClassify.md) | Returns the type of a real number |
| [MathCeil](MathCeil/MathCeil.md) | Returns integer numeric value closest from above |
| [MathCos](MathCos/MathCos.md) | Returns the cosine of a number |
| [MathExp](MathExp/MathExp.md) | Returns exponent of a number |
| [MathFloor](MathFloor/MathFloor.md) | Returns integer numeric value closest from below |
| [MathLog](MathLog/MathLog.md) | Returns natural logarithm |
| [MathLog10](MathLog10/MathLog10.md) | Returns the logarithm of a number by base 10 |
| [MathMax](MathMax/MathMax.md) | Returns the maximal value of the two numeric values |
| [MathMin](MathMin/MathMin.md) | Returns the minimal value of the two numeric values |
| [MathMod](MathMod/MathMod.md) | Returns the real remainder after the division of two numbers |
| [MathPow](MathPow/MathPow.md) | Raises the base to the specified power |
| [MathRand](MathRand/MathRand.md) | Returns a pseudorandom value within the range of 0 to 32767 |
| [MathRound](MathRound/MathRound.md) | Rounds of a value to the nearest integer |
| [MathSin](MathSin/MathSin.md) | Returns the sine of a number |
| [MathSqrt](MathSqrt/MathSqrt.md) | Returns a square root |
| [MathSrand](MathSrand/MathSrand.md) | Sets the starting point for generating a series of pseudorandom integers |
| [MathTan](MathTan/MathTan.md) | Returns the tangent of a number |
| [MathIsValidNumber](MathIsValidNumber/MathIsValidNumber.md) | Checks the correctness of a real number |
| [MathExpm1](MathExpm1/MathExpm1.md) | Returns the value of the expression MathExp(x)-1 |
| [MathLog1p](MathLog1p/MathLog1p.md) | Returns the value of the expression MathLog(1+x) |
| [MathArccosh](MathArccosh/MathArccosh.md) | Returns the hyperbolic arccosine |
| [MathArcsinh](MathArcsinh/MathArcsinh.md) | Returns the hyperbolic arcsine |
| [MathArctanh](MathArctanh/MathArctanh.md) | Returns the hyperbolic arctangent |
| [MathCosh](MathCosh/MathCosh.md) | Returns the hyperbolic cosine |
| [MathSinh](MathSinh/MathSinh.md) | Returns the hyperbolic sine |
| [MathTanh](MathTanh/MathTanh.md) | Returns the hyperbolic tangent |
| [MathSwap](MathSwap/MathSwap.md) | Change the order of bytes in the [ushort](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md)/uint/ushort types value |