npm run build
git subtree push --prefix app/dist CaspitaSrl gh-pages --force
gcloud app deploy
