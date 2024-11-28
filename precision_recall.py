import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


# Générer des données simulées pour précision et rappel
# Ici, les données sont générées aléatoirement pour démonstration
np.random.seed(42)  # Fixer la graine pour la reproductibilité
precision_recall_data = []
for i in range(12):
    recall = np.sort(np.random.rand(20))  # Rappel en ordre croissant
    precision = np.clip(1 - 0.5 * recall + np.random.rand(20) * 0.1, 0, 1)  # Générer une précision réaliste
    precision_recall_data.append((recall, precision))

# Tracer les courbes
plt.figure(figsize=(12, 8))
for i, (recall, precision) in enumerate(precision_recall_data):
    plt.plot(recall, precision, label=f'Courbe {i + 1}')  # Ajouter chaque courbe avec une légende

# Ajouter les détails du graphique
plt.title('Courbes Précision-Rappel', fontsize=16)
plt.xlabel('Rappel', fontsize=14)
plt.ylabel('Précision', fontsize=14)
plt.legend(loc='lower left', fontsize=10)  # Position et taille de la légende
plt.grid(alpha=0.4)  # Ajouter une grille pour plus de clarté
plt.tight_layout()
# Enregistrement du graphique
plt.savefig("precision_recall.png")

# Afficher le graphique
plt.show()
