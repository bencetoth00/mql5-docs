# DatabaseExport

DatabaseExport

Exports a table or an SQL request execution result to a CSV file. The file is created in the UTF-8 encoding.

|  |
| --- |
| long  DatabaseExport(     int           database,           // database handle received in DatabaseOpen     const string  table\_or\_sql,       // a table name or an SQL request     const string  filename,           // a name of a CSV file for data export     uint          flags,              // combination of flags     const string  separator           // data separator in the CSV file     ); |

Parameters

database

[in]  Database handle received in [DatabaseOpen()](../DatabaseOpen/DatabaseOpen.md).

table\_or\_sql

[in]   A name of a table or a text of an SQL request whose results are to be exported to a specified file.

filename

[in]  A file name for data export. The path is set relative to the MQL5\Files folder.

flags

[in]  Combination of flags from the [ENUM\_DATABASE\_EXPORT\_FLAGS](DatabaseExport.md) enumeration.

separator

[in]  Data separator. If NULL is specified, the '\t' tabulation character is used as a separator.  An empty string "" is considered a valid separator but the obtained CSV file cannot be read as a table – it is considered as a set of strings.

 

Return Value

Return the number of exported entries or a negative value in case of an error. To get the error code, use [GetLastError()](../../Checkup/GetLastError/GetLastError.md), the possible responses are:

- ERR\_INTERNAL\_ERROR (4001)                       – critical runtime error;
- ERR\_INVALID\_PARAMETER (4003)                  – path to the database file contains an empty string, or an incompatible combination of flags is set;
- ERR\_NOT\_ENOUGH\_MEMORY (4004)              - insufficient memory;
- ERR\_FUNCTION\_NOT\_ALLOWED(4014)           – specified pipe is not allowed;
- ERR\_PROGRAM\_STOPPED(4022)                    – operation canceled (MQL program stopped);
- ERR\_WRONG\_FILENAME (5002)                     - invalid file name;
- ERR\_TOO\_LONG\_FILENAME (5003)                 - absolute path to the file exceeds the maximum length;
- ERR\_CANNOT\_OPEN\_FILE(5004)                    – unable to open the file for writing;
- ERR\_FILE\_WRITEERROR(5026)                      – unable to write to the file;
- ERR\_DATABASE\_INTERNAL (5120)                 – internal database error;
- ERR\_DATABASE\_INVALID\_HANDLE (5121)      - invalid database handle;
- ERR\_DATABASE\_QUERY\_PREPARE(5125)        – request generation error;
- ERR\_DATABASE\_QUERY\_NOT\_READONLY       – read-only request is allowed.

 

Note

If request results are exported, the SQL request should begin with "SELECT" or "select". In other words, the SQL request cannot alter the database status, otherwise DatabaseExport() fails with an error.

Database string values may contain the conversion character ('\r' or '\r\n' ), as well as the value separator character set in the separator parameter. In this case, be sure to use the DATABASE\_EXPORT\_QUOTED\_STRINGS flag in the 'flags' parameter. If this flag is present, all displayed strings are enclosed in double quotes. If a string contains a double quote, it is replaced by two double quotes.

ENUM\_DATABASE\_EXPORT\_FLAGS

| ID | Description |
| --- | --- |
| DATABASE\_EXPORT\_HEADER | Display field names in the first string |
| DATABASE\_EXPORT\_INDEX | Display string indices |
| DATABASE\_EXPORT\_NO\_BOM | Do not insert BOM mark at the beginning of the file (BOM is inserted by default) |
| DATABASE\_EXPORT\_CRLF | Use CRLF for string break (the default is LF) |
| DATABASE\_EXPORT\_APPEND | Add data to the end of an existing file (by default, the file is overwritten). If the file does not exist, it will be created. |
| DATABASE\_EXPORT\_QUOTED\_STRINGS | Display string values in double quotes. |
| DATABASE\_EXPORT\_COMMON\_FOLDER | A CSV file is created in the common folder of all client terminals \Terminal\Common\File. |

 

Example:

|  |
| --- |
| input int InpRates=100;  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()   {    MqlRates rates[];  //--- remember the start time before receiving bars    ulong start=GetMicrosecondCount();  //--- request the last 100 bars on H1    if(CopyRates(Symbol(), PERIOD\_H1, 1, InpRates, rates)<InpRates)     {      Print("CopyRates() failed,, Error ", GetLastError());      return;     }    else     {      //--- how many bars were received and how much time it took to receive them      PrintFormat("%s: CopyRates received %d bars in %d ms ",                  \_Symbol, ArraySize(rates), (GetMicrosecondCount()-start)/1000);     }  //--- set the file name for storing the database    string filename=\_Symbol+"\_"+EnumToString(PERIOD\_H1)+"\_"+TimeToString(TimeCurrent())+".sqlite";    StringReplace(filename, ":", "-"); // ":" character is not allowed in file names  //--- open/create the database in the common terminal folder    int db=DatabaseOpen(filename, DATABASE\_OPEN\_READWRITE|DATABASE\_OPEN\_CREATE|DATABASE\_OPEN\_COMMON);    if(db==INVALID\_HANDLE)     {      Print("Database: ", filename, " open failed with code ", GetLastError());      return;     }    else      Print("Database: ", filename, " opened successfully");     //--- check if the RATES table exists    if(DatabaseTableExists(db, "RATES"))     {      //--- remove the RATES table      if(!DatabaseExecute(db, "DROP TABLE IF EXISTS RATES"))       {        Print("Failed to drop the RATES table with code ", GetLastError());        DatabaseClose(db);        return;       }     }  //--- create the RATES table    if(!DatabaseExecute(db, "CREATE TABLE RATES("                        "SYMBOL             CHAR(10),"                        "TIME               INT NOT NULL,"                        "OPEN               REAL,"                        "HIGH               REAL,"                        "LOW                REAL,"                        "CLOSE              REAL,"                        "TICK\_VOLUME        INT,"                        "SPREAD             INT,"                        "REAL\_VOLUME        INT);"))     {      Print("DB: ", filename, " create table RATES with code ", GetLastError());      DatabaseClose(db);      return;     }  //--- display the list of all fields in the RATES table    if(DatabasePrint(db, "PRAGMA TABLE\_INFO(RATES)", 0)<0)     {      PrintFormat("DatabasePrint(\"PRAGMA TABLE\_INFO(RATES)\") failed, error code=%d at line %d", GetLastError(), \_\_LINE\_\_);      DatabaseClose(db);      return;     }  //--- create a parametrized request to add bars to the RATES table    string sql="INSERT INTO RATES (SYMBOL,TIME,OPEN,HIGH,LOW,CLOSE,TICK\_VOLUME,SPREAD,REAL\_VOLUME)"               " VALUES (?1,?2,?3,?4,?5,?6,?7,?8,?9)"; // request parameters    int request=DatabasePrepare(db, sql);    if(request==INVALID\_HANDLE)     {      PrintFormat("DatabasePrepare() failed with code=%d", GetLastError());      Print("SQL request: ", sql);      DatabaseClose(db);      return;     }  //--- set the value of the first request parameter    DatabaseBind(request, 0, \_Symbol);  //--- remember the start time before adding bars to the RATES table    start=GetMicrosecondCount();    DatabaseTransactionBegin(db);    int total=ArraySize(rates);    bool request\_error=false;    for(int i=0; i<total; i++)     {      //--- set the values of the remaining parameters before adding the entry      ResetLastError();      if(!DatabaseBind(request, 1, rates[i].time))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      //--- if the previous DatabaseBind() call was successful, set the next parameter      if(!request\_error && !DatabaseBind(request, 2, rates[i].open))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      if(!request\_error && !DatabaseBind(request, 3, rates[i].high))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      if(!request\_error && !DatabaseBind(request, 4, rates[i].low))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      if(!request\_error && !DatabaseBind(request, 5, rates[i].close))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      if(!request\_error && !DatabaseBind(request, 6, rates[i].tick\_volume))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      if(!request\_error && !DatabaseBind(request, 7, rates[i].spread))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }      if(!request\_error && !DatabaseBind(request, 8, rates[i].real\_volume))       {        PrintFormat("DatabaseBind() failed with code=%d", GetLastError());        PrintFormat("Bar #%d line=%d", i+1, \_\_LINE\_\_);        request\_error=true;        break;       }         //--- execute a request for inserting the entry and check for an error      if(!request\_error && !DatabaseRead(request) && (GetLastError()!=ERR\_DATABASE\_NO\_MORE\_DATA))       {        PrintFormat("DatabaseRead() failed with code=%d", GetLastError());        DatabaseFinalize(request);        request\_error=true;        break;       }      //--- reset the request before the next parameter update      if(!request\_error && !DatabaseReset(request))       {        PrintFormat("DatabaseReset() failed with code=%d", GetLastError());        DatabaseFinalize(request);        request\_error=true;        break;       }     } //--- done going through all the bars     //--- transactions status    if(request\_error)     {      PrintFormat("Table RATES: failed to add %d bars ", ArraySize(rates));      DatabaseTransactionRollback(db);      DatabaseClose(db);      return;     }    else     {      DatabaseTransactionCommit(db);      PrintFormat("Table RATES: added %d bars in %d ms",                  ArraySize(rates), (GetMicrosecondCount()-start)/1000);     }  //--- save the RATES table to a CSV file    string csv\_filename=Symbol()+".csv";    long saved=DatabaseExport(db, "SELECT \* FROM RATES", csv\_filename, DATABASE\_EXPORT\_HEADER|DATABASE\_EXPORT\_INDEX|DATABASE\_EXPORT\_COMMON\_FOLDER, ";");    if(saved>0)      Print("Table RATES saved in ", Symbol(), ".csv");    else      Print("DatabaseExport() failed. Error ", GetLastError());  //--- close the database file and inform of that    DatabaseClose(db);    PrintFormat("Database: %s created and closed", filename); |

See also

[DatabasePrint](../DatabasePrint/DatabasePrint.md), [DatabaseImport](../DatabaseImport/DatabaseImport.md)
