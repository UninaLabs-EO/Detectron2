import json
from os import path
import matplotlib.pyplot as plt

# experiment_folder = './output/model_iter4000_lr0005_wf1_date2020_03_20__05_16_45'

def load_json_arr(json_path):
    lines = []
    with open(json_path, 'r') as f:
        for line in f:
            lines.append(json.loads(line))
    return lines

# experiment_metrics = load_json_arr(experiment_folder + '/metrics.json')
path = 'output/metrics.json'
experiment_metrics = load_json_arr(path)
fig, ax1 = plt.subplots(dpi=150)
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Loss')
# ax1.plot(
    # [x['iteration'] for x in experiment_metrics], 
    # [x['bbox_loss'] for x in experiment_metrics], color="black", label="Total Loss")
color = 'tab:blue'
retinanet=True

if retinanet:
    ax1.plot(
        [x['iteration'] for x in experiment_metrics if 'total_loss' in x], 
        [x['total_loss'] for x in experiment_metrics if 'total_loss' in x], color=color, label="Val Loss")
else:
    ax1.plot(
        [x['iteration'] for x in experiment_metrics if 'validation_loss' in x], 
        [x['validation_loss'] for x in experiment_metrics if 'validation_loss' in x], color=color, label="Val Loss")

plt.legend(['Val Loss'],loc='upper left')
 
# plt.plot(
#     [x['iteration'] for x in experiment_metrics], 
#     [x['total_loss'] for x in experiment_metrics])
# plt.plot(
#     [x['iteration'] for x in experiment_metrics if 'validation_loss' in x], 
#     [x['validation_loss'] for x in experiment_metrics if 'validation_loss' in x])
# plt.plot(
#     [x['iteration'] for x in experiment_metrics if 'bbox/AP' in x], 
#     [x['bbox/AP'] for x in experiment_metrics if 'bbox/AP' in x])



# plt.legend(['validation_loss','AP'], loc='upper left')

ax2 = ax1.twinx()

color = 'tab:orange'
ax2.set_ylabel('AP')
ax2.plot(
    [x['iteration'] for x in experiment_metrics if 'bbox/AP' in x], 
    [x['bbox/AP'] for x in experiment_metrics if 'bbox/AP' in x], color=color)
ax2.tick_params(axis='y')

plt.legend(['AP'],loc='upper right')
plt.show()

