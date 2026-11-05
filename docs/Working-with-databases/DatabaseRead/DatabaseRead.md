# DatabaseRead

DatabaseRead

Moves to the next entry as a result of a request.

|  |
| --- |
| bool  DatabaseRead(     int  request      // request handle received in DatabasePrepare     ); |

Parameters

request

[in]  Request handle received in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

Return Value

Return true if successful, otherwise false. To get the error code, use GetLastError(), the possible responses are:

- ERR\_INVALID\_PARAMETER (4003)               –  no table name specified (empty string or NULL);
- ERR\_WRONG\_STRING\_PARAMETER (5040)  – error converting a request into a UTF-8 string;
- ERR\_DATABASE\_INTERNAL (5120)              – internal database error;
- ERR\_DATABASE\_INVALID\_HANDLE (5121)    – invalid database handle;
- ERR\_DATABASE\_EXECUTE (5124)                –  request execution error;
- ERR\_DATABASE\_NO\_MORE\_DATA (5126)    – no table exists (not an error, normal completion).

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseReadBind](../DatabaseReadBind/DatabaseReadBind.md)
