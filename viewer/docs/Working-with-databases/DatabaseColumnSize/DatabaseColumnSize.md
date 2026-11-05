# DatabaseColumnSize


Gets a field size in bytes.

```cpp
int  DatabaseColumnSize(
   int  request,     // request handle received in DatabasePrepare
   int  column       // field index in the request
   );
```

Parameters

request

[in]  Request handle received in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

column

[in]  Field index in the request. Field numbering starts from zero and cannot exceed [DatabaseColumnsCount()](../DatabaseColumnsCount/DatabaseColumnsCount.md) - 1.

Return Value

If successful, the field size in bytes is returned, otherwise -1. To get the error code, use GetLastError(), the possible responses are:

- ERR\_DATABASE\_INVALID\_HANDLE (5121) – invalid request handle;
- ERR\_DATABASE\_NO\_MORE\_DATA (5126)  – 'column' index exceeds DatabaseColumnsCount() -1.

Note

The value can be obtained only if at least one [DatabaseRead()](../DatabaseRead/DatabaseRead.md) call has been preliminarily made for 'request'.

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseColumnBlob](../DatabaseColumnBlob/DatabaseColumnBlob.md), [DatabaseColumnsCount](../DatabaseColumnsCount/DatabaseColumnsCount.md), [DatabaseColumnName](../DatabaseColumnName/DatabaseColumnName.md), [DatabaseColumnType](../DatabaseColumnType/DatabaseColumnType.md)