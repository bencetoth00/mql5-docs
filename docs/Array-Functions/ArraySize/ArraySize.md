# ArraySize

ArraySize

The function returns the number of elements of a selected array.

|  |
| --- |
| int  ArraySize(     const void&  array[]    // checked array     ); |

Parameters

array[]

[in]  Array of any type.

Return Value

Value of [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Note

For a one-dimensional array, the value to be returned by the ArraySize is equal to that of [ArrayRange](../ArrayRange/ArrayRange.md)(array,0).

Example:

|  |
| --- |
| void OnStart()    {  //--- create arrays     double one\_dim[];     double four\_dim[][10][5][2];  //--- sizes     int one\_dim\_size=25;     int reserve=20;     int four\_dim\_size=5;  //--- auxiliary variable     int size;  //--- allocate memory without backup     ArrayResize(one\_dim,one\_dim\_size);     ArrayResize(four\_dim,four\_dim\_size);  //--- 1. one-dimensional array     Print("+==========================================================+");     Print("Array sizes:");     Print("1. One-dimensional array");     size=ArraySize(one\_dim);     PrintFormat("Zero dimension size = %d, Array size = %d",one\_dim\_size,size);  //--- 2. multidimensional array     Print("2. Multidimensional array");     size=ArraySize(four\_dim);     PrintFormat("Zero dimension size = %d, Array size = %d",four\_dim\_size,size);  //--- dimension sizes     int d\_1=ArrayRange(four\_dim,1);     int d\_2=ArrayRange(four\_dim,2);     int d\_3=ArrayRange(four\_dim,3);     Print("Check:");     Print("Zero dimension = Array size / (First dimension \* Second dimension \* Third dimension)");     PrintFormat("%d = %d / (%d \* %d \* %d)",size/(d\_1\*d\_2\*d\_3),size,d\_1,d\_2,d\_3);  //--- 3. one-dimensional array with memory backup     Print("3. One-dimensional array with memory backup");  //--- double the value     one\_dim\_size\*=2;  //--- allocate memory with backup     ArrayResize(one\_dim,one\_dim\_size,reserve);  //--- print out the size     size=ArraySize(one\_dim);     PrintFormat("Size with backup = %d, Actual array size = %d",one\_dim\_size+reserve,size);    } |
