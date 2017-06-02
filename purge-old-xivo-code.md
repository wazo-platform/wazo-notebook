# Pointers of what and how to purge old migration code

## Grep for conditions

In the directory containing all repos:

   grep if */debian/postinst
   
## Grep for "old"

In the directory containing all repos:

   grep if */debian/postinst

## Look in `squeeze-xivo-skaro`

* Go in the old `squeeze-xivo-skaro` repo and checkout the tag squeeze-xivo-skaro-13.01 (to purge older versions than 13.01).
* All the migration code you see in postinst files is too old, so if it still exists in the current postinst, remove it.

## Remove DB migration scripts

* Remove old SQL migration scripts from `xivo-manage-db`
