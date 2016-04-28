# slackmsg
Send messages to Slack as a bot right from command line

## As a command line
Options:

* -u: username
* -i: icon
* -c: target channel
* -h: webhook URL
* -t: text to send

```
slackmsg.py -u 'slackbot' -i ':slack:' -c '#random' -t 'hello' -h 'https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxx'
```

## As a python module
```
import slackmsg

SM = slackmsg.SlackMsg('https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxx',
                       '#random', 'slackbot', ':slack:')
SM.send('hello')
```
