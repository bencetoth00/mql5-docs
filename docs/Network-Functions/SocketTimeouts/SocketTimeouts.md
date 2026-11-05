# SocketTimeouts

SocketTimeouts

Set timeouts for receiving and sending data for a socket system object.

|  |
| --- |
| bool  SocketTimeouts(     int           socket,               // socket     uint          timeout\_send\_ms,      // data sending timeout     uint          timeout\_receive\_ms    // data obtaining timeout     ); |

Parameters

socket

[in]  Socket handle returned by the [SocketCreate](../SocketCreate/SocketCreate.md) function. When an incorrect handle is passed, the error 5270 (ERR\_NETSOCKET\_INVALIDHANDLE) is written to [\_LastError](../../Predefined-Variables/_LastError/_LastError.md).

timeout\_send\_ms

[in]  Data sending timeout in milliseconds.

timeout\_receive\_ms

[in]  Data obtaining timeout in milliseconds.

Return Value

Returns true if successful, otherwise false.

Note

Do not confuse system object timeouts with the ones set when reading data via [SocketRead](../SocketRead/SocketRead.md). SocketTimeout sets timeouts once for a socket object in the operating system. These timeouts are to be applied to all functions for reading and sending data via this socket. In SocketRead, the timeout is set for a certain data reading operation.

The function can be called only from Expert Advisors and scripts, as they run in their own execution threads. If calling from an indicator, [GetLastError()](../../Checkup/GetLastError/GetLastError.md) returns the error 4014 – "Function is not allowed for call".

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                               SocketTimeouts.mq5 |  //|                                  Copyright 2024, MetaQuotes Ltd. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2024, MetaQuotes Ltd."  #property link      "https://www.mql5.com  #property version     "1.00"     #define   TIMEOUT\_SEND     5000  #define   TIMEOUT\_RECEIVE  5000  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart(void)    {  //--- create a socket and get its handle     int socket=SocketCreate();        if(socket==INVALID\_HANDLE)       {        Print("SocketCreate() failed. Error ",GetLastError());        return;       }  //--- set timeouts for receiving and sending data for a socket system object     if(SocketTimeouts(socket,TIMEOUT\_SEND,TIMEOUT\_RECEIVE))        PrintFormat("timeouts were successfully set",socket,TIMEOUT\_SEND,TIMEOUT\_RECEIVE);     else        PrintFormat("SocketTimeouts(%d, %I64d, %I64d) failed. Error %d",socket,TIMEOUT\_SEND,TIMEOUT\_RECEIVE,GetLastError());  //--- close socket     SocketClose(socket);    } |
