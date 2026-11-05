# BufferCreate


Creates an OpenCL buffer at the specified index.

```cpp
bool  BufferCreate(
   const int   buffer_index,      // buffer index
   const uint  size_in_bytes,     // buffer size in bytes
   const uint  flags              // combination of flags that define the buffer properties
   );
```

Parameters

buffer\_index

[in]  Index buffer.

size\_in\_bytes

[in]  Buffer size in bytes.

flags

[in]  Buffer properties that are set using a combination of flags.

Return Value

In case of successful execution, returns true, otherwise - false.