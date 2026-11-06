# CLProgramFree


Eltávolít egy OpenCL-programot.

```cpp
void  CLProgramFree(
   int  program     // Handle to an OpenCL object
   );
```

Paraméterek

program

[in]  Az OpenCL-objektum kezelője.

Visszatérési érték

Nincs. Belső hiba esetén megváltozik a [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) értéke. A hibáról a [GetLastError()](../../Checkup/GetLastError/GetLastError.md) függvénnyel kérhető információ.
