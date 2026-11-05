# Extern Variables

Extern Variables

The extern keyword is used for declaring variable identifiers as identifiers of the [static storage class](../Static-Variables/Static-Variables.md) with global [lifetime](../Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md). These variables exist from the start of the program and memory for them is allocated and initialized immediately after the start of the program.

You can create programs that consist of multiple source files; in this case a directive to the preprocessor [#include](../../Preprocessor/Including-Files-(#include)/Including-Files-(#include).md) is used. Variables declared as an extern with the same type and identifier can exist in different source files of one project.

When compiling the whole project, all the extern variables with the same type and an identifier are associated with one part of memory of the global variable pool. Extern variables are useful for separate compilation of source files. Extern variables can be initialized, but only once - existence of several initialized extern variables of the same type and with the same identifier is prohibited.

See also

[Data Types](../../Data-Types/Data-Types.md), [Encapsulation and Extensibility of Types](../../Object-Oriented-Programming/Encapsulation-and-Extensibility-of-Types/Encapsulation-and-Extensibility-of-Types.md),[Initialization of Variables](../Initialization-of-Variables/Initialization-of-Variables.md), [Visibility Scope and Lifetime of Variables](../Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and Deleting Objects](../Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
