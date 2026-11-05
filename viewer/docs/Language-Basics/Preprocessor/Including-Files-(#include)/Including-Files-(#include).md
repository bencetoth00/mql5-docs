# Including Files (#include)


The #include command line can be placed anywhere in the program, but usually all inclusions are placed at the beginning of the source code. Call format:

```cpp
#include <file_name>
#include "file_name"
```

Examples:

```cpp
#include <WinUser32.mqh>
#include "mylib.mqh"
```

The preprocessor replaces the line #include <file\_name> with the content of the file WinUser32.mqh. Angle brackets indicate that the WinUser32.mqh file will be taken from the standard directory (usually it is terminal\_installation\_directory\MQL5\Include). The current directory is not included in the search.

If the file name is enclosed in quotation marks, the search is made in the current directory (which contains the main source file). The standard directory is not included in the search.

See also

[Standard Library](../../../Standard-Library/Standard-Library.md), [Importing Functions](../Importing-Functions-(#import)/Importing-Functions-(#import).md)