#!/usr/bin/env bash

#envs="WrappedCheckers WrappedCombat WrappedLumberjacks WrappedPongDuel WrappedPredatorPrey WrappedSwitch WrappedTrafficJunction"
envs="WrappedCheckers WrappedPredatorPrey"

for env in $envs;do
  python src/main.py --config=qplex --env-config=$env with local_results_path="$env/results/" use_tensorboard=True t_max=2000000 --seed 0
done
