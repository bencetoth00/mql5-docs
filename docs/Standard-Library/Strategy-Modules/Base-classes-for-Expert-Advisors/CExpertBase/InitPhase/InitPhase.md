# InitPhase

InitPhase

Gets the current phase of the object initialization.

|  |
| --- |
| ENUM\_INIT\_PHASE  InitPhase() |

Return Value

Current phase of the object initialization.

Note

The object initialization consist of several phases:

1. Start initialization.

  - start              - after finish of the constructor  
   - finish             - after successful completion of the [Init(...)](../Init/Init.md) method.  
   - allowed          - call of the [Init(...)](../Init/Init.md) method  
   - not allowed    - call of the [ValidationSettings()](../ValidationSettings/ValidationSettings.md) method and other initialization methods

2. Parameters setting phase. In this phase you need to set all the object parameters, used for creation of indicators.

  - start             - after successful completion of the [Init(...)](../Init/Init.md) method  
   - finish            - after successful completion of the [ValidationSettings()](../ValidationSettings/ValidationSettings.md) method  
   - allowed         - call of [Symbol(...)](../Symbol/Symbol.md) and [Period(...)](../Period/Period.md) methods  
   - not allowed   - call of the [Init(...)](../Init/Init.md), [SetPriceSeries(...)](../SetPriceSeries/SetPriceSeries.md), [SetOtherSeries(...)](../SetOtherSeries/SetOtherSeries.md) and [InitIndicators(...)](../InitIndicators/InitIndicators.md) methods

3. Checking of parameters.

  - start             - after successful completion of the [ValidationSettings()](../ValidationSettings/ValidationSettings.md) method  
   - finish            - after successful completion of the [InitIndicators(...)](../InitIndicators/InitIndicators.md) method  
   - allowed         - call of the [Symbol(...)](../Symbol/Symbol.md), [Period(...)](../Period/Period.md) and [InitIndicators(...)](../InitIndicators/InitIndicators.md) methods  
   - not allowed   - call of any other initialization methods

4. Finish of initialization.

  - start             - after successful completion of the [InitIndicators(...)](../InitIndicators/InitIndicators.md) method  
   - not allowed    - call of initialization methods
