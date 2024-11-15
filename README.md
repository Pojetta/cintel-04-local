# cintel-04-local

### Configure Git 
```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

### Verify Installations
```
python3 --version
git --version
git config user.name
git config user.email
```

### Clone From Git
```
git clone https://github.com/Pojetta/cintel-04-local
```

### Virtual Environment
#### Create: 
```
python3 -m venv .venv
```

#### Activate
```
source .venv/bin/activate
```

### Install Packages
```
python3 -m pip install --upgrade pip setuptools
python3 -m pip install --upgrade -r requirements.txt
```

### Git Add, Commit, Push
```
git add .
git commit -m "Your commit message"
git push -u origin main
```

### Run your App Locally
shiny run --reload --launch-browser penguins/app.py

### Prepare your App for Deployment
shiny static-assets remove
shinylive export penguins docs

### Serve the App
python3 -m http.server --directory docs --bind localhost 8008