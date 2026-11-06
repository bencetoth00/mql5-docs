# Egyéni szimbólumok

Ezek a függvények egyéni szimbólumok létrehozására és tulajdonságaik szerkesztésére szolgálnak.

Ha a terminál csatlakozik egy kereskedési szerverhez, a felhasználó hozzáfér a bróker által biztosított pénzügyi szimbólumok [idősoraihoz](../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md). Az elérhető szimbólumok a Piacfigyelő ablakban jelennek meg. Külön függvénycsoport szolgál a [szimbólumok tulajdonságainak lekérésére](../Market-Info/Market-Info.md), a kereskedési munkamenetek kezelésére és a Piacmélység változásainak fogadására.

Az itt ismertetett függvényekkel egyéni szimbólumok hozhatók létre a kereskedési szerver meglévő szimbólumai, szövegfájlok vagy külső adatforrások felhasználásával.

| Függvény | Működés |
| --- | --- |
| [CustomSymbolCreate](CustomSymbolCreate/CustomSymbolCreate.md) | Létrehoz egy egyéni szimbólumot a megadott névvel és csoportban. |
| [CustomSymbolDelete](CustomSymbolDelete/CustomSymbolDelete.md) | Törli a megadott nevű egyéni szimbólumot. |
| [CustomSymbolSetInteger](CustomSymbolSetInteger/CustomSymbolSetInteger.md) | Beállítja az egyéni szimbólum egész típusú tulajdonságát. |
| [CustomSymbolSetDouble](CustomSymbolSetDouble/CustomSymbolSetDouble.md) | Beállítja az egyéni szimbólum valós típusú tulajdonságát. |
| [CustomSymbolSetString](CustomSymbolSetString/CustomSymbolSetString.md) | Beállítja az egyéni szimbólum szöveges tulajdonságát. |
| [CustomSymbolSetMarginRate](CustomSymbolSetMarginRate/CustomSymbolSetMarginRate.md) | Beállítja a fedezeti rátákat a megbízás típusától és irányától függően. |
| [CustomSymbolSetSessionQuote](CustomSymbolSetSessionQuote/CustomSymbolSetSessionQuote.md) | Beállítja a megadott szimbólum adott hétköznapra érvényes jegyzési munkamenetének kezdő és záró idejét. |
| [CustomSymbolSetSessionTrade](CustomSymbolSetSessionTrade/CustomSymbolSetSessionTrade.md) | Beállítja a megadott szimbólum adott hétköznapra érvényes kereskedési munkamenetének kezdő és záró idejét. |
| [CustomRatesDelete](CustomRatesDelete/CustomRatesDelete.md) | Törli az egyéni szimbólum árfolyam-előzményeinek összes gyertyáját a megadott időszakból. |
| [CustomRatesReplace](CustomRatesReplace/CustomRatesReplace.md) | A megadott időszakban teljesen lecseréli az egyéni szimbólum árfolyam-előzményeit a MqlRates tömb adataira. |
| [CustomRatesUpdate](CustomRatesUpdate/CustomRatesUpdate.md) | Hozzáadja a hiányzó gyertyákat az egyéni szimbólum előzményeihez, a meglévő adatokat pedig lecseréli a MqlRates tömb adataira. |
| [CustomTicksAdd](CustomTicksAdd/CustomTicksAdd.md) | Az MqlTick tömb adatait hozzáadja az egyéni szimbólum árfolyam-előzményeihez. A szimbólumot ki kell választani a Piacfigyelőben. |
| [CustomTicksDelete](CustomTicksDelete/CustomTicksDelete.md) | Törli az egyéni szimbólum árfolyam-előzményeinek összes tickjét a megadott időszakból. |
| [CustomTicksReplace](CustomTicksReplace/CustomTicksReplace.md) | A megadott időszakban teljesen lecseréli az egyéni szimbólum tick-előzményeit az MqlTick tömb adataira. |
| [CustomBookAdd](CustomBookAdd/CustomBookAdd.md) | Beállítja az egyéni szimbólum Piacmélységének állapotát. |
