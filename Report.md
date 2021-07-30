# Project 2: Continuous Control (Report)

This project train an agent to navigate and collect bananas in a large, square world.



### Learning Algorithms:

I used Deep Deterministic Policy Gradients (DDPG) as underlying learning algorithms for training the agent. The implementation is hugely inspired from pendulum implementation provided in udacity deep-reinforcement-learning repo. In essence the program maintains two types of neural networks , actor and critic. The actor network produces action values corresponding to input states , which can help choose best action , while the critic can take that value and produce continuous value for the action taken.What's important  here is  that it takes the good part of both worlds, value based methods and policy gradient methods, and makes them work together in an synchronous way.  The implementation is in line with ddpg algirithm described in the nanodegree course.


### Chosen Hyperparameters:

Below are the hyper parameters which are used in this project:
 <p>

BUFFER_SIZE = int(1e5)  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# replay buffer size <br/>
BATCH_SIZE = 128       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# minibatch size<br/>
GAMMA = 0.99            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# discount factor<br/>
TAU = 1e-3              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# for soft update of target parameters<br/>
LR_ACTOR = 1e-4        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# learning rate of the actor <br/>
LR_CRITIC = 1e-4       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# learning rate of the critic<br/>
WEIGHT_DECAY = 0        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# L2 weight decay <br/>
</p>

### Architecture of Neural Network Used:

The actor netowrk has three layers: 
<br/>
— First layer : input size = 33 and output size = 128 <br/>
— Second layer : input size = 128 and output size = 128<br/>
— Third layer : input size = 128 and output size = 4<br/>
<br/>

The critic network has following layers:<br/>
<br/>
— First layer : input size = 33 and output size = 128<br/>
— Second layer : input size = 134 and output size = 128<br/>
— Third layer : input size = 128 and output size = 1<br/>
<br/>


### Plot of Rewards:

<img src="cctraining.png"/>

Saved Model: [ccactormodel.pt](ccactormodel.pt)



### Ideas for Future Work:

Using Double DQN and Dueling DQN to improve training.
Using Prioritized Experience Replay to further improve the training.




