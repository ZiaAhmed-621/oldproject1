Dev Notes: 

Type: Issues/Problems

Dodge input as an inherent issue of fetching keypress
even if the key is pressed much sooner than intended. This allows player
to pre-press the key and always succeed in dodging. Precisely timed keypress
MIGHT be acheivable using msvcrt module but the module seems to hold no regards
for time or effort and refuses to work.

On a side thought, the issue might be because of sleep module, not readchar or the input()
method. That being said, the sleep module is fundamnetally what drives the program, hence it
remains a problem nevertheless.

Type: Compatibility

Python 3.x interpreter with 'pip' to install modules.
Not tested on Linux or MacOS. Likely incompatible with either.

Type: Project Purpose

This project essentially pushes the terminal output to it's limits. It will never be used to
generate real time images hence the program is destined to die here, althought not without
fulfilling its purpose. The input and the interface of the command line have been thoroughly
utilized and tested to their boundaries. It is more of a learning experience than it is a 
well thought-out project.

Made by: Zia Ahmed Khan
No additional resources used (except Google for troubleshooting)
