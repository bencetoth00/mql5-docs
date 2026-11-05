# DatabaseClose

DatabaseClose

Closes a database.

|  |
| --- |
| void  DatabaseClose(     int  database      // database handle received in DatabaseOpen     ); |

Parameters

database

[in]  Database handle received in [DatabaseOpen()](../DatabaseOpen/DatabaseOpen.md).

Return Value

None.

Note

After calling DatabaseClose, all [handles of requests](../DatabasePrepare/DatabasePrepare.md)  to the database are automatically removed and become invalid.

If the handle is invalid, the function sets the ERR\_DATABASE\_INVALID\_HANDLE error. You can check the error using GetLastError().

See also

[DatabaseOpen](../DatabaseOpen/DatabaseOpen.md), [DatabasePrepare](../DatabasePrepare/DatabasePrepare.md)
