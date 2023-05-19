# https://ggc-itec2120.github.io/EarSketchBook/#_pythontutor_asg_6_3

# Lists and For Loops
# The list below contains 8 sound clips of kalimba piano.
#
# clips = [RD_WORLD_PERCUSSION_KALIMBA_PIANO_1, RD_WORLD_PERCUSSION_KALIMBA_PIANO_2, RD_WORLD_PERCUSSION_KALIMBA_PIANO_3, RD_WORLD_PERCUSSION_KALIMBA_PIANO_4, RD_WORLD_PERCUSSION_KALIMBA_PIANO_5, RD_WORLD_PERCUSSION_KALIMBA_PIANO_6, RD_WORLD_PERCUSSION_KALIMBA_PIANO_7, RD_WORLD_PERCUSSION_KALIMBA_PIANO_8]
# Write a script in EarSketch with a tempo of 115. The script should use a for loop to add each clip to the DAW. Match the screenshot below. Notice:
#
# Each clip has its own track
#
# Each clip starts one measure later.
#
# Each clip lasts for 5 measures.

## MODIFIED ASSIGNMENT
## REFACTOR THE FOLLOWING EARSKETCH TO USE A LIST AND FOR LOOP
from earsketch import *

init()
setTempo(115)

fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_1, 1, 1, 6)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_2, 2, 2, 7)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_3, 3, 3, 8)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_4, 4, 4, 9)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_5, 5, 5, 10)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_6, 6, 6, 11)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_7, 7, 7, 12)
fitMedia(RD_WORLD_PERCUSSION_KALIMBA_PIANO_8, 8, 8, 13)

finish()
