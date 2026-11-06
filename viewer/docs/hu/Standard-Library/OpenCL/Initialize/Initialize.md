# Initialize


Inicializálja az OpenCL-programot.

```cpp
bool  Initialize(
   const string  program,           // handle of the OpenCL program
   const bool    show_log=true      // keep a log
   );
```

Paraméterek

program

[in]  Az OpenCL-program kezelője.

show\_log=true

[in]  Naplóüzenetek engedélyezése.

Visszatérési érték

Sikeres inicializálás esetén true, ellenkező esetben false értéket ad vissza.
