
#!/bin/bash

set -e

for i in $(find . -name *.json); do

echo $i

jsonlint-php -v $i


done
