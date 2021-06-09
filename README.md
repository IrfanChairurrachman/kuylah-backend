# KUYLAH BACKEND

<br />
<p align="center">
  <a href="https://github.com/IrfanChairurrachman/kuylah-backend">
    <img src="https://user-images.githubusercontent.com/62320260/121286012-7208cc80-c909-11eb-81b4-a1da0dc0a3f9.png">
  </a>

  <h1 align = "center"> Kuylah: Your Smart Traveling planner! </h1>
  <p align="center">
  itinerary maker application based on android.
  </p>
</p>


<p align="center">
  <a href="https://github.com/gallangsdw/Kuylah-app/releases/tag/1.0.0"><img alt="Platform" src="https://img.shields.io/badge/platform-Android-green.svg"></a>
</p>


# Hello, Traveler! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">
welcome to kuylah! This is an Android-based application that can quickly create an itinerary with machine learning. No need to be confused anymore to think about an itinerary because with Kuylah your itinerary can be made in seconds. now, everyone can travel easily.

# About This Project
Yogyakarta is one of the cities that attracts many traveller and students outside the city, or even tourist from abroad. With their several nicknames, two of them are City of Students and City of Tourist, make this city has many destinations to travel. But, some outsiders are confused to start where they want to go and it takes more time to search one by one. 

5 of our team are students from outside this city, and we find it difficult when we want to travel in Yogyakarta. Some of us are just asking our friends to recommend the places and it can be biased because the preferences might be different.  In order to tackle this problem, we build an app to recommend the user where should they go in Yogyakarta with just a few inputs.

# REPOSITORY
<p align="center">
  <a href="https://github.com/gallangsdw/Kuylah-app"><img alt="Repository" src="https://img.shields.io/badge/Repository-Android-green"></a>
  <a href="https://github.com/IrfanChairurrachman/kuylah-backend"><img alt="Repository" src="https://img.shields.io/badge/Repository-Backend-orange"></a>
</p>

# Tech Stack
<p align="center">
  <a href="https://developer.android.com/studio"><img alt="IDE" src="https://img.shields.io/badge/IDE-Android%20Studio-green"></a>
  <a href="https://code.visualstudio.com/"><img alt="Editor" src="https://img.shields.io/badge/Editor-Visual%20Studio%20Code-blue"></a>
  <a href="https://kotlinlang.org/"><img alt="Android" src=https://img.shields.io/badge/Android-Kotlin-blue></a>
  <a href="https://scikit-learn.org/stable/"><img alt="ML" src=https://img.shields.io/badge/Machine%20Learning-Scikit%20Learn-orange></a>
  <a href="https://www.tensorflow.org/"><img alt="ML" src=https://img.shields.io/badge/Machine%20Learning-Tensorflow-orange></a>
  <a href="https://cloud.google.com/"><img alt="Code" src=https://img.shields.io/badge/Cloud-Google%20Cloud%20Platform-red></a>
</p>

# HOW TO

## Forking Project

- Fork this project (button on top right)

- Clone the new repository from forking this project (your repo)

- Try and change the code on your local machine

## Running the code

- Run `python manage.py runserver` or `python3 manage.py runserver` to run the service in your localhost.

- API url: `http://127.0.0.1:8000/api/`.

- Test the url API to generate itinerary POST method in [Postman](https://www.postman.com/) or [httpie](https://httpie.io/)

- required fields are `title`, `day`, `budget`.

## Get Code Latest Version from Source Repo ([irfanchairurrachman/kuylahbackend](https://github.com/IrfanChairurrachman/kuylah-backend))

- Connect source repo on your local machine by add upstream remote. run this command on your project terminal: `git remote add upstream https://github.com/IrfanChairurrachman/kuylah-backend.git`

- run `git remote -v` to check if upstream added

- to get latest code from source run `git pull upstream main`. Run this command everytime want to get latest version of source code.

## Pull Request to Merge Your Code with Source Code

Simple version with Vscode in this [link](https://www.petanikode.com/git-vscode/)

- Change the code and add features on your local machine.

- Run `git add .` or `git add [changed_file]`. run `git status` to see if your `add` are working.

- To commit your changes, run `git commit -m "your message"`. run `git log` to see if your commit are working.

- Upload your file to github by running `git push origin main`. See your latest update on your github repo.

- Make pull request to source code.

## Running code in VM GCP

- get latest project version by `git pull origin main` or if didn't exist yet, download it by `git clone [git url]`

- go to kuylah/settings.py and change ALLOWED_HOSTS from empty to your VM IP address.

- run `sudo nohup python3 manage.py runserver 0.0.0.0:80` and close the terminal.

- Service will running in the bakcground because `nohup` command.
