# Predefined Variables

The predefined Variables

For each executable mql5-program a set of predefined variables is supported, which reflect the state of the current price chart by the moment a mql5-program (Expert Advisor, script or custom indicator) is started.

Values of predefined variables are set by the client terminal before a mql5-program is started. Predefined variables are constant and cannot be changed from a mql5-program. As exception, there is a special variable \_LastError, which can be reset to 0 by the [ResetLastError](../Common-Functions/ResetLastError/ResetLastError.md) function.

| Variable | Value |
| --- | --- |
| [\_AppliedTo](_AppliedTo/_AppliedTo.md) | The \_AppliedTo variable allows finding out the type of data, used for indicator calculation |
| [\_Digits](_Digits/_Digits.md) | Number of decimal places |
| [\_Point](_Point/_Point.md) | Size of the current symbol point in the quote currency |
| [\_LastError](_LastError/_LastError.md) | The last error code |
| [\_Period](_Period/_Period.md) | Timeframe of the current chart |
| [\_RandomSeed](_RandomSeed/_RandomSeed.md) | Current status of the generator of pseudo-random integers |
| [\_StopFlag](_StopFlag/_StopFlag.md) | Program stop flag |
| [\_Symbol](_Symbol/_Symbol.md) | Symbol name of the current chart |
| [\_UninitReason](_UninitReason/_UninitReason.md) | Uninitialization reason code |
| [\_IsX64](_IsX64/_IsX64.md) | The \_IsX64 variable allows finding out the bit version of the terminal, in which an MQL5 application is running |

Predefined variables cannot be defined in a library. A library uses such variables that are defined in program from which this library is called.
