# File Properties


The [FileGetInteger()](../../../File-Functions/FileGetInteger/FileGetInteger.md) function is used for obtaining file properties. The identifier of the required property from the ENUM\_FILE\_PROPERTY\_INTEGER enumeration is passed to it during call.

ENUM\_FILE\_PROPERTY\_INTEGER

| ID | ID description |
| --- | --- |
| FILE\_EXISTS | Check the existence |
| FILE\_CREATE\_DATE | Date of creation |
| FILE\_MODIFY\_DATE | Date of the last modification |
| FILE\_ACCESS\_DATE | Date of the last access to the file |
| FILE\_SIZE | File size in bytes |
| FILE\_POSITION | Position of a pointer in the file |
| FILE\_END | Get the end of file sign |
| FILE\_LINE\_END | Get the end of line sign |
| FILE\_IS\_COMMON | The file is opened in a shared folder of all terminals (see [FILE\_COMMON](../File-Opening-Flags/File-Opening-Flags.md)) |
| FILE\_IS\_TEXT | The file is opened as a text file (see [FILE\_TXT](../File-Opening-Flags/File-Opening-Flags.md)) |
| FILE\_IS\_BINARY | The file is opened as a binary file (see [FILE\_BIN](../File-Opening-Flags/File-Opening-Flags.md)) |
| FILE\_IS\_CSV | The file is opened as CSV (see [FILE\_CSV](../File-Opening-Flags/File-Opening-Flags.md)) |
| FILE\_IS\_ANSI | The file is opened as ANSI (see [FILE\_ANSI](../File-Opening-Flags/File-Opening-Flags.md)) |
| FILE\_IS\_READABLE | The opened file is readable (see [FILE\_READ](../File-Opening-Flags/File-Opening-Flags.md)) |
| FILE\_IS\_WRITABLE | The opened file is writable (see [FILE\_WRITE](../File-Opening-Flags/File-Opening-Flags.md)) |

The [FileGetInteger()](../../../File-Functions/FileGetInteger/FileGetInteger.md) function has two different options of call. In the first option, for getting properties of a file, its handle is specified, which is obtained while opening the file using the [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md) function. This option allows getting all properties of a file.

The second option of the [FileGetInteger()](../../../File-Functions/FileGetInteger/FileGetInteger.md) function returns values of file properties by the file name. Using this option, only the following general properties can be obtained:

- FILE\_EXISTS – existence of a file with a specified name
- FILE\_CREATE\_DATE – date of creation of the file with the specified name
- FILE\_MODIFY\_DATE – date of modification of the file with the specified name

- FILE\_ACCESS\_DATE – date of the last access to the file with the specified name

- FILE\_SIZE – size of the file with the specified name

When trying to get properties other than specified above, the second option of FileGetInteger() call will return an error.
