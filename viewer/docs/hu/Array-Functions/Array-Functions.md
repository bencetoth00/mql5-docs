# Tömbfüggvények

# Tömbkezelő függvények

A [tömbök](../Language-Basics/Variables/Variables.md#array_define) legfeljebb négydimenziósak lehetnek. Minden dimenzió indexelése 0-tól a dimenzió mérete mínusz 1 értékig tart. Egy 50 elemű, egydimenziós tömb első eleme például `array[0]`, az utolsó pedig `array[49]`.

| Függvény | Működés |
| --- | --- |
| [ArrayBsearch](ArrayBsearch/ArrayBsearch.md) | Visszaadja az első megtalált elem indexét a tömb első dimenziójában. |
| [ArrayCopy](ArrayCopy/ArrayCopy.md) | Egy tömböt egy másikba másol. |
| [ArrayCompare](ArrayCompare/ArrayCompare.md) | Összehasonlít két [egyszerű típusokat](../Language-Basics/Data-Types/Data-Types.md#base_types) vagy [összetett objektumok](../Language-Basics/Data-Types/Data-Types.md#complex_types) nélküli egyéni struktúrákat tartalmazó tömböt. |
| [ArrayFree](ArrayFree/ArrayFree.md) | Felszabadítja bármely dinamikus tömb pufferét, és a nulladik dimenzió méretét 0-ra állítja. |
| [ArrayGetAsSeries](ArrayGetAsSeries/ArrayGetAsSeries.md) | Ellenőrzi a tömb indexelési irányát. |
| [ArrayInitialize](ArrayInitialize/ArrayInitialize.md) | Egyetlen értéket rendel egy numerikus tömb minden eleméhez. |
| [ArrayFill](ArrayFill/ArrayFill.md) | Feltölti a tömböt a megadott értékkel. |
| [ArrayIsSeries](ArrayIsSeries/ArrayIsSeries.md) | Ellenőrzi, hogy a tömb idősor-e. |
| [ArrayIsDynamic](ArrayIsDynamic/ArrayIsDynamic.md) | Ellenőrzi, hogy a tömb dinamikus-e. |
| [ArrayMaximum](ArrayMaximum/ArrayMaximum.md) | Megkeresi a legnagyobb értékű elemet. |
| [ArrayMinimum](ArrayMinimum/ArrayMinimum.md) | Megkeresi a legkisebb értékű elemet. |
| [ArrayPrint](ArrayPrint/ArrayPrint.md) | Egyszerű típusú tömböt vagy egyszerű struktúrát ír a naplóba. |
| [ArrayRange](ArrayRange/ArrayRange.md) | Visszaadja a tömb megadott dimenziójának elemszámát. |
| [ArrayResize](ArrayResize/ArrayResize.md) | Beállítja a tömb első dimenziójának új méretét. |
| [ArrayInsert](ArrayInsert/ArrayInsert.md) | A forrástömb megadott számú elemét a megadott indextől kezdve beilleszti a fogadó tömbbe. |
| [ArrayRemove](ArrayRemove/ArrayRemove.md) | A megadott indextől kezdve eltávolítja a tömb megadott számú elemét. |
| [ArrayReverse](ArrayReverse/ArrayReverse.md) | Megfordítja a tömb megadott indextől kezdődő, megadott számú elemének sorrendjét. |
| [ArraySetAsSeries](ArraySetAsSeries/ArraySetAsSeries.md) | Beállítja a tömb indexelési irányát. |
| [ArraySize](ArraySize/ArraySize.md) | Visszaadja a tömb elemeinek számát. |
| [ArraySort](ArraySort/ArraySort.md) | Az első dimenzió szerint rendezi a numerikus tömböt. |
| [ArraySwap](ArraySwap/ArraySwap.md) | Felcseréli két azonos típusú dinamikus tömb tartalmát. |
| [ArrayToFP16](ArrayToFP16/ArrayToFP16.md) | A megadott formátumban float vagy double típusú tömböt ushort típusú tömbbe másol. |
| [ArrayToFP8](ArrayToFP8/ArrayToFP8.md) | A megadott formátumban float vagy double típusú tömböt uchar típusú tömbbe másol. |
| [ArrayFromFP16](ArrayFromFP16/ArrayFromFP16.md) | A megadott formátumban ushort típusú tömböt float vagy double típusú tömbbe másol. |
| [ArrayFromFP8](ArrayFromFP8/ArrayFromFP8.md) | A megadott formátumban uchar típusú tömböt float vagy double típusú tömbbe másol. |
