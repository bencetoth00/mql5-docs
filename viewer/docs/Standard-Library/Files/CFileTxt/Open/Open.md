# Open


Opens the specified text file and, if successful, assigns it to the class instance.

```cpp
int  Open(
   const string  file_name,     // file name
   int           flags          // flags
   )
```

Parameters

file\_name

[in]  File name to open.

flags

[in]  File open flags (FILE\_TXT flag is forcibly set).

Return Value

Opened file handle.