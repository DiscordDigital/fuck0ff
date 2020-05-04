# fuck0ff
Possibly the first theme tweak for iOS 13 using a 0-day vulnerability instead of a jailbreak.
## ToDo
- [X] Add template extractor to fuck0ff.sh 
- [X] Add checks to buildfuck.py 
- [X] Add instructions on how to setup iSH to get buildfuck.py to work
- [X] Add example images and description text for this "tweak"
- [X] Implement a Syntax
- [X] Add Documentation on usage
- [X] Credit people who make this possible
- [X] Publish this on github
- [ ] (Optional) Adding matrix for language prefixes
- [ ] (Open) Add a couple themes so one can test without needing to build themes

## About fuck0ff
This project has a stupid name that is fact.\
Other than that it allows theming the iOS dialpad of the phone app.

**Screenshots**:
Screenshot 1                                       |  Screenshot 2
:-------------------------------------------------:|:---------------------------------------------------:
![](https://download.discord.digital/fuck0ff.png)  |  ![](https://download.discord.digital/fuck0ff2.png)

**What is so special about it?**\
Not only does it work without a jailbreak, it also survives restarts.\
It also can't damage the iOS filesystem, because if a file is corrupt or missing,\
then iOS will restore the original files immediately without an error.

**Is this bug fixed?**\
Yes the bug we're using here is **psychicpaper** from Siguza.\
It has been fixed in the latest beta but still can be used all the way up to iOS 13.4.1\
More information on the bug: https://siguza.github.io/psychicpaper/

**How does this work**\
Entitlements allow an app to access more than it should have access to.\
Especially when those are private entitlements.\
There is a bunch of system files that can be modified, but unfortunately not all.\
If more is discovered within the timespan of this bugs lifetime, (probably a couple months till everyone updated)\
then I'll gladly build other projects and link them to this one.

## Themes: (Coming soon)

## Syntax:
buildfuck.py
```
python3 buildfuck.py <image file> <theme name>
```
fuck0ff.sh
```
# Generating template:
./fuck0ff extract-template
# Patching theme to iPhones phone app:
./fuck0ff <theme zip file>
```

### 0 Downloading and installing iSH-Entitled
The official iSH build won't work here as it doesn't contain entitlements.\
You can sideload entitled IPA files using AltStore, check out https://altstore.io \
Download link to iSH-Entitled: http://download.discord.digital/iSH_entitled_download.php \
(I had to make a php file so Safari doesn't append a .zip suffix on iOS downloads.)


### 1 Getting Pillow to work on iSH (For buildfuck.py)
Run following commands inside of iSH (This can take up to 15 minutes or longer on iPhone 11 Pro):

```
apk update
apk upgrade
apk add python3 python3-dev build-base zlib-dev jpeg-dev bash git zip nano
python3 -m pip install --upgrade pip wheel
python3 -m pip install Pillow
```

### 2 Changing profile to setup environment
If you prefer VIM you can use VIM here.\
For starters I recommend nano which we installed in step 1.\
Type following command into iSH:
```
nano /root/.profile
```
Then type in following text:
```
mount -t real -o rw / /mnt
```
Save it [Nano: CTRL(^) + o, then CTRL(^) + x ]\
Then close iSH completely by opening your multitasking view and close iSH by moving it up.\
If you don't know what I mean you can also type `exit` into the iSH console which will reload .profile

### 3 Downloading the fuck0ff files into iSH
Type in following command to clone fuck0ff into iSH:
```
git clone https://github.com/DiscordDigital/fuck0ff
```
You can then move the files out of there into /root/ (default home directory for iSH).\
Then run following to allow execution of fuck0ff.sh
```
chmod +x fuck0ff.sh
```
### 4 Generating template
If you have your phone set to another language than english,\
go to your phones settings and change your language to english.

Then open your phone app and hit Keypad.\
Switch back to iSH and run:
```
./fuck0ff extract-template
```
Now run: 
```
ls template
```
You should see a bunch of image files starting with "en-" in that folder.\
If it is the case you're ready for step 5

### 5 Building a theme
Download a picture file, like that:
```
wget https://download.discord.digital/purple.png
```
Then you can build a theme from it like that:
```
python3 buildfuck.py purple.png purple
```
If you see a purple.zip file with the `ls` command,\
then everything worked fine and you can apply it.

### 6 Applying a theme
If you apply a theme while another one is applied already,\
then it will simply overwrite it.\
Apple purple.zip like that:
```
./fuck0ff.sh purple.zip
```
If you see Done!, then close your phone app from the multitask view.\
Then open it to see the change.

You can modify buildfuck.py to crop the input picture.\
If the picture is too small, then it won't fill the entire keypad area.\
Most phone wallpapers will work.

If you want to use the theme with another language,\
then make sure you generated the template folder while the phone was set to english.\
Then you can change the language back and modify the buildfuck.py\
You will need to change following line:
```
lang = "en"
```
Change it to:
```
lang = "custom"
```
I will later publish a matrix on which languages use a different name than custom.\
You can then rebuild your theme (it will overwrite the zip)\
and you can patch it again using fuck0ff.sh while your phone is set to your prefered language.

### Restoring old UI
Run following to restore the old design:
```
./fuck0ff remove
```
Reopen the phone app and it should be normal now.

**If a picture is shown in either a theme or a screenshot that you own. You can reach out to me to request a removal.**\
Contact: copyright[@]discord.digital

## Credits
**Big thanks** to everyone listed.\
Without them this project wouldn't be possible.
- Siguza (Psychic paper) https://github.com/Siguza
- tbodt (iSH) https://github.com/ish-app/
- rileytestut (AltStore) https://github.com/rileytestut/
- eSko (iSH Entitlements) https://github.com/jankais3r
- Pillow (Python3 image manipulation) https://github.com/python-pillow
