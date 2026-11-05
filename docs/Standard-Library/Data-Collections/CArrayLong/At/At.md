# At

At

Gets the element from the specified array position.

|  |
| --- |
| long  At(     int  pos      // position     ) const |

Parameters

pos

[in]  Position of the desired element in the array.

Return Value

The value of the element - success, LONG\_MAX - there was an attempt to get an element from a non-existing position (the last error code is ERR\_OUT\_OF\_RANGE).

Note

Of course, LONG\_MAX may be a valid value of an array element. Therefore, always check the last error code after receiving such a value.

Example:

|  |
| --- |
| //--- example for CArrayLong::At(int)  #include <Arrays\ArrayLong.mqh>  //---  void OnStart()    {     CArrayLong \*array=new CArrayLong;     //---     if(array==NULL)       {        printf("Object create error");        return;       }     //--- add arrays elements     //--- . . .     for(int i=0;i<array.Total();i++)       {        long result=array.At(i);        if(result==LONG\_MAX && GetLastError()==ERR\_OUT\_OF\_RANGE)          {           //--- Error reading from the array           printf("Get element error");           delete array;           return;          }        //--- use element        //--- . . .       }     //--- delete array     delete array;    } |
