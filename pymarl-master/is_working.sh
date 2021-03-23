#!/usr/bin/env bash

python src/main.py \
  --config=qplex \
  --env-config=matrix_game_2 with local_results_path='../../../tmp_DD/sc2_bane_vs_bane/results/' \
  save_model=True \
  use_tensorboard=True \
  save_model_interval=200000 \
  t_max=210000 \
  epsilon_finish=1.0
