# DatabaseColumnBlob


Gets a field value as an array from the current record.

```cpp
bool  DatabaseColumnBlob(
   int    request,     // request handle received in DatabasePrepare
   int    column,      // field index in the request
   void&  data[]       // the reference to the variable for receiving the value
   );
```

Parameters

request

[in]  Request handle received in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

column

[in]  Field index in the request. Field numbering starts from zero and cannot exceed [DatabaseColumnsCount()](../DatabaseColumnsCount/DatabaseColumnsCount.md) - 1.

data[]

[out]  Reference to the array for writing the field value.

Return Value

Return true if successful, otherwise false. To get the error code, use GetLastError(), the possible responses are:

- ERR\_DATABASE\_INVALID\_HANDLE (5121) – invalid request handle;
- ERR\_DATABASE\_NO\_MORE\_DATA (5126)  – 'column' index exceeds DatabaseColumnsCount() -1.

Note

The value can be obtained only if at least one [DatabaseRead()](../DatabaseRead/DatabaseRead.md) call has been preliminarily made for 'request'.

To read the value from the next record, call [DatabaseRead()](../DatabaseRead/DatabaseRead.md) preliminarily.

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseColumnSize](../DatabaseColumnSize/DatabaseColumnSize.md), [DatabaseColumnsCount](../DatabaseColumnsCount/DatabaseColumnsCount.md), [DatabaseColumnType](../DatabaseColumnType/DatabaseColumnType.md), [DatabaseColumnName](../DatabaseColumnName/DatabaseColumnName.md)