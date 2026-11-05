# ArrayReverse


Reverses the specified number of elements in the array starting with a specified index.

```cpp
bool  ArrayReverse(
   void&        array[],            // array of any type
   uint         start=0,            // index to start reversing the array from
   uint         count=WHOLE_ARRAY   // number of elements
   );
```

Parameters

array[]

[in][out]  Array.

start=0

[in]  Index the array reversal starts from.

count=WHOLE\_ARRAY

[in]  Number of reversed elements. If WHOLE\_ARRAY, then all array elements are moved in the inversed manner starting with the specified start index up to the end of the array.

Return Value

Returns true if successful, otherwise - false.

Note

The [ArraySetAsSeries()](../ArraySetAsSeries/ArraySetAsSeries.md) function does not move the array elements physically. Instead, it only changes the indexation direction backwards to arrange the access to the elements as in the [timeseries](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md). The ArrayReverse() function physically moves the array elements so that the array is "reversed".

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- declare the fixed-size array and fill in the values
   int array[10];
   for(int i=0;i<10;i++)
     {
      array[i]=i;
     }
//--- display the array before reversing the elements
   Print("Before calling ArrayReverse()");
   ArrayPrint(array);
//--- reverse 3 elements in the array and show the new set
   ArrayReverse(array,4,3);
   Print("After calling ArrayReverse()");
   ArrayPrint(array);
/*
  Execution result:
  Before calling ArrayReverse()
   0 1 2 3 4 5 6 7 8 9
  After calling ArrayReverse()
   0 1 2 3 6 5 4 7 8 9
*/
```

 

See also

[ArrayInsert](../ArrayInsert/ArrayInsert.md), [ArrayRemove](../ArrayRemove/ArrayRemove.md), [ArrayCopy](../ArrayCopy/ArrayCopy.md), [ArrayResize](../ArrayResize/ArrayResize.md), [ArrayFree](../ArrayFree/ArrayFree.md), [ArrayGetAsSeries](../ArrayGetAsSeries/ArrayGetAsSeries.md), [ArraySetAsSeries](../ArraySetAsSeries/ArraySetAsSeries.md)