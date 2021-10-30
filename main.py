import json
import matplotlib.pyplot as plt


def create_pie(traits, trait):
	labels = tuple(traits[trait].keys())
	sizes = traits[trait].values()
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')
	plt.show()

# Open _metadata
f = open('_metadata.json')
data = json.load(f)
f.close()
 
# generate rarity data
traits = {}
for x in data:
	for attribute in x["attributes"]:
		trait_type = attribute["trait_type"]
		value = attribute["value"]
		if trait_type not in traits.keys():
			traits[trait_type] = {}
		if value not in traits[trait_type].keys():
			traits[trait_type][value] = 0
		traits[trait_type][value] += 1

for trait in traits:
	for value in traits[trait]:
		traits[trait][value] = traits[trait][value] / 10000


# get rarity for each nft
nfts = {}

for x in data:
	below = len(traits["body"].keys())
	rarity = 1
	for attribute in x["attributes"]:
		trait = traits[attribute["trait_type"]][attribute["value"]]
		rarity *= trait
	nfts[x["name"]] = rarity