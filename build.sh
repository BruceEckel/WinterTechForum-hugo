#!/bin/bash

echo "Delete hugo-material-banner theme"
rm -fr themes

echo "Download latest hugo-material-banner theme"
git clone https://github.com/pavelbinar/hugo-material-banner.git themes/hugo-material-banner

echo "Hugo version"
hugo version

echo "Build Hugo site"
hugo --minify --cleanDestinationDir --baseURL $URL
