# MessageBox

# Constants of the MessageBox Dialog Window

This section contains return codes of the [MessageBox()](../../../Common-Functions/MessageBox/MessageBox.md) function. If a message window has a Cancel button, the function returns IDCANCEL, in case if the ESC key or the Cancel button is pressed. If there is no Cancel button in the message window, the pressing of ESC does not give any effect.

| Constant | Value | Description |
| --- | --- | --- |
| IDOK | 1 | "OK" button has been pressed |
| IDCANCEL | 2 | "Cancel" button has been pressed |
| IDABORT | 3 | "Abort" button has been pressed |
| IDRETRY | 4 | "Retry" button has been pressed |
| IDIGNORE | 5 | "Ignore" button has been pressed |
| IDYES | 6 | "Yes" button has been pressed |
| IDNO | 7 | "No" button has been pressed |
| IDTRYAGAIN | 10 | "Try Again" button has been pressed |
| IDCONTINUE | 11 | "Continue" button has been pressed |

 

The main flags of the [MessageBox()](../../../Common-Functions/MessageBox/MessageBox.md) function define contents and behavior of the dialog window. This value can be a combination of the following flag groups:

| Constant | Value | Description |
| --- | --- | --- |
| MB\_OK | 0x00000000 | Message window contains only one button: OK. Default |
| MB\_OKCANCEL | 0x00000001 | Message window contains two buttons: OK and Cancel |
| MB\_ABORTRETRYIGNORE | 0x00000002 | Message window contains three buttons: Abort, Retry and Ignore |
| MB\_YESNOCANCEL | 0x00000003 | Message window contains three buttons: Yes, No and Cancel |
| MB\_YESNO | 0x00000004 | Message window contains two buttons: Yes and No |
| MB\_RETRYCANCEL | 0x00000005 | Message window contains two buttons: Retry and Cancel |
| MB\_CANCELTRYCONTINUE | 0x00000006 | Message window contains three buttons: Cancel, Try Again, Continue |

To display an icon in the message window it is necessary to specify additional flags:

| Constant | Value | Description |
| --- | --- | --- |
| MB\_ICONSTOP,  MB\_ICONERROR,  MB\_ICONHAND | 0x00000010 | The STOP sign icon |
| MB\_ICONQUESTION | 0x00000020 | The question sign icon |
| MB\_ICONEXCLAMATION,  MB\_ICONWARNING | 0x00000030 | The exclamation/warning sign icon |
| MB\_ICONINFORMATION,  MB\_ICONASTERISK | 0x00000040 | The encircled i sign |

Default buttons are defined by the following flags:

| Constant | Value | Description |
| --- | --- | --- |
| MB\_DEFBUTTON1 | 0x00000000 | The first button MB\_DEFBUTTON1 - is default, if the other buttons MB\_DEFBUTTON2, MB\_DEFBUTTON3, or MB\_DEFBUTTON4 are not specified |
| MB\_DEFBUTTON2 | 0x00000100 | The second button is default |
| MB\_DEFBUTTON3 | 0x00000200 | The third button is default |
| MB\_DEFBUTTON4 | 0x00000300 | The fourth button is default |
