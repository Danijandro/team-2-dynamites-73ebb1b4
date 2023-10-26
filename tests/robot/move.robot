*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position. https://github.com/level-up-program/team-2-dynamites-73ebb1b4/blob/main/tests/robot/images/ASD-900-PIC.JPG
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Daniel                              0             0             10                    SOUTH         0           0           11
Sam                                 0             0             21                    WEST          0           0           22
Anitha                              5             5             101                   WEST          4           5           102
Dom                                 9             9             0                     SOUTH         9           8           1
Ramya                               9             0             5                     NORTH         9           1           6
Isha                                5             5             12                    WEST          4           5           13
Anita                               7             6             13                    EAST          8           6           14
XYZ                                 0             0             5                     NORTH         0           1           6
ABC                                 0             0             7                     EAST          1           0           8
EFG                                 0             9             10                    WEST          0           9           11
X1                                  0             9             8                     EAST          1           9           7
X2                                  0             9             6                     NORTH         0           9           6
X3                                  0             9             5                     SOUTH         0           8           6
X4                                  9             9             30                    NORTH         9           9           31
X5                                  9             9             40                    EAST          9           9           41
X6                                  9             9             50                    WEST          8           9           51
X7                                  9             0             105                   SOUTH         9           0           106

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}