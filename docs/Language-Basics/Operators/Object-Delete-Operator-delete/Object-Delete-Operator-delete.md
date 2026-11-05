# Object Delete Operator delete

Object Delete Operator delete

The delete operator deletes an object created by the [new](../Object-Create-Operator-new/Object-Create-Operator-new.md) operator, calls the corresponding class destructor and frees up memory occupied by the object. A real descriptor of an existing object is used as an operand. After the delete operation is executed, the [object descriptor](../../Data-Types/Object-Pointers/Object-Pointers.md) becomes invalid.

Example:

|  |
| --- |
| //--- delete figure        delete m\_shape;        m\_shape=NULL;        //--- create a new figure        NewShape(); |

See also

[Initialization of Variables](../../Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
