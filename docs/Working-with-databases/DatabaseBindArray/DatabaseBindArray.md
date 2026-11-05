# DatabaseBindArray

DatabaseBindArray

Sets an array as a parameter value.

|  |
| --- |
| bool  DatabaseBind(     int  request,      // the handle of a request created in DatabasePrepare     int  index,        // the parameter index in the request     T&   array[]       // parameter value as an array     ); |

Parameters

request

[in]  The handle of a request created in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

index

[in]  The parameter index in the request a value should be set for. The numbering starts with zero.

array[]

[in]  The array to be set as a request parameter value.

Return Value

Returns true if successful, otherwise - false. To get the error code, use GetLastError(), the possible responses are:

- ERR\_INVALID\_PARAMETER (4003)              – unsupported type;
- ERR\_ARRAY\_BAD\_SIZE (4011)                    - array size in bytes exceeds INT\_MAX;
- ERR\_DATABASE\_INVALID\_HANDLE (5121)  - invalid database handle;
- ERR\_DATABASE\_NOT\_READY (5128)    - cannot use the function to make a request at the moment (the request is being executed or already complete, DatabaseReset should be called).

Note

The function is used in case an SQL request contains "?" or "?N" parameterizable values where N means the parameter index (starting from one). At the same time, parameters indexing in DatabaseBindArray() starts from zero.

For example:

|  |
| --- |
| INSERT INTO table VALUES (?,?,?) |

The function may be called immediately after a parametrized request is created in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md) or after the request is reset using [DatabaseReset()](../DatabaseReset/DatabaseReset.md).

Use this function together with [DatabaseReset()](../DatabaseReset/DatabaseReset.md) to execute the request as many times as needed with different parameter values.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- open the dialog for selecting files with the DAT extension     string selected\_files[];     if(!FileSelectDialog("Select files to download", NULL,                         "Data files (\*.dat)|\*.dat|All files (\*.\*)|\*.\*",                         FSD\_ALLOW\_MULTISELECT, selected\_files, "tester.dat")>0)       {        Print("Files not selected. Exit");        return;       }  //--- get the size of files     ulong filesize[];     int filehandle[];     int files=ArraySize(selected\_files);     ArrayResize(filesize, files);     ZeroMemory(filesize);     ArrayResize(filehandle, files);     double total\_size=0;     for(int i=0; i<files; i++)       {        filehandle[i]=FileOpen(selected\_files[i], FILE\_READ|FILE\_BIN);        if(filehandle[i]!=INVALID\_HANDLE)          {           filesize[i]=FileSize(filehandle[i]);           //PrintFormat("%d, %s handle=%d %d bytes", i, selected\_files[i], filehandle[i], filesize[i]);           total\_size+=(double)filesize[i];          }       }  //--- check the common size of files     if(total\_size==0)       {        PrintFormat("Total files size is 0. Exit");        return;       }     //--- create or open the database in the common terminal folder     string filename="dat\_files.sqlite";     int db=DatabaseOpen(filename, DATABASE\_OPEN\_READWRITE | DATABASE\_OPEN\_CREATE);     if(db==INVALID\_HANDLE)       {        Print("DB: ", filename, " open failed with code ", GetLastError());        return;       }     else        Print("Database: ", filename, " opened successfully");  //--- if the FILES table exists, delete it     if(DatabaseTableExists(db, "FILES"))       {        //--- delete the table        if(!DatabaseExecute(db, "DROP TABLE FILES"))          {           Print("Failed to drop table FILES with code ", GetLastError());           DatabaseClose(db);           return;          }       }  //--- create the FILES table     if(!DatabaseExecute(db, "CREATE TABLE FILES("                         "NAME           TEXT NOT NULL,"                         "SIZE           INT  NOT NULL,"                         "PERCENT\_SIZE   REAL NOT NULL,"                         "DATA           BLOB NOT NULL);"))       {        Print("DB: failed to create table FILES with code ", GetLastError());        DatabaseClose(db);        return;       }  //--- display the list of all fields in the FILES table     if(DatabasePrint(db, "PRAGMA TABLE\_INFO(FILES)", 0)<0)       {        PrintFormat("DatabasePrint(\"PRAGMA TABLE\_INFO(FILES)\") failed, error code=%d at line %d", GetLastError(), \_\_LINE\_\_);        DatabaseClose(db);        return;       }     //--- create a parametrized request to add files to the FILES table     string sql="INSERT INTO FILES (NAME,SIZE,PERCENT\_SIZE,DATA)"                " VALUES (?1,?2,?3,?4);"; // request parameters     int request=DatabasePrepare(db, sql);     if(request==INVALID\_HANDLE)       {        PrintFormat("DatabasePrepare() failed with code=%d", GetLastError());        Print("SQL request: ", sql);        DatabaseClose(db);        return;       }     //--- go through all the files and add them to the FILES table     bool request\_error=false;     DatabaseTransactionBegin(db);     int count=0;     uint size;     for(int i=0; i<files; i++)       {        if(filehandle[i]!=INVALID\_HANDLE)          {           char data[];           size=FileReadArray(filehandle[i], data);           if(size==0)             {              PrintFormat("FileReadArray(%s) failed with code %d", selected\_files[i], GetLastError());              continue;             }              count++;           //--- set the values of the parameters before adding the file to the table           if(!DatabaseBind(request, 0, selected\_files[i]))             {              PrintFormat("DatabaseBind() failed at line %d with code=%d", \_\_LINE\_\_, GetLastError());              request\_error=true;              break;             }           if(!DatabaseBind(request, 1, size))             {              PrintFormat("DatabaseBind() failed at line %d with code=%d", \_\_LINE\_\_, GetLastError());              request\_error=true;              break;             }           if(!DatabaseBind(request, 2, double(size)\*100./total\_size))             {              PrintFormat("DatabaseBind() failed at line %d with code=%d", \_\_LINE\_\_, GetLastError());              request\_error=true;              break;             }           if(!DatabaseBindArray(request, 3, data))             {              PrintFormat("DatabaseBind() failed at line %d with code=%d", \_\_LINE\_\_, GetLastError());              request\_error=true;              break;             }           //--- execute a request for inserting the entry and check for an error           if(!DatabaseRead(request)&&(GetLastError()!=ERR\_DATABASE\_NO\_MORE\_DATA))             {              PrintFormat("DatabaseRead() failed with code=%d", GetLastError());              DatabaseFinalize(request);              request\_error=true;              break;             }           else              PrintFormat("%d. %s: %d bytes", count, selected\_files[i],size);           //--- reset the request before the next parameter update           if(!DatabaseReset(request))             {              PrintFormat("DatabaseReset() failed with code=%d", GetLastError());              DatabaseFinalize(request);              request\_error=true;              break;             }          }       }  //--- transactions status     if(request\_error)       {        PrintFormat("Table FILES: failed to add %d files", count);        DatabaseTransactionRollback(db);        DatabaseClose(db);        return;       }     else       {        DatabaseTransactionCommit(db);        PrintFormat("Table FILES: added %d files", count);       }     //--- close the database file and inform of that     DatabaseClose(db);     PrintFormat("Database: %s created and closed", filename);    } |

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseReset](../DatabaseReset/DatabaseReset.md), [DatabaseRead](../DatabaseRead/DatabaseRead.md), [DatabaseBind](../DatabaseBind/DatabaseBind.md)
