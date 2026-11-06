# ValidationSettings


Ellenőrzi a beállításokat.

```cpp
virtual bool  ValidationSettings()
```

Visszatérési érték

Siker esetén true, egyébként false.

Megjegyzés

A függvény ellenőrzi a Take Profit és Stop Loss szinteket. Érvényes érték a 0, illetve a pontokban megadott minimális távolságnál nagyobb érték az aktuális záróártól a Stop megbízások elhelyezéséhez.
