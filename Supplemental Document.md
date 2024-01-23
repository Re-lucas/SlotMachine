# Uploded on Github
-**Address**: https://github.com/Re-lucas/SlotMachine

# Slot Machine Game - Supplemental Document

## Variable Details

### `self.credits`
- **Purpose**: Stores the user's available credits.
- **Line of Creation**: Line 13
- **Data Type**: Integer
- **Reasoning**: Credits are represented as whole numbers, and integers are suitable for this purpose. No fractional or complex values are involved.

### `self.bet_amount`
- **Purpose**: Represents the current bet amount chosen by the user.
- **Line of Creation**: Line 14
- **Data Type**: Integer
- **Reasoning**: Similar to `self.credits`, bet amounts are whole numbers, and integers are suitable for representing discrete values.

### `self.jackpot`
- **Purpose**: Keeps track of the jackpot amount.
- **Line of Creation**: Line 15
- **Data Type**: Integer
- **Reasoning**: The jackpot is a cumulative whole number, making an integer the appropriate choice.

### `self.holds`
- **Purpose**: A list indicating whether each reel is being held.
- **Line of Creation**: Line 16
- **Data Type**: List of Booleans
- **Reasoning**: Booleans are suitable to represent the on/off state of holding a reel.

### `self.hold_count`
- **Purpose**: Counts the number of held reels.
- **Line of Creation**: Line 17
- **Data Type**: Integer
- **Reasoning**: The count is a whole number, and an integer is appropriate for this purpose.

### `self.result_labels`
- **Purpose**: Stores labels displaying the results of each spin.
- **Line of Creation**: Line 18
- **Data Type**: List of Tkinter Label Widgets
- **Reasoning**: Tkinter Label Widgets are used to display text in the graphical user interface.

### `self.games_won` and `self.games_lost`
- **Purpose**: Tracks the number of games won and lost.
- **Line of Creation**: Line 19 and 20
- **Data Type**: Integer
- **Reasoning**: Both are whole numbers, and integers are suitable for counting.

## if-block Details

### Bet Validation (Lines 26-31)
- **Role**: Ensures that the user places a valid bet within their available credits.
- **Beginning Line**: Line 26
- **Ending Line**: Line 31

### Hold Toggle Warning (Lines 40-46)
- **Role**: Provides a warning if the user attempts to hold more than two symbols.
- **Beginning Line**: Line 40
- **Ending Line**: Line 46

### Spin Validation (Lines 55-60)
- **Role**: Ensures that the user cannot spin without placing a bet or holding two symbols.
- **Beginning Line**: Line 55
- **Ending Line**: Line 60

### Jackpot Win Check (Lines 77-91)
- **Role**: Checks for a jackpot win and adjusts credits accordingly.
- **Beginning Line**: Line 77
- **Ending Line**: Line 91

### Game Over Check (Lines 94-104)
- **Role**: Ends the game when the user runs out of credits.
- **Beginning Line**: Line 94
- **Ending Line**: Line 104

## Loop Details

### Main Game Loop (Lines 106-136)
- **Purpose**: Controls the flow of the game, allowing the user to play multiple rounds.
- **Beginning Line**: Line 106
- **Ending Line**: Line 136
- **Loop Type**: While loop
- **Reasoning**: A while loop is appropriate as it allows the game to continue until the user decides to quit.

## Enhancements

### 1. Enhanced Jackpot Mechanism
- **Location**: Lines 15, 77-91
- **Description**: Modified the jackpot mechanism to be more dynamic, increasing the excitement of winning.
- **Explanation**: The jackpot now increases with each spin, creating a progressive jackpot system.

### 2. Improved GUI Styling
- **Location**: Lines 13-18, 26-31, 40-46, 55-60, 77-91, 94-104, 106-136
- **Description**: Enhanced the visual appeal of the graphical user interface.
- **Explanation**: Applied a consistent and visually appealing style to buttons, labels, and messages.

### 3. Game Statistics Display
- **Location**: Lines 13-20, 94-104
- **Description**: Added a display for the number of games won and lost.
- **Explanation**: Provides users with additional feedback on their performance.

