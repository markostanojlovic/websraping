# bezrealitky.cz scraper

##### Environemnet:
 - CentOS 7 :
   - GNOME Desktop Environment: `sudo yum groups install "GNOME Desktop"`
   - Epel Repo: `sudo yum install epel-release`
   - Additional pkgs: `sudo yum install -y git-core python-pip python-virtualenv`
   - PhantomJS: sudo docker start wernight/phantomjs
     Python PhantomJS usage:
```
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)
```

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
   ```
   wget -P ~/Downloads/ https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
   sudo unzip -d /usr/local/bin/ ~/Downloads/chromedriver_linux64.zip
   ```
   - Python ChromeDriver usage: `driver = webdriver.Chrome('/usr/local/bin/chromedriver')`
