# FreeMode


Gets the flag of memory management when deleting list elements.

```cpp
bool  FreeMode() const
```

Return Value

Flag of memory management.

Example:

```cpp
//--- example for CList::FreeMode()
#include <Arrays\List.mqh>
//---
void OnStart()
  {
   CList *list=new CList;
   //---
   if(list==NULL)
     {
      printf("Object create error");
      return;
     }
   //--- get free mode flag
   bool list_free_mode=list.FreeMode();
   //--- delete list
   delete list;
  }
```