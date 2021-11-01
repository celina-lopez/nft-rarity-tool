import json
import sys
from yaspin import yaspin
from yaspin.spinners import Spinners

sys.path.append("./utils/")

import calculate
import graph

# Open _metadata
f = open('_metadata.json')
data = json.load(f)
f.close()

with yaspin(Spinners.monkey, text="Getting rarity") as sp:
	# get traits
	traits = calculate.traits(data)
	# get each rarity
	nfts = calculate.rarity(data, traits)
	# group nft rarity
	groupings = calculate.groupings(nfts)

	graph.save_pies(traits)
	graph.save_bar(groupings, "rarity")

	sp.write("🐵 Created graphs")
  