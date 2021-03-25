#envs="WrappedCheckers WrappedCombat WrappedLumberjacks WrappedPongDuel WrappedPredatorPrey WrappedSwitch WrappedTrafficJunction"
# envs="WrappedCheckers WrappedPredatorPrey"
envs="WrappedPredatorPrey"
import subprocess

for i in range(2**31-2, 2**31):
  for env in envs.split():
    cmdstr = f'python src/main.py --config=qplex --env-config={env} with local_results_path="./{env}/results/" use_tensorboard=True seed={i}'
    print(cmdstr)
    # subprocess.run(cmdstr, shell=True)
