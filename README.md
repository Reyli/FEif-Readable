# FEif-Readable
A simply python script to convert Fire Emblem If text files into a readable format

This requires Python 3.X to work.

----------------------
How to run
----------------------
Run:  python FEifReadableScript.py

Sample Input: 
MID_A013_OP1_PCM1: $t1$Wmアクア|3$w0|$Wsアクア|$Wa$SvpVOICE_AQUA_WIN_06|着いたわ…\nここが、シュヴァリエ公国よ。$k\n$Wmサクラ|7$w0|$Wsサクラ|$Wa$E怒,|$SvpVOICE_SAKURA_EVT_01|リョウマ兄様…\n早くお会いしたいです。$k\n

Sample Output:
MID_A013_OP1_PCM1:
アクア:
着いたわ…
ここが、シュヴァリエ公国よ。▼

サクラ:
リョウマ兄様…
早くお会いしたいです。▼

You will enter the input.txt file to process.
The script should be in the same directory as the input file.
The folders included are just for organization.
If you run into any problems, try running the script from the same directory instead of the full path.

Example outputs are included in the "Expected Sample Outputs".
That folder includes human done processing to compare to the outputs by the program.

Files in the "Original Files" folder were taken from dumps from the game.


Changelog:
0.2: Fixed the bug that left digits before a character name due to a stray command.

0.1: Initial Build
