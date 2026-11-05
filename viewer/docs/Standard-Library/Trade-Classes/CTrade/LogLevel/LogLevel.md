# LogLevel


Sets logging level for messages.

```cpp
void  LogLevel(
   ENUM_LOG_LEVELS  log_level      // level
   )
```

Parameters

log\_level

[in]  New logging level.

Return Value

None.

Note

LOG\_LEVEL\_NO and less disables displaying any messages (set up automatically in the optimization mode). LOG\_LEVEL\_ERRORS enables displaying only error messages (value by default). LOG\_LEVEL\_ALL and greater enables displaying any messages (set up automatically in the test mode).

ENUM\_LOG\_LEVELS

| Identifier | Description | Value |
| --- | --- | --- |
| LOG\_LEVEL\_NO | Displaying messages disabled | 0 |
| LOG\_LEVEL\_ERRORS | Only error messages are displayed | 1 |
| LOG\_LEVEL\_ALL | All messages are displayed | 2 |