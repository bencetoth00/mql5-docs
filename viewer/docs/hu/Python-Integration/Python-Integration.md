# Python-integráció

# MetaTrader-modul Python-integrációhoz

Az MQL5 nagy teljesítményű pénzügyi kereskedési alkalmazások fejlesztésére készült. A nyelv szintaxisa és sebessége közel áll a C++-hoz; támogatja az [OpenCL](../Working-with-OpenCL/Working-with-OpenCL.md) használatát és a [Visual Studióval való integrációt](https://www.metatrader5.com/en/metaeditor/help/development/c_dll). A MetaEditor közvetlenül támogatja a .NET-könyvtárakat, és külső C++ DLL-ek is használhatók.

A Python modern, magas szintű programozási nyelv szkriptek és alkalmazások fejlesztéséhez. Számos gépi tanulási, automatizálási, adatelemzési és adatvizualizációs könyvtár érhető el hozzá.

A MetaTrader Python-csomagja lehetővé teszi, hogy a MetaTrader 5 terminálból közvetlenül, folyamatok közötti kommunikációval piaci adatokat kérj le. Az adatok statisztikai számításokhoz és gépi tanuláshoz is felhasználhatók.

A csomag telepítése parancssorból:

```bash
pip install MetaTrader5
```

A csomag frissítése:

```bash
pip install --upgrade MetaTrader5
```

### A MetaTrader 5 és a Python összekapcsolására szolgáló függvények

| Függvény | Működés |
| --- | --- |
| [initialize](initialize/initialize.md) | Kapcsolatot létesít a MetaTrader 5 terminállal. |
| [login](login/login.md) | A megadott adatokkal csatlakozik egy kereskedési számlához. |
| [shutdown](shutdown/shutdown.md) | Lezárja a korábban létrehozott terminálkapcsolatot. |
| [version](version/version.md) | Visszaadja a MetaTrader 5 terminál verzióját. |
| [last_error](last_error/last_error.md) | Visszaadja az utolsó hibára vonatkozó adatokat. |
| [account_info](account_info/account_info.md) | Lekéri az aktuális kereskedési számla adatait. |
| [terminal_info](terminal_info/terminal_info.md) | Lekéri a csatlakoztatott terminál állapotát és paramétereit. |
| [symbols_total](symbols_total/symbols_total.md) | Visszaadja a terminálban elérhető pénzügyi instrumentumok számát. |
| [symbols_get](symbols_get/symbols_get.md) | Lekéri a terminálban elérhető pénzügyi instrumentumokat. |
| [symbol_info](symbol_info/symbol_info.md) | Lekéri a megadott pénzügyi instrumentum adatait. |
| [symbol_info_tick](symbol_info_tick/symbol_info_tick.md) | Lekéri a megadott instrumentum legutóbbi tickjét. |
| [symbol_select](symbol_select/symbol_select.md) | Kiválaszt vagy eltávolít egy szimbólumot a Piacfigyelő ablakból. |
| [copy_rates_from](copy_rates_from/copy_rates_from.md) | A megadott dátumtól kezdődően gyertyákat kér le. |
| [copy_rates_from_pos](copy_rates_from_pos/copy_rates_from_pos.md) | A megadott indextől kezdődően gyertyákat kér le. |
| [copy_rates_range](copy_rates_range/copy_rates_range.md) | A megadott dátumtartomány gyertyáit kéri le. |
| [copy_ticks_from](copy_ticks_from/copy_ticks_from.md) | A megadott dátumtól kezdődően tickeket kér le. |
| [copy_ticks_range](copy_ticks_range/copy_ticks_range.md) | A megadott dátumtartomány tickjeit kéri le. |
| [orders_total](orders_total/orders_total.md) | Visszaadja az aktív megbízások számát. |
| [orders_get](orders_get/orders_get.md) | Lekéri az aktív megbízásokat, szükség esetén szimbólum vagy jegy alapján szűrve. |
| [order_calc_margin](order_calc_margin/order_calc_margin.md) | Kiszámítja egy kereskedési művelet letéti igényét a számla pénznemében. |
| [order_calc_profit](order_calc_profit/order_calc_profit.md) | Kiszámítja egy kereskedési művelet eredményét a számla pénznemében. |
| [order_check](order_check/order_check.md) | Ellenőrzi, hogy rendelkezésre áll-e a szükséges fedezet. |
| [order_send](order_send/order_send.md) | Kereskedési művelet végrehajtására irányuló kérést küld. |
| [positions_total](positions_total/positions_total.md) | Visszaadja a nyitott pozíciók számát. |
| [positions_get](positions_get/positions_get.md) | Lekéri a nyitott pozíciókat, szükség esetén szimbólum vagy jegy szerint szűrve. |
| [history_orders_get](history_orders_get/history_orders_get.md) | Lekéri az előzmények megbízásait, jegy vagy pozíció alapján szűrve. |
| [history_deals_get](history_deals_get/history_deals_get.md) | Lekéri az előzmények kötéseit, jegy vagy pozíció alapján szűrve. |

### Csatlakozás a MetaTrader 5-höz Pythonból

Telepítsd a Python 3-at, majd parancssorból a MetaTrader 5 csomagot és az igényelt adatelemző könyvtárakat. A kapcsolat létrehozásához használd az `initialize` függvényt; a munka befejezésekor zárd le a kapcsolatot a `shutdown` függvénnyel.
