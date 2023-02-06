# qspr

*Deep learning assisted material discovery and quantitative structure−property relationship prediction*

**Installation:**

download this repo and run the following cmds
```
conda create --name qspr python=3.7
conda activate qspr
conda install git
cd qspr
conda install --yes --file requirements.txt
pip install selfies
conda install -c rdkit rdkit nox cairo 
conda install pytorch torchvision -c pytorch
pip install -e .
```

If pytorch-cpu version rather than pytorch-gpu version is mistakenly installed, the problem can be solved by running the following command:
```
conda uninstall pytorch-mutex
conda uninstall cpuonly
conda install pytorch torchvision -c pytorch
```

**Generative model training for task 1:**

The configuration for RNN and clarification of parameters in task 1 is tabulated in Script 3 and Table 1. One can twick other hyper-parameters in ‘rnn.yaml’ to optimize the loss value.  The training will start through following command. 
```
MKL_SERVICE_FORCE_INTEL=1
MKL_THREADING_LAYER=GNU
python train_rnn.py
```
The output will be 
```
device:  cuda
number of workers to load data:  24
which vocabulary to use:  selfies
total number of SMILES loaded:  84445
total number of valid SELFIES:  84445
begin training...
100%|██████████| 165/165 [00:09<00:00, 16.98it/s]epoch 1, train loss: 66.12
valid rate: 1.0
model saved at epoch 1
 
100%|██████████| 165/165 [00:09<00:00, 17.56it/s]epoch 2, train loss: 44.55
valid rate: 1.0
model saved at epoch 2
…
```

**Generate new molecules**

Run the following commands to generate new molecules. The default amount of generated molecule is batch_size*num_batches=2048*20=40960, saved in SMILES format
```
MKL_SERVICE_FORCE_INTEL=1
MKL_THREADING_LAYER=GNU
python generate.py -result_dir ./run/task1/
```

**Predictive model training for task 2:**

The training hyperparameters is saved in ‘/configs/gcnn.py’. Run the following command to train the predictive model
```
MKL_SERVICE_FORCE_INTEL=1
MKL_THREADING_LAYER=GNU
python launch.py --nproc_per_node=1
run.py --config_file=./configs/gcnn.py
```

During training, you will get the following output:
```
Mean Tmelt in training data:  128.29501155802737
Standard deviation of Tmelt in training data:  78.93209297065965
Min value of Tmelt in training data:  -199.0
Max value of Tmelt in training data:  505.0 
2022-12-22 15:09:58,614  Starting training from scratch
2022-12-22 15:09:58,615  Training is set up from epoch 0
  0%|          | 0/200 [00:00<?, ?it/s]
  0%|          | 0/833 [00:00<?, ?it/s]
  0%|          | 1/833 [00:01<22:26,  1.62s/it]
  0%|          | 4/833 [00:01<04:37,  2.98it/s]
  1%|          | 8/833 [00:01<02:03,  6.71it/s]
  1%|▏         | 12/833 [00:01<01:16, 10.79it/s]
  2%|▏         | 16/833 [00:02<00:54, 15.00it/s]
  2%|▏         | 20/833 [00:02<00:42, 19.03it/s]

```

**Predict melting point of new molecule**

After defining the test dataset, prediction results can be obtained by running the following command:
```
MKL_SERVICE_FORCE_INTEL=1
MKL_THREADING_LAYER=GNU
python launch.py --nproc_per_node=1
run.py --config_file==/configs/gcnn.py --mode=predict
```
