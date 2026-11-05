# DatabaseImport

DatabaseImport

Imports data from a file into a table.

|  |
| --- |
| long  DatabaseImport(     int           database,          // database handle received in DatabaseOpen     const string  table,             // name of a table to insert data     const string  filename,          // name of a file to import data     uint          flags,             // combination of flags     const string  separator,         // data separator      ulong         skip\_rows,         // how many initial strings to skip      const string  skip\_comments      // string of characters defining comments     ); |

Parameters

database

[in]  Database handle received in [DatabaseOpen()](../DatabaseOpen/DatabaseOpen.md).

table

[in]  Name of a table the data from a file is to be added to.

filename

[in]  CSV file or ZIP archive for reading data. The name may contain subdirectories and is set relative to the MQL5\Files folder.

flags

[in]  Combination of flags from the [ENUM\_DATABASE\_IMPORT\_FLAGS](DatabaseImport.md#enum_database_import_flags) enumeration.

separator

[in]  Data separator in CSV file.

skip\_rows

[in]  Number of initial strings to be skipped when reading data from the file.

skip\_comments

[in]  String of characters for designating strings as comments. If any character from skip\_comments is detected at the beginning of a string, such a string is considered a comment and is not imported.

Return Value

Return the number of imported strings or -1 in case of an error. To get the error code, use [GetLastError()](../../Checkup/GetLastError/GetLastError.md), the possible responses are:

- ERR\_INVALID\_PARAMETER (4003)              –  no table name specified (empty string or NULL);
- ERR\_DATABASE\_INTERNAL (5120)              – internal database error;
- ERR\_DATABASE\_INVALID\_HANDLE (5121)   - invalid database handle.

 

Note

If there is no table named table, it is generated automatically. Names and field types in the created table are defined automatically based on the file data.  

If there is no table named table, it is generated automatically. Names and field types in the created table are defined automatically based on the file data.  

ENUM\_DATABASE\_IMPORT\_FLAGS

| ID | Description |
| --- | --- |
| DATABASE\_IMPORT\_HEADER | The first line contains the names of the table fields |
| DATABASE\_IMPORT\_CRLF | CRLF (the default is LF) is considered a string break |
| DATABASE\_IMPORT\_APPEND | Add data to the end of an existing table |
| DATABASE\_IMPORT\_QUOTED\_STRINGS | String values enclosed in double quotes |
| DATABASE\_IMPORT\_COMMON\_FOLDER | The file is stored in the common folder of all client terminals \Terminal\Common\File. |

Example of reading the table from the file created by the code from the [DatabaseExport](../DatabaseExport/DatabaseExport.md) example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()   {    string csv\_filename;  //--- get the names of text files for downloading from the common folder of the client terminals    string filenames[];    if(FileSelectDialog("Select a CSV file to download a table", NULL,                        "Text files (\*.csv)|\*.csv",                        FSD\_WRITE\_FILE|FSD\_COMMON\_FOLDER, filenames, "data.csv")>0)     {      //--- display the name of each selected file      if(ArraySize(filenames)==1)        csv\_filename=filenames[0];      else       {        Print("Unknown error while selecting file. Error code ", GetLastError());        return;       }     }    else     {      Print("CSV file not selected");      return;     }  //--- create or open a database    string db\_filename="test.sqlite";    int db=DatabaseOpen(db\_filename, DATABASE\_OPEN\_READWRITE|DATABASE\_OPEN\_CREATE);  //--- check if the TEST table exists    if(DatabaseTableExists(db, "TEST"))     {      //--- remove the TEST table      if(!DatabaseExecute(db, "DROP TABLE IF EXISTS TEST"))       {        Print("Failed to drop the TEST table with code ", GetLastError());        DatabaseClose(db);        return;       }     }    //--- import entries from the file to the TEST table    long imported=DatabaseImport(db, "TEST", csv\_filename, DATABASE\_IMPORT\_HEADER|DATABASE\_IMPORT\_COMMON\_FOLDER|DATABASE\_IMPORT\_APPEND, ";", 0, NULL);    if(imported>0)     {      Print(imported," lines imported in table TEST");      DatabasePrint(db,"SELECT \* FROM TEST",DATABASE\_PRINT\_NO\_INDEX);     }    else      {       Print("DatabaseImport() failed. Error ",GetLastError());      }  //--- close the database file and inform of that    DatabaseClose(db);    PrintFormat("Database: %s closed", db\_filename);   } |

See also

[DatabaseOpen](../DatabaseOpen/DatabaseOpen.md), [DatabasePrint](../DatabasePrint/DatabasePrint.md)
