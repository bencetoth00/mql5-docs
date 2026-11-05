# Close


Closes the opened position.

```cpp
virtual bool  Close()
```

Return Value

true - trade operation has been executed, otherwise - false.

Note

Closes the position (PositionClose() method of CTrade class object).

Implementation

```cpp
//+------------------------------------------------------------------+
//| Position close                                                   |
//| INPUT:  no.                                                      |
//| OUTPUT: true-if trade operation processed, false otherwise.      |
//| REMARK: no.                                                      |
//+------------------------------------------------------------------+
bool CExpert::Close()
  {
   return(m_trade.PositionClose(m_symbol.Name()));
  }
```