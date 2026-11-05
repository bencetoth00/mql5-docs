# Predefined Macro Substitutions


To simplify the debugging process and obtain information about operation of a mql5-program, there are special macro constant, values of which are set at the moment of compilation. The easiest way to use these constants is outputting values by the [Print()](../../../Common-Functions/Print/Print.md) function, as it's shown in the example.

| Constant | Description |
| --- | --- |
| \_\_CPU\_ARCHITECTURE\_\_ | Name of architecture (set of commands) EX5 file compiled for |
| \_\_DATE\_\_ | File compilation date without time (hours, minutes and seconds are equal to 0) |
| \_\_DATETIME\_\_ | File compilation date and time |
| \_\_LINE\_\_ | Line number in the source code, in which the macro is located |
| \_\_FILE\_\_ | Name of the currently compiled file |
| \_\_PATH\_\_ | An absolute path to the file that is currently being compiled |
| \_\_FUNCTION\_\_ | Name of the function, in whose body the macro is located |
| \_\_FUNCSIG\_\_ | Signature of the function in whose body the macro is located. Logging of the full description of functions can be useful in the identification of [overloaded functions](../../../Language-Basics/Functions/Function-Overloading/Function-Overloading.md) |
| \_\_MQLBUILD\_\_,\_\_MQL5BUILD\_\_ | Compiler build number |
| \_\_COUNTER\_\_ | The compiler for each encountered \_\_COUNTER\_\_ declaration substitutes the counter value from 0 to N-1 where N is a number of uses in the code.  The \_\_COUNTER\_\_ order is guaranteed when recompiling the source code with no changes.  The \_\_COUNTER\_\_ value is calculated the following way:   - the initial counter value is 0, - after each counter usage, its value is increased by 1, - first, the compiler expands all macros and templates into source code on-site, - a separate code is created for each template function specialization, - a separate code is created for each template class/structure specialization, - next, the compiler passes through the obtained source code in the defined order and replaces each detected \_\_COUNTER\_\_ usage with the current counter value.   The [example](Predefined-Macro-Substitutions.md#counter_sample) below shows how the compiler handles the source code and replaces all instances of \_\_COUNTER\_\_ it meets with sequentially increasing values. |
| \_\_RANDOM\_\_ | The compiler inserts a random [ulong](../../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#ulong) value for each \_\_RANDOM\_\_ declaration. |

Example:

```cpp
#property copyright "Copyright © 2009, MetaQuotes Software Corp."
#property link      "https://www.metaquotes.net"
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
void OnInit()
  {
//--- an example of information output at Expert Advisor initialization
   Print(" __FUNCTION__ = ",__FUNCTION__,"  __LINE__ = ",__LINE__);
//--- set the interval between the timer events
   EventSetTimer(5);
//---
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//--- an example of information output at Expert Advisor deinitialization
   Print(" __FUNCTION__ = ",__FUNCTION__,"  __LINE__ = ",__LINE__);
//---
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//--- information output at tick receipt
   Print(" __MQLBUILD__ = ",__MQLBUILD__,"  __FILE__ = ",__FILE__);
   Print(" __FUNCTION__ = ",__FUNCTION__,"  __LINE__ = ",__LINE__);
   test1(__FUNCTION__);
   test2();
//---
  }
//+------------------------------------------------------------------+
//| test1                                                            |
//+------------------------------------------------------------------+
void test1(string par)
  {
//--- information output inside the function
   Print(" __FUNCTION__ = ",__FUNCTION__,"  __LINE__ = ",__LINE__," par=",par);
  }
//+------------------------------------------------------------------+
//| test2                                                            |
//+------------------------------------------------------------------+
void test2()
  {
//--- information output inside the function
   Print(" __FUNCTION__ = ",__FUNCTION__,"  __LINE__ = ",__LINE__);
  }
//+------------------------------------------------------------------+
//| OnTimer event handler                                            |
//+------------------------------------------------------------------+
void OnTimer()
  {
//---
   Print(" __FUNCTION__ = ",__FUNCTION__,"  __LINE__ = ",__LINE__);
   test1(__FUNCTION__);
  }
```

 

The example for learning how to work with the [\_\_COUNTER\_\_](Predefined-Macro-Substitutions.md) macro

```cpp
//--- create a macro for a quick display of the expression and its value in the journal
#define print(expr) Print(#expr,"=",expr)
//--- define the MACRO_COUNTER custom macro via the predefined __COUNTER__ macro
#define MACRO_COUNTER __COUNTER__
//--- set the input value of the variable using the __COUNTER__ macro
input int InpVariable = __COUNTER__;
//--- set the value of the global variable using the __COUNTER__ macro before defining the functions
int ExtVariable = __COUNTER__;
//+------------------------------------------------------------------+
//| the function returns the __COUNTER__ value                       |
//+------------------------------------------------------------------+
int GlobalFunc(void)
  {
   return(__COUNTER__);
  }
//+------------------------------------------------------------------+
//| the template function returns the __COUNTER__ value              |
//+------------------------------------------------------------------+
template<typename T>
int GlobalTemplateFunc(void)
  {
   return(__COUNTER__);
  }
//+------------------------------------------------------------------+
//| the structure with the method returning __COUNTER__              |
//+------------------------------------------------------------------+
struct A
  {
   int               dummy;  // not used
   int               Method(void)
     {
      return(__COUNTER__);
     }
  };
//+------------------------------------------------------------------+
//| the template structure with the method returning __COUNTER__     |
//+------------------------------------------------------------------+
template<typename T>
struct B
  {
   int               dummy;  // not used
   int               Method(void)
     {
      return(__COUNTER__);
     }
  };
//+------------------------------------------------------------------+
//| the structure with the template method returning __COUNTER__     |
//+------------------------------------------------------------------+
struct C
  {
   int               dummy;  // not used
   template<typename T>
   int               Method(void)
     {
      return(__COUNTER__);
     }
  };
//+------------------------------------------------------------------+
//| the function #2, which returns the __COUNTER__ value             |
//+------------------------------------------------------------------+
int GlobalFunc2(void)
  {
   return(__COUNTER__);
  }
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart(void)
  {
// __COUNTER__ in the macro and the variables
   print(MACRO_COUNTER);
   print(InpVariable);
   print(ExtVariable);
//--- __COUNTER__ in the functions
   print(GlobalFunc());
   print(GlobalFunc());                // the value is not changed
   print(GlobalTemplateFunc<int>());
   print(GlobalTemplateFunc<int>());   // the value is not changed
   print(GlobalTemplateFunc<double>());// the value has changed
   print(GlobalFunc2());
   print(GlobalFunc2());               // the value is not changed
// __COUNTER__ in the structure
   A a1, a2;
   print(a1.Method());
   print(a2.Method());                 // the value is not changed
// __COUNTER__ in the template structure
   B<int> b1, b2;
   B<double> b3;
   print(b1.Method());
   print(b2.Method());                 // the value is not changed
   print(b3.Method());                 // the value has changed
// __COUNTER__ in the structure with the template function
   C c1, c2;
   print(c1.Method<int>());
   print(c1.Method<double>());         // the value has changed
   print(c2.Method<int>());            // the same value as during the first c1.Method<int>() call
//--- let's have another look at __COUNTER__ in the macro and the global variable
   print(MACRO_COUNTER);  // the value has changed
   print(ExtGlobal2);
  }
//--- set the value of the global variable using the __COUNTER__ macro after defining the functions
int ExtGlobal2 = __COUNTER__;
//+------------------------------------------------------------------+
/* Result
   __COUNTER__=3
   InpVariable=0
   ExtVariable=1
   GlobalFunc()=5
   GlobalFunc()=5
   GlobalTemplateFunc<int>()=8
   GlobalTemplateFunc<int>()=8
   GlobalTemplateFunc<double>()=9
   GlobalFunc2()=7
   GlobalFunc2()=7
   a1.Method()=6
   a2.Method()=6
   b1.Method()=10
   b2.Method()=10
   b3.Method()=11
   c1.Method<int>()=12
   c1.Method<double>()=13
   c2.Method<int>()=12
   __COUNTER__=4
   ExtGlobal2=2
*/
```