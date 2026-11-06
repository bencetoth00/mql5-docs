# StartIndex


Lekéri az elemzéshez használt kezdő gyertya indexét.

```cpp
virtual int  StartIndex()
```

Visszatérési érték

Az elemzéshez használt kezdő gyertya indexe.

Megjegyzés

Ha az aktuális gyertya elemzését jelző kapcsoló true értékű, a metódus 0 értéket ad vissza (az elemzés az aktuális gyertyától indul). Ha a kapcsoló nincs beállítva, 1 értéket ad vissza (az elemzés az utolsó lezárt gyertyától indul).
