# ArraySwap

ArraySwap

Swaps the contents of two dynamic arrays of the same type. For multidimensional arrays, the number of elements in all dimensions except the first one should match.

|  |
| --- |
| bool  ArraySwap(     void&  array1[],      // first array     void&  array2[]       // second array     ); |

Parameters

array1[]

[in][out]  Array of numerical type.

array2[]

[in][out]  Array of numerical type.

Return Value

Returns true if successful, otherwise false. In this case, [GetLastError()](../../Checkup/GetLastError/GetLastError.md) returns the [ERR\_INVALID\_ARRAY](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) error code.

Note

The function accepts dynamic arrays of the same type and the same dimensions except the first one. For integer types, the sign is ignored, i.e. [char](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md)==uchar)

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- arrays for storing quotes     double source\_array[][8];     double   dest\_array[][8];     MqlRates rates[];  //--- get the data of the last 20 candles on the current timeframe     int copied=CopyRates(NULL,0,0,20,rates);     if(copied<=0)       {        PrintFormat("CopyRates(%s,0,0,20,rates) failed, error=%d",                    Symbol(),GetLastError());        return;       }  //--- set the array size for the amount of copied data     ArrayResize(source\_array,copied);  //--- fill the rate\_array\_1[] array by data from rates[]     for(int i=0;i<copied;i++)       {        source\_array[i][0]=(double)rates[i].time;        source\_array[i][1]=rates[i].open;        source\_array[i][2]=rates[i].high;        source\_array[i][3]=rates[i].low;        source\_array[i][4]=rates[i].close;        source\_array[i][5]=(double)rates[i].tick\_volume;        source\_array[i][6]=(double)rates[i].spread;        source\_array[i][7]=(double)rates[i].real\_volume;       }  //--- swap data between source\_array[] and dest\_array[]     if(!ArraySwap(source\_array,dest\_array))       {        PrintFormat("ArraySwap(source\_array,rate\_array\_2) failed, error code=%d",GetLastError());        return;       }  //--- ensure that the source array has become zero after the swap     PrintFormat("ArraySwap() done: ArraySize(source\_array)=%d",ArraySize(source\_array));  //--- display the data of the dest\_array[] destination array     ArrayPrint(dest\_array);    } |

See also

[ArrayCopy](../ArrayCopy/ArrayCopy.md), [ArrayFill](../ArrayFill/ArrayFill.md), [ArrayRange](../ArrayRange/ArrayRange.md), [ArrayIsDynamic](../ArrayIsDynamic/ArrayIsDynamic.md)
