# EventKillTimer


Specifies the client terminal that is necessary to stop the generation of events from [Timer](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#timer).

```cpp
void  EventKillTimer();
```

Return Value

No return value.

Note

Typically, this function must be called from a function [OnDeinit()](../../Event-Handling/OnDeinit/OnDeinit.md), if the [EventSetTimer()](../EventSetTimer/EventSetTimer.md) function has been called from [OnInit()](../../Event-Handling/OnInit/OnInit.md). This function can also be called form the class destructor, if the EventSetTimer() function has been called in the [constructor](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#destructor) of this class.

Every Expert Advisor, as well as every indicator works with its own timer and receives events only from it. As soon as a mql5 program stops operating, the timer is destroyed forcibly if it was created but hasn't been disabled by the [EventKillTimer()](EventKillTimer.md) function