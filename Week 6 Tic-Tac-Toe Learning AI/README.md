# Tic-Tac-Toe Q-Learning AI 
 
## Project Overview 
This project demonstrates reinforcement learning by training an AI to play Tic-Tac-Toe 
through trial and error, without being explicitly programmed with strategies. 
 
## How to Run 
1. **Train the AI** 
```bash 
python train_agent.py 
``` 
Choose training intensity (1000-10000 games) 
2. **Play Against AI** 
```bash 
python play_game.py 
``` 
## How Q-Learning Works 
### The Q-Table 
The AI maintains a table of Q-values for each state-action pair: - **State**: Current board configuration - **Action**: Where to place the mark - **Q-Value**: How good that action is in that state 
### Learning Process 
1. **Exploration**: Try random moves to discover strategies 
2. **Exploitation**: Use learned knowledge to make good moves 
3. **Reward**: Win = +10, Lose = -10, Tie = +5 
4. **Update**: Adjust Q-values based on outcomes 
### My Training Results 
- Games trained: 1,000
- Final win rate: 68.6%
- States learned: 850
- Average Q-value: 0.333

**Progress Checkpoints:**
- Episode 100: 57.0% win rate (204 states learned)
- Episode 500: 64.6% win rate (618 states learned)
- Episode 1000: 68.6% win rate (850 states learned)

## What I Observed 
1. **Steady Improvement**: The AI's win rate increased from 57% at 100 games to 68.6% at 1,000 games, showing consistent learning progress.
2. **State Space Growth**: The AI learned 850 unique board configurations, developing a comprehensive understanding of different game scenarios.
3. **Exploration to Exploitation**: Early games had more random moves (exploration), but later games showed the AI confidently choosing winning strategies (exploitation). 
## Reinforcement Learning in Real Life 
1. **Game AI**: AI mastering chess, learning strategies through self-play similar to our Tic-Tac-Toe AI.
2. **Robotics**: Self-driving cars use RL to learn optimal driving behaviors, receiving rewards for safe navigation and penalties for errors.
3. **Recommendation Systems**: Netflix and YouTube use RL to learn which content to recommend, getting positive feedback when users engage and watch.

## Challenges and Solutions 
1. **Balancing Exploration vs Exploitation**: Initially the AI made too many random moves. Solution: Gradually reduced exploration rate from 30% to 5% as training progressed.
2. **Large State Space**: Tic-Tac-Toe has many possible board configurations. Solution: The Q-table dynamically stores only encountered states, learning 850 relevant positions.
3. **Credit Assignment**: Determining which moves led to winning. Solution: Updated Q-values backwards through the entire game sequence, giving credit to earlier strategic moves.

## What I Learned 
Reinforcement learning teaches agents through trial and error rather than explicit programming. The Q-learning algorithm uses rewards to update a value table, balancing exploration of new strategies with exploitation of known good moves. I learned that AI doesn't need to be told the rules of winning it discovers and optimizes strategies by playing thousands of games and learning from outcomes. This approach applies far beyond games, powering real-world systems from robotics to recommendation engines.
