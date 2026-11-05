# Operators

Operators

Language operators describe some algorithmic operations that must be executed to accomplish a task. The program body is a sequence of such operators. Operators following one by one are separated by semicolons.

| Operator | Description |
| --- | --- |
| [Compound operator {}](Compound-Operator/Compound-Operator.md) | One or more operators of any type, enclosed in curly braces {} |
| [Expression operator (;)](Expression-Operator/Expression-Operator.md) | Any expression that ends with a semicolon (;) |
| [return](Return-Operator/Return-Operator.md) operator | Terminates the current function and returns control to the calling program |
| [if-else](Conditional-Operator-if-else/Conditional-Operator-if-else.md) conditional operator | Is used when it's necessary to make a choice |
| [?:](Ternary-Operator/Ternary-Operator.md) conditional operator | A simple analog of the if-else conditional operator |
| [switch](Switch-Operator/Switch-Operator.md) selection operator | Passes control to the operator, which corresponds to the expression value |
| [while](Loop-Operator-while/Loop-Operator-while.md) loop operator | Performs an operator until the expression checked becomes false. The expression is checked before each iteration |
| [for](Loop-Operator-for/Loop-Operator-for.md) loop operator | Performs an operator until the expression checked becomes false. The expression is checked before each iteration |
| [do-while](Loop-Operator-do-while/Loop-Operator-do-while.md) loop operator | Performs an operator until the expression checked becomes false. The end condition is checked, after each loop. The loop body is always executed at least once. |
| [break](Break-Operator/Break-Operator.md) operator | Terminates the execution of the nearest attached external operator switch, while, do-while or for |
| [continue](Continue-Operator/Continue-Operator.md) operator | Passes control to the beginning of the nearest external loop operator while, do-while or for |
| [@](Matrix-product-operator/Matrix-product-operator.md) operator | Implements matrix multiplication according to the rules of linear algebra. It allows multiplying [matrices and vectors](../../Matrix-and-Vector-Methods/Matrix-and-Vector-Methods.md), as well as performing scalar multiplication of vectors. |
| [new](Object-Create-Operator-new/Object-Create-Operator-new.md) operator | Creates an object of the appropriate size and returns a descriptor of the created object. |
| [delete](Object-Delete-Operator-delete/Object-Delete-Operator-delete.md) operator | Deletes the object created by the new operator |

One operator can occupy one or more lines. Two or more operators can be located in the same line. Operators that control over the execution order (if, if-else, switch, while and for), can be nested into each other.

Example:

|  |
| --- |
| if(Month() == 12)    if(Day() == 31) Print("Happy New Year!"); |

See also

[Initialization of Variables](../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
