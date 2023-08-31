# Scripts Overview

This project contains a series of Bash scripts that perform various file and permission manipulation tasks. Each script is designed to accomplish a specific task and is described below:

## 0-i_am_betty

This script switches the current user to the user "betty".

## 1-who_am_i

This script prints the effective username of the current user.

## 2-groups

This script prints all the groups the current user is part of.

## 3-new_owner

This script changes the owner of the file "hello" to the user "betty".

## 4-create_hello

This script creates an empty file named "hello".

## 5-execute

This script adds execute permission to the owner of the file "hello".

## 6-multiple_permissions

This script adds execute permission to the owner and the group owner, and read permission to other users, to the file "hello".

## 7-all_execute

This script adds execute permission to the owner, the group owner, and other users to the file "hello".

## 8-James_Bond

This script sets the permission of the file "hello" to allow all permissions for the owner, the group owner, and others.

## 9-mode_change

This script sets the permission mode of the file "hello" to match the given numeric mode.

## 10-mirror_permissions

This script sets the permissions of the file "hello" to match the permissions of the file "olleh".

## 11-directories_permissions

This script adds execute permission to all subdirectories in the current directory for the owner, the group owner, and other users.

## 12-directory_permissions

This script creates a directory named "my_dir" with permissions 751 in the working directory.

## 13-change_group

This script changes the group owner of the file "hello" to "school".

## 100-change_owner_and_group

This script changes the owner and the group owner of all files and directories in the working directory to "vincent" and "staff" respectively.

## 101-symbolic_link_permissions

This script changes the owner and the group owner of the symbolic link "_hello" to "vincent" and "staff" respectively.

## 102-if_only

This script changes the owner of the file "hello" to "betty" only if it is owned by the user "guillaume".



