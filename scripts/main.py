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
petite_cat = PCat(me)

def main():
    print(" -- Main start -- ")
    # Chequea data
    print(petite_cat.name())
    print(petite_cat.symbol())
    print(petite_cat.decimals())
    print(petite_cat.total_supply())

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
    petite_cat.transfer(rudeus_greyart, 100)
    # Intenta transferir sin saldo
    try:
        petite_cat.transfer(rudeus_greyart, 100, eris_whats_her_face)
        print("Nope")
    except:
        print("Success")

    petite_cat.transfer(rudeus_greyart, 100, me)
    # Transfer from redeus
    petite_cat.transfer(eris_whats_her_face, 100, rudeus_greyart)
    # Transfer from redeus to himseld
    petite_cat.transfer(rudeus_greyart, 10, rudeus_greyart)
    pretty_print_balance(rudeus_greyart)
    pretty_print_balance(me)
    pretty_print_balance(eris_whats_her_face)
    print(" -- Transfer end -- \n")


def mint_tests():
    print(" -- Mint start -- ")
    # Send some tokens to TSCOG characters
    petite_cat.transfer(seol_jihu, 100)
    petite_cat.transfer(yeo_soohi, 100)
    pretty_print_balance(me)
    # Add some tokens to me
    petite_cat.mint(me, 400)
    pretty_print_balance(me)
    print(f"Total supply: {petite_cat.total_supply()}")

    # Try and mint as a non roler
    petite_cat.mint(seol_jihu, 400, yeo_soohi)
    pretty_print_balance(seol_jihu)
    # Make yeo_soohi a roler
    petite_cat.add_role(yeo_soohi, 3)
    petite_cat.mint(seol_jihu, 400, yeo_soohi)
    pretty_print_balance(seol_jihu)
    print(f"Total supply: {petite_cat.total_supply()}")
    print(" -- Mint end -- \n")


def burn_tests():
    print(" -- Burn start -- ")
    # Send some tokens to TBATE characters
    petite_cat.transfer(arthur_lewyin, 500)
    petite_cat.transfer(tessia_earlith, 200)
    # I like Caera but comeon Tessia is the one.
    petite_cat.transfer(caera_whats_her_face, 100)

    # Burn
    petite_cat.burn(499, arthur_lewyin)
    pretty_print_balance(arthur_lewyin)

    petite_cat.burn(199, tessia_earlith)
    pretty_print_balance(tessia_earlith)

    petite_cat.burn(99, caera_whats_her_face)
    pretty_print_balance(caera_whats_her_face)

    print(f"Total supply: {petite_cat.total_supply()}")
    print(" -- Burn end -- \n")


def pause_tests():
    print(" -- Pause start -- ")
    # Cause buhl fresh
    petite_cat.transfer(jay, 10000)
    petite_cat.transfer(shelly, 10000)

    # Intenta pause
    petite_cat.pause_contract(jay)
    print("If failed good!")

    petite_cat.pause_contract(me)
    print(petite_cat.paused())
    try:
        # Intenta transfer
        petite_cat.transfer(shelly, 100, jay)
    except:
        pass
    # Mint as owner
    petite_cat.mint(me, 400)
    # Mint as non owner
    petite_cat.mint(shelly, 400, jay)
    # Intenta burn
    petite_cat.burn(200, jay)
    # Now burn as owner
    petite_cat.burn(200, me)

    # Unpause
    petite_cat.pause_contract(shelly)
    print("It failed good!")
    petite_cat.pause_contract(me)

    petite_cat.transfer(jay, 100, shelly)
    petite_cat.mint(shelly, 400)
    petite_cat.burn(200, shelly)

    print(" -- Pause end -- \n")


def role_tests():
    print(" -- Role start -- ")

    # Add roles
    petite_cat.add_role(rudeus_greyart, 1) # Admin
    petite_cat.add_role(eris_whats_her_face, 2) # Pauser
    petite_cat.add_role(seol_jihu, 3) # Minter
    petite_cat.add_role(jay, 3) # Minter
    
    # Add to a role as admin
    petite_cat.add_role(arthur_lewyin, 2, rudeus_greyart)
    # Remove from a role as admin
    petite_cat.remove_role(arthur_lewyin, rudeus_greyart)

    # Now try to add a admin as admin
    petite_cat.add_role(arthur_lewyin, 1, rudeus_greyart)
    print("It failed good!")
    petite_cat.add_admin(arthur_lewyin, rudeus_greyart)
    print("It failed good!")
    petite_cat.add_admin(arthur_lewyin)

    # Now try to remove a admin as admin
    petite_cat.remove_role(arthur_lewyin, rudeus_greyart)
    print("It failed good!")
    petite_cat.remove_role(arthur_lewyin)

    # Now mint as a minter and puase as a pauser
    petite_cat.mint(seol_jihu, 400)
    petite_cat.pause_contract(eris_whats_her_face)
    # Unpause as admin
    petite_cat.pause_contract(rudeus_greyart)

    # And renounce role
    petite_cat.renounce_role(jay)
    print(f"{address_to_name(jay)}'s role: {petite_cat.role_of(jay)}")

    print(" -- Role end -- \n")


def owner_tests():
    print(" -- Owner start -- ")

    # Send some tokens to Artur (Future owner)
    petite_cat.transfer(arthur_lewyin, 10000)
    # Chequea quien es owner
    print(address_to_name(petite_cat.owner()))
    # Chequea is arthur already has a role
    if petite_cat.role_of(arthur_lewyin) != 0:
        print("Arthur has role")
        petite_cat.remove_role(arthur_lewyin)
    # Try as someone else to transfer to arthur
    petite_cat.change_owner(arthur_lewyin, caera_whats_her_face)
    print("Should fail ^^")
    # Now actually transfer to arthur
    petite_cat.change_owner(arthur_lewyin, me)
    print(address_to_name(petite_cat.owner()))

    # Pause el contract y hacemos la vaina como author
    petite_cat.pause_contract(arthur_lewyin)
    petite_cat.transfer(caera_whats_her_face, 500, arthur_lewyin)
    petite_cat.transfer(tessia_earlith, 1000, arthur_lewyin) # Because Tess is better

    # Now renouce ownership
    petite_cat.stop_being_owner(arthur_lewyin)
    print(petite_cat.owner())

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
    print(f"{address_to_name(address)}: {petite_cat.balance_of(address)}")