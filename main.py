import json
import sys

sys.path.append("./utils/")

import calculate
import graph

# Open _metadata
f = open('_metadata.json')
data = json.load(f)
f.close()
 
# get traits
traits = calculate.traits(data)
# get each rarity
nfts = calculate.rarity(data, traits)
# group nft rarity
groupings = calculate.groupings(nfts)

graph.save_pies(traits)
graph.save_bar(groupings, "rarity")
  