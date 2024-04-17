# Offline-Wallet
An offline encrypted wallet saver written in Python！

This program is an offline wallet saver written in Python, for personal use only, designed to protect your encrypted private key from malicious theft. At present, there are many ways to store encrypted private keys, but they are not convenient to use. Most people save them in txt documents, even if they are on your offline USB drive, there is still a possibility of theft when you use them.

Installation dependency:

1. Installing the Python environment
   
  To install Python on Windows:
  
Visit the official Python website to download the latest Python installation program.

Run the downloaded installation program.

Select the "Install Now" option in the installation program, which will install Python to the default directory and add it to the system's PATH environment variable.
After completing the installation, you can enter Python on the command line to verify if Python has been successfully installed.

  To install Python on macOS:
  
MacOS usually comes pre installed with Python 2. x version, but you may want to install Python 3. x. You can use Homebrew or download the installation program from the Python official website to install Python 3. x.
If you choose to use Homebrew, run the following command in the terminal to install.

Python: brew install Python

If you choose to download the installation program from the Python official website, please visit the Python official website to download the latest Python installation program and run it.
After completing the installation, you can enter python3 in the terminal to verify whether Python has been successfully installed.

  To install Python on Linux:
  
Most Linux distributions typically come pre installed with Python, which you can install through the package manager.

Ubuntu/Debian:

  sudo apt update

  sudo apt install python3

CentOS/RHEL:

  sudo yum install python3

Fedora:

  sudo dnf install python3

Arch Linux:

  sudo pacman -S python

After completing the installation, you can enter Python 3 (or Python, depending on system configuration) in the terminal to verify whether Python has been successfully installed.

2、 Installing Cryptography

  pip install cryptography

3、Running

  python wallet.py

If you want to write it as an exe program, the following steps are required:

1. Install pyinstaller
   
  pip install pyinstaller
  
3. Running
 
  pyinstaller --onefile wallet.py

Note: Packaging as exe will generate a virus and requires signature. Otherwise, it will be added to the whitelist.



安装依赖：

1、安装python环境

在 Windows 上安装 Python：

访问 Python 官方网站 下载最新的 Python 安装程序。

运行下载的安装程序。

在安装程序中选择 "Install Now" 选项，这会安装 Python 到默认的目录并将其添加到系统的 PATH 环境变量中。

完成安装后，可以在命令行中输入 python 来验证 Python 是否已成功安装。

在 macOS 上安装 Python： 
  
macOS 通常预装了 Python 2.x 版本，但你可能想要安装 Python 3.x 版本。你可以使用 Homebrew 或者从 Python 官网下载安装程序安装 Python 3.x。
如果你选择使用 Homebrew，在终端中运行以下命令安装。

Python：brew install python

如果你选择从 Python 官网下载安装程序，请访问 Python 官方网站 下载最新的 Python 安装程序并运行它。
完成安装后，可以在终端中输入 python3 来验证 Python 是否已成功安装。

在 Linux 上安装 Python：

大多数 Linux 发行版通常都预装了 Python，你可以通过包管理器安装。

Ubuntu/Debian:

sudo apt update

sudo apt install python3

CentOS/RHEL:

sudo yum install python3

Fedora:

sudo dnf install python3

Arch Linux:

sudo pacman -S python

完成安装后，可以在终端中输入 python3（或者 python，取决于系统配置）来验证 Python 是否已成功安装。

2、安装cryptography

pip install cryptography

3、运行

python wallet.py


如果要写为exe程序需要以下步骤：

1、安装pyinstaller

pip install pyinstaller

2、运行

pyinstaller --onefile wallet.py

备注：打包为exe会报毒，需进行签名，否则将其加入白名单。
