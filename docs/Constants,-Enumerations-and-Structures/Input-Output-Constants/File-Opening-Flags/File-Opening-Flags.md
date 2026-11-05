# File Opening Flags

File Opening Flags

File opening flag values specify the file access mode. Flags are defined as follows:

| Identifier | Value | Description |
| --- | --- | --- |
| FILE\_READ | 1 | File is opened for reading. Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). When opening a file specification of FILE\_WRITE and/or FILE\_READ is required. |
| FILE\_WRITE | 2 | File is opened for writing. Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). When opening a file specification of FILE\_WRITE and/or FILE\_READ is required. |
| FILE\_BIN | 4 | Binary read/write mode (without string to string conversion). Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). |
| FILE\_CSV | 8 | CSV file (all its elements are converted to strings of the appropriate type, Unicode or ANSI, and separated by separator). Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). |
| FILE\_TXT | 16 | Simple text file (the same as csv file, but without taking into account the separators). Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). |
| FILE\_ANSI | 32 | Strings of ANSI type (one byte symbols). Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). |
| FILE\_UNICODE | 64 | Strings of UNICODE type (two byte symbols). Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md). |
| FILE\_SHARE\_READ | 128 | Shared access for reading from several programs. Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md), but it does not replace the necessity to indicate FILE\_WRITE and/or the FILE\_READ flag when opening a file. |
| FILE\_SHARE\_WRITE | 256 | Shared access for writing from several programs. Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md), but it does not replace the necessity to indicate FILE\_WRITE and/or the FILE\_READ flag when opening a file. |
| FILE\_REWRITE | 512 | Possibility for the file rewrite using functions [FileCopy()](../../../File-Functions/FileCopy/FileCopy.md) and [FileMove()](../../../File-Functions/FileMove/FileMove.md). The file should exist or should be opened for writing, otherwise the file will not be opened. |
| FILE\_COMMON | 4096 | The file path in the common folder of all client terminals \Terminal\Common\Files. Flag is used in [FileOpen()](../../../File-Functions/FileOpen/FileOpen.md), [FileCopy()](../../../File-Functions/FileCopy/FileCopy.md), [FileMove()](../../../File-Functions/FileMove/FileMove.md) and in [FileIsExist()](../../../File-Functions/FileIsExist/FileIsExist.md) functions. |

One or several flags can be specified when opening a file. This is a combination of flags. The combination of flags is written using the sign of logical OR (|), which is positioned between enumerated flags. For example, to open a file in CSV format for reading and writing at the same time, specify the combination FILE\_READ|FILE\_WRITE|FILE\_CSV.

Example:

|  |
| --- |
| int filehandle=FileOpen(filename,FILE\_READ|FILE\_WRITE|FILE\_CSV); |

There are some specific features of work when you specify read and write flags:

- If FILE\_READ is specified, an attempt is made to open an existing file. If a file does not exist, file opening fails, a new file is not created.
- FILE\_READ|FILE\_WRITE – a new file is created if the file with the specified name does not exist.
- FILE\_WRITE –  the file is created again with a zero size.

When opening a file, specification of FILE\_WRITE and/or FILE\_READ is required.

Flags that define the type of reading of an open file possess priority. The highest flag is FILE\_CSV, then goes FILE\_BIN, and FILE\_TXT is of lowest priority. Thus, if several flags are specified at the same time, (FILE\_TXT|FILE\_CSV or FILE\_TXT|FILE\_BIN or FILE\_BIN|FILE\_CSV), the flag with the highest priority will be used.

Flags that define the type of encoding also have priority. FILE\_UNICODE is of a higher priority than FILE\_ANSI. So if you specify combination FILE\_UNICODE|FILE\_ANSI, flag FILE\_UNICODE will be used.

If neither FILE\_UNICODE nor FILE\_ANSI is indicated, FILE\_UNICODE is implied. If neither FILE\_CSV, nor FILE\_BIN, nor FILE\_TXT is specified, FILE\_CSV is implied.

If a file is opened for reading as a text file (FILE\_TXT or FILE\_CSV), and at the file beginning a special two-byte indication 0xff,0xfe is found, the encoding flag will be FILE\_UNICODE, even if FILE\_ANSI is specified.

See also

[File Functions](../../../File-Functions/File-Functions.md)
