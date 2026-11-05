# Namespaces

Namespaces

A namespace is a specially declared area, within which various IDs are defined: variables, functions, classes, etc. It is set using the namespace keyword:

|  |
| --- |
| namespace name of\_space {     // list of function, class and variable definitions  } |

Applying 'namespace' allows splitting the global namespace into subspaces. All IDs within the namespace are available to each other without a specification. The [::](../Operations-and-Expressions/Other-Operations/Other-Operations.md#context_allow) operator (context resolution operation) is used to access namespace members from the outside.

|  |
| --- |
| namespace ProjectData  {  class DataManager    {  public:     void              LoadData() {}    };  void Func(DataManager& manager) {}  }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- working with ProjectData namespace     ProjectData::DataManager mgr;     mgr.LoadData();     ProjectData::Func(mgr);    } |

Namespaces are used to arrange a code in the form of logical groups and to avoid name conflicts that may occur when several libraries are used in a program. In such cases, each library can be declared in its namespace to explicitly access the necessary functions and classes of each library.

A namespace can be declared in several blocks in one or several files. The compiler combines all parts together during a preprocessing and the resulting namespace contains all the members declared in all parts. Suppose that we have A class implemented in the Sample.mqh include file:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                       Sample.mqh |  //+------------------------------------------------------------------+  class A    {  public:                       A() {Print(\_\_FUNCTION\_\_);}    }; |

We want to use this class in our project, but we already have A class. To be able to use both classes and avoid ID conflict, simply wrap the included file in a namespace:

|  |
| --- |
| //--- declare the first A class  class A    {  public:                       A() {Print(\_\_FUNCTION\_\_);}    };  //--- wrap the A class from the Sample.mqh file in the Library namespace to avoid a conflict  namespace Library  {  #include "Sample.mqh"  }  //--- add yet another class to the Library namespace  namespace Library  {  class B    {  public:                       B() {Print(\_\_FUNCTION\_\_);}    };  }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- use the A class from the global namespace     A a1;  //--- use the A and B classes from the Library namespace     Library::A a2;     Library::B b;    }  //+------------------------------------------------------------------+     /\*  Result:     A::A     Library::A::A     Library::B::B  \*/ |

Namespaces can be nested. A nested namespace has unlimited access to members of its parent space, but members of the parent space do not have unlimited access to the nested namespace.

|  |
| --- |
| namespace General  {  int Func();     namespace Details  {   int Counter;   int Refresh()  {return Func(); }  }     int GetBars()   {return(iBars(Symbol(), Period()));};  int Size(int i) {return Details::Counter;}  } |

 

Global namespace

If the ID is not explicitly declared in the namespace, it is considered to be an implicit part of the global namespace. To set the global ID explicitly, use the [scope resolution operator](../Operations-and-Expressions/Other-Operations/Other-Operations.md#context_allow) without a name. This will allow you to distinguish this ID from any other element with the same name located in a different namespace.  For example, when importing a function:

|  |
| --- |
| #import "lib.dll"  int Func();  #import  //+------------------------------------------------------------------+  //|  Some function                                              |  //+------------------------------------------------------------------+  int Func()    {     return(0);    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //+--- call the imported function     Print(lib::Func());  //+--- call our function     Print(::Func());    } |

In this case, all the functions imported from the DLL function were included in the namespace of the same name. This allowed the compiler to clearly determine the function to be called.

See also

[Global Variables](../Variables/Global-Variables/Global-Variables.md), [Local Variables](../Variables/Local-Variables/Local-Variables.md), [Visibility Scope and Lifetime of Variables](../Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
