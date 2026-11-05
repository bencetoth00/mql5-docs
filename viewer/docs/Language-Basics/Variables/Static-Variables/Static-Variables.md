# Static Variables


The storage class of static defines a static variable. The static modifier is indicated before the data type.

Example:

```cpp
int somefunc()
  {
   static int flag=10;
   ...
   return(flag);
  }
```

A static variable can be [initialized](../Initialization-of-Variables/Initialization-of-Variables.md) by a constant or constant expression corresponding to its type, unlike a simple local variable, which can be initialized by any expression.

Static variables exist from the moment of program execution and are initialized only once before the specialized functions [OnInit()](../../../Event-Handling/OnInit/OnInit.md) is called. If the initial values are not specified, variables of the static storage class are taking zero initial values.

[Local variables](../Local-Variables/Local-Variables.md) declared with the static keyword retain their values throughout the function [lifetime](../Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md). With each next function call, such local variables contain the values that they had during the previous call.

Any variables in a block, except [formal parameters](../Formal-Parameters/Formal-Parameters.md) of a function, can be defined as static. If a variable declared on a local level is not a static one, memory for such a variable is allocated automatically at a program stack.

Example:

```cpp
int Counter()
  {
   static int count;
   count++;
   if(count%100==0) Print("Function Counter has been called ",count," times");
   return count;
  }
void OnStart()
  {
//---
   int c=345;
   for(int i=0;i<1000;i++)
     {
      int c=Counter();
     }
   Print("c =",c);
  }
```

See also

[Data Types](../../Data-Types/Data-Types.md), [Encapsulation and Extensibility of Types](../../Object-Oriented-Programming/Encapsulation-and-Extensibility-of-Types/Encapsulation-and-Extensibility-of-Types.md), [Initialization of Variables](../Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md), [Static Class Members](../../Object-Oriented-Programming/Static-Members-of-a-Class/Static-Members-of-a-Class.md)