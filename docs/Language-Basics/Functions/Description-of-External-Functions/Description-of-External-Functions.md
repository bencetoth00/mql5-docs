# Description of External Functions

Description of External Functions

External functions defined in another module must be explicitly described. The description includes returned type, function name and series of input parameters with their types. The absence of such a description can lead to errors when compiling, building, or executing a program. When describing an external object, use the keyword #import indicating the module.

Examples:

|  |
| --- |
| #import "user32.dll"    int     MessageBoxW(int hWnd ,string szText,string szCaption,int nType);    int     SendMessageW(int hWnd,int Msg,int wParam,int lParam);  #import "lib.ex5"    double  round(double value);  #import |

With the help of import, it is easy to describe functions that are called from external DLL or compiled EX5 libraries. EX5 libraries are compiled ex5 files, which have the [library](../../Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md) property. Only function described with [the export modifier](../Exporting-Functions/Exporting-Functions.md) can be imported from EX5 libraries.

Please keep in mind that DLL and EX5 libraries should have different names (regardless of the directories they are located in) if they are imported together. All imported functions have the scope resolution corresponding to the library's "file name".

Example:

|  |
| --- |
| #import "kernel32.dll"     int GetLastError();  #import "lib.ex5"     int GetLastError();  #import     class CFoo    {  public:     int            GetLastError() { return(12345); }     void           func()       {        Print(GetLastError());           // call of the class method        Print(::GetLastError());         // call of the MQL5 function        Print(kernel32::GetLastError()); // call of the DLL library function from kernel32.dll        Print(lib::GetLastError());      // call of the EX5 library function from lib.ex5       }    };     void OnStart()    {     CFoo foo;     foo.func();    } |

See also

[Overload](../../Object-Oriented-Programming/Overload/Overload.md), [Virtual Functions](../../Object-Oriented-Programming/Virtual-Functions/Virtual-Functions.md), [Polymorphism](../../Object-Oriented-Programming/Polymorphism/Polymorphism.md)
