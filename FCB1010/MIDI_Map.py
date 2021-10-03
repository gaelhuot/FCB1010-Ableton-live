# http://remotescripts.blogspot.com
# Original repository : https://github.com/petr-ruca/FCB1010-Remote-midi-script-for-Ableton-Live-10
# Note and CC Mappings for the FCB1010 Ableton 11+ script (APC emulation) are defined in this file
# Values may be edited with any text editor (but avoid using tabs for indentation)

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = -1  # offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0  # offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 0  # Channel assignment for all mapped buttons/pads; valid range is 0 to 15
MESSAGETYPE = 0  # Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs.
# When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values.

# General
PLAY = 93  # Global play
STOP = 92  # Global stop
REC = 94  # Global record
TAPTEMPO = -1  # Tap tempo
NUDGEUP = -1  # Tempo Nudge Up
NUDGEDOWN = -1  # Tempo Nudge Down
UNDO = 97  # Undo
REDO = 98  # Redo
LOOP = -1  # Loop on/off
PUNCHIN = -1  # Punch in
PUNCHOUT = -1  # Punch out
OVERDUB = 99  # Overdub on/off
METRONOME = -1  # Metronome on/off
RECQUANT = -1  # Record quantization on/off
DETAILVIEW = -1  # Detail view switch
CLIPTRACKVIEW = -1  # Clip/Track view switch
SELTRACKARM = 4  # Arm selected track for recording

# Device Control
DEVICELOCK = -1  # Device Lock (lock "blue hand")
DEVICEONOFF = -1  # Device on/off
DEVICENAVLEFT = -1  # Device nav left
DEVICENAVRIGHT = -1  # Device nav right
DEVICEBANKNAVLEFT = -1  # Device bank nav left
DEVICEBANKNAVRIGHT = -1  # Device bank nav right
DEVICEBANK = (-1,  # Bank 1 #All 8 banks must be assigned to positive values in order for bank selection to work
              -1,  # Bank 2
              -1,  # Bank 3
              -1,  # Bank 4
              -1,  # Bank 5
              -1,  # Bank 6
              -1,  # Bank 7
              -1,  # Bank 8
              )

# Arrangement View Controls
SEEKFWD = -1  # Seek forward
SEEKRWD = -1  # Seek rewind

# Session Navigation (aka "red box")
SESSIONLEFT = 90  # Session left
SESSIONRIGHT = 91  # Session right
SESSIONUP = 95  # Session up
SESSIONDOWN = 96  # Session down
ZOOMUP = -1  # Session Zoom up
ZOOMDOWN = -1  # Session Zoom down
ZOOMLEFT = -1  # Session Zoom left
ZOOMRIGHT = -1  # Session Zoom right

# Track Navigation
TRACKLEFT = 0  # Track left
TRACKRIGHT = 1  # Track right

# Scene Navigation
SCENEUP = 5  # Scene down
SCENEDN = 6  # Scene up

# Scene Launch
SELSCENELAUNCH = -1  # Selected scene launch
SCENELAUNCH = (-1,  # Scene 1 Launch
               -1,  # Scene 2
               -1,  # Scene 3
               -1,  # Scene 4
               -1,  # Scene 5
               )

# Clip Launch / Stop
SELCLIPLAUNCH = 3  # Selected clip launch
SELCLIPSTOP = 2  # Selected clip stop
SELTRACKSOLO = 7  # Solo selected track
SELTRACKMUTE = 8  # Mute selected track
SELTRACKSTOP = 9  # Stop selected track

STOPALLCLIPS = -1  # Stop all clips

# 8x5 Matrix note assignments
# Track no.:     1   2   3   4   5   6   7   8
CLIPNOTEMAP = ((10, 20, 30, 40, 50, 60, 70, 80),  # Row 1
               (11, 21, 31, 41, 51, 61, 71, 81),  # Row 2
               (12, 22, 32, 42, 52, 62, 72, 82),  # Row 3
               (13, 23, 33, 43, 53, 63, 73, 83),  # Row 4
               (14, 24, 34, 44, 54, 64, 74, 84),  # Row 5
               )

# TODO
# CLIPSTOPMAP = ((15, 25, 35, 45, 55, 65, 75, 85),  # Row 1
#                (16, 26, 36, 46, 56, 66, 76, 86),  # Row 2
#                (17, 27, 37, 47, 57, 67, 77, 87),  # Row 3
#                (18, 28, 38, 48, 58, 68, 78, 88),  # Row 4
#                (19, 29, 39, 49, 59, 69, 79, 89),  # Row 5
#                )

# Track Control
MASTERSEL = -1  # Master track select
TRACKSTOP = (-1,  # Track 1 Clip Stop
             -1,  # Track 2
             -1,  # Track 3
             -1,  # Track 4
             -1,  # Track 5
             -1,  # Track 6
             -1,  # Track 7
             -1,  # Track 8
             )
TRACKSEL = (-1,  # Track 1 Select
            -1,  # Track 2
            -1,  # Track 3
            -1,  # Track 4
            -1,  # Track 5
            -1,  # Track 6
            -1,  # Track 7
            -1,  # Track 8
            )
TRACKMUTE = (-1,  # Track 1 On/Off
             -1,  # Track 2
             -1,  # Track 3
             -1,  # Track 4
             -1,  # Track 5
             -1,  # Track 6
             -1,  # Track 7
             -1,  # Track 8
             )
TRACKSOLO = (-1,  # Track 1 Solo
             -1,  # Track 2
             -1,  # Track 3
             -1,  # Track 4
             -1,  # Track 5
             -1,  # Track 6
             -1,  # Track 7
             -1,  # Track 8
             )
TRACKREC = (-1,  # Track 1 Record
            -1,  # Track 2
            -1,  # Track 3
            -1,  # Track 4
            -1,  # Track 5
            -1,  # Track 6
            -1,  # Track 7
            -1,  # Track 8
            )


# Pad Translations for Drum Rack

PADCHANNEL = 0  # MIDI channel for Drum Rack notes
DRUM_PADS = (-1, -1, -1, -1,  # MIDI note numbers for 4 x 4 Drum Rack
             -1, -1, -1, -1,  # Mapping will be disabled if any notes are set to -1
             -1, -1, -1, -1,  # Notes will be "swallowed" if already mapped elsewhere
             -1, -1, -1, -1,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored

SLIDERCHANNEL = 0  # Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 180.0  # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 100.0  # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1  # Tempo control CC assignment; control range is set above
MASTERVOLUME = -1  # Master track volume
CUELEVEL = -1  # Cue level control
CROSSFADER = -1  # Crossfader control

TRACKVOL = (2,  # Track 1 Volume
            4,  # Track 2
            6,  # Track 3
            8,  # Track 4
            10,  # Track 5
            12,  # Track 6
            14,  # Track 7
            16,  # Track 8
            )
TRACKPAN = (-1,  # Track 1 Pan
            -1,  # Track 2
            -1,  # Track 3
            -1,  # Track 4
            -1,  # Track 5
            -1,  # Track 6
            -1,  # Track 7
            -1,  # Track 8
            )
TRACKSENDA = (-1,  # Track 1 Send A
              -1,  # Track 2
              -1,  # Track 3
              -1,  # Track 4
              -1,  # Track 5
              -1,  # Track 6
              -1,  # Track 7
              -1,  # Track 8
              )
TRACKSENDB = (-1,  # Track 1 Send B
              -1,  # Track 2
              -1,  # Track 3
              -1,  # Track 4
              -1,  # Track 5
              -1,  # Track 6
              -1,  # Track 7
              -1,  # Track 8
              )
TRACKSENDC = (-1,  # Track 1 Send C
              -1,  # Track 2
              -1,  # Track 3
              -1,  # Track 4
              -1,  # Track 5
              -1,  # Track 6
              -1,  # Track 7
              -1,  # Track 8
              )
PARAMCONTROL = (3,  # Param 1 #All 8 params must be assigned to positive values in order for param control to work
                5,  # Param 2
                7,  # Param 3
                9,  # Param 4
                11,  # Param 5
                13,  # Param 6
                15,  # Param 7
                17,  # Param 8
                )
