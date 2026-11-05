# Type


Gets the array type identifier.

```cpp
virtual int  Type() const
```

Return Value

Array type identifier (for CArrayFloat - 87).

Example:

```cpp
//--- example for CArrayFloat::Type()
#include <Arrays\ArrayFloat.mqh>
//---
void OnStart()
  {
   CArrayFloat *array=new CArrayFloat;
   //---
   if(array==NULL)
     {
      printf("Object create error");
      return;
     }
   //--- get array type
   int type=array.Type();
   //--- delete array
   delete array;
  }
```