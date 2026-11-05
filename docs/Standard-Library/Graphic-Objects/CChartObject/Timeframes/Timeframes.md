# Timeframes

Timeframes (Get Method)

Gets visibility flags of a graphical object.

|  |
| --- |
| int  Timeframes() const |

Return Value

Visibility flags of the graphical object attached to an instance of the class. If there is no attached object, it returns 0.

Timeframes (Set Method)

Sets visibility flags of a graphical object.

|  |
| --- |
| bool  Timeframes(     int  new\_timeframes      // visibility flags     ) |

Parameters

new\_timeframes

[in]  New visibility flags of the graphical object.

Return Value

true - success, false - cannot change the flags of visibility.

Example:

|  |
| --- |
| //--- example for CChartObject::Timeframes    #include <ChartObjects\ChartObject.mqh>    //---    void OnStart()      {       CChartObject object;       //--- get timeframes of chart object        int timeframes=object.Timeframes();       if(!(timeframes&OBJ\_PERIOD\_H1))         {          //--- set timeframes of chart object          object.Timeframes(timeframes|OBJ\_PERIOD\_H1);         }      } |
