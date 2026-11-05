# Overload

Overload

Within one class it is possible to define two or more methods that use the same name, but have different numbers of parameters. When this occurs, methods are called overloaded and such a process is referred to as method overloading.

Method overloading is one of ways of [polymorphism](../Polymorphism/Polymorphism.md) realization. Overloading of methods is performed according to the same rules as the [function overloading](../../Functions/Function-Overloading/Function-Overloading.md).

If the called function has no exact match, the compiler searches for a suitable function on three levels sequentially:

1. search within class methods.
2. search within the base class methods, consistently from the nearest ancestor to the very first.
3. search among other functions.

If there is no exact correspondence at all levels, but several suitable functions at different levels have been found, the function found at the least level is used. Within one level, there can't be more than one suitable function.

See also

[Function Overloading](../../Functions/Function-Overloading/Function-Overloading.md)
