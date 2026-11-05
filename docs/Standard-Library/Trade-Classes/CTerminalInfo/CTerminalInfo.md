# CTerminalInfo

CTerminalInfo

CTerminalInfo is a class for simplified access to the properties of mql5 program environment.

Description

CTerminalInfo class provides access to the properties of mql5 program environment.

Declaration

|  |
| --- |
| class CTerminalInfo : public CObject |

Title

|  |
| --- |
| #include <Trade\TerminalInfo.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CTerminalInfo |

Class methods by groups

| Methods for access to the properties of integer type |  |
| --- | --- |
| [Build](Build/Build.md) | Gets the build number of the client terminal |
| [IsConnected](IsConnected/IsConnected.md) | Gets the information about connection to trade server |
| [IsDLLsAllowed](IsDLLsAllowed/IsDLLsAllowed.md) | Gets the information about permission of DLL usage |
| [IsTradeAllowed](IsTradeAllowed/IsTradeAllowed.md) | Gets the information about permission to trade |
| [IsEmailEnabled](IsEmailEnabled/IsEmailEnabled.md) | Gets the information about permission to send e-mails to SMTP server and login, specified in the terminal settings |
| [IsFtpEnabled](IsFtpEnabled/IsFtpEnabled.md) | Gets the information about permission to send trade reports to FTP server and login, specified in the terminal settings |
| [MaxBars](MaxBars/MaxBars.md) | Gets the information about maximum number of bars on chart |
| [CodePage](CodePage/CodePage.md) | Gets the information about the code page of the language in the client terminal |
| [CPUCores](CPUCores/CPUCores.md) | Gets the information about the CPU cores |
| [MemoryPhysical](MemoryPhysical/MemoryPhysical.md) | Gets the information about the physical memory (in Mb) |
| [MemoryTotal](MemoryTotal/MemoryTotal.md) | Gets the information about the total memory available for the terminal/agent process (in Mb) |
| [MemoryAvailable](MemoryAvailable/MemoryAvailable.md) | Gets the information about the free memory available for the terminal/agent process (in Mb) |
| [MemoryUsed](MemoryUsed/MemoryUsed.md) | Gets the information about the memory used by the terminal/agent process (in Mb) |
| [IsX64](IsX64/IsX64.md) | Gets the information about the type of the client terminal |
| [OpenCLSupport](OpenCLSupport/OpenCLSupport.md) | Gets the information about the version of OpenCL supported by video card |
| [DiskSpace](DiskSpace/DiskSpace.md) | Gets the information about free disk space (in Mb) |
| Methods for access to the properties of string type |  |
| [Language](Language/Language.md) | Gets the language of the client terminal |
| [Name](Name/Name.md) | Gets the name of the client terminal |
| [Company](Company/Company.md) | Gets the company name of the client terminal |
| [Path](Path/Path.md) | Gets the folder of the client terminal |
| [DataPath](DataPath/DataPath.md) | Gets the data folder of the client terminal |
| [CommonDataPath](CommonDataPath/CommonDataPath.md) | Gets the common data folder of all client terminals, installed on the computer |
| Access to MQL5 API functions |  |
| [InfoInteger](InfoInteger/InfoInteger.md) | Gets the value of the property of integer type |
| [InfoString](InfoString/InfoString.md) | Gets the value of property of string type |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
