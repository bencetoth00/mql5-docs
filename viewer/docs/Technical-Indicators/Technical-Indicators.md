# Technical Indicators

# Technical Indicator Functions

All functions like iMA, iAC, iMACD, iIchimoku etc. create a copy of the corresponding technical indicator in the global cache of the client terminal. If a copy of the indicator with such parameters already exists, the new copy is not created, and the counter of references to the existing copy increases.

These functions return the handle of the appropriate copy of the indicator. Further, using this handle, you can receive data calculated by the corresponding indicator. The corresponding buffer data (technical indicators contain calculated data in their internal buffers, which can vary from 1 to 5, depending on the indicator) can be copied to a mql5-program using the [CopyBuffer()](../Timeseries-and-Indicators-Access/CopyBuffer/CopyBuffer.md) function.

You can't refer to the indicator data right after it has been created, because calculation of indicator values requires some time, so it's better to create indicator handles in OnInit(). Function [iCustom()](iCustom/iCustom.md) creates the corresponding custom indicator, and returns its handle in case it is successfully create. Custom indicators can contain up to 512 indicator buffers, the contents of which can also be obtained by the [CopyBuffer()](../Timeseries-and-Indicators-Access/CopyBuffer/CopyBuffer.md) function, using the obtained handle.

There is a universal method for creating any technical indicator using the [IndicatorCreate()](../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) function. This function accepts the following data as input parameters:

- symbol name;
- timeframe;
- type of the indicator to create;
- number of input parameters of the indicator;
- an array of [MqlParam](../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) type containing all the necessary input parameters.

The computer memory can be freed from an indicator that is no more utilized, using the [IndicatorRelease()](../Timeseries-and-Indicators-Access/IndicatorRelease/IndicatorRelease.md) function, to which the indicator handle is passed.

Note. Repeated call of the indicator function with the same parameters within one mql5-program does not lead to a multiple increase of the reference counter; the counter will be increased only once by 1. However, it's recommended to get the indicators handles in function [OnInit()](../Event-Handling/OnInit/OnInit.md) or in the class constructor, and further use these handles in other functions. The reference counter decreases when a mql5-program is deinitialized.

All indicator functions have at least 2 parameters - symbol and period. The [NULL](../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) value of the symbol means the current symbol, the 0 value of the period means the current [timeframe](../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md).

| Function | Returns the handle of the indicator: |
| --- | --- |
| [iAC](iAC/iAC.md) | Accelerator Oscillator |
| [iAD](iAD/iAD.md) | Accumulation/Distribution |
| [iADX](iADX/iADX.md) | Average Directional Index |
| [iADXWilder](iADXWilder/iADXWilder.md) | Average Directional Index by Welles Wilder |
| [iAlligator](iAlligator/iAlligator.md) | Alligator |
| [iAMA](iAMA/iAMA.md) | Adaptive Moving Average |
| [iAO](iAO/iAO.md) | Awesome Oscillator |
| [iATR](iATR/iATR.md) | Average True Range |
| [iBearsPower](iBearsPower/iBearsPower.md) | Bears Power |
| [iBands](iBands/iBands.md) | Bollinger Bands® |
| [iBullsPower](iBullsPower/iBullsPower.md) | Bulls Power |
| [iCCI](iCCI/iCCI.md) | Commodity Channel Index |
| [iChaikin](iChaikin/iChaikin.md) | Chaikin Oscillator |
| [iCustom](iCustom/iCustom.md) | Custom indicator |
| [iDEMA](iDEMA/iDEMA.md) | Double Exponential Moving Average |
| [iDeMarker](iDeMarker/iDeMarker.md) | DeMarker |
| [iEnvelopes](iEnvelopes/iEnvelopes.md) | Envelopes |
| [iForce](iForce/iForce.md) | Force Index |
| [iFractals](iFractals/iFractals.md) | Fractals |
| [iFrAMA](iFrAMA/iFrAMA.md) | Fractal Adaptive Moving Average |
| [iGator](iGator/iGator.md) | Gator Oscillator |
| [iIchimoku](iIchimoku/iIchimoku.md) | Ichimoku Kinko Hyo |
| [iBWMFI](iBWMFI/iBWMFI.md) | Market Facilitation Index by Bill Williams |
| [iMomentum](iMomentum/iMomentum.md) | Momentum |
| [iMFI](iMFI/iMFI.md) | Money Flow Index |
| [iMA](iMA/iMA.md) | Moving Average |
| [iOsMA](iOsMA/iOsMA.md) | Moving Average of Oscillator (MACD histogram) |
| [iMACD](iMACD/iMACD.md) | Moving Averages Convergence-Divergence |
| [iOBV](iOBV/iOBV.md) | On Balance Volume |
| [iSAR](iSAR/iSAR.md) | Parabolic Stop And Reverse System |
| [iRSI](iRSI/iRSI.md) | Relative Strength Index |
| [iRVI](iRVI/iRVI.md) | Relative Vigor Index |
| [iStdDev](iStdDev/iStdDev.md) | Standard Deviation |
| [iStochastic](iStochastic/iStochastic.md) | Stochastic Oscillator |
| [iTEMA](iTEMA/iTEMA.md) | Triple Exponential Moving Average |
| [iTriX](iTriX/iTriX.md) | Triple Exponential Moving Averages Oscillator |
| [iWPR](iWPR/iWPR.md) | Williams' Percent Range |
| [iVIDyA](iVIDyA/iVIDyA.md) | Variable Index Dynamic Average |
| [iVolumes](iVolumes/iVolumes.md) | Volumes |
