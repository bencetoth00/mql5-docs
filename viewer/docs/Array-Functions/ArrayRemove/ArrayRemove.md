# ArrayRemove


Removes the specified number of elements from the array starting with a specified index.

```cpp
bool  ArrayRemove(
   void&        array[],            // array of any type
   uint         start,              // index the removal starts from
   uint         count=WHOLE_ARRAY   // number of elements
   );
```

Parameters

array[]

[in][out]  Array.

start

[in]  Index, starting from which the array elements are removed.

count=WHOLE\_ARRAY

[in]  Number of removed elements. The [WHOLE\_ARRAY](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) value means removing all elements from the specified index up the end of the array.

Return Value

Returns true if successful, otherwise - false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 5052 – ERR\_SMALL\_ARRAY (too big start value),
- 5056 – ERR\_SERIES\_ARRAY (the array cannot be changed, indicator buffer),
- 4003 – ERR\_INVALID\_PARAMETER (too big count value),
- 4005 - ERR\_STRUCT\_WITHOBJECTS\_ORCLASS (fixed-size array containing complex objects with the destructor),
- 4006 - ERR\_INVALID\_ARRAY  (fixed-size array containing structure or class objects with a destructor).

 

Note

If the function is used for a fixed-size array, the array size does not change: the remaining "tail" is physically copied to the start position. For accurate understanding of how the function works, see the example below. "Physical" copying means the copied objects are not created by calling the constructor or copying operator. Instead, the binary representation of an object is copied. For this reason, you cannot apply the ArrayRemove() function to the fixed-size array containing objects with the destructor (the ERR\_INVALID\_ARRAY or ERR\_STRUCT\_WITHOBJECTS\_ORCLASS error is activated). When removing such an object, the destructor should be called twice – for the original object and its copy.

You cannot remove elements from dynamic arrays designated as the indicator buffers by the [SetIndexBuffer()](../../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) function. This will result in the ERR\_SERIES\_ARRAY error. For indicator buffers, all size changing operations are performed by the terminal's executing subsystem.

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
//--- display the array before removing the elements
   Print("Before calling ArrayRemove()");
   ArrayPrint(array);
//--- delete 2 elements from the array and display the new set
   ArrayRemove(array,4,2);
   Print("After calling ArrayRemove()");
   ArrayPrint(array);
/*
  Execution result:
  Before calling ArrayRemove()
   0 1 2 3 4 5 6 7 8 9
  After calling ArrayRemove()
   0 1 2 3 6 7 8 9 8 9
*/
```

See also

[ArrayInsert](../ArrayInsert/ArrayInsert.md), [ArrayCopy](../ArrayCopy/ArrayCopy.md), [ArrayResize](../ArrayResize/ArrayResize.md), [ArrayFree](../ArrayFree/ArrayFree.md)