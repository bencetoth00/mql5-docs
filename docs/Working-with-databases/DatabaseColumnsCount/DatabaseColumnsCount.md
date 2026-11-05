# DatabaseColumnsCount

DatabaseColumnsCount

Gets the number of fields in a request.

|  |
| --- |
| int  DatabaseColumnsCount(     int  request      // request handle received in DatabasePrepare     ); |

Parameters

request

[in]  Request handle received in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

Return Value

Number of fields or -1 in case of an error. To get the error code, use GetLastError(), the possible responses are:

- ERR\_DATABASE\_INVALID\_HANDLE (5121) - invalid request handle.

Note

There is no need to call the [DatabaseRead()](../DatabaseRead/DatabaseRead.md) function to get the number of fields of a request created in DatabasePrepare(). For the remaining DatabaseColumnXXX() functions, DatabaseRead() should be preliminarily called.

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseFinalize](../DatabaseFinalize/DatabaseFinalize.md), [DatabaseClose](../DatabaseClose/DatabaseClose.md)
