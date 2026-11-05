# Next

Next

Gets a pointer to the next element in the list.

|  |
| --- |
| CObject\*  Next() |

Return Value

Pointer to the next element in the list. If this is the last element in the list, return NULL.

Example:

|  |
| --- |
| //--- example for CObject::Next()  #include <Object.mqh>  //---  void OnStart()    {     CObject \*object\_first,\*object\_second;     //---     object\_first=new CObject;     if(object\_first==NULL)       {        printf("Object create error");        return;       }     object\_second=new CObject;     if(object\_second==NULL)       {        printf("Object create error");        delete object\_first;        return;       }     //--- set interconnect     object\_first.Next(object\_second);     object\_second.Prev(object\_first);     //--- use next object     CObject \*object=object\_first.Next();     //--- delete objects     delete object\_first;     delete object\_second;    } |
