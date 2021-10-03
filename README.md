# FCB1010 Ableton 10 / Ableton 11

## Introduction

Edited version of the petr-ruca repository: https://github.com/petr-ruca/FCB1010-Remote-midi-script-for-Ableton-Live-10

- Works on Ableton live 11 (Tested on 11.0)
- Works on Ableton live 10 (Tested on 10.1)  

I've added some code from the original script and made it able to compile on Live 11 as well (some errors when launching Live 11). 

## Installation

### Setup for FCB1010
It is necessary to add the preset present in the "Preset" folder on the FCB1010 for the script to work.

#### FCB1010 Manager
For this, you will need the following software: https://mountainutilities.eu/fcb1010
Download here : [Download link for Windows](https://mountainutilities.eu/system/files/download/fcbman-2.2.1-install.exe)

#### FCB1010 Preset installation mode
First, open the **Preset.syx** file with FCB1010 Manager. 

A little procedure is necessary on your FCB1010 to install the preset (also explained in FCB1010 Manager): 
1. Press and hold the "Down" pedal and turn on the FCB1010
2. Press the "Down" pedal once to enter the "Config" mode
3. Press pedal 7 "SYSEX RCV".

Demonstration: 
[GIF]

You can now send the preset to the FCB1010:
[PHOTO]  

### Setup for Ableton

#### Remote scripts
Copy/paste the "FCB1010" folder and place it in the "Resources\MIDI Remote Scripts" directory of Ableton.

- **Live 10** : "C:\ProgramData\Ableton\Live 10 Suite\Resources\MIDI Remote Scripts"
- **Live 11** : "C:\ProgramData\Ableton\Live 11 Suite\Resources\MIDI Remote Scripts\FCB1010"

Complete path : 
**"C:\ProgramData\Ableton\Live [Version] Suite\Resources\MIDI Remote Scripts\FCB1010"**

#### Configuration
Plug in your FCB1010 and open Ableton.
**Important information** : I personally don't plug the "MIDI IN" on the FCB1010, I already had a lot of problems with other scripts, so I just use the "MIDI OUT":
[PHOTO]

Allez dans "Options->Preferences->Link Tempo MIDI".
Dans la liste "Control surface", vous devriez maintenant voir "FCB1010" 
Choisissez le. Si le rectangle bleu apparait, félicitations, c'est installé ! 

## Actual mapping
[PHOTOS]

## Custom mapping
To edit the current mapping, go to the python file ***"MIDI_Map.py"*** of the Remote Script. 

Each command corresponds to a Variable. 
Example : 
	
    
    SESSIONRIGHT =  91 # Correspond à la note Midi "91".
    
At the bottom of the script is the mapping for the expression pedals (CF *TRACKVOL* and *PARAMCONTROL*).

Le preset installé sur le FCB1010 bind chaque pédale sur une note midi :
Example : 
- Bank 0, Footswitch 1 = 0
- Bank 0, Footswitch 5 = 0
- ....
- Bank 5, Footswitch 7 = 56
- Bank [x], Footswitch [y] = (X * 10) + (Y-1) 
- You get the idea
  
## TODO

### Visual editor
I would like to create a simple visual editor (at first) that would allow everyone to create their own custom mapping. 
The idea is that this editor generates a JSON file (for example) which is then read by the remote script. 

This would prevent people who are not very familiar with the code from having to spend hours wondering : "What is this devilry? Why is he talking about pythons and snakes for something on Ableton?" 

### Smart mapping
Overall, simplify the use and navigation as much as possible

## Ressources

- Remote script : [https://github.com/laidlaw42/ableton-live-midi-remote-scripts](https://github.com/laidlaw42/ableton-live-midi-remote-scripts)
- Original FCB1020 repository : [https://github.com/petr-ruca/FCB1010-Remote-midi-script-for-Ableton-Live-10](https://github.com/petr-ruca/FCB1010-Remote-midi-script-for-Ableton-Live-10)
- Documentation pour Ableton 10 : [https://structure-void.com/PythonLiveAPI_documentation/Live10.1.19.xml](https://structure-void.com/PythonLiveAPI_documentation/Live10.1.19.xml)
- How to make a strong Coffee (Believe me, it's useful when you have to read the Python "Doc" of Ableton) : [How to Make Strong Coffee](https://enjoyjava.com/how-to-make-strong-coffee/)