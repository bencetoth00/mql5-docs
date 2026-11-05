# Prev

Prev

Gets a pointer to the previous element in the list.

|  |
| --- |
| CObject\*  Prev() |

Return Value

Pointer to the previous element in the list. If an item is listed first, then return NULL.

Example:

|  |
| --- |
| //--- example for CObject::Prev()  #include <Object.mqh>  //---  void OnStart()    {     CObject \*object\_first,\*object\_second;     //---     object\_first=new CObject;     if(object\_first==NULL)       {        printf("Object create error");        return;       }     object\_second=new CObject;     if(object\_second==NULL)       {        printf("Object create error");        delete object\_first;        return;       }     //--- set interconnect     object\_first.Next(object\_second);     object\_second.Prev(object\_first);     //--- use prev object     CObject \*object=object\_second.Prev();     //--- delete objects     delete object\_first;     delete object\_second;    } |
