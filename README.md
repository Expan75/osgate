# osgate

osgate is an opionated open source python implmentation of an indsutrial grade IoT gateway; primarily aimed at data collection via sensors in an industrial context Design-wise. The primary opinions are:
1. Export to a local MQTT broker (bridged to a cloud broker) is the one and only way of getting data out. This ensures a cloud-agnostic and durable (via persistant sessions) data export strategy.
2. Configuration is designed with a pull-first strategy. This ensures the burden of truth is placed on some aggregate system rather than individual gateways.
3. Given the point above, no internal Database is used in favour of a single cached config .json file.

# Roadmap

This is just to frame some form of commitment. Note that these are in no particular order.

- [x] Inital Project setup with resource-2-class layout.
- [x] Lock down data sourcing strategy across connectors (two kinds; listener and poller, e.g. mqtt vs. mbus).
- [x] Durable exportService for efficent data export via MQTT cloud bridge.
- [ ] Durable Remote-first configuration with local fallback.
- [ ] Basic RPC management, including authentication by API key.
- [ ] Allow configurable data transformation/filtering on a channel level.
- [ ] MQTT connector (cabable of multiple broker sources)
- [ ] HTTP connector
- [ ] Modbus connector
- [ ] Metric-bus (Mbus) connector
- [ ] ZWAVE connector

# Getting started

### Core External Dependencies

- [Docker](https://www.docker.com/)
- [Python](https://python.org) >= 3.6
- [Mosquitto](https://mosquitto.org/) - Implmentation relies on a locally running MQTT broker (for bridging with a cloud twin).

### Running the server

Assuming all the above dependencies are installed (and path:able), use the following to start:

1. Download via Git
```console
git clone git@github.com:expan75/osgate && cd osgate
```
2. Create virutal environment and install dependencies   
```console
python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
```
3. Run the server in debug mode
```console
python3 ./osgate/main -d
```
6. Alternatively, run tests via pytest
```console
python -m test pytest
```

# Contributing

To contribute, you must first acquint yourself with [this gitbranching model](https://nvie.com/posts/a-successful-git-branching-model). In short, develop contains the latest code changes that have gone through inital code review. The develop branch is what you as a developer will branch off of for new features etc.

For releases, a release branch is used. This release branch is effectively made up by tagged checkouts of develop at various points in time. For a new release, a checkout of develop with a certain tag is used, e.g. "1.0". This release branch is then tested thourougly, lastly merged into master, i.e. the deployment of the release.

### Writing Commits

For your commits, please try to write in imperative form and keep it under 50 characters. If more is needed, e.g. for a briefer explanation, write the first 50 characters and then proceed to add a new line and as many description lines (< 70 characters a line) as you please. For a brief rundown on why this matter, check out [this excellent piece by Chris Beams](https://chris.beams.io/posts/git-commit/).

### Branch Etiquette

As a developer, you do not need to worry to much about the release strategy when developing. What you should worry about is readability and traceability. In order to understand the changes made and features added, it is important to be clear and concise when defining your new branches.

    Bad: git checkout -b login
    Better: git checkout -b feature/authentication

    Bad: git checkout -b bugfix
    Better: git checkout -b bugfix/authentication-timeout

### Code Review

Once you have defined a new branch and committed changes to it that you're happy with, it is time to create a pull request. To do so, use the web UI on GitHub.com for your branch. Remember, you want to merge into DEVELOP. See [guide](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

When you have passed code review, you are advised to squash your commits. This way every new feature will have a single commit which is easy to navigate, and revert if need be!

### Code Style and Type Usage

Regardless if you are getting reviewed or are reviewing, you should comply with the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). Note that any programming paradigm is allowed as long as you comply with the above style guide and your code is understandable.

```console
<insert linting command here>
```
### Continuous Integration and Continuous Deployment

```console
<insert ci/cd here>
```
