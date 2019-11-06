# Pointers of what and how to upgrade to the next debian version

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

## Merge DB migration scripts

* Merge and clean all alembic migration scripts. (It has never been done before)

## Previous upgrade

* See to-do list from previous upgrade:

    * [upgrade-debian-8](https://github.com/wazo-platform/wazo-notebook/blob/master/upgrade-debian-8.md)


# Specific things to do for bullseye migration

Nothing
