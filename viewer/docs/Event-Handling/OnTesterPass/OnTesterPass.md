# OnTesterPass


The function is called in EAs when the [TesterPass](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerpass) event occurs for handling a new data frame during EA optimization.

```cpp
void  OnTesterPass(void);
```

Return Value

No return value

Note

The [TesterPass](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerpass) event is generated automatically when receiving a frame during an Expert Advisor optimization in the strategy tester.

An EA having OnTesterDeInit() or OnTesterPass() event handler is automatically downloaded on a separate terminal chart during the optimization start. It has the symbol and the period that have been specified in the tester. The function is meant for handling frames received from test agents during optimization. The frame containing test results should be sent from the [OnTester()](../OnTester/OnTester.md) handler using the [FrameAdd()](../../Working-with-Optimization-Results/FrameAdd/FrameAdd.md) function.

Keep in mind that optimization frames sent by test agents using the [FrameAdd()](../../Working-with-Optimization-Results/FrameAdd/FrameAdd.md) function may come in bundles and take time to deliver. Therefore, not all frames, as well as [TesterPass](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#testerpass) events, may arrive and be processed in [OnTesterPass()](OnTesterPass.md) before the end of optimization. If you want to receive all belated frames in OnTesterDeinit(), place the code block using the [FrameNext()](../../Working-with-Optimization-Results/FrameNext/FrameNext.md) function.

After completing OnTesterDeinit() optimization, it is possible to sort all received frames again using the [FrameFirst()](../../Working-with-Optimization-Results/FrameFirst/FrameFirst.md)/[FrameFilter](../../Working-with-Optimization-Results/FrameFilter/FrameFilter.md) and [FrameNext()](../../Working-with-Optimization-Results/FrameNext/FrameNext.md) functions.

See also

[Testing trading strategies](../../MQL5-programs/Testing-Trading-Strategies/Testing-Trading-Strategies.md), [Working with optimization results](../../Working-with-Optimization-Results/Working-with-Optimization-Results.md), [OnTesterInit](../OnTesterInit/OnTesterInit.md), [OnTesterDeinit](../OnTesterDeinit/OnTesterDeinit.md), [FrameFirst](../../Working-with-Optimization-Results/FrameFirst/FrameFirst.md), [FrameFilter](../../Working-with-Optimization-Results/FrameFilter/FrameFilter.md), [FrameNext](../../Working-with-Optimization-Results/FrameNext/FrameNext.md), [FrameInputs](../../Working-with-Optimization-Results/FrameInputs/FrameInputs.md)