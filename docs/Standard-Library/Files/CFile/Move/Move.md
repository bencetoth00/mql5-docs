# Move

Move

Renames/moves file.

|  |
| --- |
| bool  Move(     const string  src\_name,      // file name     int           src\_flag,      // flag     const string  dst\_name,      // file name     int           dst\_flags      // flags     ) |

Parameters

src\_name

[in]  Source file name.

src\_flag

[in]  Source file flags (only FILE\_COMMON is used).

dst\_name

[in]  File name of the destination file.

dst\_flags

[in]  Flags of the destination file (only FILE\_REWRITE and FILE\_COMMON are used).

Return Value

true - successful, false - failed to move/rename the file.
