# Type


Gets the type identifier.

```cpp
virtual int  Type() const
```

Return Value

Type identifier (for CObject - 0).

Example:

```cpp
//--- example for CObject::Type()
#include <Object.mqh>
//---
void OnStart()
  {
   CObject *object=new CObject;
   //---
   object=new CObject;
   if(object ==NULL)
     {
      printf("Object create error");
      return;
     }
   //--- get objects type
   int type=object.Type();
   //--- delete object
   delete object;
  }
```