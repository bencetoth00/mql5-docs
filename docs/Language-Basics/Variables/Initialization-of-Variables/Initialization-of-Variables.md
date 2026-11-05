# Initialization of Variables

Initialization of Variables

Any variable can be initialized during definition. If a variable is not initialized explicitly, the value stored in this variable can be any. Implicit initialization is not used.

[Global](../Global-Variables/Global-Variables.md) and [static](../Static-Variables/Static-Variables.md) variables can be initialized only by a constant of the corresponding type or a constant expression. [Local variables](../Local-Variables/Local-Variables.md) can be initialized by any expression, not just a constant.

Initialization of global and static variables is performed only once. Initialization of local variables is made every time you call the corresponding functions.

Examples:

|  |
| --- |
| int    n       = 1;  string s       = "hello";  double f[]     = { 0.0, 0.236, 0.382, 0.5, 0.618, 1.0 };  int    a[4][4] = { {1, 1, 1, 1}, {2, 2, 2, 2}, {3, 3, 3, 3}, {4, 4, 4, 4 } };  //--- from tetris  int    right[4]={WIDTH\_IN\_PIXELS+VERT\_BORDER,WIDTH\_IN\_PIXELS+VERT\_BORDER,                   WIDTH\_IN\_PIXELS+VERT\_BORDER,WIDTH\_IN\_PIXELS+VERT\_BORDER};  //--- initialization of all fields of the structure with zero values  MqlTradeRequest request={}; |

List of values of the array elements must be enclosed in curly brackets. Missed initializing sequences are considered equal to 0.

If the size of the initialized array is not specified, it is determined by a compiler, based on the size of the initialization sequence.

Examples:

|  |
| --- |
| struct str3    {     int               low\_part;     int               high\_part;    };  struct str10    {     str3              s3;     double            d1[10];     int               i3;    };  void OnStart()    {     str10 s10\_1={{1,0},{1.0,2.1,3.2,4.4,5.3,6.1,7.8,8.7,9.2,10.0},100};     str10 s10\_2={{1,0},{},100};     str10 s10\_3={{1,0},{1.0}};  //---     Print("1.  s10\_1.d1[5] = ",s10\_1.d1[5]);     Print("2.  s10\_2.d1[5] = ",s10\_2.d1[5]);     Print("3.  s10\_3.d1[5] = ",s10\_3.d1[5]);     Print("4.  s10\_3.d1[0] = ",s10\_3.d1[0]);    } |

   
For structure type variable partial initialization is allowed, as well as for static arrays (with an implicitly set size). You can initialize one or more first elements of a structure or array, the other elements will be initialized with zeroes in this case.

See also

[Data Types](../../Data-Types/Data-Types.md), [Encapsulation and Extensibility of Types](../../Object-Oriented-Programming/Encapsulation-and-Extensibility-of-Types/Encapsulation-and-Extensibility-of-Types.md), [Visibility Scope and Lifetime of Variables](../Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
