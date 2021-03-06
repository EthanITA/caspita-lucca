#!/usr/bin/env bash
npm run build
git add app/dist -f
git commit -m "deployed" && git push CaspitaSrl `git subtree split --prefix app/dist master`:gh-pages --force
git reset --mixed HEAD~1
gcloud app deploy