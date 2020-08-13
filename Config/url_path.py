from Until.handle_ini import handle_init

online_url = handle_init.get_inivalue('online_host', 'server')
test_url = handle_init.get_inivalue('test_host', 'server')
getAwardDesc_url = online_url + '/guaGuaActivity/getAwardDesc'
getRondaData_url = online_url + '/guaGuaActivity/getRondaData'
getSwitchInfoList_url = online_url + '/switcherNew/v3/getSwitchInfoList'
getAwardMsg_url = online_url + '/guaGuaActivity/getAwardMsg'
areaOneOperation_url = online_url + '/guaGuaActivity/areaOneOperation'
areaTwoOperation_url = online_url + '/guaGuaActivity/areaTwoOperation'
