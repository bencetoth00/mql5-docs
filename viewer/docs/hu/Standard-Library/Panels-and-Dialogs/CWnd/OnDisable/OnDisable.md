# OnDisable


A belső „Disable” esemény virtuális kezelője (letiltott állapotban a vezérlő nem reagálhat a felhasználói műveletekre).

```cpp
virtual bool  OnDisable()
```

Visszatérési érték

true – az esemény feldolgozva, egyébként false.

Megjegyzés

Az alaposztály metódusa nem végez műveletet, és mindig true értéket ad vissza.
