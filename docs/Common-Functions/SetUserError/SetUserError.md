# SetUserError

SetUserError

Sets the predefined variable [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) into the value equal to [ERR\_USER\_ERROR\_FIRST](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md#err_user_error_first) + user\_error

|  |
| --- |
| void  SetUserError(     ushort user\_error,   // error number     ); |

Parameters

user\_error

[in] [Error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) number set by a user.

Return Value

No return value.

Note

After an error has been set using the SetUserError(user\_error) function, [GetLastError()](../../Checkup/GetLastError/GetLastError.md) returns value equal to [ERR\_USER\_ERROR\_FIRST](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md#err_user_error_first) + user\_error.

Example:

|  |
| --- |
| void OnStart()    {  //--- set error number 65537=(ERR\_USER\_ERROR\_FIRST +1)     SetUserError(1);  //--- get last error code     Print("GetLastError = ",GetLastError());  /\*      Result     GetLastError = 65537  \*/     } |
