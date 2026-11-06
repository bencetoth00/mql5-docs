# Mátrix- és vektorműveletek

# Mátrixok és vektorok

A mátrix `double`, `float` vagy komplex számokból álló kétdimenziós tömb. A vektor ugyanezen típusok egydimenziós tömbje. A vektornak nincs rögzített függőleges vagy vízszintes iránya; ezt a felhasználás határozza meg. Például a `Dot` művelet a bal oldali vektort vízszintesnek, a jobb oldalit függőlegesnek tekinti. Ha az irányt egyértelműen jelölni kell, használható egy sorból vagy egy oszlopból álló mátrix.

A mátrixok és vektorok dinamikusan foglalnak memóriát. Objektumok, amelyek tárolják többek között az adatok típusát és a méreteket. Tulajdonságaik a `vector_a.Size()`, `matrix_b.Rows()`, `vector_c.Norm()` és `matrix_d.Cond()` metódusokkal kérdezhetők le; a méreteik módosíthatók.

Mátrixok és vektorok létrehozásakor és inicializálásakor statikus metódusok használhatók, például `matrix::Eye()`, `matrix::Identity()`, `matrix::Ones()`, `vector::Ones()`, `matrix::Zeros()`, `vector::Zeros()`, `matrix::Full()` és `vector::Full()`.

A mátrix- és vektorműveletek jelenleg nem támogatják a komplex adattípust. Az MQL5 mátrixokat és vektorokat is átadhat DLL-eknek: az adatok pufferére mutató pointer mellett a méreteket is át kell adni a helyes feldolgozáshoz.

Az alábbi táblázat az elérhető metódusok egy részét sorolja fel. A teljes, betűrendbe szedett lista az angol oldalon található.

| Metódus | Működés | Kategória |
| --- | --- | --- |
| [Activation](Machine-learning/Activation/Activation.md) | Aktivációs függvény értékeit számítja ki, és a megadott vektorba vagy mátrixba írja. | [Gépi tanulás](Machine-learning/Machine-learning.md) |
| [ArgMax](Statistics/ArgMax/ArgMax.md) | Visszaadja a legnagyobb érték indexét. | [Statisztika](Statistics/Statistics.md) |
| [ArgMin](Statistics/ArgMin/ArgMin.md) | Visszaadja a legkisebb érték indexét. | [Statisztika](Statistics/Statistics.md) |
| [ArgSort](Manipulations/ArgSort/ArgSort.md) | Visszaadja a rendezett indexeket. | [Módosítások](Manipulations/Manipulations.md) |
| [Assign](Initialization/Assign/Assign.md) | Mátrixot, vektort vagy tömböt másol automatikus típuskonverzióval. | [Inicializálás](Initialization/Initialization.md) |
| [Average](Statistics/Average/Average.md) | Kiszámítja a mátrix vagy vektor elemeinek súlyozott átlagát. | [Statisztika](Statistics/Statistics.md) |
| [Cholesky](Transformations/Cholesky/Cholesky.md) | Elvégzi a Cholesky-felbontást. | [Transzformációk](Transformations/Transformations.md) |
| [Clip](Manipulations/Clip/Clip.md) | A mátrix vagy vektor elemeit a megadott értéktartományba korlátozza. | [Módosítások](Manipulations/Manipulations.md) |
| [Cols](Features/Cols/Cols.md) | Visszaadja a mátrix oszlopainak számát. | [Tulajdonságok](Features/Features.md) |
| [Compare](Manipulations/Compare/Compare.md) | A megadott pontossággal összehasonlít két mátrixot vagy vektort. | [Módosítások](Manipulations/Manipulations.md) |
| [Cond](Features/Cond/Cond.md) | Kiszámítja a mátrix kondíciószámát. | [Tulajdonságok](Features/Features.md) |
| [Copy](Manipulations/Copy/Copy.md) | Másolatot készít a megadott mátrixról vagy vektorról. | [Módosítások](Manipulations/Manipulations.md) |
| [Det](Features/Det/Det.md) | Kiszámítja egy négyzetes, invertálható mátrix determinánsát. | [Tulajdonságok](Features/Features.md) |
| [Dot](Products/Dot/Dot.md) | Kiszámítja két vektor skaláris szorzatát. | [Szorzatok](Products/Products.md) |
| [Eye](Initialization/Eye/Eye.md) | Egységnyi értékeket tartalmaz a főátlón, máshol nullákat tartalmazó mátrixot ad vissza. | [Inicializálás](Initialization/Initialization.md) |
| [Identity](Initialization/Identity/Identity.md) | A megadott méretű egységmátrixot hoz létre. | [Inicializálás](Initialization/Initialization.md) |
| [MatMul](Products/MatMul/MatMul.md) | Két mátrix szorzatát számítja ki. | [Szorzatok](Products/Products.md) |
| [Max](Statistics/Max/Max.md) | Visszaadja a mátrix vagy vektor legnagyobb értékét. | [Statisztika](Statistics/Statistics.md) |
| [Mean](Statistics/Mean/Mean.md) | Kiszámítja az elemek számtani átlagát. | [Statisztika](Statistics/Statistics.md) |
| [Median](Statistics/Median/Median.md) | Kiszámítja az elemek mediánját. | [Statisztika](Statistics/Statistics.md) |
| [Min](Statistics/Min/Min.md) | Visszaadja a mátrix vagy vektor legkisebb értékét. | [Statisztika](Statistics/Statistics.md) |
| [Norm](Features/Norm/Norm.md) | Visszaadja a mátrix vagy vektor normáját. | [Tulajdonságok](Features/Features.md) |
| [Ones](Initialization/Ones/Ones.md) | Csupa egyest tartalmazó mátrixot vagy vektort hoz létre. | [Inicializálás](Initialization/Initialization.md) |
| [Random](Initialization/Random/Random.md) | Véletlen értékekkel feltöltött mátrixot vagy vektort hoz létre. | [Inicializálás](Initialization/Initialization.md) |
| [Rows](Features/Rows/Rows.md) | Visszaadja a mátrix sorainak számát. | [Tulajdonságok](Features/Features.md) |
| [Sum](Statistics/Sum/Sum.md) | Visszaadja a mátrix vagy vektor elemeinek összegét. | [Statisztika](Statistics/Statistics.md) |
