#!/bin/bash
#SBATCH --account=def-dhadidi
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --mem=16000M               # memory (per node)
#SBATCH --time=0-12:00            # time (DD-HH:MM)
#SBATCH --mail-user=h.fazli.k@gmail.com
#SBATCH --mail-type=ALL
python train_image_classifier.py