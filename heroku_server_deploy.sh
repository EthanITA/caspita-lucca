#!/bin/bash
cd client
npm run build
cd -

# If it works, deploy!
git commit -am 'Automatic deploy!'
git push heroku master --force
