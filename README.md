# Monster Hunter Inventory Displayer
Scripts that read Monster Hunter save files and display a unified inventory of all the player's possessions. <br/>
Currently supports Monster Hunter World Iceborne and Monster Hunter Stories 2. <br/>
Implementation of Monster Hunter Rise planned.

## Requirements
- Installed version of 010 Editor, correctly specified in the path.

## Dependencies
- A compiled version of [IceborneSavecrypt](https://github.com/LEGENDFF/mhw-Savecrypt).
- A release of [MHST2 Save Tools](https://github.com/AsteriskAmpersand/MHST2-Save-Tools).
- The following binary templates: [SAVEDATA1000.bt](https://github.com/EnderHDMC/MHWISaveEditor/blob/master/res/mapping/SAVEDATA1000.bt), [types.bt](https://github.com/EnderHDMC/MHWISaveEditor/blob/master/res/mapping/types.bt) and [MHStories2_SaveTemplate.bt](https://github.com/sigve10/MHStories2-SaveTemplate/blob/main/MHStories2_SaveTemplate.bt).

## Usage
### Usage for Monster Hunter World
- Find your save file, usually located at `Steam/userdata/<user_id>/582010/remote/SAVEDATA1000` and copy it in the root folder of this repository.
- Run the `world_execution.py` file.

### Usage for Monster Hunter Stories 2
- Find your save file, usually located at `Steam/userdata/<user_id>/1277400/remote/mhr_slot_X` and copy it in the root folder of this repository.
- Run `libraries/AAStories2SaveTool.exe`.
- Set your save as the input, set your save as the output as well, except for the file extension, change it from .sav to .bin.
- Input your Steam ID in the corresponding field. To easily find it, go to your Steam profile and copy the series of numbers in the URL.
- Press the decrypt button, wait for a message to appear below and close the app.
- Run the `stories_2_execution.py` file.

### Usage to concatenate all games
- Run the `overall_merge.py` file.

## Credits
- [EnderHDMC](https://github.com/EnderHDMC) for his personal help and for providing the binary templates of World. <br/>
- [Legendff](https://github.com/LEGENDFF) for providing the World decryption library.
- [DSC-173](https://github.com/sigve10) for providing the Stories 2 binary template.
- [AsteriskAmpersand](https://github.com/AsteriskAmpersand) for providing the Stories 2 save decryption tool.
