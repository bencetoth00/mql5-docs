# Seek

Seek

Sets file pointer's position.

|  |
| --- |
| void  Seek(     long                offset,     // offset     ENUM\_FILE\_POSITION  origin      // origin     ) |

Parameters

offset

[in]  File offset in bytes (can be negative).

origin

[in]  Origin of the offset.

Return Value

true - successful, false - cannot change the file pointer.
