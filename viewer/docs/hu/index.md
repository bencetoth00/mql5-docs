# MQL5-referencia

A MetaQuotes Language 5 (MQL5) egy magas szintű programozási nyelv technikai indikátorok, kereskedőrobotok és a pénzügyi kereskedést automatizáló segédalkalmazások fejlesztéséhez. A MetaQuotes a saját kereskedési platformjához készítette. A nyelv szintaxisa nagyon közel áll a C++-éhoz, így objektumorientált (OOP) stílusban is lehet vele programokat fejleszteni.

Az MQL5 mellett a kereskedési platform része a [MetaEditor IDE](https://www.metatrader5.com/en/metaeditor/help) is. Fejlett kódszerkesztő eszközöket kínál, például sablonokat, kódrészleteket, hibakeresést, teljesítményprofilt és automatikus kiegészítést. A beépített [MQL5 Storage](https://www.metatrader5.com/en/metaeditor/help/mql5storage) a fájlok verziókezelését is lehetővé teszi.

A nyelvhez kapcsolódó támogatás az MQL5 Algo Trading közösségi webhelyén érhető el. Itt található a nagyméretű, ingyenes [CodeBase](https://www.mql5.com/en/code) és számos [cikk](https://www.mql5.com/en/articles) is. A cikkek többek között a neurális hálózatokkal, statisztikával és elemzéssel, nagyfrekvenciás kereskedéssel, arbitrázzsal, a kereskedési stratégiák tesztelésével és optimalizálásával, valamint a kereskedést automatizáló robotok használatával foglalkoznak.

A kereskedők és az MQL5-fejlesztők a fórumon beszélgethetnek, a [Freelance](https://www.mql5.com/en/job) szolgáltatásban alkalmazásokat rendelhetnek vagy fejleszthetnek, a [Market](https://www.mql5.com/en/market) felületén pedig automatizált kereskedési alkalmazásokat vásárolhatnak és értékesíthetnek.

Az MQL5 speciális [kereskedési függvényeket](Trade-Functions/Trade-Functions.md) és előre definiált [eseménykezelőket](Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md) biztosít. Ezek segítenek olyan Expert Advisorok (EA-k) fejlesztésében, amelyek meghatározott kereskedési szabályok szerint vezérlik a folyamatokat. Az EA-k mellett egyéni [technikai indikátorok](Custom-Indicators/Custom-Indicators.md), szkriptek és könyvtárak is készíthetők.

Ez az MQL5 nyelvi referencia a függvényeket, műveleteket, fenntartott szavakat és más nyelvi elemeket témakörök szerint mutatja be. Ismerteti a [Standard Library](Standard-Library/Standard-Library.md) osztályait is, amelyek kereskedési stratégiák, vezérlőpanelek és egyéni grafikus elemek fejlesztésére, illetve fájlok elérésére használhatók.

A CodeBase az [ALGLIB](https://www.mql5.com/en/code/1146) numerikus analíziskönyvtárat is tartalmazza, amely különféle matematikai feladatok megoldására használható.

### Könyvek az algoritmikus kereskedésről

Új ismeretek elsajátítását segíti két átfogó, MQL5-programozással foglalkozó könyvünk. Mindkettő azoknak szól, akik kereskedőrobotokat és alkalmazásokat szeretnének készíteni.

A könyvek rendszerezett felépítése megkönnyíti a tanulást. A robotok és alkalmazások lépésenkénti elkészítését bemutató kódpéldák segítenek megérteni az algoritmikus kereskedés sajátosságait. A gyakorlati feladatok az ismeretek elmélyítését és a valós kereskedési környezetben használható programozási készségek fejlesztését szolgálják.

Az [MQL5-programozás kereskedőknek](https://www.mql5.com/en/book "MQL5 oktatóanyag") című könyv az egyik legrészletesebb MQL5-útmutató, amely kezdőknek és tapasztalt programozóknak egyaránt hasznos. A kezdők megismerik a fejlesztőeszközöket és az alapvető programozási fogalmakat, majd elkészítik, lefordítják és futtatják első MetaTrader 5-alkalmazásukat. Más nyelvek programozói közvetlenül az alkalmazásfejlesztéssel kezdhetnek: MQL5-ös kereskedőrobotokat és elemzőalkalmazásokat készíthetnek.

Az [Algoritmikus kereskedés neurális hálózatokkal és MQL5-tel](https://www.mql5.com/en/neurobook "Könyv neurális hálózatokról, MQL5-ről, OpenCL-ről és Pythonról") című könyv a gépi tanulási módszerek MetaTrader 5-ös kereskedőrobotokban való alkalmazását mutatja be. Az olvasó fokozatosan ismeri meg a neurális hálózatok alapjait és algoritmikus kereskedési felhasználásukat. A könyv során saját MI-megoldást épít és tanít be, majd lépésenként új képességekkel bővíti. Az MQL5 mellett Python- és OpenCL-programozást, valamint olyan beépített mátrix- és vektorműveleteket is megismer, amelyek tömör és hatékony kóddal teszik lehetővé összetett matematikai feladatok megoldását.

### Cikkek kereskedési alkalmazások fejlesztéséről

Az MQL5-cikkek gyakorlati feladatok széles körén keresztül mutatják be a nyelv lehetőségeit. A könnyebb eligazodást témakörök segítik, például [példák](https://www.mql5.com/en/articles/examples), [Expert Advisorok](https://www.mql5.com/en/articles/expert_advisors) és [gépi tanulás](https://www.mql5.com/en/articles/machine_learning). Az MQL5 Algo Trading közösségi webhelyén havonta több tucat, kereskedők által írt új cikk jelenik meg. Ezek olvasásával és megvitatásával elmélyíthetők a modern algoritmikus kereskedéssel kapcsolatos ismeretek. A kezdők számára összeállítottunk egy [16 ajánlott cikkből álló listát](https://www.metatrader5.com/en/metaeditor/help/articles), amely gyors bevezetést ad az MQL5 használatába.

## MQL5-alkalmazások típusai

Az MQL5-programok öt fő típusba sorolhatók aszerint, hogy milyen kereskedésautomatizálási feladatot látnak el:

- **Expert Advisor:** diagramhoz kapcsolt automatizált kereskedési rendszer. Az előre meghatározott eseményeket kezelő [eseménykezelőket](Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md) tartalmazza; ezek indítják el a stratégia megfelelő elemeit. Ilyen esemény lehet a program inicializálása és leállítása, az új tick, az időzítő, a Piacmélység változása, illetve egy diagram- vagy egyéni esemény. Az Expert Advisor a megadott szabályok alapján kereskedési jelzéseket számíthat, végrehajthatja az ügyleteket, és közvetlenül a kereskedési szervernek küldheti azokat. Helye: `<Terminal_Directory>\MQL5\Experts`.
- **Egyéni indikátor:** a platform beépített indikátorai mellett a felhasználó által készített technikai indikátor. Az indikátorok nem kereskednek automatikusan, hanem elemzési feladatokat látnak el. Más indikátorok értékeit is felhasználhatják, és Expert Advisorokból is meghívhatók. Helyük: `<Terminal_Directory>\MQL5\Indicators`.
- **Szkript:** egyetlen művelet végrehajtására szolgáló program. Az Expert Advisorokkal ellentétben a szkriptek csak az indítási eseményt kezelik; a kódjuknak tartalmaznia kell az `OnStart` kezelőfüggvényt. Helyük: `<Terminal_Directory>\MQL5\Scripts`.
- **Szolgáltatás:** olyan program, amelynek működéséhez az indikátorokkal, Expert Advisorokkal és szkriptekkel ellentétben nem kell diagramhoz kapcsolódnia. A szkriptekhez hasonlóan csak az indítási eseményt kezeli. Az `OnStart` kezelőfüggvénnyel indul, és a Start eseményen kívül más eseményt nem fogad, de az [EventChartCustom](Working-with-Events/EventChartCustom/EventChartCustom.md) függvénnyel egyéni eseményeket küldhet a diagramoknak. Helye: `<Terminal_Directory>\MQL5\Services`.
- **Könyvtár:** egyéni függvények gyűjteménye. A könyvtárak a gyakran használt algoritmusok tárolására és terjesztésére szolgálnak. Helyük: `<Terminal_Directory>\MQL5\Libraries`.
- **Include-fájl:** forrásfájl a programokban gyakran használt kódrészletekhez. Fordításkor Expert Advisorok, szkriptek, egyéni indikátorok és könyvtárak forrásába illeszthető. Az include-fájlok használata előnyösebb lehet a könyvtáraknál, mert a könyvtári függvényhívások többletterhelést okozhatnak. Az include-fájl az eredeti forrásfájllal azonos mappába is kerülhet; ekkor az `#include` direktívában idézőjelet kell használni. A fájl elhelyezhető a `<Terminal_Directory>\MQL5\Include` mappában is; ebben az esetben szögletes zárójelet kell használni.

© 2000–2026, [MetaQuotes Ltd.](https://www.metaquotes.net)
