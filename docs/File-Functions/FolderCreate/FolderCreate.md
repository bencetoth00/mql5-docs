# FolderCreate

FolderCreate

Creates a directory in the Files folder (depending on the common\_flag value)

|  |
| --- |
| bool  FolderCreate(     string  folder\_name,       // line with the created folder name     int     common\_flag=0      // action area     ); |

Parameters

folder\_name

[in]  Name of the directory to be created. Contains the relative path to the folder.

common\_flag=0

[in] [Flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) defining the directory location. If common\_flag=FILE\_COMMON, the directory is located in the common folder of all client terminals \Terminal\Common\Files. Otherwise, the directory is in the local folder (MQL5\Files or MQL5\Tester\Files when testing).

Return Value

Returns true if successful, otherwise false.

Note

For reasons of security, working with files is strictly controlled in MQL5 language. Files used in file operations by means of MQL5 language cannot be located outside the file sandbox.

Example:

|  |
| --- |
| #property copyright "Copyright 2000-2024, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- description  #property description "The script shows FolderCreate() application sample."  #property description "The external parameter defines the directory for creating folders."  #property description "The folder structure is created after executing the script"     //--- display window of the input parameters during the script's launch  #property script\_show\_inputs  //--- the input parameter defines the folder, in which the script works  input bool     common\_folder=false; // common folder for all terminals  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- folder to be created in MQL5\Files     string root\_folder="Folder\_A";     if(CreateFolder(root\_folder,common\_folder))       {        //--- create the Child\_Folder\_B1 sub-folder in it        string folder\_B1="Child\_Folder\_B1";        string path=root\_folder+"\\"+folder\_B1;          // create the folder name considering the structure        if(CreateFolder(path,common\_folder))          {           //--- create 3 more sub-directories in this folder           string folder\_C11="Child\_Folder\_C11";           string child\_path=root\_folder+"\\"+folder\_C11;// create the folder name considering the structure           CreateFolder(child\_path,common\_folder);           //--- second sub-directory           string folder\_C12="Child\_Folder\_C12";           child\_path=root\_folder+"\\"+folder\_C12;           CreateFolder(child\_path,common\_folder);              //--- third sub-directory           string folder\_C13="Child\_Folder\_C13";           child\_path=root\_folder+"\\"+folder\_C13;           CreateFolder(child\_path,common\_folder);          }       }  //---    }  //+------------------------------------------------------------------+  //| Try creating a folder and display a message about that           |  //+------------------------------------------------------------------+  bool CreateFolder(string folder\_path,bool common\_flag)    {     int flag=common\_flag?FILE\_COMMON:0;     string working\_folder;  //--- define the full path depending on the common\_flag parameter     if(common\_flag)        working\_folder=TerminalInfoString(TERMINAL\_COMMONDATA\_PATH)+"\\MQL5\\Files";     else        working\_folder=TerminalInfoString(TERMINAL\_DATA\_PATH)+"\\MQL5\\Files";  //--- debugging message       PrintFormat("folder\_path=%s",folder\_path);  //--- attempt to create a folder relative to the MQL5\Files path     if(FolderCreate(folder\_path,flag))       {        //--- display the full path for the created folder        PrintFormat("Created the folder %s",working\_folder+"\\"+folder\_path);        //--- reset the error code        ResetLastError();        //--- successful execution        return true;       }     else        PrintFormat("Failed to create the folder %s. Error code %d",working\_folder+folder\_path,GetLastError());  //--- execution failed     return false;    } |

See also

[FileOpen()](../FileOpen/FileOpen.md), [FolderClean()](../FolderClean/FolderClean.md), [FileCopy()](../FileCopy/FileCopy.md)
