# EigVals


Kiszámítja egy általános mátrix sajátértékeit.

```cpp
bool matrix::EigVals(
  vector&  eigen_values      // vector of eigenvalues
   );
```

Paraméterek

eigen\_values

[out]  A sajátértékek vektora.

Visszatérési érték

Siker esetén true, egyébként false értéket ad vissza.

 

Megjegyzés

Az EigVals és az Eig közötti egyetlen különbség az, hogy az EigVals nem számítja ki a sajátvektorokat, csak a sajátértékeket.
