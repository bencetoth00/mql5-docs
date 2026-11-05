# GetPointer

GetPointer

The function returns the object [pointer](../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md).

|  |
| --- |
| void\*  GetPointer(     any\_class anyobject      // object of any class     ); |

Parameters

anyobject

[in]  Object of any class.

Return Value

The function returns the object pointer.

Note

Only class objects have pointers. Instances of [structures](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md) and simple-type variables can't have pointers. The class object not created using the new() operator, but, e.g., automatically created in the array of objects, still has a pointer. But this pointer will be of the automatic type POINTER\_AUTOMATIC, therefore the [delete()](../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md) operator can't be applied to it. Aside from that, the type pointer doesn't differ from dynamic pointers of the [POINTER\_DYNAMIC](../../Constants,-Enumerations-and-Structures/Named-Constants/Checking-Object-Pointer/Checking-Object-Pointer.md) type.

Since variables of structure types and simple types do not have pointers, it's prohibited to apply the GetPointer() function to them. It's also prohibited to pass the pointer as a function argument. In all these cases the compiler will notify an error.

An attempt to call an incorrect pointer causes the [critical termination](../../MQL5-programs/Runtime-Errors/Runtime-Errors.md) of a program. That's why the [CheckPointer()](../CheckPointer/CheckPointer.md) function should be called prior to using a pointer. A pointer can be incorrect in the following cases:

- the pointer is equal to [NULL](../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md);
- the object has been deleted using the [delete](../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md) operator.

This function can be used to check the validity of a pointer. A non-zero value guarantees, that the pointer can be used for accessing.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                             Check\_GetPointer.mq5 |  //|                        Copyright 2009, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "2009, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"     //+------------------------------------------------------------------+  //| Class implementing the list element                              |  //+------------------------------------------------------------------+  class CItem    {     int               m\_id;     string            m\_comment;     CItem\*            m\_next;  public:                       CItem() { m\_id=0; m\_comment=NULL; m\_next=NULL; }                      ~CItem() { Print("Destructor of ",m\_id,                                       (CheckPointer(GetPointer(this))==POINTER\_DYNAMIC)?                                       "dynamic":"non-dynamic"); }     void              Initialize(int id,string comm) { m\_id=id; m\_comment=comm; }     void              PrintMe() { Print(\_\_FUNCTION\_\_,":",m\_id,m\_comment); }     int               Identifier() { return(m\_id); }     CItem\*            Next() {return(m\_next); }     void              Next(CItem \*item) { m\_next=item; }    };  //+------------------------------------------------------------------+  //| Simplest class of the list                                       |  //+------------------------------------------------------------------+  class CMyList    {     CItem\*            m\_items;  public:                       CMyList() { m\_items=NULL; }                      ~CMyList() { Destroy(); }      bool             InsertToBegin(CItem\* item);      void             Destroy();    };  //+------------------------------------------------------------------+  //| Inserts list element at the beginning                            |  //+------------------------------------------------------------------+  bool CMyList::InsertToBegin(CItem\* item)    {     if(CheckPointer(item)==POINTER\_INVALID) return(false);  //---     item.Next(m\_items);     m\_items=item;  //---     return(true);    }  //+------------------------------------------------------------------+  //| Deleting the list by deleting elements                           |  //+------------------------------------------------------------------+  void CMyList::Destroy()    {  //--- service pointer to work in a loop     CItem\* item;  //--- go through the loop and try to delete dynamic pointers     while(CheckPointer(m\_items)!=POINTER\_INVALID)       {        item=m\_items;        m\_items=m\_items.Next();        if(CheckPointer(item)==POINTER\_DYNAMIC)          {           Print("Dynamyc object ",item.Identifier()," to be deleted");           delete (item);          }        else Print("Non-dynamic object ",item.Identifier()," cannot be deleted");       }  //---    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     CMyList list;     CItem   items[10];     CItem\*  item;  //--- create and add into the list a dynamic object pointer     item=new CItem;     if(item!=NULL)       {        item.Initialize(100,"dynamic");        item.PrintMe();        list.InsertToBegin(item);       }  //--- add automatic pointers into the list     for(int i=0; i<10; i++)       {        items[i].Initialize(i,"automatic");        items[i].PrintMe();        item=GetPointer(items[i]);        if(CheckPointer(item)!=POINTER\_INVALID)           list.InsertToBegin(item);       }  //--- add one more dynamic object pointer at the list beginning     item=new CItem;     if(item!=NULL)       {        item.Initialize(200,"dynamic");        item.PrintMe();        list.InsertToBegin(item);       }  //--- delete all the list elements     list.Destroy();  //--- all the list elements will be deleted after the script is over  //--- see the Experts tab in the terminal    } |

See also

[Object Pointers](../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md), [Checking the Object Pointer](../../Constants,-Enumerations-and-Structures/Named-Constants/Checking-Object-Pointer/Checking-Object-Pointer.md), [Object Delete Operator delete](../../Language-Basics/Operators/Object-Delete-Operator-delete/Object-Delete-Operator-delete.md)
