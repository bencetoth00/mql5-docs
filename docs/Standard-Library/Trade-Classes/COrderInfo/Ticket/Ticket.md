# Ticket

Ticket

Gets the ticket of an order.

|  |
| --- |
| ulong  Ticket() const |

Return Value

Order ticket if successful, otherwise - [ULONG\_MAX](../../../../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md).

Note

The order should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.
