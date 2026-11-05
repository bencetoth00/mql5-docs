# SetReturnError

SetReturnError

Sets the code that returns the terminal process when completing the operation.

|  |
| --- |
| void  SetReturnError(     int ret\_code      // client terminal completion code     ); |

Parameters

ret\_code

[in]  The code to be returned by the client terminal process when completing the operation.

Return Value

No return value.

Note

Setting the specified ret\_code return code using the SetReturnError() function is useful for analyzing reasons of the programmatic operation completion when [launching the terminal via the command line](https://www.metatrader5.com/en/terminal/help/start_advanced/start#command_line).

Unlike [TerminalClose()](../TerminalClose/TerminalClose.md), the SetReturnError() function does not complete the terminal operation. Instead, it only sets the code that returns the terminal process upon its completion.

If the SetReturnError() function is called multiple times and/or from different MQL5 programs, the terminal returns the last set return code.

The set code is returned upon the terminal process completion except for the following cases:

- a [critical error](../../MQL5-programs/Runtime-Errors/Runtime-Errors.md) has occurred during execution;
- the TerminalClose(int ret\_code) function issuing the terminal operation completion command with a specified code has been called.

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     matrix matrix\_a =       {          {-3.474589, 1.106384, -9.091977,-3.925227 },          {-5.522139, 2.366887,-15.162351,-6.357512 },          { 8.394926,-2.960067, 22.292115, 9.524129 },          { 7.803242,-2.080287, 19.217706, 8.186645 }       };     matrix matrix\_l(4,4);     matrix matrix\_u(4,4);     //--- LU decomposition     matrix\_a.LU(matrix\_l,matrix\_u);     //--- check if A = L \* U     matrix matrix\_lu=matrix\_l.MatMul(matrix\_u);     int    compare\_errors=(int)matrix\_a.Compare(matrix\_lu,1e-29);     Print("MatrixCompare errors=",compare\_errors);     //--- upon completion, the client terminal will return the number of errors in comparing two matrices     SetReturnError(compare\_errors);    } |

 

See also

[Program Running](../../MQL5-programs/Program-Running/Program-Running.md), [Runtime Errors](../../MQL5-programs/Runtime-Errors/Runtime-Errors.md), [Uninitialization Reason Codes](../../Constants,-Enumerations-and-Structures/Named-Constants/Uninitialization-Reason-Codes/Uninitialization-Reason-Codes.md), [TerminalClose](../TerminalClose/TerminalClose.md)
