# File Functions

File Functions

This is a group of functions for working with files.

For security reasons, work with files is strictly controlled in the MQL5 language. Files with which file operations are conducted using MQL5 means cannot be outside the file sandbox.

There are two directories (with subdirectories) in which working files can be located:

- terminal\_data\_folder\MQL5\FILES\ (in the terminal menu select to view "File" - "Open the data directory");
- the common folder for all the terminals installed on a computer - usually located in the directory C:\Documents and Settings\All Users\Application Data\MetaQuotes\Terminal\Common\Files.

There is a program method to obtain names of these catalogs using the [TerminalInfoString()](../Checkup/TerminalInfoString/TerminalInfoString.md) function, using the [ENUM\_TERMINAL\_INFO\_STRING](../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_string) enumeration:

|  |
| --- |
| //--- Folder that stores the terminal data     string terminal\_data\_path=TerminalInfoString(TERMINAL\_DATA\_PATH);  //--- Common folder for all client terminals     string common\_data\_path=TerminalInfoString(TERMINAL\_COMMONDATA\_PATH); |

Work with files from other directories is prohibited.

If the file is opened for writing using [FileOpen()](FileOpen/FileOpen.md), all subfolders specified in the path will be created if there are no such ones.

File functions allow working with so-called "named pipes". To do this, simply call [FileOpen()](FileOpen/FileOpen.md) function with appropriate parameters.

| Function | Action |
| --- | --- |
| [FileSelectDialog](FileSelectDialog/FileSelectDialog.md) | Create a file or folder opening/creation dialog |
| [FileFindFirst](FileFindFirst/FileFindFirst.md) | Starts the search of files in a directory in accordance with the specified filter |
| [FileFindNext](FileFindNext/FileFindNext.md) | Continues the search started by the FileFindFirst() function |
| [FileFindClose](FileFindClose/FileFindClose.md) | Closes search handle |
| [FileOpen](FileOpen/FileOpen.md) | Opens a file with a specified name and flag |
| [FileDelete](FileDelete/FileDelete.md) | Deletes a specified file |
| [FileFlush](FileFlush/FileFlush.md) | Writes to a disk all data remaining in the input/output file buffer |
| [FileGetInteger](FileGetInteger/FileGetInteger.md) | Gets an integer property of a file |
| [FileIsEnding](FileIsEnding/FileIsEnding.md) | Defines the end of a file in the process of reading |
| [FileIsLineEnding](FileIsLineEnding/FileIsLineEnding.md) | Defines the end of a line in a text file in the process of reading |
| [FileClose](FileClose/FileClose.md) | Closes a previously opened file |
| [FileIsExist](FileIsExist/FileIsExist.md) | Checks the existence of a file |
| [FileCopy](FileCopy/FileCopy.md) | Copies the original file from a local or shared folder to another file |
| [FileMove](FileMove/FileMove.md) | Moves or renames a file |
| [FileReadArray](FileReadArray/FileReadArray.md) | Reads arrays of any type except for string from the file of the BIN type |
| [FileReadBool](FileReadBool/FileReadBool.md) | Reads from the file of the CSV type a string from the current position till a delimiter (or till the end of a text line) and converts the read string to a value of bool type |
| [FileReadDatetime](FileReadDatetime/FileReadDatetime.md) | Reads from the file of the CSV type a string of one of the formats: "YYYY.MM.DD HH:MM:SS", "YYYY.MM.DD" or "HH:MM:SS" - and converts it into a datetime value |
| [FileReadDouble](FileReadDouble/FileReadDouble.md) | Reads a double value from the current position of the file pointer |
| [FileReadFloat](FileReadFloat/FileReadFloat.md) | Reads a float value from the current position of the file pointer |
| [FileReadInteger](FileReadInteger/FileReadInteger.md) | Reads int, short or char value from the current position of the file pointer |
| [FileReadLong](FileReadLong/FileReadLong.md) | Reads a long type value from the current position of the file pointer |
| [FileReadNumber](FileReadNumber/FileReadNumber.md) | Reads from the file of the CSV type a string from the current position till a delimiter (or til the end of a text line) and converts the read string into double value |
| [FileReadString](FileReadString/FileReadString.md) | Reads a string from the current position of a file pointer from a file |
| [FileReadStruct](FileReadStruct/FileReadStruct.md) | Reads the contents from a binary file  into a structure passed as a parameter, from the current position of the file pointer |
| [FileSeek](FileSeek/FileSeek.md) | Moves the position of the file pointer by a specified number of bytes relative to the specified position |
| [FileSize](FileSize/FileSize.md) | Returns the size of a corresponding open file |
| [FileTell](FileTell/FileTell.md) | Returns the current position of the file pointer of a corresponding open file |
| [FileWrite](FileWrite/FileWrite.md) | Writes data to a file of CSV or TXT type |
| [FileWriteArray](FileWriteArray/FileWriteArray.md) | Writes arrays of any type except for string into a file of BIN type |
| [FileWriteDouble](FileWriteDouble/FileWriteDouble.md) | Writes value of the double type from the current position of a file pointer into a binary file |
| [FileWriteFloat](FileWriteFloat/FileWriteFloat.md) | Writes value of the float type from the current position of a file pointer into a binary file |
| [FileWriteInteger](FileWriteInteger/FileWriteInteger.md) | Writes value of the int type from the current position of a file pointer into a binary file |
| [FileWriteLong](FileWriteLong/FileWriteLong.md) | Writes value of the long type from the current position of a file pointer into a binary file |
| [FileWriteString](FileWriteString/FileWriteString.md) | Writes the value of a string parameter into a BIN or TXT file starting from the current position of the file pointer |
| [FileWriteStruct](FileWriteStruct/FileWriteStruct.md) | Writes the contents of a structure passed as a parameter into a binary file, starting from the current position of the file pointer |
| [FileLoad](FileLoad/FileLoad.md) | Reads all data of a specified binary file into a passed array of numeric types or simple structures |
| [FileSave](FileSave/FileSave.md) | Writes to a binary file all elements of an array passed as a parameter |
| [FolderCreate](FolderCreate/FolderCreate.md) | Creates a folder in the Files directory |
| [FolderDelete](FolderDelete/FolderDelete.md) | Removes a selected directory. If the folder is not empty, then it can't be removed |
| [FolderClean](FolderClean/FolderClean.md) | Deletes all files in the specified folder |
