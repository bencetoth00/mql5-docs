# CListView

CListView

CListView is a class of the ListView complex control (with dependent controls).

Description

CListView class encapsulates list-control functionality.

Declaration

|  |
| --- |
| class CListView : public CWndClient |

Title

|  |
| --- |
| #include <Controls\ListView.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            [CWndContainer](../CWndContainer/CWndContainer.md)                [CWndClient](../CWndClient/CWndClient.md)                    CListView |

Result of the [code](CListView.md#sample) provided below:

![ControlsListView](../../../assets/controlslistview.png)

Class Methods by Groups

| Create |  |
| --- | --- |
| [Create](Create/Create.md) | Creates control |
| Chart event handlers |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| Settings |  |
| [TotalView](TotalView/TotalView.md) | Sets the number of items shown on the control |
| Add/Delete |  |
| [AddItem](AddItem/AddItem.md) | Adds an item to control list |
| Data |  |
| [Select](Select/Select.md) | Selects current list element by index |
| [SelectByText](SelectByText/SelectByText.md) | Selects current list element by text |
| [SelectByValue](SelectByValue/SelectByValue.md) | Selects current list element by value |
| Read-only data |  |
| [Value](Value/Value.md) | Gets the value of the current list element |
| Dependent controls |  |
| [CreateRow](CreateRow/CreateRow.md) | Creates a row of the ListView |
| Internal event handlers |  |
| [OnResize](OnResize/OnResize.md) | "Resize" internal event handler (virtual) |
| Dependent controls event handlers |  |
| [OnVScrollShow](OnVScrollShow/OnVScrollShow.md) | "Show" internal event handler (virtual) of VScroll dependent control |
| [OnVScrollHide](OnVScrollHide/OnVScrollHide.md) | "Hide" internal event handler (virtual) of VScroll dependent control |
| [OnScrollLineDown](OnScrollLineDown/OnScrollLineDown.md) | "ScrollLineDown" internal event handler (virtual) of VScroll dependent control |
| [OnScrollLineUp](OnScrollLineUp/OnScrollLineUp.md) | "ScrollLineUp" internal event handler (virtual) of VScroll dependent control |
| [OnItemClick](OnItemClick/OnItemClick.md) | "ItemClick" internal event handler (virtual) |
| Redraw |  |
| [Redraw](Redraw/Redraw.md) | Redraws the control |
| [RowState](RowState/RowState.md) | Sets the state of the specified row |
| [CheckView](CheckView/CheckView.md) | Checks the "visibility" of the specified row |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |
| Methods inherited from class CWndContainer  [OnMouseEvent](../CWndContainer/OnMouseEvent/OnMouseEvent.md), [ControlsTotal](../CWndContainer/ControlsTotal/ControlsTotal.md), [Control](../CWndContainer/Control/Control.md), [ControlFind](../CWndContainer/ControlFind/ControlFind.md), [MouseFocusKill](../CWndContainer/MouseFocusKill/MouseFocusKill.md), [Add](../CWndContainer/Add/Add.md), [Add](../CWndContainer/Add/Add.md), [Delete](../CWndContainer/Delete/Delete.md), [Delete](../CWndContainer/Delete/Delete.md), [Move](../CWndContainer/Move/Move.md), [Move](../CWndContainer/Move/Move.md), [Shift](../CWndContainer/Shift/Shift.md), [Enable](../CWndContainer/Enable/Enable.md), [Disable](../CWndContainer/Disable/Disable.md), [Hide](../CWndContainer/Hide/Hide.md), [Save](../CWndContainer/Save/Save.md), [Load](../CWndContainer/Load/Load.md) |
| Methods inherited from class CWndClient  [ColorBackground](../CWndClient/ColorBackground/ColorBackground.md), [ColorBorder](../CWndClient/ColorBorder/ColorBorder.md), [BorderType](../CWndClient/BorderType/BorderType.md), [VScrolled](../CWndClient/VScrolled/VScrolled.md), [VScrolled](../CWndClient/VScrolled/VScrolled.md), [HScrolled](../CWndClient/HScrolled/HScrolled.md), [HScrolled](../CWndClient/HScrolled/HScrolled.md), Id |

Example of creating a panel with list view control:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                             ControlsListView.mq5 |  //|                         Copyright 2000-2024, MetaQuotes Ltd. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2017, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property description "Control Panels and Dialogs. Demonstration class CListView"  #include <Controls\Dialog.mqh>  #include <Controls\ListView.mqh>  //+------------------------------------------------------------------+  //| defines                                                          |  //+------------------------------------------------------------------+  //--- indents and gaps  #define INDENT\_LEFT                         (11)      // indent from left (with allowance for border width)  #define INDENT\_TOP                          (11)      // indent from top (with allowance for border width)  #define INDENT\_RIGHT                        (11)      // indent from right (with allowance for border width)  #define INDENT\_BOTTOM                       (11)      // indent from bottom (with allowance for border width)  #define CONTROLS\_GAP\_X                      (5)       // gap by X coordinate  #define CONTROLS\_GAP\_Y                      (5)       // gap by Y coordinate  //--- for buttons  #define BUTTON\_WIDTH                        (100)     // size by X coordinate  #define BUTTON\_HEIGHT                       (20)      // size by Y coordinate  //--- for the indication area  #define EDIT\_HEIGHT                         (20)      // size by Y coordinate  //--- for group controls  #define GROUP\_WIDTH                         (150)     // size by X coordinate  #define LIST\_HEIGHT                         (179)     // size by Y coordinate  #define RADIO\_HEIGHT                        (56)      // size by Y coordinate  #define CHECK\_HEIGHT                        (93)      // size by Y coordinate  //+------------------------------------------------------------------+  //| Class CControlsDialog                                            |  //| Usage: main dialog of the Controls application                   |  //+------------------------------------------------------------------+  class CControlsDialog : public CAppDialog    {  private:     CListView         m\_list\_view;                     // CListView object     public:                       CControlsDialog(void);                      ~CControlsDialog(void);     //--- create     virtual bool      Create(const long chart,const string name,const int subwin,const int x1,const int y1,const int x2,const int y2);     //--- chart event handler     virtual bool      OnEvent(const int id,const long &lparam,const double &dparam,const string &sparam);     protected:     //--- create dependent controls     bool              CreateListView(void);     //--- handlers of the dependent controls events     void              OnChangeListView(void);    };  //+------------------------------------------------------------------+  //| Event Handling                                                   |  //+------------------------------------------------------------------+  EVENT\_MAP\_BEGIN(CControlsDialog)  ON\_EVENT(ON\_CHANGE,m\_list\_view,OnChangeListView)  EVENT\_MAP\_END(CAppDialog)  //+------------------------------------------------------------------+  //| Constructor                                                      |  //+------------------------------------------------------------------+  CControlsDialog::CControlsDialog(void)    {    }  //+------------------------------------------------------------------+  //| Destructor                                                       |  //+------------------------------------------------------------------+  CControlsDialog::~CControlsDialog(void)    {    }  //+------------------------------------------------------------------+  //| Create                                                           |  //+------------------------------------------------------------------+  bool CControlsDialog::Create(const long chart,const string name,const int subwin,const int x1,const int y1,const int x2,const int y2)    {     if(!CAppDialog::Create(chart,name,subwin,x1,y1,x2,y2))        return(false);  //--- create dependent controls     if(!CreateListView())        return(false);  //--- succeed     return(true);    }  //+------------------------------------------------------------------+  //| Create the "ListView" element                                    |  //+------------------------------------------------------------------+  bool CControlsDialog::CreateListView(void)    {  //--- coordinates     int x1=INDENT\_LEFT+GROUP\_WIDTH+2\*CONTROLS\_GAP\_X;     int y1=INDENT\_TOP+(EDIT\_HEIGHT+CONTROLS\_GAP\_Y)+            (BUTTON\_HEIGHT+CONTROLS\_GAP\_Y)+            (EDIT\_HEIGHT+2\*CONTROLS\_GAP\_Y);     int x2=x1+GROUP\_WIDTH;     int y2=y1+LIST\_HEIGHT-CONTROLS\_GAP\_Y;  //--- create     if(!m\_list\_view.Create(m\_chart\_id,m\_name+"ListView",m\_subwin,x1,y1,x2,y2))        return(false);     if(!Add(m\_list\_view))        return(false);  //--- fill out with strings     for(int i=0;i<16;i++)        if(!m\_list\_view.AddItem("Item "+IntegerToString(i)))           return(false);  //--- succeed     return(true);    }  //+------------------------------------------------------------------+  //| Event handler                                                    |  //+------------------------------------------------------------------+  void CControlsDialog::OnChangeListView(void)    {     Comment(\_\_FUNCTION\_\_+" \""+m\_list\_view.Select()+"\"");    }  //+------------------------------------------------------------------+  //| Global Variables                                                 |  //+------------------------------------------------------------------+  CControlsDialog ExtDialog;  //+------------------------------------------------------------------+  //| Expert initialization function                                   |  //+------------------------------------------------------------------+  int OnInit()    {  //--- create application dialog     if(!ExtDialog.Create(0,"Controls",0,40,40,380,344))        return(INIT\_FAILED);  //--- run application     ExtDialog.Run();  //--- succeed     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Expert deinitialization function                                 |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {  //--- clear comments     Comment("");  //--- destroy dialog     ExtDialog.Destroy(reason);    }  //+------------------------------------------------------------------+  //| Expert chart event function                                      |  //+------------------------------------------------------------------+  void OnChartEvent(const int id,         // event ID                      const long& lparam,   // event parameter of the long type                    const double& dparam, // event parameter of the double type                    const string& sparam) // event parameter of the string type    {     ExtDialog.ChartEvent(id,lparam,dparam,sparam);    } |
