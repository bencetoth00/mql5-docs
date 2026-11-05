# FreeMode

FreeMode

Gets the flag of memory management when deleting list elements.

|  |
| --- |
| bool  FreeMode() const |

Return Value

Flag of memory management.

Example:

|  |
| --- |
| //--- example for CList::FreeMode()    #include <Arrays\List.mqh>    //---    void OnStart()      {       CList \*list=new CList;       //---       if(list==NULL)         {          printf("Object create error");          return;         }       //--- get free mode flag       bool list\_free\_mode=list.FreeMode();       //--- delete list       delete list;      } |
