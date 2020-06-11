# Mr. Robot: WebEx Teams Chatbot

This is an example of bulding a Webex Teams chatbot in python.

## Development Ideas

This project uses [webexteamsbot](https://github.com/hpreston/webexteamsbot) as it's base.

## Environment variables

The following environment variables need to be set to use this:

* `TEAMS_BOT_TOKEN`
* `TEAMS_BOT_EMAIL`
* `TEAMS_BOT_APP_NAME`
* `TEAMS_BOT_URL`

The webexteamsbot python repo has instructions for where to get these.

## ngrok

You can use ngrok to test this out, run it as follows:

```
$ ngrok http 5000
```

The output of the URL should be used to set the environment varable `TEAMS_BOT_URL`.