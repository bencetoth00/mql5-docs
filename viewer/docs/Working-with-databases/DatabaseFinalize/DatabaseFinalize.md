# DatabaseFinalize


Removes a request created in [DatabasePrepare(](../DatabasePrepare/DatabasePrepare.md)).

```cpp
void  DatabaseFinalize(
   int  request      // request handle received in DatabasePrepare
   );
```

Parameters

request

[in]  Request handle received in DatabasePrepare().

Return Value

None.

Note

If the handle is invalid, the function sets the ERR\_DATABASE\_INVALID\_HANDLE error. You can check the error using GetLastError().

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseExecute](../DatabaseExecute/DatabaseExecute.md)