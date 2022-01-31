# osgate

Osgate is an opionated open source python implmentation of an IoT gateway; primarily aimed at data collection via sensors in an industrial context. The primary opinions are:
1. Export to a local MQTT broker (bridged to a cloud broker) is the default way of getting data out. This ensures a cloud-agnostic and durable (via persistant sessions) data export strategy.
2. Configuration is designed with a pull-first strategy. This ensures the burden of truth is placed on some aggregate system rather than individual gateways. Note that the gateway can be run using local configuration file as well (e.g., completely deployable without having set up a platform that includes remote configuration)..
3. In a further bid to reduce complexity, no on-board database is used (the configuration is cached though to ensure durability). Similarly, persistance of data is ensured given the usage of a local MQTT broker and persistant sessions.

### Minor note on architecture

The project is inspired by the gateway built by Thingsboard. In short, the main pieces are:
- Device - represents a physical entity in the real world; usually a sensor of some kind.
- Connector - bridge on which data walks to and from a device to the gateway. Facilitates all forms of communication, including commands send to the devices (e.g. mbus).
- Sink - resting place of data sourced from devices through connectors. Connectors use sinks to export and persist data.
- GatewayService - acting as controller of the gateway. Runs a jsonrpc server and delegates inbound rpc calls.

# Roadmap

This is just to frame some form of commitment. Note that these are in no particular order.

- [x] Inital Project setup with resource-2-class layout.
- [x] Lock down data sourcing strategy across connectors (two kinds; listener and poller, e.g. mqtt vs. mbus).
- [x] Durable exportService for efficent data export via MQTT cloud bridge.
- [ ] Durable Remote-first configuration with local fallback.
- [ ] Basic RPC management, including authentication by API key.
- [ ] Auth + SSL for Mqtt Brokers (both connectors and sinks)
- [ ] Allow configurable data transformation/filtering on a channel level.
- [ ] MQTT connector (cabable of multiple broker sources), including customisable topic/message matching.
- [ ] HTTP connector
- [ ] Modbus connector
- [ ] Metric-bus (Mbus) connector
- [ ] ZWAVE connector

# Getting started

### Core External Dependencies

- [Docker](https://www.docker.com/)
- [Python](https://python.org) >= 3.10
- [Mosquitto](https://mosquitto.org/) - Implmentation relies on a locally running MQTT broker (for bridging with a cloud twin).

### Running the server

This part of guide assumes you the above dependencies are installed and in your path. Note that it is possible to run the gateway without having set up any cloud bridging (this should be done before any deployment). To get started: 

1. Download via Git
    ```console
    git clone git@github.com:expan75/osgate && cd osgate
    ```
2. Create virutal environment and install dependencies   
    ```console
    python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
    ```
3. Start local MQTT broker (mosquitto)
    ```console
    # Note you may need to change the path here depending on your OS
    bash /usr/local/opt/mosquitto/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
    ```
4. Copy example configuration
    ```console
    cp ./examples/osgate.json osgate.json
    ```
5. Run the server in debug mode
    ```console
    python3 ./osgate/main -d
    ```
6. Alternatively, run tests via pytest
    ```console
    python -m test pytest
    ```

7. Alternatively, listen to the export topic(s) using mosquitto_sub to see exported data:
    ```console
    mosquitto_sub -h localhost -p 1883 -t telemetry/# -v
    ```
# Contributing

To contribute, you must first aquaint yourself with [this gitbranching model](https://nvie.com/posts/a-successful-git-branching-model). In short, develop contains the latest code changes that have gone through inital code review. The develop branch is what you as a developer will branch off of for new features etc.

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

Regardless if you are getting reviewed or are reviewing, you should comply with the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). Note that any programming paradigm is allowed as long as you comply with the above style guide and your code is understandable. In addition to the style guide, this project relies on [Black](https://github.com/psf/black) for automatic linting and code style.
```console
pip install black
black ./osgate
```

### Exceptions to whats covered in styling

Black does not yet cover all of python3.10 syntax, so if something is not detected correctly, you can always flag it:

```python
    # fmt: off
    match protocol:
        case "default":
            return DefaultConnector(name, uuid, devices, sinks, connector_metadata)
        case "mqtt":
            return MqttConnector(name, uuid, devices, sinks, connector_metadata)
        case _:
            raise NotImplementedError(
                f"No connector of protocol {protocol} exists! Perhaps there's a typo in the config."
            )
    # fmt: on
```
### Continuous Integration and Continuous Deployment
Insert brief explanation of CI/CD pipeline here.
```console
<insert ci/cd here>
```
