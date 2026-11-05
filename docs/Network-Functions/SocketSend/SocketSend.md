# SocketSend

SocketSend

Write data to a socket.

|  |
| --- |
| int  SocketSend(     int           socket,               // socket     const uchar&  buffer[],             // data buffer     uint          buffer\_len            // buffer size     ); |

Parameters

socket

[in]  Socket handle returned by the [SocketCreate](../SocketCreate/SocketCreate.md) function. When an incorrect handle is passed, the error 5270 (ERR\_NETSOCKET\_INVALIDHANDLE) is written to [\_LastError](../../Predefined-Variables/_LastError/_LastError.md).

buffer

[in]  Reference to the [uchar](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type array with the data to be sent to the socket.

buffer\_len

[in]  'buffer' array size.

Return Value

If successful, return the number of bytes written to a socket. In case of an error, -1 is returned.

Note

If an error occurs on a system socket when executing the function, connection established via [SocketConnect](../SocketConnect/SocketConnect.md) is discontinued.

In case of a data writing error, the error 5273 (ERR\_NETSOCKET\_IO\_ERROR) is written to [\_LastError](../../Predefined-Variables/_LastError/_LastError.md).

The function can be called only from Expert Advisors and scripts, as they run in their own execution threads. If calling from an indicator, [GetLastError()](../../Checkup/GetLastError/GetLastError.md) returns the error 4014 – "Function is not allowed for call".

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                SocketExample.mq5 |  //|                        Copyright 2018, MetaQuotes Software Corp. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright   "Copyright 2000-2024, MetaQuotes Ltd."  #property link        "https://www.mql5.com"  #property version     "1.00"  #property description "Add Address to the list of allowed ones in the terminal settings to let the example work"  #property script\_show\_inputs     input string Address="www.mql5.com";  input int    Port   =80;  bool         ExtTLS =false;  //+------------------------------------------------------------------+  //| Send command to the server                                       |  //+------------------------------------------------------------------+  bool HTTPSend(int socket,string request)    {     char req[];     int  len=StringToCharArray(request,req)-1;     if(len<0)        return(false);  //--- if secure TLS connection is used via the port 443     if(ExtTLS)        return(SocketTlsSend(socket,req,len)==len);  //--- if standard TCP connection is used     return(SocketSend(socket,req,len)==len);    }  //+------------------------------------------------------------------+  //| Read server response                                             |  //+------------------------------------------------------------------+  bool HTTPRecv(int socket,uint timeout)    {     char   rsp[];     string result;     uint   timeout\_check=GetTickCount()+timeout;  //--- read data from sockets till they are still present but not longer than timeout     do       {        uint len=SocketIsReadable(socket);        if(len)          {           int rsp\_len;           //--- various reading commands depending on whether the connection is secure or not           if(ExtTLS)              rsp\_len=SocketTlsRead(socket,rsp,len);           else              rsp\_len=SocketRead(socket,rsp,len,timeout);           //--- analyze the response           if(rsp\_len>0)             {              result+=CharArrayToString(rsp,0,rsp\_len);              //--- print only the response header              int header\_end=StringFind(result,"\r\n\r\n");              if(header\_end>0)                {                 Print("HTTP answer header received:");                 Print(StringSubstr(result,0,header\_end));                 return(true);                }             }          }       }     while(GetTickCount()<timeout\_check && !IsStopped());     return(false);    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     int socket=SocketCreate();  //--- check the handle     if(socket!=INVALID\_HANDLE)       {        //--- connect if all is well        if(SocketConnect(socket,Address,Port,1000))          {           Print("Established connection to ",Address,":",Port);              string   subject,issuer,serial,thumbprint;           datetime expiration;           //--- if connection is secured by the certificate, display its data           if(SocketTlsCertificate(socket,subject,issuer,serial,thumbprint,expiration))             {              Print("TLS certificate:");              Print("   Owner:  ",subject);              Print("   Issuer:  ",issuer);              Print("   Number:     ",serial);              Print("   Print: ",thumbprint);              Print("   Expiration: ",expiration);              ExtTLS=true;             }           //--- send GET request to the server           if(HTTPSend(socket,"GET / HTTP/1.1\r\nHost: www.mql5.com\r\nUser-Agent: MT5\r\n\r\n"))             {              Print("GET request sent");              //--- read the response              if(!HTTPRecv(socket,1000))                 Print("Failed to get a response, error ",GetLastError());             }           else              Print("Failed to send GET request, error ",GetLastError());          }        else          {           Print("Connection to ",Address,":",Port," failed, error ",GetLastError());          }        //--- close a socket after using        SocketClose(socket);       }     else        Print("Failed to create a socket, error ",GetLastError());    }  //+------------------------------------------------------------------+ |

See also

[SocketTimeouts](../SocketTimeouts/SocketTimeouts.md), [MathSwap](../../Math-Functions/MathSwap/MathSwap.md), [StringToCharArray](../../Conversion-Functions/StringToCharArray/StringToCharArray.md)
