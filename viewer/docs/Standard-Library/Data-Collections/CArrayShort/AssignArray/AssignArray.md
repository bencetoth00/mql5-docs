# AssignArray


Copies the elements of one array to another.

```cpp
bool  AssignArray(
   const short&  src[]      // source array
   )
```

Parameters

src[]

[in]  Reference to an array used as a source of elements to copy.

Return Value

true - successful, false - cannot copy the items.

Example:

```cpp
//--- example for CArrayShort::AssignArray(const short &[])
#include <Arrays\ArrayShort.mqh>
//---
short src[];
//---
void OnStart()
  {
   CArrayShort *array=new CArrayShort;
   //---
   if(array==NULL)
     {
      printf("Object create error");
      return;
     }
   //--- assign another array
   if(!array.AssignArray(src))
     {
      printf("Array assigned error");
      delete array;
      return;
     }
   //--- use array
   //--- . . .
   //--- delete array
   delete array;
  }
```