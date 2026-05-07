#!/bin/bash
sed -i '' 's/@media (prefers-color-scheme: dark) {/:root[data-theme="dark"], @media (prefers-color-scheme: dark) {/g' shared.css
