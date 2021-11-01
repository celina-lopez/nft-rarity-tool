import math

def groupings(nfts):
	groupings = {}
	for name in nfts:
		if int(nfts[name]) not in groupings.keys():
			groupings[int(nfts[name])] = 1
		else:
			groupings[int(nfts[name])] += 1
	sorted_groupings = {}
	for key in sorted(groupings):
		sorted_groupings[key] = groupings[key]
	return sorted_groupings

def traits(data):
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
	# calculate rarity
	for trait in traits:
		for value in traits[trait]:
			traits[trait][value] = traits[trait][value] / 10000
	return traits

def rarity(data, traits):
	# get rarity for each nft (using log since the percentages are very low)
	nfts = {}
	for x in data:
		below = len(traits["body"].keys())
		rarity = 1
		for attribute in x["attributes"]:
			trait = traits[attribute["trait_type"]][attribute["value"]]
			rarity *= trait
		nfts[x["name"]] = abs(math.log(rarity, 10))
	return nfts
