import wandb

print(f'The verison of wandb is: {wandb.__version__}')
assert wandb.__version__ == '0.15.8', f'expected version 2.1.10 but version found was {wandb.__version__}'
