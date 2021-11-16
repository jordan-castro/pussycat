# PetiteCat

PetiteCat is a new Smart Contract Dapp for the Binance Smart Chain. PetiteCat is starting out as a ERC20 token, but will be adding a NFT token soon.
The PetiteCat smart contract is a smart contract that allows users to create and sell petite cats.

PetiteCatERC20 is a Burnable, Mintable, and Pausable ERC20 token.

Burnable: Allows users to burn their tokens.
Mintable: Allows address with the MinterRole to mint new tokens.
Pausable: Allows address with the PauserRole to pause the token.
    Pausing is useful for deploying new features or fixing bugs.
    - Pausing emits a Pause event because transpacency is important.