# _RandomSeed

\_RandomSeed

Variable for storing the current state when generating pseudo-random integers. \_RandomSeed changes its value when calling [MathRand()](../../Math-Functions/MathRand/MathRand.md). Use [MathSrand()](../../Math-Functions/MathSrand/MathSrand.md) to set the required initial condition.

x random number received by MathRand() function is calculated in the following way at each call:

|  |
| --- |
| x=\_RandomSeed\*214013+2531011;  \_RandomSeed=x;  x=(x>>16)&0x7FFF; |

See also

[MathRand()](../../Math-Functions/MathRand/MathRand.md), [MathSrand()](../../Math-Functions/MathSrand/MathSrand.md), [Integer types](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md)
