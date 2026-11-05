# InitMoney

InitMoney

Initializes the money management object.

|  |
| --- |
| virtual bool  InitMoney(     CExpertMoney\*     money=NULL,        // pointer     ) |

Parameters

money

[in]  Pointer to [CExpertMoney](../../CExpertMoney/CExpertMoney.md) class object (or its descendant).

Return Value

true - successful, otherwise - false.

Note

If money is NULL, the [CExpertMoney](../../CExpertMoney/CExpertMoney.md) class will be used for initialization (it uses the minimum lot).
