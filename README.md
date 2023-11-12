# FitZap BLE protocol reverse engineering

## Metadata

- Package name: `com.lairor.fitzap`
- Frida command: `frida -R -f com.lairor.fitzap -l ble.js`
- Logcat: `su -c logcat -s FitZap`
- Target class: `com.lairor.fitzap.activity.MainActivity$3`
- Service UUID: `0000ff01-0000-1000-8000-00805f9b34fb`
- Characteristic UUID: `0000ff02-0000-1000-8000-00805f9b34fb`
- MTU: `247` (or maybe `250`?)

## How to use

Write input to Characteristic below as bytes, get output in notifications.

Recommend to use [eDebugger](https://play.google.com/store/apps/details?id=com.e.debugger), which is available on Google Play store and Chinese app markets.

## Format

### Alarm format

`altimes=10h=14m=12n=02m=0p=07on=1`: shock for 10 times ; shock at 14:12 ; index number is 02 (range from `00` to `04`) ; power is `70%` ; enabled (`1` for enable, `0` for disable) ; `m=0` is unknown yet.

## Commands

### Set time

Input format: `tset={year}{month}{day}{hour}{minute}{second}`

Input example: `tset=20231112140457`

Output: `tset={year}{month}{day}{hour}{minute}{second}`

### Get version

Input: `version=?`

Output: `version=V-0001`

### Get all alarms

Input: `alarm=?`

Output format: `alarm|{alarm_1}|{alarm_2}|...`, where all alarm follows the `Alarm format` below.

Output example: `alarm|altimes=10h=05m=55n=00m=0p=07on=1|altimes=10h=13m=28n=01m=0p=01on=0`

### Add / Edit alarm

Input: `{alarm}`, which follows the `Alarm format` below. If the `index number` exist, replace the existing alarm.

Input example: `altimes=10h=14m=05n=01m=0p=01on=1`

Output format: `{alarm}`

Output example: `altimes=10h=14m=05n=01m=0p=01on=1`

### Start / Stop `Auto zap`

Input: `randomon` / `randomoff`

Output: `random is on` / `random is off`

### Edit parameters for `Auto zap`

Input format: `rantimes={total_zap_count}h=00m={total_minute}p={power}`, where `power` ranges from `01` to `10`.

Input example: `rantimes=15h=00m=05p=01`

Output format: `rantimes={total_zap_count}h=00m={total_minute}p={power}`

Output example: `rantimes=15h=00m=05p=01`

### Single zap

Input format: `light={power}`, where `power` ranges from `01` to `10`.

Input example: `light=03` for a spark of `30%` power.

Output: `light is start`
