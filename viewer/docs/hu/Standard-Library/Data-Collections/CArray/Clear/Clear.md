# Clear


Törli a tömb összes elemét a memória felszabadítása nélkül.

```cpp
void  Clear()
```

Visszatérési érték

Nincs.

 

Példa:

```cpp
//--- example for CArray::Clear()
#include <Arrays\Array.mqh>
//---
void OnStart()
 {
 CArray *array=new CArray;
 //---
 if(array==NULL)
 {
 printf("Object create error");
 return;
 }
 //--- use array
 //--- ...
 //--- clear array
 array.Clear();
 //--- delete array
 delete array;
 }
```
