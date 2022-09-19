# last.fm to markdown

![banner](banner.png)

## 🤖 About this repo
This is a small project that I started because I wanted to have my last.fm weekly chart on my GitHub profile. I used GitHub Actions because they can be scheduled with cron jobs and you won't need to pass any sensitive information to modify the README.md file.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><a href="https://www.last.fm/music/Inti-Illimani/Imaginacion"><img src="https://lastfm.freetls.fastly.net/i/u/64s/511524241b42421f9be12d52dd1d2028.jpg" title="Inti-Illimani - Imaginacion"></a> <a href="https://www.last.fm/music/The+Clash/London+Calling"><img src="https://lastfm.freetls.fastly.net/i/u/64s/680af088e127e474fc536a5cfad36f3e.jpg" title="The Clash - London Calling"></a> <a href="https://www.last.fm/music/Avril+Lavigne/Under+My+Skin"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a0beb5604cbf4731ae6856863b82761a.png" title="Avril Lavigne - Under My Skin"></a> <a href="https://www.last.fm/music/Avril+Lavigne/Let+Go"><img src="https://lastfm.freetls.fastly.net/i/u/64s/5196120dec2446b840ca061ed819f300.jpg" title="Avril Lavigne - Let Go"></a> <a href="https://www.last.fm/music/Avril+Lavigne/The+Best+Damn+Thing"><img src="https://lastfm.freetls.fastly.net/i/u/64s/ce5eeeedb09bcf65b70a6406340a03af.jpg" title="Avril Lavigne - The Best Damn Thing"></a> <a href="https://www.last.fm/music/Iglooghost/Chinese+N%C3%BC+Yr+(EP)"><img src="https://lastfm.freetls.fastly.net/i/u/64s/081251568b04662ccb58f134de0d0cbc.jpg" title="Iglooghost - Chinese Nü Yr (EP)"></a> <a href="https://www.last.fm/music/Inti-Illimani/Inti-Illimani"><img src="https://lastfm.freetls.fastly.net/i/u/64s/d9f03fc864e26e83746cfdf0b53d1a5b.jpg" title="Inti-Illimani - Inti-Illimani"></a> <a href="https://www.last.fm/music/The+Herbaliser/Something+Wicked+This+Way+Comes"><img src="https://lastfm.freetls.fastly.net/i/u/64s/a543dd4fd89e42d4c22f067325ff742e.jpg" title="The Herbaliser - Something Wicked This Way Comes"></a> </p>

          
## 👩🏽‍💻 What you'll need
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
The cron job is scheduled to run once a day because Last.fm's API updates weekly chart data daily at 00:00, it's useless to make more than 1 request per day because you'll get the same information back every time. You can manually run the workflow in case Last.fm's API was down at the time, going to the Actions tab in your repository.

## 🚧 To do
* Allow users to choose the image size for the album covers.
* Feel free to open an issue or send a pull request for anything you believe would be useful.
