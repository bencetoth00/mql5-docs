# Eseménykezelés

Az MQL5 nyelv bizonyos [előre definiált események](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md) kezelését teszi lehetővé. Ezekhez az eseménykezelő függvényeket az MQL5-programban kell definiálni: a függvény nevének, visszatérési típusának, paramétereinek és azok típusainak pontosan meg kell egyezniük az eseménykezelő leírásával.

Az ügyfélterminál a visszatérési érték és a paraméterek típusa alapján azonosítja az eseményt kezelő függvényeket. Ha egy függvény paraméterei vagy visszatérési típusa eltér az alábbi leírástól, a függvény nem használható eseménykezelésre.

| Függvény | Leírás |
| --- | --- |
| [OnStart](OnStart/OnStart.md) | A [Start](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#start) eseménykor hívódik meg, és végrehajtja a szkript műveleteit. |
| [OnInit](OnInit/OnInit.md) | Induló indikátorokban és EA-kban, az [Init](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#init) eseménykor inicializálja az MQL5-programot. |
| [OnDeinit](OnDeinit/OnDeinit.md) | Indikátorokban és EA-kban, a [Deinit](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#deinit) eseménykor megszünteti az MQL5-program inicializálását. |
| [OnTick](OnTick/OnTick.md) | EA-kban, a [NewTick](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#newtick) eseménykor kezeli az új jegyzést. |
| [OnCalculate](OnCalculate/OnCalculate.md) | Indikátorokban, a [Calculate](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#calculate) eseménykor kezeli az ár adataiban bekövetkező változásokat. |
| [OnTimer](OnTimer/OnTimer.md) | Indikátorokban és EA-kban a terminál által rögzített időközönként előállított [Timer](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#timer) eseménykor hívódik meg. |
| [OnTrade](OnTrade/OnTrade.md) | EA-kban a kereskedési szerveren végrehajtott művelet után keletkező [Trade](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#trade) eseménykor hívódik meg. |
| [OnTradeTransaction](OnTradeTransaction/OnTradeTransaction.md) | EA-kban a [TradeTransaction](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#tradetransaction) eseménykor feldolgozza a kereskedési kérés végrehajtásának eredményét. |
| [OnBookEvent](OnBookEvent/OnBookEvent.md) | EA-kban a [BookEvent](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#bookevent) eseménykor feldolgozza a Piacmélység változásait. |
| [OnChartEvent](OnChartEvent/OnChartEvent.md) | Indikátorokban és EA-kban a [ChartEvent](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#chartevent) eseménykor feldolgozza a felhasználó vagy egy MQL5-program által előidézett diagramváltozásokat. |
| [OnTester](OnTester/OnTester.md) | EA-kban a [Tester](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#tester) eseménykor a múltbeli adatokon végzett tesztelés után hajtja végre a szükséges műveleteket. |
| [OnTesterInit](OnTesterInit/OnTesterInit.md) | EA-kban a [TesterInit](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerinit) eseménykor, a Stratégiateszter optimalizálása előtt hívódik meg. |
| [OnTesterDeinit](OnTesterDeinit/OnTesterDeinit.md) | EA-optimalizálás után, a Stratégiateszter [TesterDeinit](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerdeinit) eseményekor hívódik meg. |
| [OnTesterPass](OnTesterPass/OnTesterPass.md) | EA-kban a [TesterPass](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerpass) eseménykor feldolgozza az optimalizálás során érkező új adatkeretet. |

Az ügyfélterminál a beérkező eseményeket a megfelelő megnyitott diagramoknak küldi. Eseményt diagramok ([diagram-események](OnChartEvent/OnChartEvent.md)) és MQL5-programok ([egyéni események](../Working-with-Events/EventChartCustom/EventChartCustom.md)) is előállíthatnak. A grafikus objektumok létrehozásáról és törléséről szóló események a [CHART\_EVENT\_OBJECT\_CREATE](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) és [CHART\_EVENT\_OBJECT\_DELETE](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) diagramtulajdonságokkal engedélyezhetők vagy tilthatók. Minden MQL5-alkalmazásnak és diagramnak saját eseménysora van, amelybe az újonnan érkező események kerülnek.

A program csak arról a diagramról kap eseményeket, amelyen fut. Az események a beérkezésük sorrendjében, egymás után kerülnek feldolgozásra. Ha az eseménysor már tartalmaz egy [NewTick](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#newtick) eseményt, vagy annak feldolgozása folyamatban van, az új NewTick esemény nem kerül az MQL5-alkalmazás sorába. Ugyanez érvényes a [ChartEvent](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#chartevent) eseményre. Az időzítőesemények is így működnek: ha a [Timer](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#timer) már a sorban van vagy feldolgozás alatt áll, új Timer esemény nem kerül a sorba.

Az eseménysorok mérete korlátozott, de megfelelő programnál elegendő, ezért a túlcsordulás nem valószínű. Túlcsorduláskor az új események kimaradnak a sorból.

Események kezeléséhez erősen ajánlott elkerülni a végtelen ciklusokat. Kivételt jelenthetnek az egyszeri [Start](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#start) eseményt kezelő szkriptek.

[A könyvtárak](../index.md#library) nem kezelnek eseményeket.
