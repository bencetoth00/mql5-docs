# Global Variables of the Terminal

# Global Variables of the Client Terminal

There is a group set of functions for working with global variables.

Global variables of the client terminal should not be mixed up with variables declared in the [global scope](../Language-Basics/Variables/Global-Variables/Global-Variables.md) of the mql5 program.

Global variables are kept in the client terminal for 4 weeks since the last access, then they will be deleted automatically. An access to a global variable is not only setting of a new value, but reading of the global variable value, as well.

Global variables of the client terminal are accessible simultaneously from all mql5 programs launched in the client terminal.

| Function | Action |
| --- | --- |
| [GlobalVariableCheck](GlobalVariableCheck/GlobalVariableCheck.md) | Checks the existence of a global variable with the specified name |
| [GlobalVariableTime](GlobalVariableTime/GlobalVariableTime.md) | Returns time of the last accessing the global variable |
| [GlobalVariableDel](GlobalVariableDel/GlobalVariableDel.md) | Deletes a global variable |
| [GlobalVariableGet](GlobalVariableGet/GlobalVariableGet.md) | Returns the value of a global variable |
| [GlobalVariableName](GlobalVariableName/GlobalVariableName.md) | Returns the name of a global variable by its ordinal number in the list of global variables |
| [GlobalVariableSet](GlobalVariableSet/GlobalVariableSet.md) | Sets the new value to a global variable |
| [GlobalVariablesFlush](GlobalVariablesFlush/GlobalVariablesFlush.md) | Forcibly saves contents of all global variables to a disk |
| [GlobalVariableTemp](GlobalVariableTemp/GlobalVariableTemp.md) | Sets the new value to a global variable, that exists only in the current session of the terminal |
| [GlobalVariableSetOnCondition](GlobalVariableSetOnCondition/GlobalVariableSetOnCondition.md) | Sets the new value of the existing global variable by condition |
| [GlobalVariablesDeleteAll](GlobalVariablesDeleteAll/GlobalVariablesDeleteAll.md) | Deletes global variables with the specified prefix in their names |
| [GlobalVariablesTotal](GlobalVariablesTotal/GlobalVariablesTotal.md) | Returns the total number of global variables |
