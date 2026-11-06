# Kereskedési függvények

Ez a függvénycsoport a kereskedési műveletek kezelésére szolgál.

A kereskedési függvények használata előtt ismerd meg az alapfogalmakat: megbízás, ügylet és pozíció.

- A **megbízás** utasítás a bróker számára egy pénzügyi eszköz vételére vagy eladására. Két fő típusa a piaci és a függő megbízás. Emellett léteznek speciális Take Profit- és Stop Loss-szintek.
- Az **ügylet** pénzügyi eszköz vételét vagy eladását jelenti. A vétel a keresleti áron (Ask), az eladás a kínálati áron (Bid) történik. Ügylet piaci megbízás végrehajtásakor vagy függő megbízás aktiválásakor jöhet létre. Egy megbízás végrehajtása bizonyos esetekben több ügyletet is eredményezhet.
- A **pozíció** egy pénzügyi eszköz megvásárolt vagy eladott kontraktusainak mennyisége, vagyis kereskedési kötelezettség. A long pozíció vásárlást jelent arra számítva, hogy az ár emelkedik. A short pozíció eladási kötelezettséget jelent arra számítva, hogy az ár később csökken.

A kereskedési műveletekről további információ a [MetaTrader 5 súgójában](https://www.metatrader5.com/en/terminal/help/trading/general_concept "MetaTrader 5 súgó") található.

A kereskedési függvények Expert Advisorokban és szkriptekben használhatók. Meghívásukhoz engedélyezni kell az Expert Advisor vagy a szkript tulajdonságai között az „Élő kereskedés engedélyezése” beállítást.

A kereskedést a [Kereskedési jogosultság](../MQL5-programs/Trade-Permission/Trade-Permission.md) fejezetben ismertetett különböző tényezők engedélyezhetik vagy tilthatják.

| Függvény | Működés |
| --- | --- |
| [OrderCalcMargin](OrderCalcMargin/OrderCalcMargin.md) | Kiszámítja a megadott megbízástípushoz szükséges fedezetet a számla devizájában. |
| [OrderCalcProfit](OrderCalcProfit/OrderCalcProfit.md) | A paraméterek alapján kiszámítja az eredményt a számla devizájában. |
| [OrderCheck](OrderCheck/OrderCheck.md) | Ellenőrzi, hogy rendelkezésre áll-e a szükséges fedezet a [kereskedési művelethez](../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md). |
| [OrderSend](OrderSend/OrderSend.md) | [Kereskedési kérést](../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) küld a szervernek. |
| [OrderSendAsync](OrderSendAsync/OrderSendAsync.md) | A kereskedési szerver válaszának megvárása nélkül, aszinkron módon küld [kereskedési kérést](../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md). |
| [PositionsTotal](PositionsTotal/PositionsTotal.md) | Visszaadja a nyitott pozíciók számát. |
| [PositionGetSymbol](PositionGetSymbol/PositionGetSymbol.md) | Visszaadja a nyitott pozícióhoz tartozó szimbólumot. |
| [PositionSelect](PositionSelect/PositionSelect.md) | Kiválaszt egy nyitott pozíciót további kezeléshez. |
| [PositionSelectByTicket](PositionSelectByTicket/PositionSelectByTicket.md) | A megadott jegyszám alapján kiválaszt egy pozíciót. |
| [PositionGetDouble](PositionGetDouble/PositionGetDouble.md) | Lekéri a nyitott pozíció kért double típusú tulajdonságát. |
| [PositionGetInteger](PositionGetInteger/PositionGetInteger.md) | Lekéri a nyitott pozíció kért datetime vagy int típusú tulajdonságát. |
| [PositionGetString](PositionGetString/PositionGetString.md) | Lekéri a nyitott pozíció kért szöveges tulajdonságát. |
| [PositionGetTicket](PositionGetTicket/PositionGetTicket.md) | Visszaadja a nyitott pozíciók listájában a megadott indexű pozíció jegyszámát. |
| [OrdersTotal](OrdersTotal/OrdersTotal.md) | Visszaadja a megbízások számát. |
| [OrderGetTicket](OrderGetTicket/OrderGetTicket.md) | Visszaadja a megfelelő megbízás jegyszámát. |
| [OrderSelect](OrderSelect/OrderSelect.md) | Kiválaszt egy megbízást további kezelésre. |
| [OrderGetDouble](OrderGetDouble/OrderGetDouble.md) | Lekéri a megbízás kért double típusú tulajdonságát. |
| [OrderGetInteger](OrderGetInteger/OrderGetInteger.md) | Lekéri a megbízás kért datetime vagy int típusú tulajdonságát. |
| [OrderGetString](OrderGetString/OrderGetString.md) | Lekéri a megbízás kért szöveges tulajdonságát. |
| [HistorySelect](HistorySelect/HistorySelect.md) | Lekéri a megadott szerveridőszak tranzakció- és megbízáselőzményeit. |
| [HistorySelectByPosition](HistorySelectByPosition/HistorySelectByPosition.md) | Lekéri a megadott [pozícióazonosítóhoz](../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer) tartozó ügyletek előzményeit. |
| [HistoryOrderSelect](HistoryOrderSelect/HistoryOrderSelect.md) | Kiválaszt egy előzményben szereplő megbízást további kezelésre. |
| [HistoryOrdersTotal](HistoryOrdersTotal/HistoryOrdersTotal.md) | Visszaadja az előzményekben szereplő megbízások számát. |
| [HistoryOrderGetTicket](HistoryOrderGetTicket/HistoryOrderGetTicket.md) | Visszaadja az előzményekben szereplő megfelelő megbízás jegyszámát. |
| [HistoryOrderGetDouble](HistoryOrderGetDouble/HistoryOrderGetDouble.md) | Lekéri az előzményekben szereplő megbízás kért double tulajdonságát. |
| [HistoryOrderGetInteger](HistoryOrderGetInteger/HistoryOrderGetInteger.md) | Lekéri az előzményekben szereplő megbízás kért datetime vagy int tulajdonságát. |
| [HistoryOrderGetString](HistoryOrderGetString/HistoryOrderGetString.md) | Lekéri az előzményekben szereplő megbízás kért szöveges tulajdonságát. |
| [HistoryDealSelect](HistoryDealSelect/HistoryDealSelect.md) | Kiválaszt egy előzményben szereplő ügyletet a megfelelő függvényekkel történő további lekéréshez. |
| [HistoryDealsTotal](HistoryDealsTotal/HistoryDealsTotal.md) | Visszaadja az előzményekben szereplő ügyletek számát. |
| [HistoryDealGetTicket](HistoryDealGetTicket/HistoryDealGetTicket.md) | Visszaadja az előzményekben szereplő megfelelő ügylet jegyszámát. |
| [HistoryDealGetDouble](HistoryDealGetDouble/HistoryDealGetDouble.md) | Lekéri az előzményekben szereplő ügylet kért double típusú tulajdonságát. |
| [HistoryDealGetInteger](HistoryDealGetInteger/HistoryDealGetInteger.md) | Lekéri az előzményekben szereplő ügylet kért datetime vagy int típusú tulajdonságát. |
| [HistoryDealGetString](HistoryDealGetString/HistoryDealGetString.md) | Lekéri az előzményekben szereplő ügylet kért szöveges tulajdonságát. |
