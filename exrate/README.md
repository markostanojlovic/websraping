### Used tools:

- Python3 - used virt env 
- Selenium - installed in virt env
- PhantomJS - used docker image 

---

`docker run -d -p 8910:8910 wernight/phantomjs phantomjs --webdriver=8910`

```python
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)
```

---

### Instruction how to use:

```bash
#docker conatainer up and running
docker ps -a
curl http://127.0.0.1:8910
cd exrate
. exrate/bin/activate
python3 get_rate.py
# when finished deactivate python virt env
deactivate
```

---


