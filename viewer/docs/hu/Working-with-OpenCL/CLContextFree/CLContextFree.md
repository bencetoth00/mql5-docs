# CLContextFree


Eltávolít egy OpenCL-környezetet.

```cpp
void  CLContextFree(
   int  context     // Handle to an OpenCL context
   );
```

Paraméterek

context

[in]  Az OpenCL-környezet kezelője.

Visszatérési érték

Nincs. Belső hiba esetén megváltozik a [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) értéke. A hibáról a [GetLastError()](../../Checkup/GetLastError/GetLastError.md) függvénnyel kérhető információ.
