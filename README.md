# Last.fm Widget for GitHub Profile

This widget pulls my top artist for the week off of my lastfm profile & using Github workflows, automatically update my profile readme.

This is a fork of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown). That repo pulls the users's top albums for the week and displayed images of each album cover. In this fork, I modified the code so that I could instead display the names (no images) of my top artists for the week as while as some listening stats. If you're interested, definately go check out the original repo! It's well documented and makes integrating with Last.fm a breeze.

## Sample Output: 
#### artists I have on repeat:
<!-- LASTFM-TOP-ARTIST:START -->
1. [Lenny Kravitz](https://www.last.fm/music/Lenny+Kravitz) - listened to 34 times this week
2. [Hanni El Khatib](https://www.last.fm/music/Hanni+El+Khatib) - listened to 32 times this week
3. [Billie Eilish](https://www.last.fm/music/Billie+Eilish) - listened to 25 times this week
4. [Mothé](https://www.last.fm/music/Moth%C3%A9) - listened to 25 times this week
5. [Addison Rae & Cascada](https://www.last.fm/music/Addison+Rae+&+Cascada) - listened to 17 times this week
<!-- LASTFM-TOP-ARTIST:STOP -->

#### the song I've hyperfixated on this month:
<!-- LASTFM-TOP-TRACK:START -->
* [Diet Pepsi / Everytime We Touch (Mixed)](https://www.last.fm/music/Addison+Rae+&+Cascada/_/Diet+Pepsi+%2F+Everytime+We+Touch+(Mixed)) - Addison Rae & Cascada (17 plays in the last 30 days)
<!-- LASTFM-TOP-TRACK:END -->


# Want to Use This Widget? Here's How:

### Setting up your README:
If you don't already have a README.md file for the repo you want to use this widget in, start by creating one. Then, add the following markdown text to your README.md file. 
```
#### artists I have on repeat:
<!-- LASTFM-TOP-ARTIST:START -->
1. 
2. 
3. 
4. 
5. 
<!-- LASTFM-TOP-ARTIST:STOP -->

#### the song I've hyperfixated on this month:
<!-- LASTFM-TOP-TRACK:START -->
* 
<!-- LASTFM-TOP-TRACK:END -->
```
You can modify the headers for the above text, but make sure that the tags remain. Additionally, because of the way that this widget updates the markdown file, the proper space (e.g. 5 spaces for top artist & 1 space for top song) must be added to the markdown file. Your lastfm data will be populated here!

### Get an API key & setup your GitHub Secrets
1. Get a Last.fm API key (you can generate one [here](https://www.last.fm/api/account/create))
2. Set up a GitHub Secret called ```LASTFM_API_KEY``` with the value given by last.fm.
3. add another GitHub Secret, ```LASTFM_USER```, with your last.fm username.

### Create a workflow
Add a ```lastfm.yml``` workflow file to the ```.github/workflows``` folder in your repository with the following code:
```diff
name: lastfm-to-markdown

on:
  schedule:
    - cron: '2 0 * * *'
  workflow_dispatch:

jobs:
  lastfm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: lastfm to markdown
        uses: grace-raper/lastfm-widget@v1.0
        with:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
          ARTIST_COUNT: 5
          SONG_COUNT: 1
      - name: commit changes
        continue-on-error: true
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "updates top artists & top song with latest last.fm data" -a

      - name: push changes
        continue-on-error: true
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}\
          branch: main
```

If all of this was done correctly, you should see your last.fm data populate in your README.md file!
