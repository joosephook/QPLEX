#!/usr/bin/env bash

envs="WrappedCheckers WrappedCombat WrappedLumberjacks WrappedPongDuel WrappedPredatorPrey WrappedSwitch WrappedTrafficJunction"

for env in $envs;do
  python src/main.py --config=qplex --env-config=$env with local_results_path="$env/results/" save_model=True use_tensorboard=True save_model_interval=100 t_max=200 epsilon_finish=0.1
  echo "Testing $env"
  echo "Continue?"
  read answer
done
