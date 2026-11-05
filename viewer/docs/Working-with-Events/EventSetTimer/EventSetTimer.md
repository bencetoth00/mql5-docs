# EventSetTimer


The function indicates to the client terminal, that for this indicator or Expert Advisor, events from the [timer](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#timer) must be generated with the specified periodicity.

```cpp
bool  EventSetTimer(
   int  seconds      // number of seconds
   );
```

Parameters

seconds

[in] Number of seconds that determine the frequency of the timer event occurrence.

Return Value

In case of success returns true, otherwise false. In order to get an [error code](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

Normally, this function must be called from the [OnInit()](../../Event-Handling/OnInit/OnInit.md) function or from a class [constructor](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#constructor). In order to handle events coming from the timer, the Expert Advisor must have the [OnTimer()](../../Event-Handling/OnTimer/OnTimer.md) function.

Every Expert Advisor, as well as every indicator works with its own timer and receives events only from it. As soon as a mql5 program stops operating, the timer is destroyed forcibly if it was created but hasn't been disabled by the [EventKillTimer()](../EventKillTimer/EventKillTimer.md) function.

For each program no more than one timer can be run. Each mql5 program and each chart has its own queue of events, in which all the newly received events are placed. If the [Timer](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#timer) event is present in the queue or is being processed, the new Timer event will not be placed in the queue of the mql5 program.