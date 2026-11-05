# Client Terminal Properties

Client Terminal Properties

Information about the client terminal can be obtained by two functions: [TerminalInfoInteger()](../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) and [TerminalInfoString()](../../../Checkup/TerminalInfoString/TerminalInfoString.md). For parameters, these functions accept values from ENUM\_TERMINAL\_INFO\_INTEGER and ENUM\_TERMINAL\_INFO\_STRING respectively.

ENUM\_TERMINAL\_INFO\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| TERMINAL\_BUILD | The client terminal build number | int |
| TERMINAL\_COMMUNITY\_ACCOUNT | The flag indicates the presence of MQL5.community authorization data in the terminal | bool |
| TERMINAL\_COMMUNITY\_CONNECTION | Connection to MQL5.community | bool |
| TERMINAL\_CONNECTED | Connection to a trade server | bool |
| TERMINAL\_DLLS\_ALLOWED | Permission to use DLL | bool |
| TERMINAL\_TRADE\_ALLOWED | [Permission to trade](../../../MQL5-programs/Trade-Permission/Trade-Permission.md) | bool |
| TERMINAL\_EMAIL\_ENABLED | Permission to send e-mails using SMTP-server and login, specified in the terminal settings | bool |
| TERMINAL\_FTP\_ENABLED | Permission to send reports using FTP-server and login, specified in the terminal settings | bool |
| TERMINAL\_NOTIFICATIONS\_ENABLED | Permission to send notifications to smartphone | bool |
| TERMINAL\_MAXBARS | The maximal bars count on the chart | int |
| TERMINAL\_MQID | The flag indicates the presence of MetaQuotes ID data for [Push notifications](../../../Network-Functions/SendNotification/SendNotification.md) | bool |
| TERMINAL\_CODEPAGE | Number of [the code page of the language](../../Input-Output-Constants/Use-of-a-Codepage/Use-of-a-Codepage.md) installed in the client terminal | int |
| TERMINAL\_CPU\_CORES | The number of CPU cores in the system | int |
| TERMINAL\_DISK\_SPACE | Free disk space for the MQL5\Files folder of the terminal (agent), MB | int |
| TERMINAL\_MEMORY\_PHYSICAL | Physical memory in the system, MB | int |
| TERMINAL\_MEMORY\_TOTAL | Memory available to the process of the terminal (agent), MB | int |
| TERMINAL\_MEMORY\_AVAILABLE | Free memory of the terminal (agent) process, MB | int |
| TERMINAL\_MEMORY\_USED | Memory used by the terminal (agent), MB | int |
| TERMINAL\_X64 | Indication of the "64-bit terminal" | bool |
| TERMINAL\_OPENCL\_SUPPORT | The version of the supported OpenCL in the format of 0x00010002 = 1.2.  "0" means that OpenCL is not supported | int |
| TERMINAL\_SCREEN\_DPI | The resolution of information display on the screen is measured as number of Dots in a line per Inch (DPI).  Knowing the parameter value, you can set the size of graphical objects so that they look the same on monitors with different resolution characteristics. | int |
| TERMINAL\_SCREEN\_LEFT | The left coordinate of the virtual screen. A virtual screen is a rectangle that covers all monitors. If the system has two monitors ordered from right to left, then the left coordinate of the virtual screen can be on the border of two monitors. | int |
| TERMINAL\_SCREEN\_TOP | The top coordinate of the virtual screen | int |
| TERMINAL\_SCREEN\_WIDTH | Terminal width | int |
| TERMINAL\_SCREEN\_HEIGHT | Terminal height | int |
| TERMINAL\_LEFT | The left coordinate of the terminal relative to the virtual screen | int |
| TERMINAL\_TOP | The top coordinate of the terminal relative to the virtual screen | int |
| TERMINAL\_RIGHT | The right coordinate of the terminal relative to the virtual screen | int |
| TERMINAL\_BOTTOM | The bottom coordinate of the terminal relative to the virtual screen | int |
| TERMINAL\_PING\_LAST | The last known value of a ping to a trade server in microseconds. One second comprises of one million microseconds | int |
| TERMINAL\_VPS | Indication that the terminal is launched on the [MetaTrader Virtual Hosting server](https://www.mql5.com/en/vps) (MetaTrader VPS) | bool |
| Key identifier | Description |  |
| TERMINAL\_KEYSTATE\_LEFT | State of the "Left arrow" key | int |
| TERMINAL\_KEYSTATE\_UP | State of the "Up arrow" key | int |
| TERMINAL\_KEYSTATE\_RIGHT | State of the "Right arrow" key | int |
| TERMINAL\_KEYSTATE\_DOWN | State of the "Down arrow" key | int |
| TERMINAL\_KEYSTATE\_SHIFT | State of the "Shift" key | int |
| TERMINAL\_KEYSTATE\_CONTROL | State of the "Ctrl" key | int |
| TERMINAL\_KEYSTATE\_MENU | State of the "Windows" key | int |
| TERMINAL\_KEYSTATE\_CAPSLOCK | State of the "CapsLock" key | int |
| TERMINAL\_KEYSTATE\_NUMLOCK | State of the "NumLock" key | int |
| TERMINAL\_KEYSTATE\_SCRLOCK | State of the "ScrollLock" key | int |
| TERMINAL\_KEYSTATE\_ENTER | State of the "Enter" key | int |
| TERMINAL\_KEYSTATE\_INSERT | State of the "Insert" key | int |
| TERMINAL\_KEYSTATE\_DELETE | State of the "Delete" key | int |
| TERMINAL\_KEYSTATE\_HOME | State of the "Home" key | int |
| TERMINAL\_KEYSTATE\_END | State of the "End" key | int |
| TERMINAL\_KEYSTATE\_TAB | State of the "Tab" key | int |
| TERMINAL\_KEYSTATE\_PAGEUP | State of the "PageUp" key | int |
| TERMINAL\_KEYSTATE\_PAGEDOWN | State of the "PageDown" key | int |
| TERMINAL\_KEYSTATE\_ESCAPE | State of the "Escape" key | int |

Call to TerminalInfoInteger(TERMINAL\_KEYSTATE\_XXX) returns the same state code of a key as the [GetKeyState()](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate) function in MSDN.

 

Example of scaling factor calculation:

|  |
| --- |
| //--- Creating a 1.5 inch wide button on a screen  int screen\_dpi = TerminalInfoInteger(TERMINAL\_SCREEN\_DPI); // Find DPI of the user monitor  int base\_width = 144;                                      // The basic width in the screen points for standard monitors with DPI=96  int width      = (button\_width \* screen\_dpi) / 96;         // Calculate the button width for the user monitor (for the specific DPI)  ...     //--- Calculating the scaling factor as a percentage  int scale\_factor=(TerminalInfoInteger(TERMINAL\_SCREEN\_DPI) \* 100) / 96;  //--- Use of the scaling factor  width=(base\_width \* scale\_factor) / 100; |

In the above example, the graphical [resource](../../../MQL5-programs/Resources/Resources.md) looks the same on monitors with different resolution characteristics. The size of control elements (buttons, dialog windows, etc.) corresponds to personalization settings.

 

ENUM\_TERMINAL\_INFO\_DOUBLE

| Identifier | Description | Type |
| --- | --- | --- |
| TERMINAL\_COMMUNITY\_BALANCE | Balance in MQL5.community | double |
| TERMINAL\_RETRANSMISSION | Percentage of resent network packets in the TCP/IP protocol for all running applications and services on the given computer. Packet loss occurs even in the fastest and correctly configured networks. In this case, there is no confirmation of packet delivery between the recipient and the sender, therefore lost packets are resent.     It is not an indication of the connection quality between a particular terminal and a trade server, since the percentage is calculated for the entire network activity, including system and background activity.     The TERMINAL\_RETRANSMISSION value is requested from the operating system once per minute. The terminal itself does not calculate this value. | double |

 

[File operations](../../../File-Functions/File-Functions.md) can be performed only in two directories; corresponding paths can be obtained using the request for TERMINAL\_DATA\_PATH and TERMINAL\_COMMONDATA\_PATH properties.

ENUM\_TERMINAL\_INFO\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| TERMINAL\_LANGUAGE | Language of the terminal | string |
| TERMINAL\_COMPANY | Company name | string |
| TERMINAL\_NAME | Terminal name | string |
| TERMINAL\_PATH | Folder from which the terminal is started | string |
| TERMINAL\_DATA\_PATH | Folder in which terminal data are stored | string |
| TERMINAL\_COMMONDATA\_PATH | Common path for all of the terminals installed on a computer | string |
| TERMINAL\_CPU\_NAME | CPU name | string |
| TERMINAL\_CPU\_ARCHITECTURE | CPU architecture | string |
| TERMINAL\_OS\_VERSION | User's OS name | string |
| TERMINAL\_COLORTHEME\_NAME | Terminal color scheme; possible values: Light and Dark. | string |

For a better understanding of paths, stored in properties of TERMINAL\_PATH, TERMINAL\_DATA\_PATH and TERMINAL\_COMMONDATA\_PATH parameters, it is recommended to execute the script, which will return these values for the current copy of the client terminal, installed on your computer

Example: Script returns information about the client terminal paths

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                          Check\_TerminalPaths.mq5 |  //|                        Copyright 2009, MetaQuotes Software Corp. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "2009, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //---     Print("TERMINAL\_PATH = ",TerminalInfoString(TERMINAL\_PATH));     Print("TERMINAL\_DATA\_PATH = ",TerminalInfoString(TERMINAL\_DATA\_PATH));     Print("TERMINAL\_COMMONDATA\_PATH = ",TerminalInfoString(TERMINAL\_COMMONDATA\_PATH));    } |

As result of the script execution in the Experts Journal you will see a messages, like the following:

![Getting data on a working folder of the terminal](../../../assets/terminal_paths.png "Getting data on a working folder of the terminal")

 

 

Get Terminal Color Scheme Information

The terminal supports two color schemes: Light (default) and Dark. When developing custom applications with graphical user interfaces, programmers should take the current terminal color scheme into account. Visual components used in the application should be dynamically adaptable to enhance user experience and maintain visual consistency.

To support this, the language provides functions for detecting the terminal color scheme:

- The TERMINAL\_COLORTHEME\_NAME value from the [ENUM\_TERMINAL\_INFO\_STRING](Client-Terminal-Properties.md#enum_terminal_info_string) enumeration allows you to retrieve the name of the current color scheme using the [TerminalInfoString](../../../Checkup/TerminalInfoString/TerminalInfoString.md) function. Possible values: Light and Dark.
- Use the THEME\_COLOR\_\* values from the [ENUM\_TERMINAL\_INFO\_INTEGER](Client-Terminal-Properties.md#enum_terminal_info_integer) enumeration to retrieve the colors of specific UI elements through the [TerminalInfoInteger](../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function.

 

| Identifier | Description | Property type |
| --- | --- | --- |
| THEME\_COLOR\_WINDOW | Window background | color |
| THEME\_COLOR\_WINDOWTEXT | Text in the window | color |
| THEME\_COLOR\_BTNTEXT | Button text | color |
| THEME\_COLOR\_GRAYTEXT | Inactive (disabled) text | color |
| THEME\_COLOR\_INFOTEXT | Tooltip text | color |
| THEME\_COLOR\_INFOBK | Tooltip background | color |
| THEME\_COLOR\_3DFACE | Front face of 3D elements | color |
| THEME\_COLOR\_3DLIGHT | Light side of 3D elements | color |
| THEME\_COLOR\_3DSHADOW | Shadow side of 3D elements | color |
| THEME\_COLOR\_3DDKSHADOW | Dark shadow of 3D elements | color |
| THEME\_COLOR\_3DHILIGHT | Highlight of 3D elements | color |
| THEME\_COLOR\_HIGHLIGHT | Background of selected elements | color |
| THEME\_COLOR\_HIGHLIGHTTEXT | Text of selected elements | color |
| THEME\_COLOR\_BTNFACE | Button front face | color |
| THEME\_COLOR\_BTNHILIGHT | Button highlight | color |
| THEME\_COLOR\_BTNSHADOW | Button shadow | color |
| THEME\_COLOR\_MENU | Menu background | color |
| THEME\_COLOR\_MENUBAR | Menu bar background | color |
| THEME\_COLOR\_MENUTEXT | Menu text | color |
| THEME\_COLOR\_MENUHILIGHT | Highlight of selected menu item | color |
| THEME\_COLOR\_ACTIVECAPTION | Active window title | color |
| THEME\_COLOR\_INACTIVECAPTION | Inactive window title | color |
| THEME\_COLOR\_GRADIENTINACTIVECAPTION | Gradient of inactive window title | color |
| THEME\_COLOR\_CAPTIONTEXT | Window title text | color |
| THEME\_COLOR\_INACTIVECAPTIONTEXT | Inactive window title text | color |
| THEME\_COLOR\_HOTTEXT | Hyperlinks or active elements | color |
| THEME\_COLOR\_NONE | Color not selected | color |
| THEME\_COLOR\_SEPARATOR | Separator | color |
| THEME\_COLOR\_SCROLLBACK | Scrollbar | color |
| THEME\_COLOR\_LINE1 | Background color of odd rows in the Journal | color |
| THEME\_COLOR\_LINE2 | Background color of even rows in the Journal | color |
| THEME\_COLOR\_GRID | Grid color in the Journal | color |
| THEME\_COLOR\_SUMMARY | Background color of summary row in the Journal | color |
| THEME\_COLOR\_ERROR | Error message text color | color |
| THEME\_COLOR\_INVALID | Invalid value text color | color |
| THEME\_COLOR\_NEGATIVE | Negative value color | color |
| THEME\_COLOR\_POSITIVE | Positive value color | color |
| THEME\_COLOR\_LINK | Link color | color |
| THEME\_COLOR\_LINKHOVER | Link hover color | color |
| THEME\_COLOR\_LINKTESTER | Link color from [cached results of previous](https://www.metatrader5.com/en/terminal/help/algotrading/strategy_optimization#cache) testing/optimization runs | color |
| THEME\_COLOR\_TEXTUP | "Button released" state | color |
| THEME\_COLOR\_TEXTDOWN | "Button pressed" state | color |
| THEME\_COLOR\_BACKUP | Color of "BUY" and "SELL" buttons in "One Click Trading" when the quote increases | color |
| THEME\_COLOR\_BACKDOWN | Color of "BUY" and "SELL" buttons in "One Click Trading" when the quote decreases | color |
| THEME\_COLOR\_CLOSE | "Close" operation button color | color |
| THEME\_COLOR\_BUY | "BUY" operation button color | color |
| THEME\_COLOR\_SELL | "SELL" operation button color | color |
| THEME\_COLOR\_DEPOSIT | "Deposit" button color | color |
| THEME\_COLOR\_WITHDRAWAL | "Withdrawal" button color | color |
| THEME\_COLOR\_BID | Bid line color | color |
| THEME\_COLOR\_ASK | Ask line color | color |
| THEME\_COLOR\_STOPS | Stop line color | color |
| THEME\_COLOR\_STOPS\_RED | StopLoss value highlight when profit is negative (Trade tab) | color |
| THEME\_COLOR\_STOPS\_GREEN | StopLoss value highlight when profit is positive (Trade tab) | color |
| THEME\_COLOR\_CONFIRM | "Accept" button color in the order submission window | color |
| THEME\_COLOR\_REQUOTE | "Requote" button color in the order submission window | color |
| THEME\_COLOR\_REJECT | "Reject" button color in the order submission window | color |
| THEME\_COLOR\_NOTIFICATION | Color of a change notification from the server in the order submission window | color |
| THEME\_COLOR\_RATING | Rating bar color in the [learning system](https://www.metatrader5.com/en/releasenotes/terminal/2151) | color |
| THEME\_COLOR\_BOOK\_BUY | Background color of buy levels in the Depth of Market | color |
| THEME\_COLOR\_BOOK\_SELL | Background color of sell levels in the Depth of Market | color |
| THEME\_COLOR\_BOOK\_LAST | Color of the last trade in the Depth of Market | color |
| THEME\_COLOR\_BOOK\_STOP | StopLoss level color in the Depth of Market | color |
| THEME\_COLOR\_BOOK\_SPREAD | Background color of levels within the spread in the Depth of Market | color |
| THEME\_COLOR\_TICKS\_BID | Bid line color on the tick chart in the order submission window | color |
| THEME\_COLOR\_TICKS\_ASK | Ask line color on the tick chart in the order submission window | color |
| THEME\_COLOR\_TICKS\_LAST | Last line color on the tick chart in the order submission window | color |
| THEME\_COLOR\_TICKS\_CROSS | Crosshair color on the tick chart in the order submission window | color |
| THEME\_COLOR\_TICKS\_SL | StopLoss line color on the tick chart in the order submission window | color |
| THEME\_COLOR\_TICKS\_TP | TakeProfit line color on the tick chart in the order submission window | color |
| THEME\_COLOR\_TESTER\_START | "Start" button color in testing/optimization | color |
| THEME\_COLOR\_TESTER\_STOP | "Stop" button color in testing/optimization | color |
| THEME\_COLOR\_TESTER\_START\_FRAME | Border color of the "Start" button in testing/optimization | color |
| THEME\_COLOR\_TESTER\_STOP\_FRAME | Border color of the "Stop" button in testing/optimization | color |
| THEME\_COLOR\_TESTER\_PROGRESS | Progress bar color in testing/optimization | color |
| THEME\_COLOR\_TESTER\_BALANCE | Balance line color in the Strategy Tester | color |
| THEME\_COLOR\_TESTER\_EQUITY | Equity line color in the Strategy Tester | color |
| THEME\_COLOR\_TESTER\_MARGIN | Deposit Load graph color in the Strategy Tester | color |
| THEME\_COLOR\_PROFILER\_CALL | Color of the code line with a call during Profiling | color |
| THEME\_COLOR\_PROFILER\_CALLSEL | Selected code line color with a call during Profiling | color |
| THEME\_COLOR\_PROFILER\_LINE | Line color in the Profiler Journal | color |
| THEME\_COLOR\_PROFILER\_LINESEL | Selected line color in the Profiler Journal | color |
