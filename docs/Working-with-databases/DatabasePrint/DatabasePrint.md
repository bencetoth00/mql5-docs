# DatabasePrint

DatabasePrint

Prints a table or an SQL request execution result in the Experts journal.

|  |
| --- |
| long  DatabasePrint(     int           database,          // database handle received in DatabaseOpen     const string  table\_or\_sql,      // a table or an SQL request     uint          flags              // combination of flags     ); |

Parameters

database

[in]  Database handle received in [DatabaseOpen()](../DatabaseOpen/DatabaseOpen.md).

table\_or\_sql

[in]  A name of a table or a text of an SQL request whose results are displayed in the Experts journal.

flags

[in]  Combination of flags defining the output formatting. The flags are defined as follows:

DATABASE\_PRINT\_NO\_HEADER      – do not display table column names (field names)  
DATABASE\_PRINT\_NO\_INDEX         – do not display string indices  
DATABASE\_PRINT\_NO\_FRAME        – do not display a frame separating a header and data  
DATABASE\_PRINT\_STRINGS\_RIGHT – align strings to the right.

If flags=0, the columns and the strings are displayed, the header and the data are separated by the frame, while the strings are aligned to the left.

Return Value

Return the number of exported strings or -1 in case of an error. To get the error code, use [GetLastError()](../../Checkup/GetLastError/GetLastError.md), the possible responses are:

- ERR\_INTERNAL\_ERROR (4001)                       – critical runtime error;
- ERR\_NOT\_ENOUGH\_MEMORY (4004)              - insufficient memory;
- ERR\_DATABASE\_INTERNAL (5120)                 – internal database error;
- ERR\_DATABASE\_INVALID\_HANDLE (5121)      - invalid database handle;

Note

If the journal displays request results, the SQL request should begin with "SELECT" or "select". In other words, the SQL request cannot alter the database status, otherwise DatabasePrint() fails with an error.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string filename="departments.sqlite";  //--- create or open the database in the common terminal folder     int db=DatabaseOpen(filename, DATABASE\_OPEN\_READWRITE | DATABASE\_OPEN\_CREATE |DATABASE\_OPEN\_COMMON);     if(db==INVALID\_HANDLE)       {        Print("DB: ", filename, " open failed with code ", GetLastError());        return;       }     //--- create the COMPANY table     if(!CreataTableCompany(db))       {        DatabaseClose(db);        return;       }  //--- create the DEPARTMENT table     if(!CreataTableDepartment(db))       {        DatabaseClose(db);        return;       }     //--- display the list of all fields in the COMPANY and DEPARTMENT tables     PrintFormat("Try to print request \"PRAGMA TABLE\_INFO(COMPANY);PRAGMA TABLE\_INFO(DEPARTMENT)\"");     if(DatabasePrint(db, "PRAGMA TABLE\_INFO(COMPANY);PRAGMA TABLE\_INFO(DEPARTMENT)", 0)<0)       {        PrintFormat("DatabasePrint(\"PRAGMA TABLE\_INFO()\") failed, error code=%d", GetLastError());        DatabaseClose(db);        return;       }  //--- display the COMPANY table in the log     PrintFormat("Try to print request \"SELECT \* from COMPANY\"");     if(DatabasePrint(db, "SELECT \* from COMPANY", 0)<0)       {        Print("DatabasePrint failed with code ", GetLastError());        DatabaseClose(db);        return;       }  //--- request text for combining the COMPANY and DEPARTMENT tables     string request="SELECT EMP\_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT "                    "ON COMPANY.ID = DEPARTMENT.EMP\_ID";  //--- display the table combining result     PrintFormat("Try to print request \"SELECT EMP\_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT\"");     if(DatabasePrint(db, request, 0)<0)       {        Print("DatabasePrint failed with code ", GetLastError());        DatabaseClose(db);        return;       }  //--- close the database     DatabaseClose(db);    }  /\*  Conclusion:  Try to print request "PRAGMA TABLE\_INFO(COMPANY);PRAGMA TABLE\_INFO(DEPARTMENT)"  #| cid name    type     notnull dflt\_value pk  -+-------------------------------------------  1|   0 ID      INT            1             1   2|   1 NAME    TEXT           1             0   3|   2 AGE     INT            1             0   4|   3 ADDRESS CHAR(50)       0             0   5|   4 SALARY  REAL           0             0   #| cid name   type     notnull dflt\_value pk  -+------------------------------------------  1|   0 ID     INT            1             1   2|   1 DEPT   CHAR(50)       1             0   3|   2 EMP\_ID INT            1             0   Try to print request "SELECT \* from COMPANY"  #| ID NAME  AGE ADDRESS     SALARY  -+--------------------------------  1|  1 Paul   32 California 25000.0   2|  2 Allen  25 Texas      15000.0   3|  3 Teddy  23 Norway     20000.0   4|  4 Mark   25 Rich-Mond  65000.0   5|  5 David  27 Texas      85000.0   6|  6 Kim    22 South-Hall 45000.0   7|  7 James  24 Houston    10000.0   Try to print request "SELECT EMP\_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT"  #| EMP\_ID NAME  DEPT         -+-------------------------  1|      1 Paul  IT Billing    2|      2 Allen Engineering   3|        Teddy               4|        Mark                5|        David               6|        Kim                 7|      7 James Finance       \*/  //+------------------------------------------------------------------+  //| Create the COMPANY table                           |  //+------------------------------------------------------------------+  bool CreateTableCompany(int database)    {  //--- if the COMPANY table exists, delete it     if(DatabaseTableExists(database, "COMPANY"))       {        //--- delete the table        if(!DatabaseExecute(database, "DROP TABLE COMPANY"))          {           Print("Failed to drop table COMPANY with code ", GetLastError());           return(false);          }       }  //--- create the COMPANY table     if(!DatabaseExecute(database, "CREATE TABLE COMPANY("                         "ID INT PRIMARY KEY     NOT NULL,"                         "NAME           TEXT    NOT NULL,"                         "AGE            INT     NOT NULL,"                         "ADDRESS        CHAR(50),"                         "SALARY         REAL );"))       {        Print("DB: create table COMPANY failed with code ", GetLastError());        return(false);       }     //--- enter data to the COMPANY table     if(!DatabaseExecute(database, "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 25000.00); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'David', 27, 'Texas', 85000.0); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (6, 'Kim', 22, 'South-Hall', 45000.0); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (7, 'James', 24, 'Houston', 10000.00); "))       {        Print("COMPANY insert failed with code ", GetLastError());        return(false);       }  //--- success     return(true);    }  //+------------------------------------------------------------------+  //| Create the DEPARTMENT table                       |  //+------------------------------------------------------------------+  bool CreateTableDepartment(int database)    {  //--- if the DEPARTMENT table exists, delete it     if(DatabaseTableExists(database, "DEPARTMENT"))       {        //--- delete the table        if(!DatabaseExecute(database, "DROP TABLE DEPARTMENT"))          {           Print("Failed to drop table DEPARTMENT  with code ", GetLastError());           return(false);          }       }  //--- create the DEPARTMENT table     if(!DatabaseExecute(database, "CREATE TABLE DEPARTMENT ("                         "ID      INT PRIMARY KEY   NOT NULL,"                         "DEPT    CHAR(50)          NOT NULL,"                         "EMP\_ID  INT               NOT NULL);"))       {        Print("DB: create table DEPARTMENT failed with code ", GetLastError());        return(false);       }     //--- enter data to the DEPARTMENT table     if(!DatabaseExecute(database, "INSERT INTO DEPARTMENT (ID,DEPT,EMP\_ID) VALUES (1, 'IT Billing', 1); "                         "INSERT INTO DEPARTMENT (ID,DEPT,EMP\_ID) VALUES (2, 'Engineering', 2); "                         "INSERT INTO DEPARTMENT (ID,DEPT,EMP\_ID) VALUES (3, 'Finance', 7);"))       {        Print("DEPARTMENT insert failed with code ", GetLastError());        return(false);       }  //--- success     return(true);    }  //+------------------------------------------------------------------- |

See also

[DatabaseExport](../DatabaseExport/DatabaseExport.md), [DatabaseImport](../DatabaseImport/DatabaseImport.md)
