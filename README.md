# **Annoying Discord Bot** (ADB)
## A super obnoxious discord bot.

### 1) **Setup**

Access your discord developer profile via this [link](https://discord.com/developers), and click in the "New Application" button:

![](/home/sandesvitor/Pictures/bot1.png)

Create a .env file 
```shell
$ docker build -t bot-image .
```

### 1) **Build**
```shell
$ docker build -t bot-image .
```

### 2) **Run**
```shell
$ docker run -env-file=.env bot-image .
```
