# Strategy Modules

Classes for Creating and Testing Trading Strategies

This section contains technical details of working with classes for creation and testing of trading strategies and description of the relevant components of the MQL5 standard library.

The use of these classes will save time when creating (and especially testing) trading strategies.

MQL5 Standard Library (in terms of trading strategies) is placed in the terminal directory, in the Include\Expert folder.

| Base classes | Description |
| --- | --- |
| [CExpertBase](Base-classes-for-Expert-Advisors/CExpertBase/CExpertBase.md) | Base class for all trading strategy classes |
| [CExpert](Base-classes-for-Expert-Advisors/CExpert/CExpert.md) | Base class for Expert Advisor |
| [CExpertSignal](Base-classes-for-Expert-Advisors/CExpertSignal/CExpertSignal.md) | Base class for Trading Signal classes |
| [CExpertTrailing](Base-classes-for-Expert-Advisors/CExpertTrailing/CExpertTrailing.md) | Base class for Trailing Stop classes |
| [CExpertMoney](Base-classes-for-Expert-Advisors/CExpertMoney/CExpertMoney.md) | Base class for Money Management classes |

| Trading signal classes | Description |
| --- | --- |
| [CSignalAC](Modules-of-Trade-Signals/Signals-of-the-Indicator-Accelerator-Oscillator/Signals-of-the-Indicator-Accelerator-Oscillator.md) | The module of signals based on market models of the indicator Accelerator Oscillator. |
| [CSignalAMA](Modules-of-Trade-Signals/Signals-of-the-Indicator-Adaptive-Moving-Average/Signals-of-the-Indicator-Adaptive-Moving-Average.md) | The module of signals based on market models of the indicator Adaptive Moving Average. |
| [CSignalAO](Modules-of-Trade-Signals/Signals-of-the-Indicator-Awesome-Oscillator/Signals-of-the-Indicator-Awesome-Oscillator.md) | The module of signals based on market models of the indicator Awesome Oscillator. |
| [CSignalBearsPower](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Bears-Power/Signals-of-the-Oscillator-Bears-Power.md) | The module of signals based on market models of the oscillator Bears Power. |
| [CSignalBullsPower](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Bulls-Power/Signals-of-the-Oscillator-Bulls-Power.md) | The module of signals based on market models of the oscillator Bulls Power. |
| [CSignalCCI](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Commodity-Channel-Index/Signals-of-the-Oscillator-Commodity-Channel-Index.md) | The module of signals based on market models of the oscillator Commodity Channel Index. |
| [CSignalDeM](Modules-of-Trade-Signals/Signals-of-the-Oscillator-DeMarker/Signals-of-the-Oscillator-DeMarker.md) | The module of signals based on market models of the oscillator DeMarker. |
| [CSignalDEMA](Modules-of-Trade-Signals/Signals-of-the-Indicator-Double-Exponential-Moving-Average/Signals-of-the-Indicator-Double-Exponential-Moving-Average.md) | The module of signals based on market models of the indicator Double Exponential Moving Average. |
| [CSignalEnvelopes](Modules-of-Trade-Signals/Signals-of-the-Indicator-Envelopes/Signals-of-the-Indicator-Envelopes.md) | The module of signals based on market models of the indicator Envelopes. |
| [CSignalFrAMA](Modules-of-Trade-Signals/Signals-of-the-Indicator-Fractal-Adaptive-Moving-Average/Signals-of-the-Indicator-Fractal-Adaptive-Moving-Average.md) | The module of signals based on market models of the indicator Fractal Adaptive Moving Average. |
| [CSignalITF](Modules-of-Trade-Signals/Signals-of-the-Intraday-Time-Filter/Signals-of-the-Intraday-Time-Filter.md) | The module of filtration of signals by time. |
| [CSignalMACD](Modules-of-Trade-Signals/Signals-of-the-Oscillator-MACD/Signals-of-the-Oscillator-MACD.md) | The module of signals based on market models of the oscillator MACD. |
| [CSignalMA](Modules-of-Trade-Signals/Signals-of-the-Indicator-Moving-Average/Signals-of-the-Indicator-Moving-Average.md) | The module of signals based on market models of the indicator Moving Average. |
| [CSignalSAR](Modules-of-Trade-Signals/Signals-of-the-Indicator-Parabolic-SAR/Signals-of-the-Indicator-Parabolic-SAR.md) | The module of signals based on market models of the indicator Parabolic SAR. |
| [CSignalRSI](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Relative-Strength-Index/Signals-of-the-Oscillator-Relative-Strength-Index.md) | The module of signals based on market models of the oscillator Relative Strength Index. |
| [CSignalRVI](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Relative-Vigor-Index/Signals-of-the-Oscillator-Relative-Vigor-Index.md) | The module of signals based on market models of the oscillator Relative Vigor Index. |
| [CSignalStoch](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Stochastic/Signals-of-the-Oscillator-Stochastic.md) | The module of signals based on market models of the oscillator Stochastic. |
| [CSignalTRIX](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Triple-Exponential-Average/Signals-of-the-Oscillator-Triple-Exponential-Average.md) | The module of signals based on market models of the oscillator Triple Exponential Average. |
| [CSignalTEMA](Modules-of-Trade-Signals/Signals-of-the-Indicator-Triple-Exponential-Moving-Average/Signals-of-the-Indicator-Triple-Exponential-Moving-Average.md) | The module of signals based on market models of the indicator Triple Exponential Moving Average. |
| [CSignalWPR](Modules-of-Trade-Signals/Signals-of-the-Oscillator-Williams-Percent-Range/Signals-of-the-Oscillator-Williams-Percent-Range.md) | The module of signals based on market models of the oscillator Williams Percent Range. |

| Trailing Stop classes | Description |
| --- | --- |
| [CTrailingFixedPips](Trailing-Stop-Classes/CTrailingFixedPips/CTrailingFixedPips.md) | This class implements Trailing Stop algorithm based on fixed points |
| [CTrailingMA](Trailing-Stop-Classes/CTrailingMA/CTrailingMA.md) | This class implements Trailing Stop algorithm based on the values of Moving Average indicator |
| [CTrailingNone](Trailing-Stop-Classes/CTrailingNone/CTrailingNone.md) | A stub class, it does not use any Trailing Stop algorithm |
| [CTrailingPSAR](Trailing-Stop-Classes/CTrailingPSAR/CTrailingPSAR.md) | This class implements Trailing Stop algorithm based on the values of Parabolic SAR indicator |

| Money Management classes | Description |
| --- | --- |
| [CMoneyFixedLot](Money-Management-Classes/CMoneyFixedLot/CMoneyFixedLot.md) | A class with an algorithm based on trading with predefined fixed lot size. |
| [CMoneyFixedMargin](Money-Management-Classes/CMoneyFixedMargin/CMoneyFixedMargin.md) | A class with an algorithm based on trading with predefined fixed margin. |
| [CMoneyFixedRisk](Money-Management-Classes/CMoneyFixedRisk/CMoneyFixedRisk.md) | A class with an algorithm based on trading with predefined risk. |
| [CMoneyNone](Money-Management-Classes/CMoneyNone/CMoneyNone.md) | A class with an algorithm based on trading with minimal allowed lot size. |
| [CMoneySizeOptimized](Money-Management-Classes/CMoneySizeOptimized/CMoneySizeOptimized.md) | A class with an algorithm based on trading with variable lot size, depending on the results of the previous deals. |
