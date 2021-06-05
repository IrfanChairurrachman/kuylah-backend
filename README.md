# KUYLAH BACKEND

## TIM KUYLAH GOKIL GOKILL WOHOOO

<br />
<p align="center">
  <a href="https://github.com/IrfanChairurrachman/kuylah-backend">
    <img src="inventory/logo-kuylah.png" alt="Logo" width="200" height="200">
  </a>

  <h2 align="center">Kuylah</h2>
</p>

## HOW TO

### Forking Project

- Fork this project (button on top right)

- Clone the new repository from forking this project (your repo)

- Try and change the code on your local machine

### Running the code

- Run `python manage.py runserver` or `python3 manage.py runserver` to run the service in your localhost.

- API url: `http://127.0.0.1:8000/api/`.

- Test the url API to generate itinerary POST method in [Postman](https://www.postman.com/) or [httpie](https://httpie.io/)

- required fields are `title`, `day`, `budget`.

### Get Code Latest Version from Source Repo ([irfanchairurrachman/kuylahbackend](https://github.com/IrfanChairurrachman/kuylah-backend))

- Connect source repo on your local machine by add upstream remote. run this command on your project terminal: `git remote add upstream https://github.com/IrfanChairurrachman/kuylah-backend.git`

- run `git remote -v` to check if upstream added

- to get latest code from source run `git pull upstream main`. Run this command everytime want to get latest version of source code.

### Pull Request to Merge Your Code with Source Code

Simple version with Vscode in this [link](https://www.petanikode.com/git-vscode/)

- Change the code and add features on your local machine.

- Run `git add .` or `git add [changed_file]`. run `git status` to see if your `add` are working.

- To commit your changes, run `git commit -m "your message"`. run `git log` to see if your commit are working.

- Upload your file to github by running `git push origin main`. See your latest update on your github repo.

- Make pull request to source code.

### Running code in VM GCP

- get latest project version by `git pull origin main` or if didn't exist yet, download it by `git clone [git url]`

- go to kuylah/settings.py and change ALLOWED_HOSTS from empty to your VM IP address.

- run `sudo nohup python3 manage.py runserver 0.0.0.0:80` and close the terminal.

- Service will running in the bakcground because `nohup` command.
