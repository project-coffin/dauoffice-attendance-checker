## Dau office checker

It makes more comfortable to check attendance with terminal.

### Let's check

If you'd like to use this, take the process.
I'll try to make it more easy to start meantime.

1. install packages

```
pip install -r requirements.txt
```

2. download chromedriver file

```shell
pip install chromedriver
```

compare your chromedriver path with CHROMEDRIVER_PATH in settings.py

3. create profile.py

```python
# configures for user

COMPANY_NAME = 'Company'
NAME = "YourName"
LOGIN_INFO = {
    'ID': 'ID@email.com',
    'PASSWORD': 'password'
}
```

Done!

4. check your attendance

write commands in project folder root-level.

```shell
// check '출근하기'
python main.py in

// check '퇴근하기'
python main.py out
```

### My To-do

- [ ] test it works
- [ ] add chromedriver file in project folder
- [ ] error-handling
- [ ] check local profile
