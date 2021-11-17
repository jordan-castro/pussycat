"""
Deploys the contract and tests the functionality.
"""

print(" -- Script start -- ")


from brownie import accounts
from .pcat import PCat


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

# Deploy contract
pussy_cat = PCat(me)

def main():
    print(" -- Main start -- ")
    # Chequea data
    print(pussy_cat.name())
    print(pussy_cat.symbol())
    print(pussy_cat.decimals())
    print(pussy_cat.total_supply())

    # transfer_tests()
    # mint_tests()
    # burn_tests()
    pause_tests()
    # role_tests()
    # owner_tests()
    print(" -- Main end -- ")


def transfer_tests():
    print(" -- Transfer start -- ")
    # Intenta transferir normal
    pussy_cat.transfer(rudeus_greyart, 100)
    # Intenta transferir sin saldo
    try:
        pussy_cat.transfer(rudeus_greyart, 100, eris_whats_her_face)
        print("Nope")
    except:
        print("Success")

    pussy_cat.transfer(rudeus_greyart, 100, me)
    # Transfer from redeus
    pussy_cat.transfer(eris_whats_her_face, 100, rudeus_greyart)
    # Transfer from redeus to himseld
    pussy_cat.transfer(rudeus_greyart, 10, rudeus_greyart)
    pretty_print_balance(rudeus_greyart)
    pretty_print_balance(me)
    pretty_print_balance(eris_whats_her_face)
    print(" -- Transfer end -- \n")


def mint_tests():
    print(" -- Mint start -- ")
    # Send some tokens to TSCOG characters
    pussy_cat.transfer(seol_jihu, 100)
    pussy_cat.transfer(yeo_soohi, 100)
    pretty_print_balance(me)
    # Add some tokens to me
    pussy_cat.mint(me, 400)
    pretty_print_balance(me)
    print(f"Total supply: {pussy_cat.total_supply()}")

    # Try and mint as a non roler
    pussy_cat.mint(seol_jihu, 400, yeo_soohi)
    pretty_print_balance(seol_jihu)
    # Make yeo_soohi a roler
    pussy_cat.add_role(yeo_soohi, 3)
    pussy_cat.mint(seol_jihu, 400, yeo_soohi)
    pretty_print_balance(seol_jihu)
    print(f"Total supply: {pussy_cat.total_supply()}")
    print(" -- Mint end -- \n")


def burn_tests():
    print(" -- Burn start -- ")
    # Send some tokens to TBATE characters
    pussy_cat.transfer(arthur_lewyin, 500)
    pussy_cat.transfer(tessia_earlith, 200)
    # I like Caera but comeon Tessia is the one.
    pussy_cat.transfer(caera_whats_her_face, 100)

    # Burn
    pussy_cat.burn(499, arthur_lewyin)
    pretty_print_balance(arthur_lewyin)

    pussy_cat.burn(199, tessia_earlith)
    pretty_print_balance(tessia_earlith)

    pussy_cat.burn(99, caera_whats_her_face)
    pretty_print_balance(caera_whats_her_face)

    print(f"Total supply: {pussy_cat.total_supply()}")
    print(" -- Burn end -- \n")


def pause_tests():
    print(" -- Pause start -- ")
    # Cause buhl fresh
    pussy_cat.transfer(jay, 10000)
    pussy_cat.transfer(shelly, 10000)

    # Intenta pause
    pussy_cat.pause_contract(jay)
    print("If failed good!")

    pussy_cat.pause_contract(me)
    print(pussy_cat.paused())
    try:
        # Intenta transfer
        pussy_cat.transfer(shelly, 100, jay)
    except:
        pass
    # Mint as owner
    pussy_cat.mint(me, 400)
    # Mint as non owner
    pussy_cat.mint(shelly, 400, jay)
    # Intenta burn
    pussy_cat.burn(200, jay)
    # Now burn as owner
    pussy_cat.burn(200, me)

    # Unpause
    pussy_cat.pause_contract(shelly)
    print("It failed good!")
    pussy_cat.pause_contract(me)

    pussy_cat.transfer(jay, 100, shelly)
    pussy_cat.mint(shelly, 400)
    pussy_cat.burn(200, shelly)

    print(" -- Pause end -- \n")


def role_tests():
    print(" -- Role start -- ")

    # Add roles
    pussy_cat.add_role(rudeus_greyart, 1) # Admin
    pussy_cat.add_role(eris_whats_her_face, 2) # Pauser
    pussy_cat.add_role(seol_jihu, 3) # Minter
    pussy_cat.add_role(jay, 3) # Minter
    
    # Add to a role as admin
    pussy_cat.add_role(arthur_lewyin, 2, rudeus_greyart)
    # Remove from a role as admin
    pussy_cat.remove_role(arthur_lewyin, rudeus_greyart)

    # Now try to add a admin as admin
    pussy_cat.add_role(arthur_lewyin, 1, rudeus_greyart)
    print("It failed good!")
    pussy_cat.add_admin(arthur_lewyin, rudeus_greyart)
    print("It failed good!")
    pussy_cat.add_admin(arthur_lewyin)

    # Now try to remove a admin as admin
    pussy_cat.remove_role(arthur_lewyin, rudeus_greyart)
    print("It failed good!")
    pussy_cat.remove_role(arthur_lewyin)

    # Now mint as a minter and puase as a pauser
    pussy_cat.mint(seol_jihu, 400)
    pussy_cat.pause_contract(eris_whats_her_face)
    # Unpause as admin
    pussy_cat.pause_contract(rudeus_greyart)

    # And renounce role
    pussy_cat.renounce_role(jay)
    print(f"{address_to_name(jay)}'s role: {pussy_cat.role_of(jay)}")

    print(" -- Role end -- \n")


def owner_tests():
    print(" -- Owner start -- ")

    # Send some tokens to Artur (Future owner)
    pussy_cat.transfer(arthur_lewyin, 10000)
    # Chequea quien es owner
    print(address_to_name(pussy_cat.owner()))
    # Chequea is arthur already has a role
    if pussy_cat.role_of(arthur_lewyin) != 0:
        print("Arthur has role")
        pussy_cat.remove_role(arthur_lewyin)
    # Try as someone else to transfer to arthur
    pussy_cat.change_owner(arthur_lewyin, caera_whats_her_face)
    print("Should fail ^^")
    # Now actually transfer to arthur
    pussy_cat.change_owner(arthur_lewyin, me)
    print(address_to_name(pussy_cat.owner()))

    # Pause el contract y hacemos la vaina como author
    pussy_cat.pause_contract(arthur_lewyin)
    pussy_cat.transfer(caera_whats_her_face, 500, arthur_lewyin)
    pussy_cat.transfer(tessia_earlith, 1000, arthur_lewyin) # Because Tess is better

    # Now renouce ownership
    pussy_cat.stop_being_owner(arthur_lewyin)
    print(pussy_cat.owner())

    print(" -- Owner end -- \n")


def address_to_name(address):
    name = "Unknown"
    if address == me:
        name = "Me"
    elif address == rudeus_greyart:
        name = "Rudeus Greyart"
    elif address == eris_whats_her_face:
        name = "Eris"
    elif address == seol_jihu:
        name = "Seol Jihu"
    elif address == yeo_soohi:
        name = "Yeo Soohi"
    elif address == arthur_lewyin:
        name = "Arthur Lewyin"
    elif address == tessia_earlith:
        name = "Tessia Earlith"
    elif address == caera_whats_her_face:
        name = "Caera"
    elif address == jay:
        name = "Jay"
    elif address == shelly:
        name = "Shelly"

    return name


def pretty_print_balance(address):
    print(f"{address_to_name(address)}: {pussy_cat.balance_of(address)}")