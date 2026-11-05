# ArrayInsert


Inserts the specified number of elements from a source array to a receiving one starting from a specified index.

```cpp
bool  ArrayInsert(
   void&        dst_array[],          // receiving array
   const void&  src_array[],          // source array
   uint         dst_start,            // receiver array index to be inserted
   uint         src_start=0,          // source array index to be copied
   uint         count=WHOLE_ARRAY     // number of elements to insert
   );
```

Parameters

dst\_array[]

[in][out]  Receiving array the elements should be added to.

src\_array[]

[in]  Source array the elements are to be added from.

dst\_start

[in]  Index in the receiving array for inserting elements from the source array.

src\_start=0

[in]  Index in the source array, starting from which the elements of the source array are taken for insertion.

count

[in]  Number of elements to be added from the source array. The [WHOLE\_ARRAY](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) means all elements from the specified index up to the end of the array.

Return Value

Returns true if successful, otherwise - false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 5052 – ERR\_SMALL\_ARRAY (the start and/or count parameters are set incorrectly or the src\_array[] source array is empty),
- 5056 – ERR\_SERIES\_ARRAY (the array cannot be changed, indicator buffer),
- 4006 – ERR\_INVALID\_ARRAY (copying to oneself is not allowed, or the arrays are of different types, or there is a fixed-size array containing class objects or destructor structures),
- 4005 - ERR\_STRUCT\_WITHOBJECTS\_ORCLASS (the array contains no [POD structures](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure) meaning a simple copying is impossible),
- Errors occurred when changing the dst\_array[] receiving array size are provided in the [ArrayRemove()](../ArrayRemove/ArrayRemove.md) function description.

 

Note

If the function is used for a fixed-size array, the size of the dst\_array[] receiving array itself does not change. Starting from the dst\_start position, the elements of the receiving array are shifted to the right (the last counts of the elements "come off"), while the elements copied from the source array take their place.

You cannot insert the elements to the dynamic arrays designated as the indicator buffers by the [SetIndexBuffer()](../../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) function. For indicator buffers, all size changing operations are performed by the terminal's executing subsystem.

In the source array, the elements are copied starting from the src\_start index. The source array size remains unchanged. The elements to be added to the receiving array are not links to the source array elements. This means that subsequent changes of the elements in any of the two arrays are not reflected in the second one.

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- declare the fixed-size array and fill in the values
   int array_dest[10];
   for(int i=0;i<10;i++)
     {
      array_dest[i]=i;
     }
   //--- source array
   int array_source[10];
   for(int i=0;i<10;i++)
     {
      array_source[i]=10+i;
     }
//--- display arrays before inserting the elements
   Print("Before calling ArrayInsert()");
   ArrayPrint(array_dest);
   ArrayPrint(array_source);
//--- insert 3 elements from the source array and show the new set of the receiving array
   ArrayInsert(array_dest,array_source,4,0,3);
   Print("After calling ArrayInsert()");
   ArrayPrint(array_dest);
/*
  Execution result
   Before calling ArrayInsert()
   0 1 2 3 4 5 6 7 8 9
   After calling ArrayInsert()
   0 1 2 3 10 11 12 7 8 9
*/
```

 

See also

[ArrayRemove](../ArrayRemove/ArrayRemove.md), [ArrayCopy](../ArrayCopy/ArrayCopy.md), [ArrayResize](../ArrayResize/ArrayResize.md), [ArrayFree](../ArrayFree/ArrayFree.md)