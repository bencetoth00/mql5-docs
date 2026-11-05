# DatabaseReadBind

DatabaseReadBind

Moves to the next record and reads data into the structure from it.

|  |
| --- |
| bool  DatabaseReadBind(     int    request,           // the handle of a request created in DatabasePrepare     void&  struct\_object      // the reference to the structure for reading the record      ); |

Parameters

request

[in]  The handle of a request created in [DatabasePrepare()](../DatabasePrepare/DatabasePrepare.md).

struct\_object

[out]  The reference to the structure the data from the current record is to be read to. The structure should only have numerical types and/or strings (arrays are not allowed) as members and cannot be a descendant.

Return Value

Return true if successful, otherwise false. To get the error code, use GetLastError(), the possible responses are:

- ERR\_INVALID\_PARAMETER (4003)               –  no table name specified (empty string or NULL);
- ERR\_WRONG\_STRING\_PARAMETER (5040)  – error converting a request into a UTF-8 string;
- ERR\_DATABASE\_INTERNAL (5120)              – internal database error;
- ERR\_DATABASE\_INVALID\_HANDLE (5121)    – invalid database handle;
- ERR\_DATABASE\_EXECUTE (5124)                –  request execution error;
- ERR\_DATABASE\_NO\_MORE\_DATA (5126)    – no table exists (not an error, normal completion).

 

Note

A number of fields in the struct\_object structure should not exceed [DatabaseColumnsCount()](../DatabaseColumnsCount/DatabaseColumnsCount.md). If the number of fields in the struct\_object structure is less than the number of fields in the record, the partial reading is performed. The remaining data can be explicitly obtained using the corresponding [DatabaseColumnText()](../DatabaseColumnText/DatabaseColumnText.md), [DatabaseColumnInteger()](../DatabaseColumnInteger/DatabaseColumnInteger.md) and other functions.

Example:

|  |
| --- |
| struct Person    {     int               id;     string            name;     int               age;     string            address;     double            salary;    };  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     int db;     string filename="company.sqlite";  //--- open     db=DatabaseOpen(filename, DATABASE\_OPEN\_READWRITE | DATABASE\_OPEN\_CREATE |DATABASE\_OPEN\_COMMON);     if(db==INVALID\_HANDLE)       {        Print("DB: ", filename, " open failed with code ", GetLastError());        return;       }  //--- if the table COMPANY exists then drop the table     if(DatabaseTableExists(db, "COMPANY"))       {        //--- delete the table        if(!DatabaseExecute(db, "DROP TABLE COMPANY"))          {           Print("Failed to drop table COMPANY with code ", GetLastError());           DatabaseClose(db);           return;          }       }  //--- create table     if(!DatabaseExecute(db, "CREATE TABLE COMPANY("                         "ID INT PRIMARY KEY     NOT NULL,"                         "NAME           TEXT    NOT NULL,"                         "AGE            INT     NOT NULL,"                         "ADDRESS        CHAR(50),"                         "SALARY         REAL );"))       {        Print("DB: ", filename, " create table failed with code ", GetLastError());        DatabaseClose(db);        return;       }     //--- insert data     if(!DatabaseExecute(db, "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 25000.00 ); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 ); "                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );"                         "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );"))       {        Print("DB: ", filename, " insert failed with code ", GetLastError());        DatabaseClose(db);        return;       }     //--- prepare the request     int request=DatabasePrepare(db, "SELECT \* FROM COMPANY WHERE SALARY>15000");     if(request==INVALID\_HANDLE)       {        Print("DB: ", filename, " request failed with code ", GetLastError());        DatabaseClose(db);        return;       }  //--- print records     Person person;     Print("Persons with salary > 15000:");     for(int i=0; DatabaseReadBind(request, person); i++)        Print(i, ":  ", person.id, " ", person.name, " ", person.age, " ", person.address, " ", person.salary);  //--- delete request after use     DatabaseFinalize(request);        Print("Some statistics:");  //--- prepare new request about total salary     request=DatabasePrepare(db, "SELECT SUM(SALARY) FROM COMPANY");     if(request==INVALID\_HANDLE)       {        Print("DB: ", filename, " request failed with code ", GetLastError());        DatabaseClose(db);        return;       }     while(DatabaseRead(request))       {        double total\_salary;        DatabaseColumnDouble(request, 0, total\_salary);        Print("Total salary=", total\_salary);       }  //--- delete request after use     DatabaseFinalize(request);     //--- prepare new request about average salary     request=DatabasePrepare(db, "SELECT AVG(SALARY) FROM COMPANY");     if(request==INVALID\_HANDLE)       {        Print("DB: ", filename, " request failed with code ", GetLastError());        ResetLastError();        DatabaseClose(db);        return;       }     while(DatabaseRead(request))       {        double aver\_salary;        DatabaseColumnDouble(request, 0, aver\_salary);        Print("Average salary=", aver\_salary);       }  //--- delete request after use     DatabaseFinalize(request);     //--- close database     DatabaseClose(db);    }  //+-------------------------------------------------------------------  /\*  Output:  Persons with salary > 15000:  0:  1 Paul 32 California 25000.0  1:  3 Teddy 23 Norway 20000.0  2:  4 Mark 25 Rich-Mond  65000.0  Some statistics:  Total salary=125000.0  Average salary=31250.0  \*/ |

See also

[DatabasePrepare](../DatabasePrepare/DatabasePrepare.md), [DatabaseRead](../DatabaseRead/DatabaseRead.md)
