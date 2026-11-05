# last_error

last\_error

Return data on the last error.

|  |
| --- |
| last\_error() |

Return Value

Return the last error code and description as a tuple.

Note

last\_error() allows obtaining an error code in case of a failed execution of a MetaTrader 5 library function. It is similar to [GetLastError()](../../Checkup/GetLastError/GetLastError.md). However, it applies its own error codes. Possible values:

| Constant | Value | Description |
| --- | --- | --- |
| RES\_S\_OK | 1 | generic success |
| RES\_E\_FAIL | -1 | generic fail |
| RES\_E\_INVALID\_PARAMS | -2 | invalid arguments/parameters |
| RES\_E\_NO\_MEMORY | -3 | no memory condition |
| RES\_E\_NOT\_FOUND | -4 | no history |
| RES\_E\_INVALID\_VERSION | -5 | invalid version |
| RES\_E\_AUTH\_FAILED | -6 | authorization failed |
| RES\_E\_UNSUPPORTED | -7 | unsupported method |
| RES\_E\_AUTO\_TRADING\_DISABLED | -8 | auto-trading disabled |
| RES\_E\_INTERNAL\_FAIL | -10000 | internal IPC general error |
| RES\_E\_INTERNAL\_FAIL\_SEND | -10001 | internal IPC send failed |
| RES\_E\_INTERNAL\_FAIL\_RECEIVE | -10002 | internal IPC recv failed |
| RES\_E\_INTERNAL\_FAIL\_INIT | -10003 | internal IPC initialization fail |
| RES\_E\_INTERNAL\_FAIL\_CONNECT | -10003 | internal IPC no ipc |
| RES\_E\_INTERNAL\_FAIL\_TIMEOUT | -10005 | internal timeout |

Example:

|  |
| --- |
| import MetaTrader5 as mt5  # display data on the MetaTrader 5 package  print("MetaTrader5 package author: ",mt5.\_\_author\_\_)  print("MetaTrader5 package version: ",mt5.\_\_version\_\_)     # establish connection to the MetaTrader 5 terminal  if not mt5.initialize():      print("initialize() failed, error code =",mt5.last\_error())      quit()     # shut down connection to the MetaTrader 5 terminal  mt5.shutdown() |

See also

[version](../version/version.md), [GetLastError](../../Checkup/GetLastError/GetLastError.md)
