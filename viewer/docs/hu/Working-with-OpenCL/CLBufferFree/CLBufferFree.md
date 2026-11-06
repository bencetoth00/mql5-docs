# CLBufferFree


Törli az OpenCL puffert.

```cpp
void  CLBufferFree(
   int   buffer     // Handle to an OpenCL buffer
   );
```

Paraméterek

buffer

[in]  Az OpenCL-puffer kezelője.

Visszatérési érték

Nincs. Belső hiba esetén megváltozik a [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) értéke. A hibáról a [GetLastError()](../../Checkup/GetLastError/GetLastError.md) függvénnyel kérhető információ.
