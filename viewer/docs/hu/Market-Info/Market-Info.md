# Piaci információk

Ezek a függvények a piac állapotáról szolgáltatnak adatokat.

| Függvény | Működés |
| --- | --- |
| [SymbolsTotal](SymbolsTotal/SymbolsTotal.md) | A rendelkezésre álló szimbólumok számát adja vissza; a kiválasztottakat vagy az összeset veszi figyelembe. |
| [SymbolExist](SymbolExist/SymbolExist.md) | Ellenőrzi, hogy létezik-e a megadott nevű szimbólum. |
| [SymbolName](SymbolName/SymbolName.md) | Visszaadja a megadott szimbólum nevét. |
| [SymbolSelect](SymbolSelect/SymbolSelect.md) | Kiválaszt egy szimbólumot a Piacfigyelő ablakban, vagy eltávolítja onnan. |
| [SymbolIsSynchronized](SymbolIsSynchronized/SymbolIsSynchronized.md) | Ellenőrzi, hogy a terminálban kiválasztott szimbólum adatai [szinkronban vannak-e](../Timeseries-and-Indicators-Access/Organizing-Data-Access/Organizing-Data-Access.md#synchronized) a kereskedési szerver adataival. |
| [SymbolInfoDouble](SymbolInfoDouble/SymbolInfoDouble.md) | Visszaadja a szimbólum megfelelő tulajdonságának double típusú értékét. |
| [SymbolInfoInteger](SymbolInfoInteger/SymbolInfoInteger.md) | Visszaadja a megadott szimbólum megfelelő tulajdonságának egész típusú (long, datetime, int vagy bool) értékét. |
| [SymbolInfoString](SymbolInfoString/SymbolInfoString.md) | Visszaadja a megadott szimbólum megfelelő tulajdonságának szöveges értékét. |
| [SymbolInfoMarginRate](SymbolInfoMarginRate/SymbolInfoMarginRate.md) | Visszaadja a fedezeti rátákat a megbízás típusától és irányától függően. |
| [SymbolInfoTick](SymbolInfoTick/SymbolInfoTick.md) | A megadott szimbólum aktuális árait egy [MqlTick](../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) típusú változóban adja vissza. |
| [SymbolInfoSessionQuote](SymbolInfoSessionQuote/SymbolInfoSessionQuote.md) | Lekéri a megadott szimbólum adott hétköznapra érvényes jegyzési munkameneteinek kezdő és záró idejét. |
| [SymbolInfoSessionTrade](SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) | Lekéri a megadott szimbólum adott hétköznapra érvényes kereskedési munkameneteinek kezdő és záró idejét. |
| [MarketBookAdd](MarketBookAdd/MarketBookAdd.md) | Megnyitja a kiválasztott szimbólum Piacmélységét, és feliratkozik a változásokról szóló értesítésekre. |
| [MarketBookRelease](MarketBookRelease/MarketBookRelease.md) | Bezárja a kiválasztott szimbólum Piacmélységét, és lemond a változásokról szóló értesítésekről. |
| [MarketBookGet](MarketBookGet/MarketBookGet.md) | A megadott szimbólum Piacmélységének rekordjait tartalmazó [MqlBookInfo](../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) struktúratömböt adja vissza. |
