# all trailing whitespace is intentional

TEMPLATE_SPACES = 38
ASSET_WIDTH = 11
ASSET_HEIGHT = 12

TEMPLATE = r'''
    +--------------------------------------+
    | your choice              AI's choice |
    | {24}{25}{26} |
    |                                      |
    | {0}              {12} |
    | {1}              {13} |
    | {2}              {14} |
    | {3}              {15} |
    | {4}     {27}     {16} |
    | {5}    {28} vs {29}    {17} |
    | {6}   {30}   {18} |
    | {7}              {19} |
    | {8}              {20} |
    | {9}              {21} |
    | {10}              {22} |
    | {11}              {23} |
    |                                      |
    +--------------------------------------+
'''

EMPTY = '{}\n'.format(' ' * ASSET_WIDTH) * ASSET_HEIGHT

ROCK = r'''           
           
           
           
   _.-._   
  | | | |-.
 / )|_|_|_|
| |-^-^-^-'
|     ||  |
\     '   /
 |       | 
 |       | '''

PAPER = r'''    .-.    
  .-| |-.  
  | | | |  
  | | | |-.
  | | | | |
  |_|_|_| |
 / )    `-|
| | `--   |
|     ||  |
\     '   /
 |       | 
 |       | '''

SCISSORS = r'''    .-.    
  .-| |    
  | | |    
  | | |    
  | | |_   
  |_|_| |-.
 / )  |_|_|
| |   `-^-'
|     ||  |
\     '   /
 |       | 
 |       | '''
