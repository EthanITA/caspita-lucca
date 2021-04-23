#!/bin/bash
npm run build

# If it works, deploy!
git commit -am 'Automatic deploy!'
git push heroku master
