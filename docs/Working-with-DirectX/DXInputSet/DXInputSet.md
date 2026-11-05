# DXInputSet

DXInputSet

Sets shader inputs.

|  |
| --- |
| bool  DXInputSet(     int          input,      // graphic context handle     const void&  data        // data for setting       ); |

Parameters

input

[in]  Handle of inputs for a shader obtained in [DXInputCreate()](../DXInputCreate/DXInputCreate.md).

data

[in]  Data for setting shader inputs.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.
