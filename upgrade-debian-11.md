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

## Bump GPG keys expiration

* Builder key
* Release key for Wazo Platform
* Secondary release key for Wazo Platform
* See the wiki

## Previous upgrade

* See to-do list from previous upgrade:

    * [upgrade-debian-8](upgrade-debian-8.md)
    * [upgrade-debian-10](upgrade-debian-10.md)


# Specific things to do for bullseye migration

Be careful with the following packages. Since they don't have the `~wazo1` in their version, the
package version can be bigger than the debian version if the project version is the same:

* `python3-asynqp`
* `python3-hstspreload`
* `python3-rfc3986`
* `python3-sqlalchemy-continuum`
* `python3-swaggerpy`
