# Runtime Errors

Runtime Errors

[GetLastError()](../../../Checkup/GetLastError/GetLastError.md) is the function that returns the last error code that is stored in the predefined variable [\_LastError](../../../Predefined-Variables/_LastError/_LastError.md). This value can be reset to zero by the [ResetLastError()](../../../Common-Functions/ResetLastError/ResetLastError.md) function.

| Constant | Code | Description |
| --- | --- | --- |
| ERR\_SUCCESS | 0 | The operation completed successfully |
| ERR\_INTERNAL\_ERROR | 4001 | Unexpected internal error |
| ERR\_WRONG\_INTERNAL\_PARAMETER | 4002 | Wrong parameter in the inner call of the client terminal function |
| ERR\_INVALID\_PARAMETER | 4003 | Wrong parameter when calling the system function |
| ERR\_NOT\_ENOUGH\_MEMORY | 4004 | Not enough memory to perform the system function |
| ERR\_STRUCT\_WITHOBJECTS\_ORCLASS | 4005 | The structure contains objects of strings and/or dynamic arrays and/or structure of such objects and/or classes |
| ERR\_INVALID\_ARRAY | 4006 | Array of a wrong type, wrong size, or a damaged object of a dynamic array |
| ERR\_ARRAY\_RESIZE\_ERROR | 4007 | Not enough memory for the relocation of an array, or an attempt to change the size of a static array |
| ERR\_STRING\_RESIZE\_ERROR | 4008 | Not enough memory for the relocation of string |
| ERR\_NOTINITIALIZED\_STRING | 4009 | Not initialized string |
| ERR\_INVALID\_DATETIME | 4010 | Invalid date and/or time |
| ERR\_ARRAY\_BAD\_SIZE | 4011 | Total amount of elements in the array cannot exceed 2147483647 |
| ERR\_INVALID\_POINTER | 4012 | Wrong pointer |
| ERR\_INVALID\_POINTER\_TYPE | 4013 | Wrong type of pointer |
| ERR\_FUNCTION\_NOT\_ALLOWED | 4014 | Function is not allowed for call |
| ERR\_RESOURCE\_NAME\_DUPLICATED | 4015 | The names of the [dynamic](../../../Common-Functions/ResourceCreate/ResourceCreate.md) and the [static](../../../MQL5-programs/Resources/Resources.md) resource match |
| ERR\_RESOURCE\_NOT\_FOUND | 4016 | Resource with this name has not been found in EX5 |
| ERR\_RESOURCE\_UNSUPPORTED\_TYPE | 4017 | Unsupported resource type or its size exceeds 16 Mb |
| ERR\_RESOURCE\_NAME\_IS\_TOO\_LONG | 4018 | The resource name exceeds 63 characters |
| ERR\_MATH\_OVERFLOW | 4019 | Overflow occurred when calculating math function |
| ERR\_SLEEP\_ERROR | 4020 | Out of test end date after calling Sleep() |
| ERR\_PROGRAM\_STOPPED | 4022 | Test forcibly stopped from the outside. For example, optimization interrupted, visual testing window closed or testing agent stopped |
| ERR\_INVALID\_TYPE | 4023 | Invalid type |
| ERR\_INVALID\_HANDLE | 4024 | Invalid handle |
| ERR\_TOO\_MANY\_OBJECTS | 4025 | Object pool filled out |
| Charts |  |  |
| ERR\_CHART\_WRONG\_ID | 4101 | Wrong chart ID |
| ERR\_CHART\_NO\_REPLY | 4102 | Chart does not respond |
| ERR\_CHART\_NOT\_FOUND | 4103 | Chart not found |
| ERR\_CHART\_NO\_EXPERT | 4104 | No Expert Advisor in the chart that could handle the event |
| ERR\_CHART\_CANNOT\_OPEN | 4105 | Chart opening error |
| ERR\_CHART\_CANNOT\_CHANGE | 4106 | Failed to change chart symbol and period |
| ERR\_CHART\_WRONG\_PARAMETER | 4107 | Error value of the parameter for the [function of working with charts](../../../Chart-Operations/Chart-Operations.md) |
| ERR\_CHART\_CANNOT\_CREATE\_TIMER | 4108 | Failed to create timer |
| ERR\_CHART\_WRONG\_PROPERTY | 4109 | Wrong chart property ID |
| ERR\_CHART\_SCREENSHOT\_FAILED | 4110 | Error creating screenshots |
| ERR\_CHART\_NAVIGATE\_FAILED | 4111 | Error navigating through chart |
| ERR\_CHART\_TEMPLATE\_FAILED | 4112 | Error applying template |
| ERR\_CHART\_WINDOW\_NOT\_FOUND | 4113 | Subwindow containing the indicator was not found |
| ERR\_CHART\_INDICATOR\_CANNOT\_ADD | 4114 | Error adding an indicator to chart |
| ERR\_CHART\_INDICATOR\_CANNOT\_DEL | 4115 | Error deleting an indicator from the chart |
| ERR\_CHART\_INDICATOR\_NOT\_FOUND | 4116 | Indicator not found on the specified chart |
| Graphical Objects |  |  |
| ERR\_OBJECT\_ERROR | 4201 | Error working with a graphical object |
| ERR\_OBJECT\_NOT\_FOUND | 4202 | Graphical object was not found |
| ERR\_OBJECT\_WRONG\_PROPERTY | 4203 | Wrong ID of a graphical object property |
| ERR\_OBJECT\_GETDATE\_FAILED | 4204 | Unable to get date corresponding to the value |
| ERR\_OBJECT\_GETVALUE\_FAILED | 4205 | Unable to get value corresponding to the date |
| MarketInfo |  |  |
| ERR\_MARKET\_UNKNOWN\_SYMBOL | 4301 | Unknown symbol |
| ERR\_MARKET\_NOT\_SELECTED | 4302 | Symbol is not selected in MarketWatch |
| ERR\_MARKET\_WRONG\_PROPERTY | 4303 | Wrong identifier of a symbol property |
| ERR\_MARKET\_LASTTIME\_UNKNOWN | 4304 | Time of the last tick is not known (no ticks) |
| ERR\_MARKET\_SELECT\_ERROR | 4305 | Error adding or deleting a symbol in MarketWatch |
| ERR\_MARKET\_SELECT\_LIMIT | 4306 | Exceeded the limit of selected symbols in MarketWatch |
| ERR\_MARKET\_SESSION\_INDEX | 4307 | Wrong session ID when calling the SymbolInfoSessionQuote/SymbolInfoSessionTrade function |
| History Access |  |  |
| ERR\_HISTORY\_NOT\_FOUND | 4401 | Requested history not found |
| ERR\_HISTORY\_WRONG\_PROPERTY | 4402 | Wrong ID of the history property |
| ERR\_HISTORY\_TIMEOUT | 4403 | Exceeded history request timeout |
| ERR\_HISTORY\_BARS\_LIMIT | 4404 | Number of requested bars limited by terminal settings |
| ERR\_HISTORY\_LOAD\_ERRORS | 4405 | Multiple errors when loading history |
| ERR\_HISTORY\_SMALL\_BUFFER | 4407 | Receiving array is too small to store all requested data |
| Global\_Variables |  |  |
| ERR\_GLOBALVARIABLE\_NOT\_FOUND | 4501 | Global variable of the client terminal is not found |
| ERR\_GLOBALVARIABLE\_EXISTS | 4502 | Global variable of the client terminal with the same name already exists |
| ERR\_GLOBALVARIABLE\_NOT\_MODIFIED | 4503 | Global variables were not modified |
| ERR\_GLOBALVARIABLE\_CANNOTREAD | 4504 | Cannot read file with global variable values |
| ERR\_GLOBALVARIABLE\_CANNOTWRITE | 4505 | Cannot write file with global variable values |
| ERR\_MAIL\_SEND\_FAILED | 4510 | Email sending failed |
| ERR\_PLAY\_SOUND\_FAILED | 4511 | Sound playing failed |
| ERR\_MQL5\_WRONG\_PROPERTY | 4512 | Wrong identifier of the program property |
| ERR\_TERMINAL\_WRONG\_PROPERTY | 4513 | Wrong identifier of the terminal property |
| ERR\_FTP\_SEND\_FAILED | 4514 | File sending via ftp failed |
| ERR\_NOTIFICATION\_SEND\_FAILED | 4515 | Failed to send a [notification](../../../Network-Functions/SendNotification/SendNotification.md) |
| ERR\_NOTIFICATION\_WRONG\_PARAMETER | 4516 | Invalid parameter for sending a notification – an empty string or [NULL](../../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) has been passed to the [SendNotification()](../../../Network-Functions/SendNotification/SendNotification.md) function |
| ERR\_NOTIFICATION\_WRONG\_SETTINGS | 4517 | Wrong settings of notifications in the terminal (ID is not specified or permission is not set) |
| ERR\_NOTIFICATION\_TOO\_FREQUENT | 4518 | Too frequent sending of notifications |
| ERR\_FTP\_NOSERVER | 4519 | FTP server is not specified |
| ERR\_FTP\_NOLOGIN | 4520 | FTP login is not specified |
| ERR\_FTP\_FILE\_ERROR | 4521 | File not found in the MQL5\Files directory to send on FTP server |
| ERR\_FTP\_CONNECT\_FAILED | 4522 | FTP connection failed |
| ERR\_FTP\_CHANGEDIR | 4523 | FTP path not found on server |
| Custom Indicator Buffers |  |  |
| ERR\_BUFFERS\_NO\_MEMORY | 4601 | Not enough memory for the distribution of indicator buffers |
| ERR\_BUFFERS\_WRONG\_INDEX | 4602 | Wrong indicator buffer index |
| Custom Indicator Properties |  |  |
| ERR\_CUSTOM\_WRONG\_PROPERTY | 4603 | Wrong ID of the custom indicator property |
| Account |  |  |
| ERR\_ACCOUNT\_WRONG\_PROPERTY | 4701 | Wrong account property ID |
| ERR\_TRADE\_WRONG\_PROPERTY | 4751 | Wrong trade property ID |
| ERR\_TRADE\_DISABLED | 4752 | Trading by Expert Advisors prohibited |
| ERR\_TRADE\_POSITION\_NOT\_FOUND | 4753 | Position not found |
| ERR\_TRADE\_ORDER\_NOT\_FOUND | 4754 | Order not found |
| ERR\_TRADE\_DEAL\_NOT\_FOUND | 4755 | Deal not found |
| ERR\_TRADE\_SEND\_FAILED | 4756 | Trade request sending failed |
| ERR\_TRADE\_CALC\_FAILED | 4758 | Failed to calculate profit or margin |
| Indicators |  |  |
| ERR\_INDICATOR\_UNKNOWN\_SYMBOL | 4801 | Unknown symbol |
| ERR\_INDICATOR\_CANNOT\_CREATE | 4802 | Indicator cannot be created |
| ERR\_INDICATOR\_NO\_MEMORY | 4803 | Not enough memory to add the indicator |
| ERR\_INDICATOR\_CANNOT\_APPLY | 4804 | The indicator cannot be applied to another indicator |
| ERR\_INDICATOR\_CANNOT\_ADD | 4805 | Error applying an indicator to chart |
| ERR\_INDICATOR\_DATA\_NOT\_FOUND | 4806 | Requested data not found |
| ERR\_INDICATOR\_WRONG\_HANDLE | 4807 | Wrong indicator handle |
| ERR\_INDICATOR\_WRONG\_PARAMETERS | 4808 | Wrong number of parameters when creating an indicator |
| ERR\_INDICATOR\_PARAMETERS\_MISSING | 4809 | No parameters when creating an indicator |
| ERR\_INDICATOR\_CUSTOM\_NAME | 4810 | The first parameter in the array must be the name of the custom indicator |
| ERR\_INDICATOR\_PARAMETER\_TYPE | 4811 | Invalid parameter type in the array when creating an indicator |
| ERR\_INDICATOR\_WRONG\_INDEX | 4812 | Wrong index of the requested indicator buffer |
| Depth of Market |  |  |
| ERR\_BOOKS\_CANNOT\_ADD | 4901 | Depth Of Market can not be added |
| ERR\_BOOKS\_CANNOT\_DELETE | 4902 | Depth Of Market can not be removed |
| ERR\_BOOKS\_CANNOT\_GET | 4903 | The data from Depth Of Market can not be obtained |
| ERR\_BOOKS\_CANNOT\_SUBSCRIBE | 4904 | Error in subscribing to receive new data from Depth Of Market |
| File Operations |  |  |
| ERR\_TOO\_MANY\_FILES | 5001 | More than 64 files cannot be opened at the same time |
| ERR\_WRONG\_FILENAME | 5002 | Invalid file name |
| ERR\_TOO\_LONG\_FILENAME | 5003 | Too long file name |
| ERR\_CANNOT\_OPEN\_FILE | 5004 | File opening error |
| ERR\_FILE\_CACHEBUFFER\_ERROR | 5005 | Not enough memory for cache to read |
| ERR\_CANNOT\_DELETE\_FILE | 5006 | File deleting error |
| ERR\_INVALID\_FILEHANDLE | 5007 | A file with this handle was closed, or was not opening at all |
| ERR\_WRONG\_FILEHANDLE | 5008 | Wrong file handle |
| ERR\_FILE\_NOTTOWRITE | 5009 | The file must be opened for writing |
| ERR\_FILE\_NOTTOREAD | 5010 | The file must be opened for reading |
| ERR\_FILE\_NOTBIN | 5011 | The file must be opened as a binary one |
| ERR\_FILE\_NOTTXT | 5012 | The file must be opened as a text |
| ERR\_FILE\_NOTTXTORCSV | 5013 | The file must be opened as a text or CSV |
| ERR\_FILE\_NOTCSV | 5014 | The file must be opened as CSV |
| ERR\_FILE\_READERROR | 5015 | File reading error |
| ERR\_FILE\_BINSTRINGSIZE | 5016 | String size must be specified, because the file is opened as binary |
| ERR\_INCOMPATIBLE\_FILE | 5017 | A text file must be for string arrays, for other arrays - binary |
| ERR\_FILE\_IS\_DIRECTORY | 5018 | This is not a file, this is a directory |
| ERR\_FILE\_NOT\_EXIST | 5019 | File does not exist |
| ERR\_FILE\_CANNOT\_REWRITE | 5020 | File can not be rewritten |
| ERR\_WRONG\_DIRECTORYNAME | 5021 | Wrong directory name |
| ERR\_DIRECTORY\_NOT\_EXIST | 5022 | Directory does not exist |
| ERR\_FILE\_ISNOT\_DIRECTORY | 5023 | This is a file, not a directory |
| ERR\_CANNOT\_DELETE\_DIRECTORY | 5024 | The directory cannot be removed |
| ERR\_CANNOT\_CLEAN\_DIRECTORY | 5025 | Failed to clear the directory (probably one or more files are blocked and removal operation failed) |
| ERR\_FILE\_WRITEERROR | 5026 | Failed to write a resource to a file |
| ERR\_FILE\_ENDOFFILE | 5027 | Unable to read the next piece of data from a CSV file (FileReadString, FileReadNumber, FileReadDatetime, FileReadBool), since the end of file is reached |
| String Casting |  |  |
| ERR\_NO\_STRING\_DATE | 5030 | No date in the string |
| ERR\_WRONG\_STRING\_DATE | 5031 | Wrong date in the string |
| ERR\_WRONG\_STRING\_TIME | 5032 | Wrong time in the string |
| ERR\_STRING\_TIME\_ERROR | 5033 | Error converting string to date |
| ERR\_STRING\_OUT\_OF\_MEMORY | 5034 | Not enough memory for the string |
| ERR\_STRING\_SMALL\_LEN | 5035 | The string length is less than expected |
| ERR\_STRING\_TOO\_BIGNUMBER | 5036 | Too large number, more than ULONG\_MAX |
| ERR\_WRONG\_FORMATSTRING | 5037 | Invalid format string |
| ERR\_TOO\_MANY\_FORMATTERS | 5038 | Amount of format specifiers more than the parameters |
| ERR\_TOO\_MANY\_PARAMETERS | 5039 | Amount of parameters more than the format specifiers |
| ERR\_WRONG\_STRING\_PARAMETER | 5040 | Damaged parameter of string type |
| ERR\_STRINGPOS\_OUTOFRANGE | 5041 | Position outside the string |
| ERR\_STRING\_ZEROADDED | 5042 | 0 added to the string end, a useless operation |
| ERR\_STRING\_UNKNOWNTYPE | 5043 | Unknown data type when converting to a string |
| ERR\_WRONG\_STRING\_OBJECT | 5044 | Damaged string object |
| Operations with Arrays |  |  |
| ERR\_INCOMPATIBLE\_ARRAYS | 5050 | Copying incompatible arrays. String array can be copied only to a string array, and a numeric array - in numeric array only |
| ERR\_SMALL\_ASSERIES\_ARRAY | 5051 | The receiving array is declared as AS\_SERIES, and it is of insufficient size |
| ERR\_SMALL\_ARRAY | 5052 | Too small array, the starting position is outside the array |
| ERR\_ZEROSIZE\_ARRAY | 5053 | An array of zero length |
| ERR\_NUMBER\_ARRAYS\_ONLY | 5054 | Must be a numeric array |
| ERR\_ONEDIM\_ARRAYS\_ONLY | 5055 | Must be a one-dimensional array |
| ERR\_SERIES\_ARRAY | 5056 | Timeseries cannot be used |
| ERR\_DOUBLE\_ARRAY\_ONLY | 5057 | Must be an array of type double |
| ERR\_FLOAT\_ARRAY\_ONLY | 5058 | Must be an array of type float |
| ERR\_LONG\_ARRAY\_ONLY | 5059 | Must be an array of type long |
| ERR\_INT\_ARRAY\_ONLY | 5060 | Must be an array of type int |
| ERR\_SHORT\_ARRAY\_ONLY | 5061 | Must be an array of type short |
| ERR\_CHAR\_ARRAY\_ONLY | 5062 | Must be an array of type char |
| ERR\_STRING\_ARRAY\_ONLY | 5063 | String array only |
| Operations with OpenCL |  |  |
| ERR\_OPENCL\_NOT\_SUPPORTED | 5100 | [OpenCL functions](../../../Working-with-OpenCL/Working-with-OpenCL.md) are not supported on this computer |
| ERR\_OPENCL\_INTERNAL | 5101 | Internal error occurred when [running OpenCL](../../../Working-with-OpenCL/CLExecute/CLExecute.md) |
| ERR\_OPENCL\_INVALID\_HANDLE | 5102 | Invalid [OpenCL handle](../../../Working-with-OpenCL/CLProgramCreate/CLProgramCreate.md) |
| ERR\_OPENCL\_CONTEXT\_CREATE | 5103 | Error creating the [OpenCL context](../../../Working-with-OpenCL/CLContextCreate/CLContextCreate.md) |
| ERR\_OPENCL\_QUEUE\_CREATE | 5104 | Failed to create a run queue in OpenCL |
| ERR\_OPENCL\_PROGRAM\_CREATE | 5105 | Error occurred when [compiling an OpenCL program](../../../Working-with-OpenCL/CLProgramCreate/CLProgramCreate.md) |
| ERR\_OPENCL\_TOO\_LONG\_KERNEL\_NAME | 5106 | Too long kernel name [(OpenCL kernel)](../../../Working-with-OpenCL/CLKernelCreate/CLKernelCreate.md) |
| ERR\_OPENCL\_KERNEL\_CREATE | 5107 | Error creating an [OpenCL kernel](../../../Working-with-OpenCL/CLKernelCreate/CLKernelCreate.md) |
| ERR\_OPENCL\_SET\_KERNEL\_PARAMETER | 5108 | Error occurred when [setting parameters](../../../Working-with-OpenCL/CLSetKernelArg/CLSetKernelArg.md) for the OpenCL kernel |
| ERR\_OPENCL\_EXECUTE | 5109 | [OpenCL program](../../../Working-with-OpenCL/CLExecute/CLExecute.md) runtime error |
| ERR\_OPENCL\_WRONG\_BUFFER\_SIZE | 5110 | Invalid size of the OpenCL buffer |
| ERR\_OPENCL\_WRONG\_BUFFER\_OFFSET | 5111 | Invalid offset in the OpenCL buffer |
| ERR\_OPENCL\_BUFFER\_CREATE | 5112 | Failed to create an [OpenCL buffer](../../../Working-with-OpenCL/CLBufferCreate/CLBufferCreate.md) |
| ERR\_OPENCL\_TOO\_MANY\_OBJECTS | 5113 | Too many OpenCL objects |
| ERR\_OPENCL\_SELECTDEVICE | 5114 | OpenCL device selection error |
| Working with databases |  |  |
| ERR\_DATABASE\_INTERNAL | 5120 | Internal database error |
| ERR\_DATABASE\_INVALID\_HANDLE | 5121 | Invalid database handle |
| ERR\_DATABASE\_TOO\_MANY\_OBJECTS | 5122 | Exceeded the maximum acceptable number of Database objects |
| ERR\_DATABASE\_CONNECT | 5123 | Database connection error |
| ERR\_DATABASE\_EXECUTE | 5124 | Request execution error |
| ERR\_DATABASE\_PREPARE | 5125 | Request generation error |
| ERR\_DATABASE\_NO\_MORE\_DATA | 5126 | No more data to read |
| ERR\_DATABASE\_STEP | 5127 | Failed to move to the next request entry |
| ERR\_DATABASE\_NOT\_READY | 5128 | Data for reading request results are not ready yet |
| ERR\_DATABASE\_BIND\_PARAMETERS | 5129 | Failed to auto substitute parameters to an SQL request |
| Operations with WebRequest |  |  |
| ERR\_WEBREQUEST\_INVALID\_ADDRESS | 5200 | Invalid URL |
| ERR\_WEBREQUEST\_CONNECT\_FAILED | 5201 | Failed to connect to specified URL |
| ERR\_WEBREQUEST\_TIMEOUT | 5202 | Timeout exceeded |
| ERR\_WEBREQUEST\_REQUEST\_FAILED | 5203 | HTTP request failed |
| Operations with network (sockets) |  |  |
| ERR\_NETSOCKET\_INVALIDHANDLE | 5270 | Invalid socket handle passed to function |
| ERR\_NETSOCKET\_TOO\_MANY\_OPENED | 5271 | Too many open sockets (max 128) |
| ERR\_NETSOCKET\_CANNOT\_CONNECT | 5272 | Failed to connect to remote host |
| ERR\_NETSOCKET\_IO\_ERROR | 5273 | Failed to send/receive data from socket |
| ERR\_NETSOCKET\_HANDSHAKE\_FAILED | 5274 | Failed to establish secure connection (TLS Handshake) |
| ERR\_NETSOCKET\_NO\_CERTIFICATE | 5275 | No data on certificate protecting the connection |
| Custom Symbols |  |  |
| ERR\_NOT\_CUSTOM\_SYMBOL | 5300 | A custom symbol must be specified |
| ERR\_CUSTOM\_SYMBOL\_WRONG\_NAME | 5301 | The name of the custom symbol is invalid. The symbol name can only contain Latin letters without punctuation, spaces or special characters (may only contain ".", "\_", "&" and "#"). It is not recommended to use characters <, >, :, ", /,\, |, ?, \*. |
| ERR\_CUSTOM\_SYMBOL\_NAME\_LONG | 5302 | The name of the custom symbol is too long. The length of the symbol name must not exceed 32 characters including the ending 0 character |
| ERR\_CUSTOM\_SYMBOL\_PATH\_LONG | 5303 | The path of the custom symbol is too long. The path length should not exceed 128 characters including "Custom\\", the symbol name, group separators and the ending 0 |
| ERR\_CUSTOM\_SYMBOL\_EXIST | 5304 | A custom symbol with the same name already exists |
| ERR\_CUSTOM\_SYMBOL\_ERROR | 5305 | Error occurred while creating, deleting or changing the custom symbol |
| ERR\_CUSTOM\_SYMBOL\_SELECTED | 5306 | You are trying to delete a custom symbol selected in Market Watch |
| ERR\_CUSTOM\_SYMBOL\_PROPERTY\_WRONG | 5307 | An invalid custom symbol property |
| ERR\_CUSTOM\_SYMBOL\_PARAMETER\_ERROR | 5308 | A wrong parameter while setting the property of a custom symbol |
| ERR\_CUSTOM\_SYMBOL\_PARAMETER\_LONG | 5309 | A too long string parameter while setting the property of a custom symbol |
| ERR\_CUSTOM\_TICKS\_WRONG\_ORDER | 5310 | [Ticks](../../Data-Structures/Price-Data-Structure/Price-Data-Structure.md) in the array are [not arranged](../../../Custom-Symbols/CustomTicksAdd/CustomTicksAdd.md) in the order of time |
| Economic Calendar |  |  |
| ERR\_CALENDAR\_MORE\_DATA | 5400 | Array size is insufficient for receiving descriptions of all values |
| ERR\_CALENDAR\_TIMEOUT | 5401 | Request time limit exceeded |
| ERR\_CALENDAR\_NO\_DATA | 5402 | Country is not found |
| Working with databases |  |  |
| ERR\_DATABASE\_ERROR | 5601 | Generic error |
| ERR\_DATABASE\_LOGIC | 5602 | SQLite internal logic error |
| ERR\_DATABASE\_PERM | 5603 | Access denied |
| ERR\_DATABASE\_ABORT | 5604 | Callback routine requested abort |
| ERR\_DATABASE\_BUSY | 5605 | Database file locked |
| ERR\_DATABASE\_LOCKED | 5606 | Database table locked |
| ERR\_DATABASE\_NOMEM | 5607 | Insufficient memory for completing operation |
| ERR\_DATABASE\_READONLY | 5608 | Attempt to write to readonly database |
| ERR\_DATABASE\_INTERRUPT | 5609 | Operation terminated by sqlite3\_interrupt() |
| ERR\_DATABASE\_IOERR | 5610 | Disk I/O error |
| ERR\_DATABASE\_CORRUPT | 5611 | Database disk image corrupted |
| ERR\_DATABASE\_NOTFOUND | 5612 | Unknown operation code in sqlite3\_file\_control() |
| ERR\_DATABASE\_FULL | 5613 | Insertion failed because database is full |
| ERR\_DATABASE\_CANTOPEN | 5614 | Unable to open the database file |
| ERR\_DATABASE\_PROTOCOL | 5615 | Database lock protocol error |
| ERR\_DATABASE\_EMPTY | 5616 | Internal use only |
| ERR\_DATABASE\_SCHEMA | 5617 | Database schema changed |
| ERR\_DATABASE\_TOOBIG | 5618 | String or BLOB exceeds size limit |
| ERR\_DATABASE\_CONSTRAINT | 5619 | Abort due to constraint violation |
| ERR\_DATABASE\_MISMATCH | 5620 | Data type mismatch |
| ERR\_DATABASE\_MISUSE | 5621 | Library used incorrectly |
| ERR\_DATABASE\_NOLFS | 5622 | Uses OS features not supported on host |
| ERR\_DATABASE\_AUTH | 5623 | Authorization denied |
| ERR\_DATABASE\_FORMAT | 5624 | Not used |
| ERR\_DATABASE\_RANGE | 5625 | Bind parameter error, incorrect index |
| ERR\_DATABASE\_NOTADB | 5626 | File opened that is not database file |
| Matrix and Vector Methods |  |  |
| ERR\_MATRIX\_INTERNAL | 5700 | Internal error of the matrix/vector executing subsystem |
| ERR\_MATRIX\_NOT\_INITIALIZED | 5701 | Matrix/vector not [initialized](../../../Matrix-and-Vector-Methods/Initialization/Initialization.md) |
| ERR\_MATRIX\_INCONSISTENT | 5702 | Inconsistent size of matrices/vectors in operation |
| ERR\_MATRIX\_INVALID\_SIZE | 5703 | Invalid matrix/vector size |
| ERR\_MATRIX\_INVALID\_TYPE | 5704 | Invalid matrix/vector type |
| ERR\_MATRIX\_FUNC\_NOT\_ALLOWED | 5705 | Function not available for this matrix/vector |
| ERR\_MATRIX\_CONTAINS\_NAN | 5706 | Matrix/vector contains non-numbers (Nan/Inf) |
| ONNX models |  |  |
| ERR\_ONNX\_INTERNAL | 5800 | ONNX internal error |
| ERR\_ONNX\_NOT\_INITIALIZED | 5801 | ONNX Runtime API initialization error |
| ERR\_ONNX\_NOT\_SUPPORTED | 5802 | Property or value not supported by MQL5 |
| ERR\_ONNX\_RUN\_FAILED | 5803 | ONNX runtime API run error |
| ERR\_ONNX\_INVALID\_PARAMETERS\_COUNT | 5804 | Invalid number of parameters passed to OnnxRun |
| ERR\_ONNX\_INVALID\_PARAMETER | 5805 | Invalid parameter value |
| ERR\_ONNX\_INVALID\_PARAMETER\_TYPE | 5806 | Invalid parameter type |
| ERR\_ONNX\_INVALID\_PARAMETER\_SIZE | 5807 | Invalid parameter size |
| ERR\_ONNX\_WRONG\_DIMENSION | 5808 | Tensor dimension not set or invalid |
| User errors |  |  |
| ERR\_USER\_ERROR\_FIRST | 65536 | [User defined](../../../Common-Functions/SetUserError/SetUserError.md) errors start with this code |

See also

[Trade Server Return Codes](../Trade-Server-Return-Codes/Trade-Server-Return-Codes.md)
