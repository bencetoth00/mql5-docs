# Type


Gets the array type identifier.

```cpp
virtual int  Type() const
```

Return Value

Array type identifier (for CArrayString - 89).

Example:

```cpp
//--- example for CArrayString::Type()
#include <Arrays\ArrayString.mqh>
//---
void OnStart()
  {
   CArrayString *array=new CArrayString;
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