# InsertSort


Inserts an element in a sorted array.

```cpp
bool  InsertSort(
   int  element      // element to insert
   )
```

Parameters

element

[in]  Value of the element to be inserted into a sorted array

Return Value

true - successful, false - cannot insert the element.

Example:

```cpp
//--- example for CArrayInt::InsertSort(int)
#include <Arrays\ArrayInt.mqh>
//---
void OnStart()
  {
   CArrayInt *array=new CArrayInt;
   //---
   if(array==NULL)
     {
      printf("Object create error");
      return;
     }
   //--- add arrays elements
   //--- . . .
   //--- sort array
   array.Sort();
   //--- insert element
   if(!array.InsertSort(10000))
     {
      printf("Insert error");
      delete array;
      return;
     }
   //--- delete array
   delete array;
  }
```