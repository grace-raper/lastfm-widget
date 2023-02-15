# Lastfm Widget for GitHub Profile

This widget pulls my top artist for the week off of my lastfm profile & using Github workflows, automatically update my profile readme.

This is a fork of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown). That repo pulls the users's top albums for the week and displayed images of each album cover. In this fork, I modified the code so that I could instead display the names (no images) of my top artists for the week as while as some listening stats. If you're interested, definately go check out the original repo! It's well documented and makes integrating with Last.fm a breeze.
          
## What you'll need
* A README.md file.
* Last.fm API key
  * Fill [this form](https://www.last.fm/api/account/create) to instantly get one. Requires a last.fm account.
* Set up a GitHub Secret called ```LASTFM_API_KEY``` with the value given by last.fm.
* Also set up a ```LASTFM_USER``` GitHub Secret with the user you'll get the weekly charts for.
* Add a ```<!-- lastfm -->``` tag in your README.md file, with two blank lines below it. The album covers will be placed here.

## Instructions
To use this release, add a ```lastfm.yml``` workflow file to the ```.github/workflows``` folder in your repository with the following code:
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
        uses: melipass/lastfm-to-markdown@v1.3.1
        with:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
#         INCLUDE_LINK: true # Optional. Defaults is false. If you want to include the link to the album page, set this to true.
#         IMAGE_COUNT: 6 # Optional. Defaults to 10. Feel free to remove this line if you want.
      - name: commit changes
        continue-on-error: true
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "Updated last.fm's weekly chart" -a

      - name: push changes
        continue-on-error: true
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}\
          branch: main
```

## Example output
#### artists I have on repeat:
<!-- LASTFM-TOP-ARTIST:START -->
1. [Mickey Darling](https://www.last.fm/music/Mickey+Darling) - listened to 20 times this week
2. [Taylor Swift](https://www.last.fm/music/Taylor+Swift) - listened to 17 times this week
3. [Colony House](https://www.last.fm/music/Colony+House) - listened to 10 times this week
4. [YUNGBLUD](https://www.last.fm/music/YUNGBLUD) - listened to 6 times this week
5. [Barns Courtney](https://www.last.fm/music/Barns+Courtney) - listened to 2 times this week
<!-- LASTFM-TOP-ARTIST:STOP -->

#### the song I've hyperfixated on this month:
<!-- LASTFM-TOP-TRACK:START -->
* [Reverse Cowgirl](https://www.last.fm/music/Mickey+Darling/_/Reverse+Cowgirl) - Mickey Darling (7 plays in the last 30 days)
<!-- LASTFM-TOP-TRACK:END -->