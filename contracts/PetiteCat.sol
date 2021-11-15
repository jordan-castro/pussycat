// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// import "C:/Users/jorda/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "C:/Users/jorda/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/ERC20.sol";
import "C:/Users/jorda/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/security/Pausable.sol";
import "C:/Users/jorda/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "C:/Users/jorda/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "../contracts/AccessControl.sol";

/// @title PetiteCat Token
/// @author James Garfield
/// @notice A ERC20 token for the PetiteCat project.
/// @dev Token is Pausable, Mintable, and Burnable.
contract PetiteCat is AccessControl, ERC20Burnable, ERC20Pausable {
    uint256 private constant PAUSE_ROLE = 2;
    uint256 private constant MINT_ROLE = 3;
    
    // Contruct the ERC20 token
    constructor() ERC20("PetiteCat", "PTC") {
        uint totalSupply = 1000000;
        _mint(msg.sender, totalSupply);
    }

    /// @dev Because we are using the ERC20Pausable contract, and the ERC20Burnable contract.
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override(ERC20, ERC20Pausable) {
        super._beforeTokenTransfer(from, to, amount);
    }

    /// @dev pause the contract.
    /// @dev Must be called by pauser or owner.
    /// If the contract is paused, then it will unpause.  
    function pauseContract() public roleOrOwner(PAUSE_ROLE) {
        if (paused()) {
            _unpause();
        } else {
            _pause();
        }
    }

    /// @dev Mint tokens to the given address.
    /// @param _to The address to mint tokens to.
    /// @param _amount The amount of tokens to mint.
    /// @dev Must be called by owner or minter.
    function mint(address _to, uint256 _amount) public roleOrOwner(MINT_ROLE) whenNotPaused {
        _mint(_to, _amount);
    }

    /* Override burn methods so that you can only burn when the contract is not paused. */    
    
    /// @dev Destroys `amount` tokens from the caller.
    ///
    /// See {ERC20Burnable}.
    ///
    function burn(uint256 amount) public override whenNotPaused {
        super.burn(amount);
    }
    function burnFrom(address account, uint256 amount) public override whenNotPaused {
        super.burnFrom(account, amount);
    }
}