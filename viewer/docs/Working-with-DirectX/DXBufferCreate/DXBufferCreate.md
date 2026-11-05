# DXBufferCreate


Creates a buffer of a specified type based on a data array.

```cpp
int  DXBufferCreate(
   int                  context,               // graphic context handle
   ENUM_DX_BUFFER_TYPE  buffer_type,           // type of a created buffer
   const void&          data[],                // buffer data
   uint                 start=0,               // initial index
   uint                 count=WHOLE_ARRAY      // number of elements
   );
```

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

buffer\_type

[in]  Buffer type from the ENUM\_DX\_BUFFER\_TYPE enumeration.

data[]

[in]  Data for creating a buffer.

start=0

[in]  Index of the first element of the array, starting from which the array values are used to create a buffer. By default, the data is taken from the beginning of the array.

count=WHOLE\_ARRAY

[in]  Number of values.  By default, the entire array is used (count=[WHOLE\_ARRAY](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md)).

Return Value

The handle for a created buffer or INVALID\_HANDLE in case of an error. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

For the index buffer, the data[] array should be of 'uint' type, while the vertex buffer receives the array of structures describing vertices.

A created handle that is no longer in use should be explicitly released by the [DXRelease()](../DXRelease/DXRelease.md) function.

ENUM\_DX\_BUFFER\_TYPE

| ID | Value | Description |
| --- | --- | --- |
| DX\_BUFFER\_VERTEX | 1 | Vertex buffer |
| DX\_BUFFER\_INDEX | 2 | Index buffer |