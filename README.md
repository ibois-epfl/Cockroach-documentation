# 11:37 10/09/2021 : Instructions and notes, Cockroach Docu Alpha

This is just a barebone website, it needs to be first filled with documentation of Cockroach C++ version. Github repo needs to be structured with CMake.

---

## Install Jekyll on win machine locally

Clone the repo. And install Jekyll/Ruby for win, follow the link [here](https://jekyllrb.com/docs/installation/windows/). More documentation on Jekylls [here](https://www.youtube.com/watch?v=EvYs1idcGnM&list=PLWzwUIYZpnJuT0sH4BN56P5oWTdHJiTNq&index=1)

## Use Jekyll on win machine

Go to the documentation directory.

If you are using the ruby gems v 3.0.0 the 'webrick' doesn't ship with. You need to add it manually after the wizard ruby installation is finished:

```console
$ bundle add webrick
```

Open the project on VSCode and open a new cmd which points to the local directory of the cloned repo. If you are on IBOIS server you have to type this cmd:

```console
$ pushd \\enac1files\IBOIS\name-folder
```

Once Jekyll is installed and the VSCode project is ready you can run Jekyll locally. Note that to make the changes effective they need to be pushed to the GitHub repo on-line.

```console
$ bundle exec jekyll serve --trace
```

### Troubleshooting
Cockroach docs run on the `2.3.4` version of bundle. If you recive an error that the bundle do not correspond force the install bundle by running this in the console:
```console
gem install bundler:2.1.4
bundle _2.1.4_ install
```


---

## Things to add:
- C++ GitHub code repo of Cockroach
- C++ Cockroach docu
- Google analytics embedded to track viewrs and documentations which is most useful
- Custome made DNS domain (www.Cockroach.com)

## Tutorials
- [Jekyll tutorial](https://www.youtube.com/watch?v=EvYs1idcGnM&list=PLWzwUIYZpnJuT0sH4BN56P5oWTdHJiTNq&index=1)
