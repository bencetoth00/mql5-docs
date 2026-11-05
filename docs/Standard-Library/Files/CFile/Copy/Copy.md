# Copy

Copy

Copies a file.

|  |
| --- |
| bool  Copy(     const string  src\_name,      // file name     int           src\_flag,      // flag     const string  dst\_name,      // file name     int           dst\_flags      // flags     ) |

Parameters

src\_name

[in]  Name of a source file.

src\_flag

[in]  Flags of a source file (only FILE\_COMMON is used).

dst\_name

[in]  File name of the destination file.

dst\_flags

[in]  Flags of the destination file (only FILE\_REWRITE and FILE\_COMMON are used).

Return Value

true - successful, false - cannot copy the file.
