# LabelMake


A szegmens értéke és eredeti címkéje alapján előállítja a szegmens címkéjét.

```cpp
 string  LabelMake(
   const string  text,     // label
   const double  value,    // value
   const bool    to_left,  // flag
   )
```

Paraméterek

text

[in] A címke.

value

[in] Az érték. 

to\_left

[in]  Meghatározza a címkeelemek sorrendjét:

- true — előbb a címke, majd az érték.
- false — előbb az érték, majd a címke.

Visszatérési érték

A szegmens címkéje.
