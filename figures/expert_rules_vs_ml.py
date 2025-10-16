import matplotlib.pyplot as plt
import numpy as np

diseases = ['ASMD', 'Gaucher', 'Saposin']
models = ['Expert Rules', 'VAE', 'COPOD', 'Autoencoder', 'SUOD', 'ECOD']

data = {
    'ASMD': {
        'scores': [0.751, 0.580, 0.574],
        'errors': [0.068, 0.149, 0.284],
        'models': ['Expert Rules', 'VAE', 'COPOD']
    },
    'Gaucher': {
        'scores': [0.749, 0.626, 0.576],
        'errors': [0.048, 0.056, 0.187],
        'models': ['Expert Rules', 'Autoencoder', 'SUOD']
    },
    'Saposin': {
        'scores': [0.631, 0.360, 0.342],
        'errors': [0.111, 0.214, 0.270],
        'models': ['Expert Rules', 'COPOD', 'ECOD']
    }
}

colors = ['#440154', '#31688e', '#35b779', '#fde724', '#21918c', '#5ec962']
model_to_color = {
    'Expert Rules': '#f1595f',
    'VAE': '#79c36a',
    'COPOD': '#599ad3',
    'Autoencoder': '#f9a65a',
    'SUOD': '#9e66ab',
    'ECOD': '#cd7058'
}

fig, ax = plt.subplots(figsize=(12, 7))

bar_width = 0.25
x_positions = np.arange(len(diseases))

for idx, disease in enumerate(diseases):
    disease_data = data[disease]
    scores = disease_data['scores']
    errors = disease_data['errors']
    models_list = disease_data['models']
    
    for model_idx, (model, score, error) in enumerate(zip(models_list, scores, errors)):
        x = x_positions[idx] + (model_idx - 1) * bar_width
        color = model_to_color[model]
        bar = ax.bar(x, score, bar_width, label=model if idx == 0 else "", 
                     color=color, edgecolor='black', linewidth=1.2)
        
        ax.errorbar(x, score, yerr=error, fmt='none', ecolor='black', capsize=4, linewidth=1.5)

ax.set_ylabel('Mean F1-Score', fontsize=14, fontweight='bold')
ax.set_xticks(x_positions)
ax.set_xticklabels(diseases, fontsize=14)
ax.tick_params(axis='y', labelsize=14)
ax.set_ylim(0, 1.0)
ax.grid(axis='y', alpha=0.3, linestyle='--')

from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=model_to_color[m], edgecolor='black', 
                          label=m) for m in ['Expert Rules', 'VAE', 'COPOD', 'Autoencoder', 'SUOD', 'ECOD']]
ax.legend(handles=legend_elements, title='Screening Model', loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()
