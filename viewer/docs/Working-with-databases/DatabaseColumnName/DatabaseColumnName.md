# DatabaseColumnName


Gets a field name by index.

```cpp
bool  DatabaseColumnName(
   int      request,     // request handle received in DatabasePrepare
   int      column,      // field index in the request
   string&  name         // the reference to the variable for receiving the field name
   );
```

Parameters

request

[in]  Request handle received in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

column

[in]  Field index in the request. Field numbering starts from zero and cannot exceed [DatabaseColumnsCount()](../DatabaseColumnsCount/DatabaseColumnsCount.md) - 1.

name

[out]  Variable for writing the field name.

Return Value

Return true if successful, otherwise false. To get the error code, use GetLastError(), the possible responses are:

- ERR\_DATABASE\_INVALID\_HANDLE (5121) – invalid request handle;
- ERR\_DATABASE\_NO\_MORE\_DATA (5126)  – 'column' index exceeds DatabaseColumnsCount() -1.

Note

The value can be obtained only if at least one [DatabaseRead()](../DatabaseRead/DatabaseRead.md) call has been preliminarily made for 'request'.

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseColumnsCount](../DatabaseColumnsCount/DatabaseColumnsCount.md), [DatabaseColumnType](../DatabaseColumnType/DatabaseColumnType.md)