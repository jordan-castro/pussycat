from brownie import PetiteCatERC20


class PCat:
    """
    Wrapper for brownie.PetiteCat solidity code.
    """
    def __init__(self, _from) -> None:
        self.deployer = _from
        self.contract = PetiteCatERC20.deploy({'from': _from})

    def __try_catch__(self, func, *args):
        try:
            return func(*args)
        except Exception as e:
            print(f"Error: {e}")
    
    def name(self) -> str:
        return self.contract.name()

    def symbol(self) -> str:
        return self.contract.symbol()

    def total_supply(self) -> int:
        return self.contract.totalSupply()

    def decimals(self) -> int:
        return self.contract.decimals()

    def balance_of(self, _owner: str) -> int:
        return self.contract.balanceOf(_owner)

    def transfer(self, _to: str, _value: int, sender = None) -> bool:
        return self.contract.transfer(_to, _value, {'from': sender or self.deployer})

    def transfer_from(self, _from: str, _to: str, _value: int, sender = None) -> bool:
        return self.contract.transferFrom(_from, _to, _value, {'from': sender or self.deployer})

    def approve(self, _spender: str, _value: int, sender=None) -> bool:
        return self.contract.approve(_spender, _value, {'from': sender or self.deployer})

    def allowance(self, _owner: str, _spender: str) -> int:
        return self.contract.allowance(_owner, _spender)

    def pause_contract(self, sender=None):
        self.__try_catch__(self.contract.pauseContract, {'from': sender or self.deployer})

    def burn(self, amount, sender=None):
        self.__try_catch__(self.contract.burn, amount, {'from': sender or self.deployer})

    def mint(self, to, amount, sender=None):
        self.__try_catch__(self.contract.mint, to, amount, {'from': sender or self.deployer})

    def change_owner(self, new_owner, sender=None):
        self.__try_catch__(self.contract.changeOwner, new_owner, {'from': sender or self.deployer})

    def add_admin(self, admin, sender=None):
        self.__try_catch__(self.contract.addAdmin, admin, {'from': sender or self.deployer})

    def add_role(self, address, role, sender=None):
        self.__try_catch__(self.contract.addRole, address, role, {'from': sender or self.deployer})

    def stop_being_owner(self, sender=None):
        self.__try_catch__(self.contract.stopBeingOwner, {'from': sender or self.deployer})

    def renounce_role(self, sender=None):
        self.__try_catch__(self.contract.renounceRole, {'from': sender or self.deployer})

    def remove_role(self, address, sender=None):
        self.__try_catch__(self.contract.removeRole, address, {'from': sender or self.deployer})

    def owner(self) -> str:
        return self.contract.owner()

    def is_owner(self, address) -> bool:
        return self.contract.isOwner(address)

    def is_admin(self, address) -> bool:
        return self.contract.isAdmin(address)

    def is_role(self, address, role) -> bool:
        return self.contract.isRole(address, role)

    def paused(self) -> bool:
        return self.contract.paused()
    
    def role_of(self, account) -> int:
        return self.contract.roleOf(account)