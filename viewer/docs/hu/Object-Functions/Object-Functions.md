# Objektumfüggvények

Ez a függvénycsoport egy megadott diagram grafikus objektumainak kezelésére szolgál.

A grafikus objektumok tulajdonságait meghatározó, valamint az objektumokat létrehozó [ObjectCreate()](ObjectCreate/ObjectCreate.md) és mozgató [ObjectMove()](ObjectMove/ObjectMove.md) függvények parancsokat küldenek a diagramnak. Sikeres híváskor a parancs bekerül a diagram eseménysorába. A grafikus objektumok látható tulajdonságai az eseménysor feldolgozásakor változnak meg.

Ezért e függvények meghívása után ne várj azonnali vizuális frissítést. A terminál általában automatikusan frissíti a diagram objektumait, például új jegyzés érkezésekor vagy a diagramablak átméretezésekor. A grafikus objektumok kényszerített frissítésére használd a [ChartRedraw()](../Chart-Operations/ChartRedraw/ChartRedraw.md) függvényt.

| Függvény | Működés |
| --- | --- |
| [ObjectCreate](ObjectCreate/ObjectCreate.md) | A megadott típusú objektumot hoz létre a megadott diagramon. |
| [ObjectName](ObjectName/ObjectName.md) | Visszaadja a megadott diagram adott alablakában található, megfelelő típusú objektum nevét. |
| [ObjectDelete](ObjectDelete/ObjectDelete.md) | Eltávolítja a megadott nevű objektumot a diagramról vagy annak megadott alablakából. |
| [ObjectsDeleteAll](ObjectsDeleteAll/ObjectsDeleteAll.md) | Eltávolítja a megadott típusú összes objektumot a diagramról vagy annak megadott alablakából. |
| [ObjectFind](ObjectFind/ObjectFind.md) | Név alapján megkeresi a megadott azonosítójú objektumot. |
| [ObjectGetTimeByValue](ObjectGetTimeByValue/ObjectGetTimeByValue.md) | Visszaadja a megadott objektumár-értékhez tartozó időt. |
| [ObjectGetValueByTime](ObjectGetValueByTime/ObjectGetValueByTime.md) | Visszaadja az objektum árértékét a megadott időponthoz. |
| [ObjectMove](ObjectMove/ObjectMove.md) | Módosítja a megadott objektum rögzítési pontjának koordinátáit. |
| [ObjectsTotal](ObjectsTotal/ObjectsTotal.md) | Visszaadja a megadott típusú objektumok számát a diagramon vagy annak megadott alablakában. |
| [ObjectGetDouble](ObjectGetDouble/ObjectGetDouble.md) | Visszaadja az objektum megfelelő tulajdonságának double értékét. |
| [ObjectGetInteger](ObjectGetInteger/ObjectGetInteger.md) | Visszaadja az objektum megfelelő tulajdonságának egész típusú értékét. |
| [ObjectGetString](ObjectGetString/ObjectGetString.md) | Visszaadja az objektum megfelelő tulajdonságának szöveges értékét. |
| [ObjectSetDouble](ObjectSetDouble/ObjectSetDouble.md) | Beállítja az objektum megfelelő tulajdonságának értékét. |
| [ObjectSetInteger](ObjectSetInteger/ObjectSetInteger.md) | Beállítja az objektum megfelelő tulajdonságának értékét. |
| [ObjectSetString](ObjectSetString/ObjectSetString.md) | Beállítja az objektum megfelelő tulajdonságának értékét. |
| [TextSetFont](TextSetFont/TextSetFont.md) | Beállítja a rajzolási módszerekkel megjelenített szöveg betűtípusát; az alapértelmezett Arial 20. |
| [TextOut](TextOut/TextOut.md) | Szöveget ír a grafikus [erőforrás](../Common-Functions/ResourceCreate/ResourceCreate.md) létrehozására szolgáló egyéni tömbbe (pufferbe). |
| [TextGetSize](TextGetSize/TextGetSize.md) | Visszaadja a karakterlánc szélességét és magasságát az aktuális [betűtípus-beállításokkal](TextSetFont/TextSetFont.md). |

Minden grafikus objektumnak egyedi nevet kell adni az adott [diagramon](../Chart-Operations/Chart-Operations.md), az alablakokat is beleértve. Az objektum átnevezése két eseményt vált ki: a régi nevű objektum törlését és az új nevű objektum létrehozását.

Objektum létrehozása vagy valamely [tulajdonságának](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md) módosítása után ajánlott meghívni a [ChartRedraw()](../Chart-Operations/ChartRedraw/ChartRedraw.md) függvényt. Ez utasítja az ügyfélterminált a diagram és minden [látható objektum](../Constants,-Enumerations-and-Structures/Objects-Constants/Visibility-of-Objects/Visibility-of-Objects.md) kényszerített újrarajzolására.
