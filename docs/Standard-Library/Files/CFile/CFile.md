# CFile

CFile

CFile is a base class for CFileBin and CFileTxt classes.

Description

CFile class provides the simplified access to MQL5 API file and folder functions for all of its descendants.

Declaration

|  |
| --- |
| class CFile: public CObject |

Title

|  |
| --- |
| #include <Files\File.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CFile  Direct descendants  [CFileBin](../CFileBin/CFileBin.md), CFilePipe, [CFileTxt](../CFileTxt/CFileTxt.md) |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Handle](Handle/Handle.md) | Gets file handle |
| [Filename](Filename/Filename.md) | Gets file name |
| [Flags](Flags/Flags.md) | Gets file flags |
| [SetUnicode](SetUnicode/SetUnicode.md) | Sets/clears the FILE\_UNICODE flag |
| [SetCommon](SetCommon/SetCommon.md) | Sets/clears the FILE\_COMMON flag |
| General methods for files |  |
| [Open](Open/Open.md) | Opens file |
| [Close](Close/Close.md) | Closes file |
| [Delete](Delete/Delete.md) | Deletes file |
| [IsExist](IsExist/IsExist.md) | Checks file for existence |
| [Copy](Copy/Copy.md) | Copies file |
| [Move](Move/Move.md) | Renames/moves file |
| [Size](Size/Size.md) | Gets file size |
| [Tell](Tell/Tell.md) | Gets current file position |
| [Seek](Seek/Seek.md) | Sets current file position |
| [Flush](Flush/Flush.md) | Flushes data on disk |
| [IsEnding](IsEnding/IsEnding.md) | Checks file for end |
| [IsLineEnding](IsLineEnding/IsLineEnding.md) | Checks line for end |
| General methods for folders |  |
| [FolderCreate](FolderCreate/FolderCreate.md) | Creates folder |
| [FolderDelete](FolderDelete/FolderDelete.md) | Deletes folder |
| [FolderClean](FolderClean/FolderClean.md) | Clears folder |
| Files and folders search methods |  |
| [FileFindFirst](FileFindFirst/FileFindFirst.md) | Begins file search |
| [FileFindNext](FileFindNext/FileFindNext.md) | Continues file search |
| [FileFindClose](FileFindClose/FileFindClose.md) | Closes search handle |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
