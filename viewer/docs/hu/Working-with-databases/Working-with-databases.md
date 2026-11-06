# Adatbázisok használata

Az adatbázis-kezelő függvények a népszerű, könnyen használható [SQLite](https://www.sqlite.org/index.html) motort alkalmazzák. Az adatbázis teljes egészében egyetlen fájlban tárolható a felhasználó számítógépén.

A függvényekkel SQL-lekérdezések segítségével hozhatók létre táblák, adhatók hozzá vagy módosíthatók adatok, illetve kérdezhetők le rekordok. Használhatók többek között kereskedési előzmények és jegyzések fogadására, optimalizálási és teszteredmények tárolására, más elemzőeszközökkel való adatcserére, valamint MQL5-alkalmazások beállításainak mentésére.

A lekérdezések [statisztikai](Working-with-databases.md#math) és [matematikai](Working-with-databases.md#stats) függvényeket is használhatnak. A nagy adathalmazok ismétlődő feldolgozása sok esetben SQL-lekérdezésekkel és a [DatabaseExecute](DatabaseExecute/DatabaseExecute.md)/[DatabasePrepare](DatabasePrepare/DatabasePrepare.md) függvényekkel oldható meg összetett ciklusok helyett. A [DatabaseReadBind](DatabaseReadBind/DatabaseReadBind.md) egyetlen hívással egy kész struktúrába olvashatja be a rekord összes mezőjét.

Az olvasás és írás gyorsításához az adatbázis a `DATABASE_OPEN_MEMORY` jelzővel a memóriában is létrehozható. Ez az adatbázis csak az adott alkalmazás számára érhető el. Lemezen tárolt adatbázis esetén a nagyobb tömeges módosításokat érdemes tranzakcióba foglalni a [DatabaseTransactionBegin](DatabaseTransactionBegin/DatabaseTransactionBegin.md), `DatabaseTransactionCommit` és `DatabaseTransactionRollback` függvényekkel; ez jelentősen gyorsíthatja a műveleteket.

A használat részleteiről az [SQLite: natív SQL-adatbázis-kezelés MQL5-ben](https://www.mql5.com/en/articles/7463) című cikkben olvashatsz.

| Függvény | Működés |
| --- | --- |
| [DatabaseOpen](DatabaseOpen/DatabaseOpen.md) | Megnyitja vagy létrehozza az adatbázist a megadott fájlban. |
| [DatabaseClose](DatabaseClose/DatabaseClose.md) | Bezár egy adatbázist. |
| [DatabaseImport](DatabaseImport/DatabaseImport.md) | Fájlból importál adatokat egy táblába. |
| [DatabaseExport](DatabaseExport/DatabaseExport.md) | Táblát vagy SQL-lekérdezés eredményét exportálja CSV-fájlba. |
| [DatabasePrint](DatabasePrint/DatabasePrint.md) | Táblát vagy lekérdezési eredményt ír ki az Expert naplóba. |
| [DatabaseTableExists](DatabaseTableExists/DatabaseTableExists.md) | Ellenőrzi, hogy létezik-e a tábla az adatbázisban. |
| [DatabaseExecute](DatabaseExecute/DatabaseExecute.md) | Végrehajt egy lekérdezést a megadott adatbázison. |
| [DatabasePrepare](DatabasePrepare/DatabasePrepare.md) | Lekérdezéskezelőt készít, amely a DatabaseRead függvénnyel futtatható. |
| [DatabaseReset](DatabaseReset/DatabaseReset.md) | Visszaállítja a lekérdezést, például a DatabasePrepare után. |
| [DatabaseBind](DatabaseBind/DatabaseBind.md) | Beállít egy paraméterértéket a lekérdezésben. |
| [DatabaseBindArray](DatabaseBindArray/DatabaseBindArray.md) | Tömböt állít be lekérdezési paraméterként. |
| [DatabaseRead](DatabaseRead/DatabaseRead.md) | A lekérdezés eredményének következő rekordjára lép. |
| [DatabaseReadBind](DatabaseReadBind/DatabaseReadBind.md) | A következő rekord adatait egy struktúrába olvassa. |
| [DatabaseFinalize](DatabaseFinalize/DatabaseFinalize.md) | Felszabadítja a DatabasePrepare által létrehozott lekérdezést. |
| [DatabaseTransactionBegin](DatabaseTransactionBegin/DatabaseTransactionBegin.md) | Elindít egy tranzakciót. |
| [DatabaseTransactionCommit](DatabaseTransactionCommit/DatabaseTransactionCommit.md) | Véglegesíti a tranzakciót. |
| [DatabaseTransactionRollback](DatabaseTransactionRollback/DatabaseTransactionRollback.md) | Visszavonja a tranzakció módosításait. |
| [DatabaseColumnsCount](DatabaseColumnsCount/DatabaseColumnsCount.md) | Visszaadja a lekérdezés mezőinek számát. |
| [DatabaseColumnName](DatabaseColumnName/DatabaseColumnName.md) | Index alapján visszaadja egy mező nevét. |
| [DatabaseColumnType](DatabaseColumnType/DatabaseColumnType.md) | Index alapján visszaadja egy mező típusát. |
| [DatabaseColumnSize](DatabaseColumnSize/DatabaseColumnSize.md) | Visszaadja egy mező méretét bájtban. |
| [DatabaseColumnText](DatabaseColumnText/DatabaseColumnText.md) | Az aktuális rekord mezőjét szövegként adja vissza. |
| [DatabaseColumnInteger](DatabaseColumnInteger/DatabaseColumnInteger.md) | Az aktuális rekord mezőjét `int` értékként adja vissza. |
| [DatabaseColumnLong](DatabaseColumnLong/DatabaseColumnLong.md) | Az aktuális rekord mezőjét `long` értékként adja vissza. |
| [DatabaseColumnDouble](DatabaseColumnDouble/DatabaseColumnDouble.md) | Az aktuális rekord mezőjét `double` értékként adja vissza. |
| [DatabaseColumnBlob](DatabaseColumnBlob/DatabaseColumnBlob.md) | Az aktuális rekord mezőjét tömbként adja vissza. |

### Statisztikai függvények

Az adatbázis-lekérdezések többek között módusz-, medián-, percentilis-, szórás- és varianciaszámító függvényeket is használhatnak.

### Matematikai függvények

Az SQLite lekérdezéseiben trigonometrikus, hiperbolikus, exponenciális, logaritmikus és kerekítő függvények is elérhetők. A pontos felsorolást és működést az [SQLite matematikai függvényeinek dokumentációja](https://sqlite.org/lang_mathfunc.html) ismerteti.
