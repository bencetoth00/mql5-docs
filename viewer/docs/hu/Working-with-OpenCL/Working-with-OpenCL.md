# OpenCL használata

Az [OpenCL](https://www.khronos.org/opencl/) programok OpenCL 1.1-et vagy újabb verziót támogató videokártyákon végzett számításokra szolgálnak. A modern videokártyák több száz kisebb, specializált processzort tartalmaznak, amelyek párhuzamosan végezhetnek egyszerű matematikai műveleteket. Az OpenCL párhuzamos számítási modellje bizonyos feladatoknál jelentős gyorsulást adhat.

Egyes videokártyákon a `double` típusú számok kezelése alapértelmezés szerint nincs engedélyezve. Ez az 5105-ös fordítási hibát okozhatja. A támogatás bekapcsolásához add hozzá az alábbi direktívát az OpenCL-programhoz: [#pragma OPENCL EXTENSION cl_khr_fp64 : enable](https://www.khronos.org/registry/OpenCL/sdk/1.0/docs/man/xhtml/cl_khr_fp64.html). Ha a videokártya nem támogatja a `double` típust, a direktíva engedélyezése nem oldja meg a problémát.

Az OpenCL-forráskódot célszerű külön CL-fájlokban tárolni, majd [erőforrás-változókkal](../MQL5-programs/Resources/Resources.md#resourcevariables) beilleszteni az MQL5-programba.

### OpenCL-programhibák kezelése

Az OpenCL-program legutóbbi hibájáról a [CLGetInfoInteger](CLGetInfoInteger/CLGetInfoInteger.md) és a [CLGetInfoString](CLGetInfoString/CLGetInfoString.md) függvénnyel kérhető le hibakód és szöveges leírás.

A legutóbbi hibakód lekéréséhez hívd meg a [CLGetInfoInteger](CLGetInfoInteger/CLGetInfoInteger.md) függvényt; a `handle` paraméter ilyenkor figyelmen kívül marad, értéke lehet nulla. A hibakódok leírása az [OpenCL specifikációban](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_API.html#CL_SUCCESS) található. Ismeretlen hibakód esetén a függvény az `unknown OpenCL error N` szöveget adja vissza, ahol az `N` a hibakód.

```cpp
//--- a 'handle' első paramétert a legutóbbi hibakód lekérésekor figyelmen kívül hagyja
int code = (int)CLGetInfoInteger(0,CL_LAST_ERROR);
```

A hiba szöveges leírásához a hibakódot kell átadni a [CLGetInfoString](CLGetInfoString/CLGetInfoString.md) függvény `handle` paramétereként. Ha a hibakód helyett a `CL_LAST_ERROR` értéket adod át, a függvény közvetlenül a legutóbbi hiba leírását adja vissza.

```cpp
//--- a legutóbbi OpenCL-hibakód lekérése
int    code = (int)CLGetInfoInteger(0,CL_LAST_ERROR);
string desc; // hiba szöveges leírása
//--- a kód alapján lekérjük a hiba leírását
if(!CLGetInfoString(code,CL_ERROR_DESCRIPTION,desc))
   desc="cannot get OpenCL error description,"+(string)GetLastError();
Print(desc);
//--- a kód előzetes lekérése nélkül, közvetlenül a legutóbbi hiba leírása
if(!CLGetInfoString(CL_LAST_ERROR,CL_ERROR_DESCRIPTION,desc))
   desc="cannot get OpenCL error description,"+(string)GetLastError();
Print(desc);
```

A leírás az OpenCL belső felsorolásának nevét tartalmazza. A kódok értelmezése az [OpenCL specifikációban](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_API.html#CL_SUCCESS) található. Például a `CL_INVALID_KERNEL_ARGS` azt jelenti, hogy a kernel futtatásakor egyes argumentumok nincsenek beállítva vagy érvénytelenek.

### OpenCL-programok kezelésére szolgáló függvények

| Függvény | Működés |
| --- | --- |
| [CLHandleType](CLHandleType/CLHandleType.md) | Visszaadja egy OpenCL-leíró típusát az `ENUM_OPENCL_HANDLE_TYPE` felsorolás értékeként. |
| [CLGetInfoInteger](CLGetInfoInteger/CLGetInfoInteger.md) | Lekéri egy OpenCL-objektum vagy -eszköz egész típusú tulajdonságát. |
| [CLContextCreate](CLContextCreate/CLContextCreate.md) | Létrehoz egy OpenCL-környezetet. |
| [CLContextFree](CLContextFree/CLContextFree.md) | Felszabadít egy OpenCL-környezetet. |
| [CLGetDeviceInfo](CLGetDeviceInfo/CLGetDeviceInfo.md) | Lekéri az eszköz tulajdonságait az OpenCL-illesztőprogramtól. |
| [CLProgramCreate](CLProgramCreate/CLProgramCreate.md) | OpenCL-programot hoz létre forráskódból. |
| [CLProgramFree](CLProgramFree/CLProgramFree.md) | Felszabadít egy OpenCL-programot. |
| [CLKernelCreate](CLKernelCreate/CLKernelCreate.md) | Létrehoz egy OpenCL-kernelt. |
| [CLKernelFree](CLKernelFree/CLKernelFree.md) | Felszabadít egy OpenCL-kernelt. |
| [CLSetKernelArg](CLSetKernelArg/CLSetKernelArg.md) | Beállítja az OpenCL-kernel egyik paraméterét. |
| [CLSetKernelArgMem](CLSetKernelArgMem/CLSetKernelArgMem.md) | OpenCL-puffert ad át a kernel egyik paramétereként. |
| [CLSetKernelArgMemLocal](CLSetKernelArgMemLocal/CLSetKernelArgMemLocal.md) | Helyi puffert állít be a kernel argumentumaként. |
| [CLBufferCreate](CLBufferCreate/CLBufferCreate.md) | Létrehoz egy OpenCL-puffert. |
| [CLBufferFree](CLBufferFree/CLBufferFree.md) | Felszabadít egy OpenCL-puffert. |
| [CLBufferWrite](CLBufferWrite/CLBufferWrite.md) | Tömböt ír egy OpenCL-pufferbe. |
| [CLBufferRead](CLBufferRead/CLBufferRead.md) | Beolvassa egy OpenCL-puffer tartalmát egy tömbbe. |
| [CLExecute](CLExecute/CLExecute.md) | Futtat egy OpenCL-programot. |
| [CLExecutionStatus](CLExecutionStatus/CLExecutionStatus.md) | Visszaadja az OpenCL-program végrehajtási állapotát. |

Lásd még: [OpenCL a standard könyvtárban](../Standard-Library/OpenCL/OpenCL.md), [Erőforrások](../MQL5-programs/Resources/Resources.md#resourcevariables).
