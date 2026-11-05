# References: Modifier & and Keyword this


## Passing Parameters by Reference

In MQL5 parameters of [simple](../Data-Types.md#base_types) types can be passed both by value and by reference, while parameters of [compound](../Data-Types.md#complex_types) types are always passed by reference. To inform the compiler that a parameter must be passed by reference, the ampersand character & is added before the parameter name.

Passing a parameter by reference means passing the address of the variable, that's why all changes in the parameter that is passed by reference will be immediately reflected in the source variable. Using parameter passing by reference, you can implement return of several results of a function at the same time. In order to prevent changing of a parameter passed by reference, use the [const](../../Variables/Variables.md#const) modifier.

Thus, if the input parameter of a function is an [array](../../Variables/Variables.md#array_define), a structure or class object, symbol '&' is placed in the function header after the variable type and before its name.

Example

```cpp
class CDemoClass
  {
private:
   double            m_array[];
public:
   void              setArray(double &array[]);
  };
//+------------------------------------------------------------------+
//| filling the array                                                |
//+------------------------------------------------------------------+
void  CDemoClass::setArray(double &array[])
  {
   if(ArraySize(array)>0)
     {
     ArrayResize(m_array,ArraySize(array));
     ArrayCopy(m_array, array);
     }
  }
```

In the above example [class](../Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#class) CDemoClass is declared, which contains the [private](../../Variables/Variables.md#private) member - array m\_array[] of [double](../Real-Types-(double,-float)/Real-Types-(double,-float).md) type. [Function](../../Functions/Functions.md) setArray() is declared, to which array[] is passed by reference. If the function header doesn't contain the indication about passing by reference, i.e. doesn't contain the ampersand character, an error message will be generated at the attempt to compile such a code.

Despite the fact that the array is passed by reference, we can't assign one array to another. We need to perform the element-wise copying of contents of the source array to the recipient array. The presence of & in the function description is the obligatory condition for arrays and structures when passed as the function parameter.

## Keyword this

A variable of class type (object) can be passed both by reference and by [pointer](../Object-Pointers/Object-Pointers.md). As well as reference, the pointer allows having access to an object. After the object pointer is declared, the [new](../../Operators/Object-Create-Operator-new/Object-Create-Operator-new.md) operator should be applied to it to create and initialize it.

The reserved word this is intended for obtaining the reference of the object to itself, which is available inside class or structure methods. this always references to the object, in the method of which it is used, and the expression [GetPointer](../../../Common-Functions/GetPointer/GetPointer.md)(this) gives the pointer of the object, whose member is the function, in which call of GetPointer() is performed. In MQL5 functions can't return objects, but they can return the object pointer.

Thus, if we need a function to return an object, we can return the pointer of this object in the form of GetPointer(this). Let's add function getDemoClass() that returns pointer of the object of this class, into the description of CDemoClass.

```cpp
class CDemoClass
  {
private:
   double            m_array[];
public:
   void              setArray(double &array[]);
   CDemoClass       *getDemoClass();
  };
//+------------------------------------------------------------------+
//| filling the array                                                |
//+------------------------------------------------------------------+
void  CDemoClass::setArray(double &array[])
  {
   if(ArraySize(array)>0)
     {
      ArrayResize(m_array,ArraySize(array));
      ArrayCopy(m_array,array);
     }
  }
//+------------------------------------------------------------------+
//| returns its own pointer                                          |
//+------------------------------------------------------------------+
CDemoClass *CDemoClass::getDemoClass(void)
  {
   return(GetPointer(this));
  }
```

Structures don't have pointers, operators new and delete can't be applied to them, GetPointer(this) can't be used.

See also

[Object Pointers](../Object-Pointers/Object-Pointers.md), [Creating and Deleting Objects](../../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md), [Visibility Scope and Lifetime of Variables](../../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md)