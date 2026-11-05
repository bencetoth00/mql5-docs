# FolderDelete

FolderDelete

Deletes specified folder.

|  |
| --- |
| bool  FolderDelete(     const string  folder\_name      // folder name     ) |

Parameters

folder\_name

[in]  Name of the folder to delete. It contains path to the folder relative to the folder defined by FILE\_COMMON flag.

Return Value

true - successful, false - cannot delete the folder.

Note

The working folder is dependent on the flag that was previously set/reset using the SetCommon() method.
