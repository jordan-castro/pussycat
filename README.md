# PussyCat

![pcat](https://github.com/user-attachments/assets/3c408271-a4df-48d5-9b58-d000344cff8c)

PussyCat is a new Smart Contract Dapp for the Binance Smart Chain. PussyCat is starting out as a ERC20 token, but will be adding a ERC721 token (NFT) soon.

PussyCatERC20 is a Burnable, Mintable, and Pausable ERC20 token.

    - Burnable: Allows users to burn their tokens.
    - Mintable: Allows address with the MinterRole to mint new tokens.
    - Pausable: Allows address with the PauserRole to pause the token.
        - Pausing is useful for deploying new features or fixing bugs.
        - Pausing emits a Pause event because transpacency is important.
