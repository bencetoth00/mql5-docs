# Continue Operator


The continue operator passes control to the beginning of the nearest outward loop [while](../Loop-Operator-while/Loop-Operator-while.md), [do-while](../Loop-Operator-do-while/Loop-Operator-do-while.md) or [for](../Loop-Operator-for/Loop-Operator-for.md) operator, the next iteration being called. The purpose of this operator is opposite to that of [break](../Break-Operator/Break-Operator.md) operator.

Example:

```cpp
//--- Sum of all nonzero elements
int func(int array[])
  {
   int array_size=ArraySize(array);
   int sum=0;
   for(int i=0;i<array_size; i++)
     {
      if(a[i]==0) continue;
      sum+=a[i];
     }
   return(sum);
  }
```

See also

[Initialization of Variables](../../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)