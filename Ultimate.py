#Wellcome to Hacker Min

name: CI

# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:pkg update
pkg upgrade
pkg install python
pkg install python2
pip install requests
pip2 install mechanize
pip install requests
pkg install git
    # The type of runner that the job will run on
    runs-on: cd HackerIMA

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: git clone https://github.com/HackerIMA/HackerIMA.git

      # Runs a single command using the runners shell
      - name: cd HackerIMA
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: python2 Ultimate.py
        run: python2 Ultimate.py
          echo Add other actions to build,
          echo test, and deploy your project.
