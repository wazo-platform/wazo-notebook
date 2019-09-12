# Backports from Debian

The list of packages backported is in `debian-repo-main/buster-partial.list`.


## Backport a new package

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
