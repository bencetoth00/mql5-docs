# CNormalMembershipFunction

CNormalMembershipFunction

Class for implementing a symmetrical Gaussian membership function with the B and Sigma parameters.

Description

The symmetrical Gaussian membership function is formed using Gaussian distribution.  The function is smooth and takes non-zero values along the entire definition area.  

![fuzzy_norm_function](../../../../../assets/fuzzy_norm_function.png)

[A sample code](CNormalMembershipFunction.md#sample) for plotting a chart is displayed below.

Declaration

|  |
| --- |
| class CNormalMembershipFuncion : public IMembershipFunction |

Title

|  |
| --- |
| #include <Math\Fuzzy\membershipfunction.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../../Basic-Class-CObject/Basic-Class-CObject.md)        [IMembershipFunction](../IMembershipFunction/IMembershipFunction.md)            CNormalMembershipFunction |

Class methods

| Class method | Description |
| --- | --- |
| [B](B/B.md) | Gets and sets the membership function center. |
| [Sigma](Sigma/Sigma.md) | Gets and sets the parameter of the membership function curvature. |
| [GetValue](GetValue/GetValue.md) | Calculates the value of the membership function by a specified argument. |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../../Basic-Class-CObject/Save/Save.md), [Load](../../../../Basic-Class-CObject/Load/Load.md), [Type](../../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../../Basic-Class-CObject/Compare/Compare.md) |

Example

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                     NormalMembershipFunction.mq5 |  //|                         Copyright 2000-2024, MetaQuotes Ltd. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #include <Math\Fuzzy\membershipfunction.mqh>  #include <Graphics\Graphic.mqh>  //--- Create membership functions  CNormalMembershipFunction func1(5,0.5);  CNormalMembershipFunction func2(5,1);  CNormalMembershipFunction func3(5,3);  //--- Create wrappers for membership functions  double NormalMembershipFunction1(double x) { return(func1.GetValue(x)); }  double NormalMembershipFunction2(double x) { return(func2.GetValue(x)); }  double NormalMembershipFunction3(double x) { return(func3.GetValue(x)); }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- create graphic     CGraphic graphic;     if(!graphic.Create(0,"NormalMembershipFunction",0,30,30,780,380))       {        graphic.Attach(0,"NormalMembershipFunction");       }     graphic.HistoryNameWidth(70);     graphic.BackgroundMain("NormalMembershipFunction");     graphic.BackgroundMainSize(16);  //--- create curve     graphic.CurveAdd(NormalMembershipFunction1,0.0,10.0,0.1,CURVE\_LINES,"[5, 0.0]");     graphic.CurveAdd(NormalMembershipFunction2,0.0,10.0,0.1,CURVE\_LINES,"[5, 1]");     graphic.CurveAdd(NormalMembershipFunction3,0.0,10.0,0.1,CURVE\_LINES,"[5, 3]");  //--- sets the X-axis properties     graphic.XAxis().AutoScale(false);     graphic.XAxis().Min(0.0);     graphic.XAxis().Max(10.0);     graphic.XAxis().DefaultStep(1.0);  //--- sets the Y-axis properties     graphic.YAxis().AutoScale(false);     graphic.YAxis().Min(0.0);     graphic.YAxis().Max(1.1);     graphic.YAxis().DefaultStep(0.2);  //--- plot     graphic.CurvePlotAll();     graphic.Update();    } |
