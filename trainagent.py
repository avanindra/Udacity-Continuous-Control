from unityagents import UnityEnvironment
import numpy as np
import matplotlib.pyplot as plt 
import torch
from collections import deque

from ccagentmulti import Agent


scores = [] 													 # initialize the score 
scores_window = deque(maxlen = 100) 
                          
def ddpgLearn(n_episodes = 500, max_t = 1000):

    for episode in range(n_episodes):
        env_info = env.reset(train_mode=True)[brain_name]            # reset the environment
        states = env_info.vector_observations
        agent.reset()                                                # reset the agent noise
        score = np.zeros(n_agents)
        
        while True:
            actions = agent.act(states)
        
            env_info = env.step( actions )[brain_name]               # send the action to the environment                            
            next_states = env_info.vector_observations               # get the next state        
            rewards = env_info.rewards                               # get the reward        
            dones = env_info.local_done                              # see if episode has finished        

            agent.step(states, actions, rewards, next_states, dones)

            score += rewards                                         # update the score
        
            states = next_states                                     # roll over the state to next time step        
                                                        
            if np.any( dones ):                                      # exit loop if episode finished        
                break                                        

        agent.checkpoint()

        scores.append(np.mean(score))
        scores_window.append(np.mean(score))

        print('\rEpisode: \t{} \tScore: \t{:.2f} \tAverage Score: \t{:.2f}'.format(episode, np.mean(score), np.mean(scores_window)), end="")  

        # if episode % 10:
			# torch.save(agent.actor_local.state_dict(), 'checkpoint_actor.pth')
		# torch.save(agent.critic_local.state_dict(), 'checkpoint_critic.pth')
        
        if np.mean(scores_window) >= 30.0:
        	print('\nEnvironment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(episode, np.mean(scores_window)))
	        break    


if __name__ == '__main__':

	DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

	env = UnityEnvironment(file_name = 'C:/projects/deep-reinforcement-learning/p2_continuous-control/Reacher_Windows_x86_64/Reacher.exe')


	# get the default brain
	brain_name = env.brain_names[0]
	brain = env.brains[brain_name]


	# reset the environment
	env_info = env.reset(train_mode=True)[brain_name]
	# number of agents in the environment
	n_agents = len(env_info.agents)
	print('Number of agents:', n_agents)
	# number of actions
	action_size = brain.vector_action_space_size
	print('Number of actions:', action_size)
	# examine the state space 
	state = env_info.vector_observations[0]
	print('States look like:', state)
	state_size = len(state)
	print('States have length:', state_size)

	agent = Agent(
					DEVICE, 
					state_size , n_agents, action_size , 4
			)

	


	ddpgLearn()

	torch.save(agent.actor_local.state_dict(), 'actormodel.pth')
	torch.save(agent.critic_local.state_dict(), 'criticmodel.pth')

	fig = plt.figure()
	ax = fig.add_subplot(111)
	plt.plot(np.arange(len(scores)), scores)
	plt.title('Progress of the agent over the episodes')
	plt.ylabel('Score')
	plt.xlabel('Episode #')
	plt.savefig('trainingplot.png')
	plt.show()
	   	    