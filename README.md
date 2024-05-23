# Skånetrafiken DirectLogin

A script that will login to Skånetrafiken WiFi without needing to access their login portal. The portal is really slow and 50% of the time it does not show up.

## Installation

Clone this repo.

```bash
git clone https://www.github.com/lukaspalm/Skanetrafiken-Directlogin.git
```

Change directory to Skanetrafiken-DirectLogin and install requirements

```bash
cd Skanetrafiken-DirectLogin
python -m pip install -r requirements.txt
```

## Usage
Firstly you need to connect to a WiFi called *Skånetrafiken*. When connecting, the message "an action is needed", "you need to login" or something similar is displayed. When this shows up you run the script inside of the *Skånetrafiken-Directlogin/*  folder.  

Run the script when inside of the folder like this:


```bash
python login.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
  
If you find a bug or the script does not work, please open an issue or contact me on discord (username "lukaspalm").

## License

[MIT](https://choosealicense.com/licenses/mit/)
