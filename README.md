# Monster Hunter Inventory Displayer
Scripts that read Monster Hunter save files and display a unified inventory of all the player's possessions. <br/>
Currently supports Monster Hunter World Iceborne only. <br/>
Implementation of Monster Hunter Rise planned.

### Requirements
- Installed version of 010 Editor, correctly specified in the path
- Maven

### Usage
- Go to [that repository](https://github.com/LEGENDFF/mhw-Savecrypt), compile the library and leave the .jar file in the res/lib folder of this repository.
- Download the two following files and save them in the res/mapping folder : [SAVEDATA1000.bt](https://github.com/EnderHDMC/MHWISaveEditor/blob/master/res/mapping/SAVEDATA1000.bt) and [types.bt](https://github.com/EnderHDMC/MHWISaveEditor/blob/master/res/mapping/types.bt).
- Run the scripts in the following order : decryption, inventory and merge.
- Contemplate !

### Credits
- [EnderHDMC](https://github.com/EnderHDMC) for his personal help and for providing the binary tables. <br/>
- [Legendff](https://github.com/LEGENDFF) for providing the decryption library.
