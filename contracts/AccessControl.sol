// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "C:/Users/jorda/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/utils/Context.sol";

/**
    @title AccessControl

    @dev El accesso para MonterCock y sus contracts.

    Note insperacion viene por {KittyAccess} y el {AccessControl} de OpenZeppelin 
    Note Some roles are preset:
        - Admin: 1
        - NoRole: 0
    Note Owner is already defined as _owner. And is set when constructed based on the sender.
 */
abstract contract AccessControl is Context {
    address private _owner;
    uint256 private constant ADMIN_ROLE = 1;
    uint256 private constant NO_ROLE = 0;

    mapping(address => uint256) private userToRole;
    // mapping(uint256 => string) roleName; ??? Possible

    // Empty constructor
    constructor() {
        _setOwner(_msgSender());
    }

    /* Modifiers */
    modifier adminOrOwner() {
        address sender = _msgSender();
        require(
            sender == _owner || userToRole[sender] == ADMIN_ROLE,
            "AccessControl: Must be owner or admin to call."
        );
        _;
    }

    modifier onlyOwner() {
        require(_msgSender() == _owner, "AccessControl: Address is not owner.");
        _;
    }

    /// @dev Tambien puede ser owner.
    modifier adminOrRole(uint256 role) {
        address sender = _msgSender();
        require(
            userToRole[sender] == role ||
                userToRole[sender] == ADMIN_ROLE,
            // string(
                // abi.encodePacked(
                    "AccessControl: Must be admin or of role"
                // )
            // )
        );
        _;
    }

    modifier roleOrOwner(uint256 role) {
        address sender = _msgSender();
        require(
            userToRole[sender] == role || sender == _owner,
            // string(
                // abi.encodePacked(
                    "AccessControl: Must be owner or of role"
                    // role
                // )
            // )
        );
        _;
    }

    modifier onlyRole(uint256 role) {
        require(
            userToRole[_msgSender()] == role,
            // string(
                // abi.encodePacked(
                    "AccessControl: Must be of role"
                    // role
                // )
            // )
        );
        _;
    }

    /// @dev To call functions using this modifier the caller needs to be the role or admin/owner.
    modifier roleAndAbove(uint256 role) {
        address sender = _msgSender();
        require(
            userToRole[sender] == role ||
            isAdmin(sender) || 
            isOwner(sender),
            "AccessControl: Must be of role or higher." 
        );
        _;
    }

    function stopBeingOwner() public onlyOwner {
        _setOwner(address(0));
    }

    function changeOwner(address _newOwner) public onlyOwner {
        _setOwner(_newOwner);
    }

    function addAdmin(address _newAdmin) public onlyOwner {
        _setAdmin(_newAdmin);
    }

    function addRole(address _newRoler, uint256 role) public adminOrOwner {
        // Only owner can add admin
        if (_msgSender() != _owner) {
            require(role != ADMIN_ROLE, "AccessControl: Cannot add admin role.");
        }
        _setRole(_newRoler, role);
    }

    function renounceRole() public {
        address sender = _msgSender();
        require(
            userToRole[sender] != NO_ROLE,
            "AccessControl: This account has no role to renounce."
        );
        userToRole[sender] = NO_ROLE;
    }

    function removeRole(address _toBeRemoved) public adminOrOwner {
        require(
            _toBeRemoved != address(0),
            "AccessControl: You can not remove the 0 address."
        );
        // Only the owner can remove admins
        if (_msgSender() != _owner) {
            require(userToRole[_toBeRemoved] != ADMIN_ROLE, "AccessControl: You can not remove an admin.");
        }
        require(
            _toBeRemoved != _owner,
            "AccessControl: You can not remove the owner."
        );
        userToRole[_toBeRemoved] = 0;
    }

    /* Setters */

    function _setOwner(address owner_) private {
        require(
            _owner != owner_,
            "AccessControl: Owner can not be set to themselves."
        );
        _owner = owner_;
    }

    function _setAdmin(address _admin) private {
        require(
            _admin != address(0),
            "AccessControl: Account can not be 0 address."
        );
        require(
            userToRole[_admin] != ADMIN_ROLE,
            "AccessControl: Account is already admin."
        );
        userToRole[_admin] = ADMIN_ROLE;
    }

    function _setRole(address account, uint256 role) private {
        require(userToRole[account] == NO_ROLE, "AccessControl: Account is already role.");
        require(role != NO_ROLE, "AccessControl: Can not set account to 0 role.");
        require(
            account != address(0),
            "AccessControl: Account can not be the 0 address."
        );
        require(
            userToRole[account] != role,
            "AccessControl: Account is already role."
        );

        userToRole[account] = role;
    }

    /* Getters */

    function owner() public view returns (address) {
        return _owner;
    }

    function isOwner(address _potentialOwner) public view returns (bool) {
        return _potentialOwner == _owner;
    }

    function isAdmin(address _potentialAdmin) public view returns (bool) {
        return userToRole[_potentialAdmin] == ADMIN_ROLE;
    }

    function isRole(address _potentialRoler, uint256 _roleToCheck)
        public
        view
        returns (bool)
    {
        return userToRole[_potentialRoler] == _roleToCheck;
    }

    function roleOf(address _account) public view returns (uint256) {
        return userToRole[_account];
    }

    // function isRoleOrOwner()
}
