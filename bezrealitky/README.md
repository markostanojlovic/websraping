# bezrealitky.cz scraper

##### Environemnet:
 - CentOS 7 :
   - GNOME Desktop Environment: `sudo yum groups install "GNOME Desktop"`
   - Epel Repo: `sudo yum install epel-release`
   - Additional pkgs: `sudo yum install -y git-core python-pip python-virtualenv`
   - Chrome browser: 
```
echo "[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
" > /etc/yum.repos.d/google-chrome.repo
yum install -y google-chrome-stable
```
 - Python :
   - Install Selenium: `sudo pip install selenium`
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) - Webdriver for Chrome : 
 
