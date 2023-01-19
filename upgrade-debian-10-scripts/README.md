

# Extract buster packages list
apt list > apt_list

# Extract current dependencies
cd wazo-pbx
find -name \*requirements\*.txt ! -path '*/.tox/*' -exec cat {} \; | sed 's/ *#.*//g' | grep '==' | sort -u >| stretch.txt

# Generate update.txt
./buster.sh

# Update all requirements files
find -name \*requirements\*.txt ! -path '*/.tox/*' | ./update.sh

# Commit and push
repo forall -c '[ -n "$(git status -s)" ] && git commit -m "update requirement to buster" -a && git push origin buster:buster'
