# CheckPointer

CheckPointer

The function returns the type of the object [pointer](../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md).

|  |
| --- |
| ENUM\_POINTER\_TYPE  CheckPointer(     object\* anyobject      // object pointer     ); |

Parameters

anyobject

[in]  Object pointer.

Return value

Returns a value from the [ENUM\_POINTER\_TYPE](../../Constants,-Enumerations-and-Structures/Named-Constants/Checking-Object-Pointer/Checking-Object-Pointer.md) enumeration.

Note

An attempt to call an incorrect pointer results in the [critical termination](../../MQL5-programs/Runtime-Errors/Runtime-Errors.md) of a program. That's why it's necessary to call the CheckPointer function before using a pointer. A pointer can be incorrect in the following cases:

- the pointer is equal to [NULL](../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md);
- the object has been deleted using the [delete](../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md) operator.

This function can be used for checking pointer validity. A non-zero value warranties that the pointer can be used for accessing.

To quickly validate the pointer, you can also use operator "!" ([example](../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md#lnot)) which checks it via an implicit call of the [CheckPointer](CheckPointer.md) function.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Deletes list by deleting its elements                            |  //+------------------------------------------------------------------+  void CMyList::Destroy()    {  //--- service pointer for working in the loop     CItem\* item;  //--- go through loop and try to delete dynamic pointers     while(CheckPointer(m\_items)!=POINTER\_INVALID)       {        item=m\_items;        m\_items=m\_items.Next();        if(CheckPointer(item)==POINTER\_DYNAMIC)          {           Print("Dynamic object ",item.Identifier()," to be deleted");           delete (item);          }        else Print("Non-dynamic object ",item.Identifier()," cannot be deleted");       }  //---    } |

See also

[Object Pointers](../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md), [Checking the Object Pointer](../../Constants,-Enumerations-and-Structures/Named-Constants/Checking-Object-Pointer/Checking-Object-Pointer.md), [Object Delete Operator delete](../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md)
