# Return Operator


The return operator terminates the current [function](../../Functions/Functions.md) execution and returns control to the calling program. The expression calculation result is returned to the calling function. The expression can contain an assignment operator.

Example:

```cpp
int CalcSum(int x, int y)
  {
   return(x+y);
  }
```

In functions with the [void](../../Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) return type, the return operator without expression must be used:

```cpp
void SomeFunction()
  {
   Print("Hello!");
   return;    // this operator can be removed
  }
```

The right brace of the function means implicit execution of the return operator without expression.

What can be returned: [simple types](../../Data-Types/Data-Types.md#base_types), [simple structures](../../Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure), [object pointers](../../Data-Types/Object-Pointers/Object-Pointers.md). With  the return operator you can't return any arrays, class objects, variables of compound structure type.

See also

[Initialization of Variables](../../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)