# Games Overview

This document provides a comprehensive overview of all 22 games available in the Haive Games package.

## Complete Game List

### 1. **Chess**

- **Type**: Classic Board Game
- **Players**: 2 (White vs Black)
- **Config**: `ChessConfig`
- **Agent**: `ChessAgent`
- **Description**: Full chess implementation with all rules including castling, en passant, and promotion
- **Key Features**: Move validation, check/checkmate detection, PGN notation support

### 2. **Checkers**

- **Type**: Classic Board Game
- **Players**: 2 (Red vs Black)
- **Config**: `CheckersAgentConfig`
- **Agent**: `CheckersAgent`
- **Description**: American checkers with king promotion and multi-jump captures
- **Key Features**: Forced captures, king movement, draw detection

### 3. **Tic-Tac-Toe**

- **Type**: Abstract Strategy
- **Players**: 2 (X vs O)
- **Config**: `TicTacToeConfig`
- **Agent**: `TicTacToeAgent`
- **Description**: Classic 3x3 grid game
- **Key Features**: Win detection, draw detection, optimal play analysis

### 4. **Connect 4**

- **Type**: Abstract Strategy
- **Players**: 2
- **Config**: `Connect4AgentConfig`
- **Agent**: `Connect4Agent`
- **Description**: Drop pieces to connect four in a row
- **Key Features**: Gravity simulation, diagonal win detection

### 5. **Reversi (Othello)**

- **Type**: Classic Board Game
- **Players**: 2 (Black vs White)
- **Config**: `ReversiConfig`
- **Agent**: `ReversiAgent`
- **Description**: Flip opponent pieces by surrounding them
- **Key Features**: Valid move detection, automatic flipping, endgame scoring

### 6. **Mancala**

- **Type**: Classic Board Game
- **Players**: 2
- **Config**: `MancalaConfig`
- **Agent**: `MancalaAgent`
- **Description**: Ancient seed-sowing game
- **Key Features**: Capture rules, extra turn mechanics, endgame collection

### 7. **Nim**

- **Type**: Mathematical Strategy
- **Players**: 2
- **Config**: `NimConfig`
- **Agent**: `NimAgent`
- **Description**: Remove objects from piles, last to move wins
- **Key Features**: Multiple pile configurations, misère variant support

### 8. **Mastermind**

- **Type**: Puzzle/Deduction
- **Players**: 2 (Codemaker vs Codebreaker)
- **Config**: `MastermindConfig`
- **Agent**: `MastermindAgent`
- **Description**: Deduce secret color code through feedback
- **Key Features**: Feedback generation, strategy analysis

### 9. **Poker**

- **Type**: Card Game
- **Players**: 2-6
- **Config**: `PokerAgentConfig`
- **Agent**: `PokerAgent`
- **Description**: Texas Hold'em style poker
- **Key Features**: Betting rounds, hand evaluation, bluffing support

### 10. **Texas Hold'em**

- **Type**: Card Game
- **Players**: 2-6
- **Config**: `HoldemGameAgentConfig`
- **Agent**: `HoldemGameAgent`
- **Description**: Full Texas Hold'em implementation
- **Key Features**: Advanced betting, side pots, all-in handling, rich UI

### 11. **Battleship**

- **Type**: Strategy Game
- **Players**: 2
- **Config**: `BattleshipAgentConfig`
- **Agent**: `BattleshipAgent`
- **Description**: Naval combat with hidden ship placement
- **Key Features**: Ship placement validation, hit/miss tracking, AI strategies

### 12. **Risk**

- **Type**: Strategy Game
- **Players**: 2-6
- **Config**: `RiskConfig`
- **Agent**: `RiskAgent`
- **Description**: World domination through territorial control
- **Key Features**: Territory management, dice combat, reinforcement allocation

### 13. **Monopoly**

- **Type**: Economic Board Game
- **Players**: 2-4
- **Config**: `MonopolyAgentConfig`
- **Agent**: `MonopolyAgent`
- **Description**: Property trading and development game
- **Key Features**: Property management, rent collection, trading, jail mechanics

### 14. **Clue (Cluedo)**

- **Type**: Deduction Game
- **Players**: 3-6
- **Config**: `ClueConfig`
- **Agent**: `ClueAgent`
- **Description**: Solve the murder mystery
- **Key Features**: Deduction logic, suggestion/accusation system, note-taking

### 15. **Mafia**

- **Type**: Social Deduction
- **Players**: 5-12
- **Config**: `MafiaAgentConfig`
- **Agent**: `MafiaAgent`
- **Description**: Day/night phases with hidden roles
- **Key Features**: Role assignment, voting mechanics, special abilities

### 16. **Among Us**

- **Type**: Social Deduction
- **Players**: 4-10
- **Config**: `AmongUsAgentConfig`
- **Agent**: `AmongUsAgent`
- **Description**: Find the impostor(s) among the crew
- **Key Features**: Task completion, emergency meetings, ejection voting

### 17. **Dominoes**

- **Type**: Tile Game
- **Players**: 2-4
- **Config**: `DominoesAgentConfig`
- **Agent**: `DominoesAgent`
- **Description**: Match tiles by number
- **Key Features**: Multiple variants, blocking detection, score calculation

### 18. **Fox and Geese**

- **Type**: Asymmetric Strategy
- **Players**: 2 (Fox vs Geese)
- **Config**: `FoxAndGeeseConfig`
- **Agent**: `FoxAndGeeseAgent`
- **Description**: Fox tries to reach the henhouse, geese try to trap fox
- **Key Features**: Asymmetric gameplay, movement restrictions

### 19. **Go**

- **Type**: Classic Board Game
- **Players**: 2 (Black vs White)
- **Config**: `GoAgentConfig`
- **Agent**: `GoAgent`
- **Description**: Ancient territorial control game
- **Key Features**: Capture mechanics, ko rule, territory scoring, SGF support

### 20. **Debate**

- **Type**: Structured Argument Game
- **Players**: 2+ (Debaters + optional Judge)
- **Config**: `DebateAgentConfig`
- **Agent**: `DebateAgent`
- **Description**: Formal debate with rounds and scoring
- **Key Features**: Topic selection, argument tracking, rebuttal system, judging

### 21. **Base Game Framework**

- **Type**: Framework
- **Config**: `GameConfig`
- **Agent**: `GameAgent`
- **Description**: Base implementation for creating new games

### 22. **Multi-Player Framework**

- **Type**: Framework
- **Config**: `MultiPlayerGameConfig`
- **Agent**: `MultiPlayerGameAgent`
- **Description**: Framework for multi-player game implementations

## Game Statistics

- **Total Games**: 22 (20 full games + 2 frameworks)
- **2-Player Games**: 15
- **Multi-Player Games**: 7
- **Card Games**: 3
- **Board Games**: 8
- **Strategy Games**: 5
- **Social Deduction**: 3
- **Abstract/Other**: 3

## Common Interfaces

All games share common interfaces:

```python
# Common configuration pattern
config = GameConfig(
    aug_llm_configs={
        "player_1": llm_config_1,
        "player_2": llm_config_2
    },
    max_rounds=100  # or max_moves, max_turns, etc.
)

# Common agent pattern
agent = GameAgent(config)
initial_state = agent.get_initial_state()

# Common execution pattern
for state in agent.app.stream(initial_state):
    # Process game state
    if state.get('game_over'):
        break
```
