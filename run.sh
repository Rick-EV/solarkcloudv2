#!/usr/bin/with-contenv bashio
set +e
#python3 -m http.server 8000

while :
do
CONFIG_PATH=/data/options.json

solark_user=""
solark_pass=""
solark_serial=""
HA_LongLiveToken=""
Home_Assistant_IP=""

solark_user="$(bashio::config 'solark_user')"
solark_pass="$(bashio::config 'solark_pass')"
solark_serial="$(bashio::config 'solark_serial')"
HA_LongLiveToken="$(bashio::config 'HA_LongLiveToken')"
Home_Assistant_IP="$(bashio::config 'Home_Assistant_IP')"
Home_Assistant_PORT="$(bashio::config 'Home_Assistant_PORT')"
Refresh_rate="$(bashio::config 'Refresh_rate')"
Enable_HTTPS="$(bashio::config 'Enable_HTTPS')"


VarCurrentDate=$(date +%Y-%m-%d)

clear
#python3 -m http.server 8000


python3 /main.py



echo "All Done! Waiting " $Refresh_rate " seconds to rinse and repeat."
sleep $Refresh_rate
done
