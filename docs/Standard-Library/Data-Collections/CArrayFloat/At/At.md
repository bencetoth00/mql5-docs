# At

At

Gets the element from the specified array position.

|  |
| --- |
| float  At(     int  pos      // position      ) const |

Parameters

pos

[in]  Position of the desired element in the array.

Return Value

The value of the element - success, FLT\_MAX - there was an attempt to get an element from a non-existing position (the last error code is ERR\_OUT\_OF\_RANGE).

Note

Of course, FLT\_MAX may be a valid value of an array element. Therefore, always check the last error code after receiving such a value.

Example:

|  |
| --- |
| //--- example for CArrayFloat::At(int)  #include <Arrays\ArrayFloat.mqh>  //---  void OnStart()    {     CArrayFloat \*array=new CArrayFloat;     //---     if(array==NULL)       {        printf("Object create error");        return;       }     //--- add arrays elements     //--- . . .     for(int i=0;i<array.Total();i++)       {        float result=array.At(i);        if(result==FLT\_MAX && GetLastError()==ERR\_OUT\_OF\_RANGE)          {           //--- error reading from array           printf("Get element error");           delete array;           return;          }        //--- use element        //--- . . .       }     //--- delete array     delete array;    } |
