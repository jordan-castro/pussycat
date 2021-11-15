from brownie import PetiteCat, accounts


# Account names are not important, but they must be unique.
me = accounts[0]
# MT
rudeus_greyart = accounts[1]
eris_whats_her_face = accounts[2]
# TSCOG
seol_jihu = accounts[3]
yeo_soohi = accounts[4]
# TBATE
arthur_lewyin = accounts[5]
tessia_earlith = accounts[6]
caera_whats_her_face = accounts[7]
# WB
jay = accounts[8]
shelly = accounts[9]


def main():
    # Deploy contract
    petite_cat = PetiteCat.deploy({'from': me})
    # Chequea data
    print(petite_cat.name())
    print(petite_cat.symbol())
    print(petite_cat.decimals())
    print(petite_cat.totalSupply())