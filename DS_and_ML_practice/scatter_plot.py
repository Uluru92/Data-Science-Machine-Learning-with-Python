import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
cax = ax.scatter(X['AveRooms'], X['AveBedrms'], c=X['MedHouseVal'])
fig.colorbar(cax)
ax.set_ylabel('Average Bedrooms')
ax.set_xlabel('Average Rooms')