# FrameAdd


Adds a frame with data. There are two variants of the function.

1. Adding data from a file

```cpp
bool  FrameAdd(
   const string  name,        // Public name/label
   long          id,          // Public ID
   double        value,       // Value
   const string  filename     // Name of a data file
   );
```

2. Adding data from an array of any type

```cpp
bool  FrameAdd(
   const string  name,        // Public name/label
   long          id,          // Public ID
   double        value,       // Value
   const void&   data[]       // Array of any type
   );
```

Parameters

name

[in]  Public frame label. It can be used for a filter in the [FrameFilter()](../FrameFilter/FrameFilter.md) function.

id

[in]  A public identifier of the frame. It can be used for a filter in the [FrameFilter()](../FrameFilter/FrameFilter.md) function.

value

[in]  A numeric value to write into the frame. It is used to transmit a single pass result like in the [OnTester()](../../Event-Handling/OnTester/OnTester.md) function.

filename

[in]  The name of the file that contains data to add to the frame. The file must be locate in the folder MQL5/Files.

data

[in]  An array of any type to write into the frame. Passed by reference.

Return Value

Returns true if successful, otherwise false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.