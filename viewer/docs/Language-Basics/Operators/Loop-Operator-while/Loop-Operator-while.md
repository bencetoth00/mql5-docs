# Loop Operator while

# While Loop Operator

The while operator consists of a checked expression and the operator, which must be fulfilled:

```cpp
while(expression)
  operator;
```

If the expression is true, the operator is executed until the expression becomes false. If the expression is false, the control is passed to the next operator. The expression value is defined before the operator is executed. Therefore, if the expression is false from the very beginning, the operator will not be executed at all.

Note

If it is expected that a large number of iterations will be handled in a loop, it is advisable that you check the fact of forced program termination using the [IsStopped()](../../../Checkup/IsStopped/IsStopped.md) function.

Example:

```cpp
while(k<n && !IsStopped())
  {
   y=y*x;
   k++;
  }
```

See also

[Initialization of Variables](../../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)