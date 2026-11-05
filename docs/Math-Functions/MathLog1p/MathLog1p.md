# MathLog1p

MathLog1p

Returns the value of the expression MathLog(1+x).

|  |
| --- |
| double  MathLog1p(     double  value      // value to take the logarithm     ); |

Parameters

value

[in]  The value, the logarithm of which is to be calculated.

Return Value

The natural logarithm of the value (value + 1) if successful. If value is < -1, the function returns NaN (undefined value). If value is equal to -1, the function returns INF (infinity).

Note

At values of x close to 0, the MathLog1p(x) function generates much more accurate values than the MathLog(1+x) function.

Instead of the MathLog1p() function you can use the log1p() function.

 

Example:

|  |
| --- |
| #define GRAPH\_WIDTH  750  #define GRAPH\_HEIGHT 350     #include <Graphics\Graphic.mqh>     CGraphic ExtGraph;  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get 9 values from 0 to 8 with step 1     vector X(9,VectorArange);     Print("vector X = \n",X);  //--- for each vector value, calculate the logarithm for the expression (1 + X vector value)     X=MathLog1p(X);     Print("MathLog1p(X) = \n",X);       //--- transfer the calculated values from the vector to the array     double y\_array[];     X.Swap(y\_array);     //--- draw a graph of the calculated vector values     CurvePlot(y\_array,clrDodgerBlue);     //--- wait for pressing the Escape or PgDn keys to delete the graph (take a screenshot) and exit     while(!IsStopped())       {        if(StopKeyPressed())           break;        Sleep(16);       }     //--- clean up     ExtGraph.Destroy();     /\*     result:     vector X =      [0,1,2,3,4,5,6,7,8]     MathLog1p(X) =      [0,0.6931471805599453,1.09861228866811,1.386294361119891,1.6094379124341,1.791759469228055,1.945910149055313,2.079441541679836,2.19722457733622]     \*/    }  //+------------------------------------------------------------------+  //| Fill a vector with 'value' in 'step' increments                  |  //+------------------------------------------------------------------+  template<typename T>   void VectorArange(vector<T> &vec,T value=0.0,T step=1.0)     {      for(ulong i=0; i<vec.Size(); i++,value+=step)         vec[i]=value;     }  //+------------------------------------------------------------------+  //| When pressing ESC, return 'true'                                 |  //| When pressing PgDn, take a graph screenshot and return 'true'    |  //| Otherwise, return 'false'                                        |  //+------------------------------------------------------------------+  bool StopKeyPressed()    {  //--- if ESC is pressed, return 'true'     if(TerminalInfoInteger(TERMINAL\_KEYSTATE\_ESCAPE)!=0)        return(true);  //--- if PgDn is pressed and a graph screenshot is successfully taken, return 'true'     if(TerminalInfoInteger(TERMINAL\_KEYSTATE\_PAGEDOWN)!=0 && MakeAndSaveScreenshot(MQLInfoString(MQL\_PROGRAM\_NAME)+"\_Screenshot"))        return(true);  //--- return 'false'      return(false);    }  //+------------------------------------------------------------------+  //| Create a graph object and draw a curve                           |  //+------------------------------------------------------------------+  void CurvePlot(double &x\_array[], double &y\_array[], const color colour)    {     ExtGraph.Create(ChartID(), "Graphic", 0, 0, 0, GRAPH\_WIDTH, GRAPH\_HEIGHT);     ExtGraph.CurveAdd(x\_array, y\_array, ColorToARGB(colour), CURVE\_LINES);     ExtGraph.IndentUp(30);     ExtGraph.CurvePlotAll();     string text1="Press ESC to delete the graph and stop the script, or";     string text2="Press PgDn to create a screen, delete the graph and stop the script";     ExtGraph.TextAdd(54, 9, text1, ColorToARGB(clrBlack));     ExtGraph.TextAdd(54,21, text2, ColorToARGB(clrBlack));     ExtGraph.Update();    }  //+------------------------------------------------------------------+  //| Take a screenshot and save the image to a file                   |  //+------------------------------------------------------------------+  bool MakeAndSaveScreenshot(const string file\_name)    {     string file\_names[];     ResetLastError();     int selected=FileSelectDialog("Save Picture", NULL, "All files (\*.\*)|\*.\*", FSD\_WRITE\_FILE, file\_names, file\_name+".png");     if(selected<1)       {        if(selected<0)           PrintFormat("%s: FileSelectDialog() function returned error %d", \_\_FUNCTION\_\_, GetLastError());        return false;       }          bool res=false;     if(ChartSetInteger(0,CHART\_SHOW,false))        res=ChartScreenShot(0, file\_names[0], GRAPH\_WIDTH, GRAPH\_HEIGHT);     ChartSetInteger(0,CHART\_SHOW,true);     return(res);    } |

 

Result:

![MathLog1p_Screenshot](../../assets/mathlog1p_screenshot.png)

See also

[Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [Statistics](../../Standard-Library/Mathematics/Statistics/Statistics.md), [Scientific Charts](../../Standard-Library/Scientific-Charts/Scientific-Charts.md), [Client Terminal Properties](../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md)
