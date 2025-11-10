import matplotlib.pyplot as plt
import seaborn as sns

# load the tips dataset
tips = sns.load_dataset("tips")

# set x and y variables
x = tips.groupby(['day'])['total_bill'].mean().index
y = tips.groupby(['day'])['total_bill'].mean()

# create figure and axis objects
fig, ax = plt.subplots()

# plot line
ax.plot(x, y, marker='o')

# set axis labels and title
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Average Total Bill ($)')
ax.set_title('Tips Dataset')

# display plot
plt.show()


