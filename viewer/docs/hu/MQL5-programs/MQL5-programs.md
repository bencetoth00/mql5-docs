# MQL5-programok

Az MQL5-programokat futtatás előtt le kell fordítani a Compile gombbal vagy az F7 billentyűvel. A fordításnak hibamentesen kell lefutnia; az esetleges figyelmeztetéseket érdemes megvizsgálni. Sikeres fordításkor a megfelelő mappában létrejön az azonos nevű, EX5 kiterjesztésű futtatható fájl, például a `terminal_dir\MQL5\Experts`, `terminal_dir\MQL5\Indicators` vagy `terminal_dir\MQL5\Scripts` mappában.

Az MQL5-programok működését az alábbi témakörök ismertetik:

- [Programindítás](Program-Running/Program-Running.md) – az előre definiált eseménykezelők meghívásának sorrendje.
- [Kereskedési stratégiák tesztelése](Testing-Trading-Strategies/Testing-Trading-Strategies.md) – az MQL5-programok működése a Stratégiateszterben.
- [Ügyfélterminál-események](Client-Terminal-Events/Client-Terminal-Events.md) – a programok által kezelhető események leírása.
- [Importált függvények hívása](Call-of-Imported-Functions/Call-of-Imported-Functions.md) – a hívás sorrendje, a megengedett paraméterek, a keresés részletei és az importált függvények hívási konvenciója.
- [Futásidejű hibák](Runtime-Errors/Runtime-Errors.md) – információk a futásidejű és kritikus hibákról.

Az Expert Advisorokat, egyéni indikátorokat és szkripteket a Navigátor ablakból húzd át a megnyitott diagramra.

Egy Expert Advisor leállításához távolítsd el a diagramról: a diagram helyi menüjében válaszd az Expert listát, jelöld ki az Expert Advisort, majd kattints az Eltávolítás gombra. Az Expert Advisorok működését az AutoTrading gomb állapota is befolyásolja.

Az egyéni indikátor leállításához távolítsd el a diagramról.

Az egyéni indikátorok és az Expert Advisorok addig működnek, amíg el nem távolítod őket a diagramról. A csatolt Expert Advisorok és indikátorok adatai az ügyfélterminál-munkamenetek között is megmaradnak.

A szkriptek egyszer futnak le, majd a végrehajtás befejezésekor, az aktuális diagram állapotának változásakor vagy az ügyfélterminál leállításakor automatikusan törlődnek. A terminál újraindítása után a szkriptek nem indulnak el, mert a rájuk vonatkozó információ nem kerül mentésre.

Egy diagramon legfeljebb egy Expert Advisor és egy szkript, valamint korlátlan számú indikátor működhet.

A szolgáltatásoknak nem kell diagramhoz kapcsolódniuk; kiegészítő feladatok végrehajtására valók. Egy szolgáltatással például létrehozhatsz egy [egyéni szimbólumot](../Custom-Symbols/Custom-Symbols.md), megnyithatod a diagramját, végtelen ciklusban adatokat fogadhatsz hozzá a [hálózati függvényekkel](../Network-Functions/Network-Functions.md), majd folyamatosan frissítheted az adatokat.
