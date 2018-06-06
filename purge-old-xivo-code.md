# Pointers of what and how to purge old migration code

## Grep for conditions

In the directory containing all repos:
```
   grep if */debian/*postinst
```

## Grep for "old"

In the directory containing all repos:
```
   grep old */debian/*postinst
```

## Remove DB migration scripts

* Remove old SQL migration scripts from `xivo-manage-db`

# Code scheduled for removal

## 17.14

* In version 17.14 the xivo-client-qt was renamed to wazo-client-qt. A function named renameConfigFile was added to rename the configuration. This function should be removed.
