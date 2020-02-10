# Backports from Debian

The list of packages backported is in `debian-repo-main/buster-partial.list`.


## Backport a new package from Debian

* Edit `debian-repo-main/buster-partial.list` and add:

```
my-package install
```

Note: `my-package` must be the source package name, not the binary
package name, e.g. `stevedore`, not `python-stevedore`.

* Then run on `mirror.wazo.community`:

```
reprepro update wazo-dev-buster
```

# Backports from newer Wazo Platform versions

## wazo-ansible

* Add tag wazo-XX.XX.0 (signed)
* Add tag wazo-XX.XX.1 (signed)
* Move tag wazo-XX.XX to wazo-XX.XX.1 (signed): used by install script & ISO builder

## Other packages

* Add tag wazo-XX.XX.1
* Copy package to wazo-rc-buster
  * `reprepro-main copysrc wazo-rc-buster wazo-dev-buster mypackage`
* Copy package to pelican-buster
  * `reprepro-main copysrc pelican-buster wazo-rc-buster mypackage`
* Copy package to archive
  * Uncomment `Update wazo-rc-buster` in `/data/reprepro/archive/conf/distributions`
  * `reprepro-archive checkupdate wazo-XX.XX`
  * `reprepro-archive update wazo-XX.XX`
  * Recomment `Update wazo-rc-buster` in `/data/reprepro/archive/conf/distributions`
