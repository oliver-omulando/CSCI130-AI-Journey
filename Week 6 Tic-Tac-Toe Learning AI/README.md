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
- Games trained: [Your number] - Final win rate: [Your percentage]% - States learned: [Your number] 
## What I Observed 
[Write 2-3 observations about how the AI's play improved] 
## Reinforcement Learning in Real Life 
1. **Game AI**: [Example] 
2. **Robotics**: [Example] 
3. **Recommendation Systems**: [Example] 
## Challenges and Solutions 
[Write 2-3 challenges you faced] 
## What I Learned 
[3-4 sentences about RL concepts you understand now]
