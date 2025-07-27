# Permissions and Groups Setup

## Custom Permissions:
Defined in `Article` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups:
Created via Django Admin:
- **Viewers** → can_view
- **Editors** → can_create, can_edit
- **Admins** → all permissions

## How It Works:
Views are protected using `@permission_required` decorator.
Each user is assigned to a group with relevant permissions.

To test:
- Log in as users in each group.
- Try accessing each view (list, create, edit, delete).
