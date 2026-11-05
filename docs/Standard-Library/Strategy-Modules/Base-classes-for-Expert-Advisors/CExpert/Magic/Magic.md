# Magic

Magic

Sets the Expert Advisor ID (magic).

|  |
| --- |
| void  Magic(     ulong  value     // new value     ) |

Parameters

value

[in]  New value of Expert Advisor ID.

Return Value

None.

Note

If EA's identifier is changed, the same identifier is assigned to all auxiliary objects.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Sets magic number for object and its dependent objects           |  //| INPUT:  value - new value of magic number.                       |  //| OUTPUT: no.                                                      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  void CExpert::Magic(ulong value)    {     if(m\_trade!=NULL)    m\_trade.SetExpertMagicNumber(value);     if(m\_signal!=NULL)   m\_signal.Magic(value);     if(m\_money!=NULL)    m\_money.Magic(value);     if(m\_trailing!=NULL) m\_trailing.Magic(value);  //---     CExpertBase::Magic(value);    } |
