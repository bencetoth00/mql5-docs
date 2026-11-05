# WaitEvent

WaitEvent

Sets the event waiting flag.

|  |
| --- |
| void  WaitEvent(     ENUM\_TRADE\_EVENTS    event         // flag     ) |

Parameters

event

[in]  Flag of waiting for an event (from ENUM\_TRADE\_EVENTS enumeration) to set.

Return Value

None.

Event flags

|  |
| --- |
| //--- flags of expected events  enum ENUM\_TRADE\_EVENTS    {     TRADE\_EVENT\_NO\_EVENT              =0,         // no expected events     TRADE\_EVENT\_POSITION\_OPEN         =0x1,       // flag of expecting the "opening of position" event     TRADE\_EVENT\_POSITION\_VOLUME\_CHANGE=0x2,       // flag of expecting of the "modification of position volume" event     TRADE\_EVENT\_POSITION\_MODIFY       =0x4,       // flag of expecting of the "modification of stop order of position" event     TRADE\_EVENT\_POSITION\_CLOSE        =0x8,       // flag of expecting of the "closing of position" event     TRADE\_EVENT\_POSITION\_STOP\_TAKE    =0x10,      // flag of expecting of the "triggering of stop order of position"     TRADE\_EVENT\_ORDER\_PLACE           =0x20,      // flag of expecting of the "placing of pending order" event     TRADE\_EVENT\_ORDER\_MODIFY          =0x40,      // flag of expecting of the "modification of pending order" event     TRADE\_EVENT\_ORDER\_DELETE          =0x80,      // flag of expecting of the "deletion of pending order" event     TRADE\_EVENT\_ORDER\_TRIGGER         =0x100      // flag of expecting of the "triggering of pending order" event    }; |
