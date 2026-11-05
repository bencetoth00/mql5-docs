# Common Functions

Common Functions

General-purpose functions not included into any specialized group are listed here.

| Function | Action |
| --- | --- |
| [Alert](Alert/Alert.md) | Displays a message in a separate window |
| [CheckPointer](CheckPointer/CheckPointer.md) | Returns the type of the object pointer |
| [Comment](Comment/Comment.md) | Outputs a comment in the left top corner of the chart |
| [CryptEncode](CryptEncode/CryptEncode.md) | Transforms the data from array with the specified method |
| [CryptDecode](CryptDecode/CryptDecode.md) | Performs the inverse transformation of the data from array |
| [DebugBreak](DebugBreak/DebugBreak.md) | Program breakpoint in debugging |
| [ExpertRemove](ExpertRemove/ExpertRemove.md) | Stops Expert Advisor and unloads it from the chart |
| [GetPointer](GetPointer/GetPointer.md) | Returns the object [pointer](../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md) |
| [GetTickCount](GetTickCount/GetTickCount.md) | Returns the number of milliseconds that have elapsed since the system was started |
| [GetTickCount64](GetTickCount64/GetTickCount64.md) | Returns the number of milliseconds that have elapsed since the system was started |
| [GetMicrosecondCount](GetMicrosecondCount/GetMicrosecondCount.md) | Returns the number of microseconds that have elapsed since the start of MQL5 program |
| [MessageBox](MessageBox/MessageBox.md) | Creates, displays a message box and manages it |
| [PeriodSeconds](PeriodSeconds/PeriodSeconds.md) | Returns the number of seconds in the period |
| [PlaySound](PlaySound/PlaySound.md) | Plays a sound file |
| [Print](Print/Print.md) | Displays a message in the log |
| [PrintFormat](PrintFormat/PrintFormat.md) | Formats and prints the sets of symbols and values in a log file in accordance with a preset format |
| [ResetLastError](ResetLastError/ResetLastError.md) | Sets the value of a predetermined variable [\_LastError](../Predefined-Variables/_LastError/_LastError.md) to zero |
| [ResourceCreate](ResourceCreate/ResourceCreate.md) | Creates an image resource based on a data set |
| [ResourceFree](ResourceFree/ResourceFree.md) | Deletes [dynamically created resource](ResourceCreate/ResourceCreate.md#dynamic_resourcecreate) (freeing the memory allocated for it) |
| [ResourceReadImage](ResourceReadImage/ResourceReadImage.md) | Reads data from the graphical resource [created by ResourceCreate() function](ResourceCreate/ResourceCreate.md#dynamic_resourcecreate) or [saved in EX5 file during compilation](../MQL5-programs/Resources/Resources.md#resource_include) |
| [ResourceSave](ResourceSave/ResourceSave.md) | Saves a resource into the specified file |
| [SetUserError](SetUserError/SetUserError.md) | Sets the predefined variable \_LastError into the value equal to ERR\_USER\_ERROR\_FIRST + user\_error |
| [SetReturnError](SetReturnError/SetReturnError.md) | Sets the code that returns the terminal process when completing the operation. |
| [Sleep](Sleep/Sleep.md) | Suspends execution of the current Expert Advisor or script within a specified interval |
| [TerminalClose](TerminalClose/TerminalClose.md) | Commands the terminal to complete operation |
| [TesterHideIndicators](TesterHideIndicators/TesterHideIndicators.md) | Sets the mode of displaying/hiding indicators used in an EA |
| [TesterStatistics](TesterStatistics/TesterStatistics.md) | It returns the value of a specified statistic calculated based on testing results |
| [TesterStop](TesterStop/TesterStop.md) | Gives program operation completion command when [testing](https://www.metatrader5.com/en/terminal/help/algotrading/testing) |
| [TesterDeposit](TesterDeposit/TesterDeposit.md) | Emulates depositing funds during a test. It can be used in some money management systems |
| [TesterWithdrawal](TesterWithdrawal/TesterWithdrawal.md) | Emulates the operation of money withdrawal in the process of testing |
| [TranslateKey](TranslateKey/TranslateKey.md) | Returns a Unicode character by a virtual key code |
| [ZeroMemory](ZeroMemory/ZeroMemory.md) | Resets a variable passed to it by reference. The variable can be of any type, except for classes and structures that have constructors. |
