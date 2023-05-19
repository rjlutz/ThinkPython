# SOLUTION

from earsketch import *

init()
setTempo(115)

clips = [RD_WORLD_PERCUSSION_KALIMBA_PIANO_1,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_2,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_3,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_4,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_5,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_6,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_7,
         RD_WORLD_PERCUSSION_KALIMBA_PIANO_8]

for index, clip in enumerate(clips):
    fitMedia(clip, index + 1, index + 1, index + 6)

finish()