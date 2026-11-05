# DatabaseOpen


Opens or creates a database in a specified file.

```cpp
int  DatabaseOpen(
   string  filename,      // file name
   uint    flags          // combination of flags
   );
```

Parameters

filename

[in]  File name relative to the "MQL5\Files" folder.

flags

[in]  Combination of flags from the [ENUM\_DATABASE\_OPEN\_FLAGS](DatabaseOpen.md#enum_database_open_flags) enumeration.

Return Value

If executed successfully, the function returns the database handle, which is then used to access the database. Otherwise, it returns [INVALID\_HANDLE](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md). To get the error code, use GetLastError(), the possible responses are:

- ERR\_INTERNAL\_ERROR (4001)                       – critical runtime error;
- ERR\_WRONG\_INTERNAL\_PARAMETER (4002)  - internal error, while accessing the "MQL5\Files" folder;
- ERR\_INVALID\_PARAMETER (4003)                  – path to the database file contains an empty string, or an incompatible combination of flags is set;
- ERR\_NOT\_ENOUGH\_MEMORY (4004)              - insufficient memory;
- ERR\_WRONG\_FILENAME (5002)                     - wrong database file name;
- ERR\_TOO\_LONG\_FILENAME (5003)                 - absolute path to the database file exceeds the maximum length;
- ERR\_DATABASE\_TOO\_MANY\_OBJECTS (5122) - exceeded the maximum acceptable number of Database objects;
- ERR\_DATABASE\_CONNECT (5123)                  - database connection error;

- ERR\_DATABASE\_MISUSE (5621)                      - incorrect use of the SQLite library.

Note

If the filename parameter features NULL or the empty string "", a temporary file is created on the disk. It is automatically deleted after closing the database connection.

If the filename parameter features ":memory:", the database is created in the memory and is automatically deleted after the connection to it is closed.

If the flags parameter features none of the DATABASE\_OPEN\_READONLY or DATABASE\_OPEN\_READWRITE flags, the DATABASE\_OPEN\_READWRITE flag is used.

If the file extension is not specified, ".sqlite" is used.

ENUM\_DATABASE\_OPEN\_FLAGS

| ID | Description |
| --- | --- |
| DATABASE\_OPEN\_READONLY | Read only |
| DATABASE\_OPEN\_READWRITE | Open for reading and writing |
| DATABASE\_OPEN\_CREATE | Create the file on a disk if necessary |
| DATABASE\_OPEN\_MEMORY | Create a database in RAM |
| DATABASE\_OPEN\_COMMON | The file is in the common folder of all terminals |

See also

[DatabaseClose](../DatabaseClose/DatabaseClose.md)