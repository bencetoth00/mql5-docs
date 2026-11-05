# In-File Position

Positioning Inside a File

Most of [file functions](../../../File-Functions/File-Functions.md) are associated with data read/write operations. At the same time, using the [FileSeek()](../../../File-Functions/FileSeek/FileSeek.md) you can specify the position of a file pointer to a position inside the file, from which the next read or write operation will be performed. The ENUM\_FILE\_POSITION enumeration contains valid pointer positions, relative to which you can specify the shift in bytes for the next operation.

ENUM\_FILE\_POSITION

| Identifier | Description |
| --- | --- |
| SEEK\_SET | File beginning |
| SEEK\_CUR | Current position of a file pointer |
| SEEK\_END | File end |

See also

[FileIsEnding](../../../File-Functions/FileIsEnding/FileIsEnding.md), [FileIsLineEnding](../../../File-Functions/FileIsLineEnding/FileIsLineEnding.md)
