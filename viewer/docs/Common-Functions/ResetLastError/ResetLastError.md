# ResetLastError


Sets the value of the predefined variable [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) into zero.

```cpp
void  ResetLastError();
```

Return Value

No return value.

Note

It should be noted that the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function doesn't zero the \_LastError variable. Usually the ResetLastError() function is called before calling a function, after which an [error](../../MQL5-programs/Runtime-Errors/Runtime-Errors.md) appearance is checked.

 

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- reset the last error code before calling the function,
//--- otherwise, GetLastError() may return the previous error code
   long lres=SymbolInfoInteger("123456",SYMBOL_DIGITS);
   PrintFormat("lres=%d  error=%d",lres,GetLastError());
   lres=SymbolInfoInteger(_Symbol,SYMBOL_DIGITS);
   PrintFormat("lres=%d  error=%d",lres,GetLastError());
   ResetLastError();
   lres=SymbolInfoInteger(_Symbol,SYMBOL_DIGITS);
   PrintFormat("lres=%d  error=%d",lres,GetLastError());
  }
```