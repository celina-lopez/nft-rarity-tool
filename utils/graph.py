import matplotlib.pyplot as plt

COLORS = ['#FF0075', '#FF0000', '#FF9300', '#FBFF00', '#49FF00', '#99DDCC', '#FF5DA2', '#FF5DA2', '#9C19E0', '#000D6B', '#A2CDCD', '#C6D57E', '#E4BAD4', '#98DDCA', '#FFD3B4', '#D5ECC2', '#CE97B0', '#FBC6A4', '#F0D9FF', '#FCFFA6', '#C1FFD7', '#B5DEFF', '#CAB8FF', '#506D84', '#6B4F4F', '#43C0AC', '#FF5D9E', '#00BD56', '#85EF47', '#207DFF', '#FFD369', '#C0E218', '#E48900', '#9EDE73', '#CF0000', '#72147E', '#F21170', '#FA9905', '#FA9905', '#F0D9E7', '#FB7AFC', '#7DEDFF', '#7C83FD', '#28FFBF', '#F56FAD', '#77D970', '#172774']

def create_pie(traits, trait, figure):
	labels = tuple(traits[trait].keys())
	sizes = traits[trait].values()
	fig = plt.figure(num=figure, figsize=(13, 13), dpi=80, facecolor='w', edgecolor='k')
	patches, text = plt.pie(sizes, colors=COLORS, startangle=90, normalize=True)
	plt.axis('equal')
	plt.legend(patches, labels, loc="upper center", bbox_to_anchor=(0.5, -0.02))
	plt.tight_layout()
	plt.savefig("./graphs/" + trait + ".png")

def save_pies(traits):
	figure = 1
	for x in traits.keys():
		create_pie(traits, x, figure)
		figure += 1

def save_bar(groupings, name):
	plt.bar(range(len(groupings)), list(groupings.values()), align='center', color=COLORS)
	plt.xticks(range(len(groupings)), list(groupings.keys()))
	plt.savefig("./graphs/" + name + ".png")
