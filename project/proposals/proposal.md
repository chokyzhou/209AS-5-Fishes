# MDP on Single-player Games

### Summary:
* In this project, we propose a bot modeled by MDP that can play flappy bird. Hopefully, the bot could outperform existing solutions by flapping fewer times when acheiving the same score.

### Project git repo(s):  [Click me](https://github.com/chokyzhou/209AS-5-Fishes/tree/v2/project)

## Big picture 

### What is the overall problem that this and related research is trying to solve?
* Some games are designed to be competitive. Players try best to achieve the highest score and claim the top 1 spot. However, the player's performance is stochastic. What if there exists a player that can perform at top level consistently?
* A bot however, can play a game using mathematical foundation and state of the art algorithms. If the bot is trained well, the bot can play well consistently.

### Why should people (everyone) care about the problem?
* A bot can do well in a task that needs high performance and consistency. This saves the cost that trains an expert while reducing risks of relying on humans who are not consistent. 

### What has been done so far to address this problem?
* An abstraction method for MDPs based on stochastic two-player games has been proposed. 
* DeepMind, OpenAI and Universe have high level abstractions to build super human bots using deep neral networks.

## Specific project scope

### What subset of the overall big picture problem are you addressing in particular?
* We are interested in making a bot that plays flappy bird. Before our work, various methods have been proposed to beat the game. However, most of the work focus on beating the game. The bird can flap as many times as it want as long as it does't touch the pipe. Our objective is to improve on their work by letting the bird flap as few times as possible. 
* In summary, we want to find smallest flaps when passing pipes.

### How does solving this subproblem lead towards solving the big picture problem?.
* Consistency - the bot can consistently beat the game.
* High performance - beat the game efficiently by flapping as few times as possible.
  
### What is your specific approach to solving this subproblem?
* TODO

### How can you be reasonably sure this approach will result in a solution?
* Flappy bird can be categorized as a MDP problem. For example, action is click, state is every single pixels, reward is if the bird has touched the pipe.
* The next step is to solve the MDP problem, which we have gained some experience through coursework.

### How will we know that this subproblem has been satisfactorily solved, using quantitative metrics?
* First, the baseline is to make sure that our bot can score 100 by passing 100 pipes. Then we can compare to other bots by measuring how many flaps are made during scoring.

## Broader impact
(even if someone doesn't care about the big picture problem that you started with, why should they still care about the specific work that you've produced?  Who else can use your processes and results, and how?)

### What is the value of your approach beyond this specific solution?

### What is the value of this solution beyond solely solving this subproblem and getting us closer to solving the big picture problem?

## Background / related work / references
### [flappy bird ai](https://medium.com/analytics-vidhya/how-i-built-an-ai-to-play-flappy-bird-81b672b66521)
### [2-player mdp](https://www.researchgate.net/publication/221406673_Game-based_Abstraction_for_Markov_Decision_Processes)

## System capabilities, validation deliverables, engineering tasks

### Detailed schedule (weekly capabilities / deliverables / tasks):
