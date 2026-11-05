# SignalSubscribe

SignalSubscribe

Subscribes to the trading signal.

|  |
| --- |
| bool  SignalSubscribe(     long     signal\_id     // signal id      ); |

Parameters

signal\_id

[in]  Signal identifier.

Return Value

Returns true if subscription was successful, otherwise returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).
