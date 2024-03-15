# KVRNotfallTermin Monitor

This Python script monitors the availability of [Emergency Appointments at KVR](https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_abh.html?cts=1000113). The users still need to make the appointment by themselves.

The program will beep, print, and save the time stamp when an appointment is available.

With time stamps logged in the file `log.txt`, one can plot the history time distribution of appointment availability.

## Features

- Support Windows, MacOS, and Linux
- Keep monitoring and logging unless terminated
- Prevent the OS from sleep

## Installation

```shell
pip install -r requirements.txt
```

## Start Monitoring

```shell
python main.py
```

The program start with a sound test, during which you could adjust the volume of your device.

## Visualization

Plot the history time distribution of appointment availability:

```shell
python plot.py
```

## Acknowledgment

Modified from [KVRNotfallTermin](https://github.com/troywei123/KVRNotfalltermin).

OCR provided by [ddddocr](https://github.com/sml2h3/ddddocr).
