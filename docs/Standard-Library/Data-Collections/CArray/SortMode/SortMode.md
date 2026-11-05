# SortMode

SortMode

Gets the sorting mode for an array.

|  |
| --- |
| int  SortMode() const; |

Return Value

Sorting mode.

Example:

|  |
| --- |
| //--- example for CArray::SortMode()  #include <Arrays\Array.mqh>  //---  void OnStart()    {     CArray \*array=new CArray;     //---     if(array==NULL)       {        printf("Object create error");        return;       }     //--- check sort mode     int sort\_mode=array.SortMode();     //--- use array     //--- ...     //--- delete array     delete array;    } |
