# Network Functions

Network functions

MQL5 programs can exchange data with remote servers, as well as send push notifications, emails and data via FTP.

- The [Socket\*](SocketCreate/SocketCreate.md) group of functions allows establishing a TCP connection (including a secure TLS) with a remote host via system sockets. The operation principle is simple: [create a socket](SocketCreate/SocketCreate.md), [connect to the server](SocketConnect/SocketConnect.md) and start [reading](SocketRead/SocketRead.md) and [writing](SocketSend/SocketSend.md) data.
- The [WebRequest](WebRequest/WebRequest.md) function is designed to work with web resources and allows sending HTTP requests (including GET and POST) easily.
- [SendFTP](SendFTP/SendFTP.md), [SendMail](SendMail/SendMail.md) and [SendNotification](SendNotification/SendNotification.md) are more simple functions for sending files, emails and mobile notifications.

For end-user security, the list of allowed IP addresses is implemented on the client terminal side. The list contains IP addresses the MQL5 program is allowed to connect to via the Socket\* and WebRequest functions. For example, if the program needs to connect to https://www.someserver.com, this address should be explicitly indicated by a terminal user in the list. An address cannot be added programmatically.

![Adding the address to the list](../assets/allow_net_request.png "Adding the address to the list")

Add an explicit message to the MQL5 program to notify a user of the need for additional configuration. You can do that via [#property description](../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md), [Alert](../Common-Functions/Alert/Alert.md) or [Print](../Common-Functions/Print/Print.md).

| Function | Action |
| --- | --- |
| [SocketCreate](SocketCreate/SocketCreate.md) | Create a socket with specified flags and return its handle |
| [SocketClose](SocketClose/SocketClose.md) | Close a socket |
| [SocketConnect](SocketConnect/SocketConnect.md) | Connect to the server with timeout control |
| [SocketIsConnected](SocketIsConnected/SocketIsConnected.md) | Checks if the socket is currently connected |
| [SocketIsReadable](SocketIsReadable/SocketIsReadable.md) | Get a number of bytes that can be read from a socket |
| [SocketIsWritable](SocketIsWritable/SocketIsWritable.md) | Check whether data can be written to a socket at the current time |
| [SocketTimeouts](SocketTimeouts/SocketTimeouts.md) | Set timeouts for receiving and sending data for a socket system object |
| [SocketRead](SocketRead/SocketRead.md) | Read data from a socket |
| [SocketSend](SocketSend/SocketSend.md) | Write data to a socket |
| [SocketTlsHandshake](SocketTlsHandshake/SocketTlsHandshake.md) | Initiate secure TLS (SSL) connection to a specified host via TLS Handshake protocol |
| [SocketTlsCertificate](SocketTlsCertificate/SocketTlsCertificate.md) | Get data on the certificate used to secure network connection |
| [SocketTlsRead](SocketTlsRead/SocketTlsRead.md) | Read data from secure TLS connection |
| [SocketTlsReadAvailable](SocketTlsReadAvailable/SocketTlsReadAvailable.md) | Read all available data from secure TLS connection |
| [SocketTlsSend](SocketTlsSend/SocketTlsSend.md) | Send data via secure TLS connection |
| [WebRequest](WebRequest/WebRequest.md) | Send an HTTP request to a specified server |
| [SendFTP](SendFTP/SendFTP.md) | Send a file to an address specified on the FTP tab |
| [SendMail](SendMail/SendMail.md) | Send an email to an address specified in the Email tab of the options window |
| [SendNotification](SendNotification/SendNotification.md) | Send push notifications to mobile terminals whose MetaQuotes IDs are specified in the Notifications tab |
