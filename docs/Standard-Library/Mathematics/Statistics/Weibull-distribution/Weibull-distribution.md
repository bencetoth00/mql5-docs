# Weibull distribution

Weibull distribution

This section contains functions for working with Weibull distribution. They allow to calculate density, probability, quantiles and to generate pseudo-random numbers distributed according to the Weibull law. The Weibull distribution is defined by the following formula:

![pdf_weibull_distribution](../../../../assets/pdf_weibull_distribution.png)

where:

- x — value of the random variable

- a —  parameter of the distribution (shape)

- b — parameter of the distribution (scale)

![DemoWeibullDistribution](../../../../assets/demoweibulldistribution.png)

In addition to the calculation of the individual random variables, the library also implements the ability to work with arrays of random variables.  

| Function | Description |
| --- | --- |
| [MathProbabilityDensityWeibull](MathProbabilityDensityWeibull/MathProbabilityDensityWeibull.md) | Calculates the probability density function of the Weibull distribution |
| [MathCumulativeDistributionWeibull](MathCumulativeDistributionWeibull/MathCumulativeDistributionWeibull.md) | Calculates the value of the Weibull probability distribution function |
| [MathQuantileWeibull](MathQuantileWeibull/MathQuantileWeibull.md) | Calculates the value of the inverse Weibull distribution function for the specified probability |
| [MathRandomWeibull](MathRandomWeibull/MathRandomWeibull.md) | Generates a pseudorandom variable/array of pseudorandom variables distributed according to the Weibull law |
| [MathMomentsWeibull](MathMomentsWeibull/MathMomentsWeibull.md) | Calculates the theoretical numerical values of the first 4 moments of the Weibull distribution |

Example:

|  |
| --- |
| #include <Graphics\Graphic.mqh>  #include <Math\Stat\Weibull.mqh>  #include <Math\Stat\Math.mqh>  #property script\_show\_inputs  //--- input parameters  input double a\_par=1;      // parameter of the distribution (shape)  input double b\_par=5;      // parameter of the distribution (scale)  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- hide the price chart     ChartSetInteger(0,CHART\_SHOW,false);  //--- initialize the random number generator       MathSrand(GetTickCount());  //--- generate a sample of the random variable     long chart=0;     string name="GraphicNormal";     int n=1000000;       // the number of values in the sample     int ncells=51;       // the number of intervals in the histogram     double x[];          // centers of the histogram intervals     double y[];          // the number of values from the sample falling within the interval     double data[];       // sample of random values     double max,min;      // the maximum and minimum values in the sample  //--- obtain a sample from the Weibull distribution     MathRandomWeibull(a\_par,b\_par,n,data);  //--- calculate the data to plot the histogram     CalculateHistogramArray(data,x,y,max,min,ncells);  //--- obtain the sequence boundaries and the step for plotting the theoretical curve     double step;     GetMaxMinStepValues(max,min,step);     step=MathMin(step,(max-min)/ncells);  //--- obtain the theoretically calculated data at the interval of [min,max]     double x2[];     double y2[];     MathSequence(min,max,step,x2);     MathProbabilityDensityWeibull(x2,a\_par,b\_par,false,y2);  //--- set the scale     double theor\_max=y2[ArrayMaximum(y2)];     double sample\_max=y[ArrayMaximum(y)];     double k=sample\_max/theor\_max;     for(int i=0; i<ncells; i++)        y[i]/=k;  //--- output charts     CGraphic graphic;     if(ObjectFind(chart,name)<0)        graphic.Create(chart,name,0,0,0,780,380);     else        graphic.Attach(chart,name);     graphic.BackgroundMain(StringFormat("Weibull distribution a=%G b=%G",a\_par,b\_par));     graphic.BackgroundMainSize(16);  //--- disable automatic scaling of the X axis     graphic.XAxis().AutoScale(false);     graphic.XAxis().Max(max);     graphic.XAxis().Min(min);  //--- plot all curves     graphic.CurveAdd(x,y,CURVE\_HISTOGRAM,"Sample").HistogramWidth(6);  //--- and now plot the theoretical curve of the distribution density     graphic.CurveAdd(x2,y2,CURVE\_LINES,"Theory");     graphic.CurvePlotAll();  //--- plot all curves     graphic.Update();    }  //+------------------------------------------------------------------+  //|  Calculate frequencies for data set                              |  //+------------------------------------------------------------------+  bool CalculateHistogramArray(const double &data[],double &intervals[],double &frequency[],                               double &maxv,double &minv,const int cells=10)    {     if(cells<=1) return (false);     int size=ArraySize(data);     if(size<cells\*10) return (false);     minv=data[ArrayMinimum(data)];     maxv=data[ArrayMaximum(data)];     double range=maxv-minv;     double width=range/cells;     if(width==0) return false;     ArrayResize(intervals,cells);     ArrayResize(frequency,cells);  //--- define the interval centers     for(int i=0; i<cells; i++)       {        intervals[i]=minv+i\*width;        frequency[i]=0;       }  //--- fill the frequencies of falling within the interval     for(int i=0; i<size; i++)       {        int ind=int((data[i]-minv)/width);        if(ind>=cells) ind=cells-1;        frequency[ind]++;       }     return (true);    }  //+------------------------------------------------------------------+  //|  Calculates values for sequence generation                       |  //+------------------------------------------------------------------+  void GetMaxMinStepValues(double &maxv,double &minv,double &stepv)    {  //--- calculate the absolute range of the sequence to obtain the precision of normalization     double range=MathAbs(maxv-minv);     int degree=(int)MathRound(MathLog10(range));  //--- normalize the maximum and minimum values to the specified precision     maxv=NormalizeDouble(maxv,degree);     minv=NormalizeDouble(minv,degree);  //--- sequence generation step is also set based on the specified precision     stepv=NormalizeDouble(MathPow(10,-degree),degree);     if((maxv-minv)/stepv<10)        stepv/=10.;    } |
