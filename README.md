# Udacity-Continuous-Control


### Project Details

<img src="env.gif"/>

The goal of this project is to solve the Reacher environment. In this environment, double-jointed arms can move to target locations. Agent must be able to reach and go along with a moving ball controlling its arms. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm for each arm . There are 20 arms. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

The environment is considered solved if a reward of +30 is obtain for 100 consecutive episodes.


### Getting Started

1. Create (and activate) a new environment with Python 3.6.

   - __Linux__ or __Mac__: 

   ```bash
   conda create --name drlnd python=3.6
   source activate drlnd
   ```

   - __Windows__: 

   ```bash
   conda create --name drlnd python=3.6 
   activate drlnd
   ```

2. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.

   ```bash
   git clone https://github.com/yuhouzhou/deep-reinforcement-learning.git
   cd deep-reinforcement-learning/python
   pip install .
   ```

3. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.  

   ```bash
   python -m ipykernel install --user --name drlnd --display-name "drlnd"
   ```

4. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu.

5. Download the environment from one of the links below.  You need only select the environment that matches your operating system:

   - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
   - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
   - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
   - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)

   (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

   (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

6. Place the files in this repo in the `p2_continuous_control/` folder. 

7. After above steps you are ready to run the `p2_continuous_control/Continuous_Control.ipynb`


### Instructions

There are two ways , one can run the continuous control agent training:<br/>

1. Run Continuous_Control.ipynb ( with zypyter notebook, this is modified version of code supplied with the udacity project assignment. You need to spcify the environment path.)
2. Run trainagent.py with supplying environment path at commandline.

The programs generate two outputs: 
1. actormodel.pth  ( the network weights for the actor network).
2. criticmodel.pth (the networks weights for critic network)

