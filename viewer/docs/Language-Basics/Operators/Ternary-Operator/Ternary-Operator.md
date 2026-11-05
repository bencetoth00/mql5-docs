# Ternary Operator ?:


The general form of the ternary operator is as follows:

```cpp
expression1 ? expression2 : expression3
```

For the first operand - "expression1" - any expression that results in a [bool](../../Data-Types/Integer-Types/Bool-Type/Bool-Type.md) type value can be used. If the result is true, then the operator set by the second operand, i.e. "expression2" is executed.

If the first operand is false, the third operand - "expression3" is performed. The second and third operands, i.e. "expression2" and "expression3" should return values of one type and should not be of [void](../../Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) type. The result of the conditional operator execution is the result of expression2 or result of the expression3, depending on the result of expression1.

```cpp
//--- normalize difference between open and close prices for a day range
double true_range = (High==Low)?0:(Close-Open)/(High-Low);
```

This entry is equivalent to the following:

```cpp
   double true_range;
   if(High==Low)true_range=0;               // if High and Low are equal
   else true_range=(Close-Open)/(High-Low); // if the range is not null
```

 

## Operator Use Restrictions

Based on the value of "expression1", the operator must return one of the two values - either "expression2" or "expression3". There are several limitations to these expressions:

1. Do not mix [user-defined type](../../Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md) with [simple type](../../Data-Types/Data-Types.md#base_types) or [enumeration](../../Data-Types/Integer-Types/Enumerations/Enumerations.md). [NULL](../../Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) can be used for the [pointer](../../Data-Types/Object-Pointers/Object-Pointers.md).
2. If types of values are simple, the operator will be of the maximum type (see [Type casting](../../Data-Types/Typecasting/Typecasting.md)).
3. If one of the values is an enumeration and the second one is of a numeric type, the enumeration is replaced by int and the second rule is applied.
4. If both values are enumerations, their types must be identical, and the operator will be of type enumeration.

Restrictions for the user-defined types (classes or structures):

1. Types must be identical or one should be [derived](../../Object-Oriented-Programming/Inheritance/Inheritance.md) from the other one.
2. If types are not identical (inheritance), then the child is implicitly cast to the parent, i.e. the operator will be of the parent type.
3. Do not mix object and the pointer – both expressions must be either objects or [pointers](../../Data-Types/Object-Pointers/Object-Pointers.md). [NULL](../../Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) can be used for the pointer.

Note

Be careful when using the conditional operator as an argument of an [overloaded function](../../Functions/Function-Overloading/Function-Overloading.md), because the type of the result of a conditional operator is defined at the time of program compilation. And this type is [determined](../../Data-Types/Typecasting/Typecasting.md) as the larger of the types "expression2" and "expression3".

Example:

```cpp
void func(double d) { Print("double argument: ",d); }
void func(string s) { Print("string argument: ",s); }
bool   Expression1=true;
double Expression2=M_PI;
string Expression3="3.1415926";
void OnStart()
  {
   func(Expression2);
   func(Expression3);
   func(Expression1?Expression2:Expression3);   // warning on implicit casting to string
   func(!Expression1?Expression2:Expression3);  // warning on implicit casting to string
  }
//   Result:
//   double argument: 3.141592653589793
//   string argument: 3.1415926
//   string argument: 3.141592653589793
//   string argument: 3.1415926
```

See also

[Initialization of Variables](../../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)