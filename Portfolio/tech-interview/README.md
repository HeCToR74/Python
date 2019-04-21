# Tech Interview

```
python -m pip install --upgrade pip

pip install virtualenv

virtualenv venv

venv\Scripts\activate.bat  # for Windows
source venv/bin/activate  # for UNIX

pip install -r requirements.txt
```

# UI piece
### For installing new npm packages in terminal and run WebPack you should be in the directory where `package.json` is located (folder with your project) and type:

```
sudo apt install nvm # for ubuntu
brew install nvm # for mac
install node.js from official site # for windows

nvm install --lts
npm install
```

### Run WebPack
Go to the folder with `package.json` file 
(folder with your project)
* For add AWS:S3 credential
```
Create file .env
add credential in this file
```
* For build
```
npm run build
```
* For watch
```
npm start
```

### Run UI tests:
Following command runs all tests in `static/test` 
```
npm test
```