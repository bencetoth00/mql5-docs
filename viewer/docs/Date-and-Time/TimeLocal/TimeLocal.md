# TimeLocal


Returns the local time of a computer, where the client terminal is running. There are 2 variants of the function.

Call without parameters

```cpp
datetime  TimeLocal();
```

Call with MqlDateTime type parameter

```cpp
datetime  TimeLocal(
   MqlDateTime&  dt_struct      // Variable of structure type
   );
```

Parameters

dt\_struct

[out]  Variable of structure type [MqlDateTime](../../Constants,-Enumerations-and-Structures/Data-Structures/Date-Type-Structure/Date-Type-Structure.md).

Return Value

Value of [datetime](../../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) type

Note

If the MqlDateTime structure type variable has been passed as a parameter, it is filled accordingly.

To arrange high-resolution counters and timers, use the [GetTickCount()](../../Common-Functions/GetTickCount/GetTickCount.md) function, which produces values in milliseconds.

During testing in the strategy tester, TimeLocal() is always equal to [TimeCurrent()](../TimeCurrent/TimeCurrent.md) simulated server time.

Example:

```cpp
void OnStart()
  {
//--- declare the MqlDateTime variable to be filled with PC local time data
   MqlDateTime tm={};
   datetime    time1=TimeLocal();   // first form of call: PC local time
   datetime    time2=TimeLocal(tm); // second form of call: PC local time with filling the MqlDateTime structure
//--- display the result of receiving PC local time and filling the structure with the corresponding data in the log
   PrintFormat("Local time: %s\n- Year: %u\n- Month: %02u\n- Day: %02u\n- Hour: %02u\n- Min: %02u\n- Sec: %02u\n- Day of Year: %03u\n- Day of Week: %u (%s)",
               (string)time1, tm.year, tm.mon, tm.day, tm.hour, tm.min, tm.sec, tm.day_of_year, tm.day_of_week, EnumToString((ENUM_DAY_OF_WEEK)tm.day_of_week));
   /*
   result:
   Local time: 2024.04.18 19:44:09
   - Year: 2024
   - Month: 04
   - Day: 18
   - Hour: 19
   - Min: 44
   - Sec: 09
   - Day of Year: 108
   - Day of Week: 4 (THURSDAY)
   */
  }
```