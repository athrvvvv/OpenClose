## OpenClose 📖📕

An application to open and close apps in windows using python packages such as **AppOpener, Os, Sys**. 

⚠️ OpenClose is only functional on windows 🪟

---

> ### Building Application 🔨 and Quick Start ⚡

``` sh
git clone https://github.com/athrvvvv/OpenClose.git
cd OpenClose
pip install -r requirements.txt
pyinstaller pyinstaller --name OpenClose --hidden-import 'AppOpener' --onefile --icon=icon.ico 'main.py'
```
After the above steps, you may find the application in `dist` folder ✅

---

> ### Understand Application ☝️😎

1. N = Neutrat: One can Open or Close applications simultaneously 📝
2. O = Open: One can only open applications 📖
3. C = Close: One can only close applications 📕

We call these things as status, one can always change the status by using `set N/O/C` in the application 🤝❤️