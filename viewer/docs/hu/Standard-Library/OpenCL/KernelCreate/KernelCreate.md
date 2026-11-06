# KernelCreate


Belépési pontot hoz létre az OpenCL-programban a megadott indexen.

```cpp
bool  KernelCreate(
   const int     kernel_index,     // index of the kernel
   const string  kernel_name       // name of the kernel
   );
```

Paraméterek

kernel\_index

[in]  A kernel objektum indexe.

kernel\_name

[in]  A kernel objektum neve.

Visszatérési érték

Sikeres végrehajtás esetén true, ellenkező esetben false értéket ad vissza.
