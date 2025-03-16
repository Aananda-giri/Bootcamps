# Part-1: Introduction

* SB3 is to RL what scikit-learn is to ML


## Requirements:
pytorch
stable-baseline3

pip install gym[box2d]


## Intro
1. Environment: what we are trying to solve (e.g. game)
2. Model: what: trained algorighm
3. Agent: Interact with environment
4. Observation: sense environment
5. Action: what agent will do in environment
6. Step: (progressing in environment) take action, get new observation, reward, done


## Actions: 
1. Discrete: Left, right, up, down
2. Continuous: e.g. servo torque (-1 to 1) (harder to learn than discrete actions)
   - continuous actions can be converted to discrete actions most of the time


```python
# pip install gym[box2d]

```



# Reference
* [youtube-playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDf0O2DWwLZBfJeYY-JOeZB1)
