# Global Variables


Global variables are created by placing their declarations outside function descriptions. Global variables are defined at the same level as functions, i.e., they are not local in any block.

Example:

```cpp
int GlobalFlag=10;   // Global variable
int OnStart()
  {
   ...
  }
```

The scope of global variables is the entire program. Global variables are accessible from all functions defined in the program. They are initialized to zero unless another initial value is explicitly defined. A global variable can be initialized only by a constant or constant expression that corresponds to its type.

Global variables are initialized only once after the program is loaded into the client terminal memory and before the first handling of the [Init](../../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#init) event. For global variables representing class objects, during their initialization the corresponding constructors are called. In scripts global variables are initialized before handling the [Start](../../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#start) event.

Note: Variables declared at global level must not be mixed up with the client terminal global variables that can be accessed using the [GlobalVariable...()](../../../Global-Variables-of-the-Terminal/Global-Variables-of-the-Terminal.md) functions.

See also

[Data Types](../../Data-Types/Data-Types.md), [Encapsulation and Extensibility of Types](../../Object-Oriented-Programming/Encapsulation-and-Extensibility-of-Types/Encapsulation-and-Extensibility-of-Types.md),[Initialization of Variables](../Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)