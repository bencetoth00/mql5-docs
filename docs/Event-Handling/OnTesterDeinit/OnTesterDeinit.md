# OnTesterDeinit

OnTesterDeinit

The function is called in EAs when the [TesterDeinit](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerdeinit) event occurs after EA optimization.

|  |
| --- |
| void  OnTesterDeinit(void); |

Return Value

No return value

Note

The [TesterDeinit](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerdeinit) event is generated after the end of EA optimization in the strategy tester.

An EA having OnTesterDeInit() or OnTesterPass() event handler is automatically downloaded on a separate terminal chart during the optimization start. It has the symbol and the period that have been specified in the tester. The function is designed for the final processing of all [optimization results](../../Working-with-Optimization-Results/Working-with-Optimization-Results.md).

Keep in mind that optimization frames sent by test agents using the [FrameAdd()](../../Working-with-Optimization-Results/FrameAdd/FrameAdd.md) function may come in bundles and take time to deliver. Therefore, not all frames, as well as [TesterPass](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerpass) events, may arrive and be processed in [OnTesterPass()](../OnTesterPass/OnTesterPass.md) before the end of optimization. If you want to receive all belated frames in OnTesterDeinit(), place the code block using the [FrameNext()](../../Working-with-Optimization-Results/FrameNext/FrameNext.md) function.

See also

[Testing trading strategies](../../MQL5-programs/Testing-Trading-Strategies/Testing-Trading-Strategies.md), [Working with optimization results](../../Working-with-Optimization-Results/Working-with-Optimization-Results.md), [TesterStatistics](../../Common-Functions/TesterStatistics/TesterStatistics.md), [OnTesterInit](../OnTesterInit/OnTesterInit.md), [OnTesterPass](../OnTesterPass/OnTesterPass.md), [ParameterGetRange](../../Working-with-Optimization-Results/ParameterGetRange/ParameterGetRange.md), [ParameterSetRange](../../Working-with-Optimization-Results/ParameterSetRange/ParameterSetRange.md)
