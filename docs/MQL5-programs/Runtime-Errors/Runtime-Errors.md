# Runtime Errors

Runtime Errors

The executing subsystem of the client terminal has an opportunity to save the [error code](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) in case it occurs during a MQL5 program run. There is a predefined variable [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) for each executable MQL5 program.

Before starting the [OnInit](../../Event-Handling/OnInit/OnInit.md) function, the \_LastError variable is reset. In case an erroneous situation occurs during calculations or in the process of internal function calls, the \_LastError variable accepts a corresponding error code. The value stored in this variable can be obtained using the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

There are several critical errors in case of which a program is terminated immediately:

- division by zero
- going beyond array boundary
- using an incorrect [object pointer](../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md)
