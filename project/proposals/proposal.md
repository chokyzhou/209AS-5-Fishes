# MDP on Single-player Games

### Summary:
* In this project, we propose an abstraction method for MDPs based on stochastic single-player games. If time is allowed, we might add RL to increase performance. 

### Project git repo(s):  [Click me](https://github.com/chokyzhou/209AS-5-Fishes/tree/v2/project)

## Big picture 

### What is the overall problem that this and related research is trying to solve?
* Various bots, scripts and algorithms have been proposed to beat a specific single-player game. And above methods are not generic solutions to other games even in the same genre.
* Imagine a bot that is capable of beating game regardless of game types.

### Why should people (everyone) care about the problem?
* 

### What has been done so far to address this problem?
* An abstraction method for MDPs based on stochastic two-player games has been proposed. 
* DeepMind, OpenAI and Universe have high level abstractions to build super human bots using deep neral networks.

## Specific project scope

### What subset of the overall big picture problem are you addressing in particular?
* We are interested in making a framework that decouple a 2D video game into an MDP problem.

### How does solving this subproblem lead towards solving the big picture problem?.
* After a game is transformed into an MDP, the game can then be conquered by MDP simulator.
  
### What is your specific approach to solving this subproblem?
* We propose an abstraction method for MDPs based on stochastic single-player games. The method can describe most single-player games as MDPs.
* 

### How can you be reasonably sure this approach will result in a solution?
* Mostly single player games can be categorized as MDPs.

### How will we know that this subproblem has been satisfactorily solved, using quantitative metrics?
* The subproblem can be tested by using the simulator built in class.

## Broader impact
(even if someone doesn't care about the big picture problem that you started with, why should they still care about the specific work that you've produced?  Who else can use your processes and results, and how?)

### What is the value of your approach beyond this specific solution?

### What is the value of this solution beyond solely solving this subproblem and getting us closer to solving the big picture problem?

## Background / related work / references
### [flappy bird ai](https://medium.com/analytics-vidhya/how-i-built-an-ai-to-play-flappy-bird-81b672b66521)
### [2-player mdp](https://www.researchgate.net/publication/221406673_Game-based_Abstraction_for_Markov_Decision_Processes)

## System capabilities, validation deliverables, engineering tasks

### Detailed schedule (weekly capabilities / deliverables / tasks):
