# Type


Gets the array type identifier.

```cpp
virtual int  Type() const
```

Return Value

Array type identifier (for CArrayObj - 7778).

Example:

```cpp
//--- example for CArrayObj::Type()
#include <Arrays\ArrayObj.mqh>
//---
void OnStart()
  {
   CArrayObj *array=new CArrayObj;
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