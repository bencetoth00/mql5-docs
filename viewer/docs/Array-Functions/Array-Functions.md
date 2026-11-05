# Array Functions

# Group of Functions for Working with Arrays

[Arrays](../Language-Basics/Variables/Variables.md#array_define) are allowed to be maximum four-dimensional. Each dimension is indexed from 0 to dimension\_size-1. In a particular case of a one-dimensional array of 50 elements, calling of the first element will appear as array[0], of the last one - as array[49].

| Function | Action |
| --- | --- |
| [ArrayBsearch](ArrayBsearch/ArrayBsearch.md) | Returns index of the first found element in the first array dimension |
| [ArrayCopy](ArrayCopy/ArrayCopy.md) | Copies one array into another |
| [ArrayCompare](ArrayCompare/ArrayCompare.md) | Returns the result of comparing two arrays of [simple types](../Language-Basics/Data-Types/Data-Types.md#base_types) or custom structures without [complex objects](../Language-Basics/Data-Types/Data-Types.md#complex_types) |
| [ArrayFree](ArrayFree/ArrayFree.md) | Frees up buffer of any dynamic array and sets the size of the zero dimension in 0. |
| [ArrayGetAsSeries](ArrayGetAsSeries/ArrayGetAsSeries.md) | Checks direction of array indexing |
| [ArrayInitialize](ArrayInitialize/ArrayInitialize.md) | Sets all elements of a numeric array into a single value |
| [ArrayFill](ArrayFill/ArrayFill.md) | Fills an array with the specified value |
| [ArrayIsSeries](ArrayIsSeries/ArrayIsSeries.md) | Checks whether an array is a timeseries |
| [ArrayIsDynamic](ArrayIsDynamic/ArrayIsDynamic.md) | Checks whether an array is dynamic |
| [ArrayMaximum](ArrayMaximum/ArrayMaximum.md) | Search for an element with the maximal value |
| [ArrayMinimum](ArrayMinimum/ArrayMinimum.md) | Search for an element with the minimal value |
| [ArrayPrint](ArrayPrint/ArrayPrint.md) | Prints an array of a simple type or a simple structure into journal |
| [ArrayRange](ArrayRange/ArrayRange.md) | Returns the number of elements in the specified dimension of the array |
| [ArrayResize](ArrayResize/ArrayResize.md) | Sets the new size in the first dimension of the array |
| [ArrayInsert](ArrayInsert/ArrayInsert.md) | Inserts the specified number of elements from a source array to a receiving one starting from a specified index |
| [ArrayRemove](ArrayRemove/ArrayRemove.md) | Removes the specified number of elements from the array starting with a specified index |
| [ArrayReverse](ArrayReverse/ArrayReverse.md) | Reverses the specified number of elements in the array starting with a specified index |
| [ArraySetAsSeries](ArraySetAsSeries/ArraySetAsSeries.md) | Sets the direction of array indexing |
| [ArraySize](ArraySize/ArraySize.md) | Returns the number of elements in the array |
| [ArraySort](ArraySort/ArraySort.md) | Sorting of numeric arrays by the first dimension |
| [ArraySwap](ArraySwap/ArraySwap.md) | Swaps the contents of two dynamic arrays of the same type |
| [ArrayToFP16](ArrayToFP16/ArrayToFP16.md) | Copies an array of type float or double into an array of type [ushort](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#ushort) with the given format |
| [ArrayToFP8](ArrayToFP8/ArrayToFP8.md) | Copies an array of type float or double into an array of type [uchar](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#uchar) with the given format |
| [ArrayFromFP16](ArrayFromFP16/ArrayFromFP16.md) | Copies an array of type [ushort](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#ushort) into an array of float or double type with the given format |
| [ArrayFromFP8](ArrayFromFP8/ArrayFromFP8.md) | Copies an array of type [uchar](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#uchar) into an array of float or double type with the given format |
