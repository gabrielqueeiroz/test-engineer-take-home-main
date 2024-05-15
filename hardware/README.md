# Embedded Systems Automation Testing Take-Home

## How to execute

- **Manually execution** <br>On the terminal, insert the command:
``` python -m unittest TestMockDAQDevice ```. The results shall appear after the run
- **CI execution** <br>Perform a push or a pull request and check on Actions tab. The results shall appear in there.

## General information
- **Work directory** <br> It's important to be on hardware directory before executing the tests
- **Test intepretation** <br> It should show three dots, one for each runned test on terminal. If any fails, the details will be displayed on the terminal/log.