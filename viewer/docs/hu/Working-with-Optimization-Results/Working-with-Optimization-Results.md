# Optimalizálási eredmények feldolgozása

Ezekkel a függvényekkel egyéni módon dolgozhatók fel a Stratégiateszter optimalizálási eredményei. Optimalizálás közben a tesztügynökökből, valamint helyben Expert Advisorokból és szkriptekből is meghívhatók.

Amikor Expert Advisort futtatsz a Stratégiateszterben, egyszerű típusokból vagy [egyszerű struktúrákból](../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure) álló saját adattömböt hozhatsz létre. Az egyszerű struktúra nem tartalmazhat stringet, osztályobjektumot vagy dinamikus tömb objektumát. Az adatkészlet a [FrameAdd()](FrameAdd/FrameAdd.md) függvénnyel egy speciális keretbe menthető. Az Expert Advisor optimalizálása során minden tesztügynök keretek sorozatát küldheti a terminálnak. A fogadott keretek az Expert Advisor nevét viselő `*.MQD` fájlba kerülnek, a `terminal_directory\MQL5\Files\Tester` mappába, az ügynököktől való beérkezés sorrendjében. Ha egy tesztügynöktől keret érkezik az ügyfélterminálba, létrejön a [TesterPass](../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerpass) esemény.

A keretek a számítógép memóriájában vagy megadott nevű fájlban is tárolhatók. Az MQL5 nem korlátozza a keretek számát.

### Memória- és lemezterület-korlátok az MQL5 Cloud Networkben

Az [MQL5 Cloud Networkben](https://www.metatrader5.com/en/terminal/help/algotrading/strategy_optimization#cloud_start) futtatott optimalizálásokra korlátozás vonatkozik: az Expert Advisor nem írhat 4 GB-nál több adatot lemezre, és nem használhat 4 GB-nál több memóriát. A korlát túllépésekor a hálózati ügynök nem tudja helyesen befejezni a számítást, ezért nem kapod meg az eredményt. A számításra fordított idő díját azonban felszámítják.

Ha minden optimalizálási menetből adatot szeretnél, [küldj kereteket](Working-with-Optimization-Results.md) a lemezre írás helyett. Az MQL5 Cloud Networkben futó Expert Advisor fájlműveleteinek elkerülésére használható például ez az ellenőrzés:

```cpp
   int handle=INVALID_HANDLE;
   bool file_operations_allowed=true;
   if(MQLInfoInteger(MQL_OPTIMIZATION) || MQLInfoInteger(MQL_FORWARD))
      file_operations_allowed=false;
   if(file_operations_allowed)
     {
      ...
      handle=FileOpen(...);
      ...
     }
```

| Függvény | Működés |
| --- | --- |
| [FrameFirst](FrameFirst/FrameFirst.md) | A keretolvasó mutatóját az elejére állítja, és törli a korábban beállított szűrőt. |
| [FrameFilter](FrameFilter/FrameFilter.md) | Beállítja a keretolvasó szűrőjét, és a mutatót az elejére állítja. |
| [FrameNext](FrameNext/FrameNext.md) | Beolvas egy keretet, majd a mutatót a következőre állítja. |
| [FrameInputs](FrameInputs/FrameInputs.md) | Lekéri azokat a [bemeneti paramétereket](../Language-Basics/Variables/Input-Variables/Input-Variables.md), amelyek alapján a keret készült. |
| [FrameAdd](FrameAdd/FrameAdd.md) | Adatokat tartalmazó keretet ad hozzá. |
| [ParameterGetRange](ParameterGetRange/ParameterGetRange.md) | Lekéri a bemeneti változó értéktartományát és lépésközét az Expert Advisor Stratégiateszterben történő optimalizálásakor. |
| [ParameterSetRange](ParameterSetRange/ParameterSetRange.md) | Beállítja, hogyan vegyen részt a [bemeneti változó](../Language-Basics/Variables/Input-Variables/Input-Variables.md) az optimalizálásban: érték, lépésköz, kezdeti és végső érték. |

Lásd még: [Tesztelési statisztikák](../Constants,-Enumerations-and-Structures/Environment-State/Testing-Statistics/Testing-Statistics.md), [Futó MQL5-program tulajdonságai](../Constants,-Enumerations-and-Structures/Environment-State/Running-MQL5-Program-Properties/Running-MQL5-Program-Properties.md).
