# LittleBit's Fediverse Handler

This tool will allow you to type "fedi:/@username@domain" into your browser's address bar to open a social media profile. 

This was originally intended to work with Fediverse profiles, like @littlebit670@mastodon.social, but through testing it also works with other platforms.

# Examples of handles

You can open any profile that would fit into the handle format of @username@example.com, such as Mastodon, YouTube, Twitter, TikTok, Meta Threads, and many others.

Some examples of handles (for my profiles): @littlebit670@mastodon.social, @littlebit670@twitter.com, @littlebit943@tiktok.com, @littlebit672@threads.net.

# How to install
Installing the script is quite simple.

## Modify the .reg file
There is a Windows Registry file called `FediverseOpener.reg` in the repository. The file should look like this:

```reg
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\fedi]
@="URL:LittleBit Fediverse Handler"
"URL Protocol"=""
[HKEY_CLASSES_ROOT\fedi\shell]
[HKEY_CLASSES_ROOT\fedi\shell\open]
[HKEY_CLASSES_ROOT\fedi\shell\open\command]
@="\"C:\\Users\\<YOUR USERNAME>\\AppData\\Local\\Programs\\Python\\Python310\\python.exe\" \"C:\\Users\\<YOUR USERNAME>\\.littlebitstudios\\FediNameOpener.py\" \"%1\""

; Replace <YOUR USERNAME> with your username.
; Your username is usually the first 5 letters of your email address if you set up the PC using a Microsoft Account.
```

Open this file in VS Code or Notepad and replace the spots that say `<YOUR USERNAME>` with your Windows user folder name.
If you set up a PC using a Microsoft Account, this is usually the first 5 letters of your email address. All of the user folders on your system should be in `C:\Users\`.

## Install Python
This tool is a Python script. You will need to install Python.

On most modern versions of Windows, you can install Python with `winget`:
```pwsh
winget install python
```

Depending on the version of Python, you may need to modify the .reg file with the correct directory for the Python interpreter.

## Move the Python file
Create a folder in your user folder called `.littlebitstudios`. You may need to enable hidden files in Windows File Explorer. Move `FediNameOpener.py` to this folder.

## Commit the registry entries
***WARNING: Make sure you edited the .reg file in the first step! Committing bad registry entries may cause problems for your PC!***

Double-click `FediverseOpener.reg` in File Explorer and accept the UAC prompt. Accept the prompt from Registry Editor to commit the registry entries to your system.

# Usage
Open a web browser and type `fedi:/@username@domain` into the address bar. A message asking you if it's OK to open Python may appear.
Try it with one of your own profiles! I tested it to work with Twitter, YouTube, TikTok, Meta Threads, and Mastodon. 

# Licensing
As with most of my software, this is open-source software licensed with the MIT License.