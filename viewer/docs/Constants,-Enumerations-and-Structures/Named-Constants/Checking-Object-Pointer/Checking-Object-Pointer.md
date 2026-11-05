# Checking Object Pointer


The [CheckPointer()](../../../Common-Functions/CheckPointer/CheckPointer.md) function is used for checking the type of the [object pointer](../../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md). The function returns a value of the ENUM\_POINTER\_TYPE enumeration. If an incorrect pointer is used, the program execution will be immediately terminated.

Objects created by the [new()](../../../Language-Basics/Operators/Object-Create-Operator-new/Object-Create-Operator-new.md) operator are of POINTER\_DYNAMIC type. The [delete() operator](../../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md) can and should be used only for such pointers.

All other pointers are of POINTER\_AUTOMATIC type, which means that this object has been created automatically by the mql5 program environment. Such objects are deleted automatically after being used.

ENUM\_POINTER\_TYPE

| Constant | Description |
| --- | --- |
| POINTER\_INVALID | Incorrect pointer |
| POINTER\_DYNAMIC | Pointer of the object created by the [new()](../../../Language-Basics/Operators/Object-Create-Operator-new/Object-Create-Operator-new.md) operator |
| POINTER\_AUTOMATIC | Pointer of any objects created automatically (not using new()) |

See also

[Runtime errors](../../../MQL5-programs/Runtime-Errors/Runtime-Errors.md), [Object Delete Operator delete](../../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md), [CheckPointer](../../../Common-Functions/CheckPointer/CheckPointer.md)
