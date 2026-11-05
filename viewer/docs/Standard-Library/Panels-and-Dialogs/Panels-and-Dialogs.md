# Panels and Dialogs

# Classes for Creating Control Panels and Dialogs

This section contains technical details of working with classes for creation of controls panels and dialogs, as well as description of the relevant components of the MQL5 standard library.

The use of these classes will save time when developing custom interactive MQL5 applications, including Expert Advisors and indicators.

MQL5 Standard Library (in terms of classes for creation of control panels and dialogs) is placed in the terminal data folder, in the MQL5\Include\Controls.

Find the examples of working with classes in the following articles:

- [How to create a graphical panel of any complexity level](https://www.mql5.com/en/articles/4503)
- [Improving Panels: Adding transparency, changing background color and inheriting from CAppDialog/CWndClient](https://www.mql5.com/en/articles/4575)
- [Adding a control panel to an indicator or an Expert Advisor in no time](https://www.mql5.com/en/articles/2171)
- [Create your own graphical panels in MQL5](https://www.mql5.com/en/articles/345)
- [Creating active control panels in MQL5 for trading](https://www.mql5.com/en/articles/62)

The sample Expert Advisor, which illustrates the operation of these classes, can be found in MQL5\Expert\Examples\Controls.

| Auxiliary structures | Description |
| --- | --- |
| [CRect](CRect/CRect.md) | Structure of the rectangular area |
| [CDateTime](CDateTime/CDateTime.md) | Structure for working with date and time |

| Base classes | Description |
| --- | --- |
| [CWnd](CWnd/CWnd.md) | Base class for all controls |
| [CWndObj](CWndObj/CWndObj.md) | Base class for controls and dialogs |
| [CWndContainer](CWndContainer/CWndContainer.md) | Base class for complex controls |

| Simple controls | Description |
| --- | --- |
| [CLabel](CLabel/CLabel.md) | Control, based on "Text label" graphic object |
| [CBmpButton](CBmpButton/CBmpButton.md) | Control, based on "Bitmap label" graphic object |
| [CButton](CButton/CButton.md) | Control, based on "Button" graphic object |
| [CEdit](CEdit/CEdit.md) | Control, based on "Edit field" graphic object |
| [CPanel](CPanel/CPanel.md) | Control, based on "Rectangle label" |
| [CPicture](CPicture/CPicture.md) | Control, based on "Bitmap label" |

| Complex controls | Description |
| --- | --- |
| [CScroll](CScroll/CScroll.md) | Base class of the scroll bar |
| [CScrollV](CScrollV/CScrollV.md) | Vertical scroll bar |
| [CScrollH](CScrollH/CScrollH.md) | Horizontal scroll bar |
| [CWndClient](CWndClient/CWndClient.md) | Base class of the client area with scroll bars |
| [CListView](CListView/CListView.md) | List view |
| [CComboBox](CComboBox/CComboBox.md) | Combo box |
| [CCheckBox](CCheckBox/CCheckBox.md) | Check box |
| [CCheckGroup](CCheckGroup/CCheckGroup.md) | Check group |
| [CRadioButton](CRadioButton/CRadioButton.md) | Radio button |
| [CRadioGroup](CRadioGroup/CRadioGroup.md) | Radio group |
| [CSpinEdit](CSpinEdit/CSpinEdit.md) | Increment/decrement field |
| [CDialog](CDialog/CDialog.md) | Dialog |
| [CAppDialog](CAppDialog/CAppDialog.md) | Main dialog of MQL5 application |
