import time
from netmiko import ConnectHandler
import re


#Port
def port_config(port, state):
    cmd = 'port edit '+ port +' state ' + state
    print('Executing command:    ' + cmd)
    ssh.send_config_set(cmd)

def port_getstate(port):
    port = ssh.send_command('port show status ' + port)
    print(port)
    port_state = re.findall("State.{8}", port)[0]
    port_state = re.sub('State     : ','',port_state)
    if port_state == 'D':
        port_state = 'Disabled'
    else:
        port_state = 'Enabled'
    return port_state

def port_get_statistics_tx_packet(port):
    all_port_statistic = ssh.send_command('port show statistics ')
    port_statistic_tx_pkg = re.findall(port+'.{45}',all_port_statistic)
    port_statistic_tx_pkg = port_statistic_tx_pkg[0][10:]
    return int(re.sub(',', '', port_statistic_tx_pkg).strip())

def port_get_statistics_rx_packet(port):
    all_port_statistic = ssh.send_command('port show statistics ')
    port_statistic_rx_pkg = re.findall(port+'.{76}',all_port_statistic)
    port_statistic_rx_pkg = port_statistic_rx_pkg[0][60:]
    return int(re.sub(',', '', port_statistic_rx_pkg).strip())

def port_get_statistic(port):
    port_statistic = ssh.send_command('port show statistics '+ port)
    print(port_statistic)
    return port_statistic

def port_get_statistics_all_port():
    all_port_statistic = ssh.send_command('port show statistics ')
    print(all_port_statistic)
    return all_port_statistic

def port_reset():

    port_config('PORT-1', state='Enable')
    port_config('PORT-2', state='Enable')
    port_config('PORT-3', state='Enable')
    port_config('PORT-4', state='Enable')
    port_config('PORT-5', state='Enable')
    port_config('PORT-6', state='Enable')
    port_config('PORT-7', state='Enable')
    port_config('PORT-8', state='Enable')
    port_config('PORT-9', state='Enable')
    port_config('PORT-10', state='Enable')
    port_config('PORT-11', state='Enable')
    port_config('PORT-12', state='Enable')


#Filter
def filter_add(filter_name, vlanID):
    cmd= 'filter add l2 '+filter_name+'  vlan1-id '+str(vlanID) +' enable'
    print('Executing command:    ' + cmd)
    filter = ssh.send_config_set(cmd)

def filter_edit(filter_name, vlanID):
    cmd= 'filter edit l2 '+filter_name+'  vlan1-id '+vlanID +' enable'
    print('Executing command:    ' + cmd)
    filter = ssh.send_config_set(cmd)

def filter_delete(filter_name):
    cmd= 'filter delete l2 '+ filter_name
    print('Executing command:    ' + cmd)
    filter = ssh.send_config_set(cmd)

#Policy
def policy_show_configuration(port, index):
    traffic = change_port_to_Traffic(port)
    cmd= 'policy show configuration '+ traffic +' '+ str(index)
    print('Executing command:    ' + cmd)
    policy = ssh.send_config_set(cmd)
    print(policy)
    return policy

def policy_show_statistic(port, index):
    traffic = change_port_to_Traffic(port)
    cmd= 'policy show statistics '+ traffic +' '+ str(index)
    print('Executing command:    ' + cmd)
    policy = ssh.send_config_set(cmd)
    print(policy)
    return policy

def policy_edit(port,index,outport,filter, action, state):
    traffic = change_port_to_Traffic(port)
    index =str(index)
    cmd = 'policy edit ' + traffic + ' ' +index+ ' out-port '+ outport + ' filter l2 ' +filter + ' action '+ action + ' state ' +state
    print('Executing command:    ' + cmd)
    policy = ssh.send_config_set(cmd)


#User

def user_add(user_name):
    cmd = 'user add '+ user_name
    print('Executing command:    ' + cmd)
    ssh.send_config_set(cmd)

def user_permission(user_name, permission):
    cmd = 'user permissions edit ' + user_name + ' add-group ' + permission
    print('Executing command:    ' + cmd)
    ssh.send_config_set(cmd)

def user_edit(user_name, email):
    cmd = 'user edit ' + user_name + ' email ' + email
    print('Executing command:    ' + cmd)
    ssh.send_config_set(cmd)

def user_delete(user_name):
    cmd = 'user delete ' + user_name
    print('Executing command:    ' + cmd)
    ssh.send_config_set(cmd)

#interface

def interface_add(interface_name, IPaddress):
    pass

def interface_edit(interface_name, IPaddress):
    pass

def interface_delete(interface_name):
    pass



#TOOL
def add_result(testcase_name, result):
    name_len = len(testcase_name)
    max_len = 50
    space_len = max_len - name_len
    space = ''
    for i in range(space_len):
        space += ' '
    return '\t'+testcase_name + space + result + '\n'

def info_testcase_executing(testcase_name):
    print('-------------------------------------------------------------------')
    print('\t\tExecuting Testcase: '+ testcase_name)
    print('-------------------------------------------------------------------')

def info_testcase_result(testcase_name, result):
    name_len = len(testcase_name)
    max_len = 100
    space = max_len - name_len
    print('-------------------------------------------------------------------')
    print('\t\t' +testcase_name + '\t\t'+ result)
    print('-------------------------------------------------------------------')

def change_port_to_Traffic(port):
    return re.sub('PORT','Traffic',port)


# Test case

#Port test
def test_disable_one_port():
    # This testcase will Disable PORT-3 of device
    testcase_name = 'Test_disable_one_port'
    result= ''

    info_testcase_executing(testcase_name)

    port_under_test = 'PORT-3'
    port_config(port_under_test, state='Disable')

    print(ssh.send_command('port show status'))

    port_under_test_state = port_getstate(port_under_test)

    if port_under_test_state == 'Disabled':
        result= 'PASSED'
    else:
        result= 'FAILED'

    info_testcase_result(testcase_name,result)
    port_reset()
    return add_result(testcase_name,result)

def test_disable_all_port():
    # This testcase will Disable all PORT of device
    testcase_name = 'Test_disable_all_port'
    result= ''

    info_testcase_executing(testcase_name)
    port_reset()
    for i in lport:
        port_config(i, state='Disable')

    print(ssh.send_command('port show status'))
    port_under_test = lport
    port_under_test_state = []
    for i in range(len(port_under_test)):
        port_under_test_state.append(port_getstate(port_under_test[i]))
        if port_under_test_state[i] =="Disabled":
            pass
        else:
            print('State of PORT-'+ str(i+1) + ' is '+ port_under_test_state[i] )
            result='FAILED'

            info_testcase_result(testcase_name,result)

            return add_result(testcase_name,result)

    result = 'PASSED'

    info_testcase_result(testcase_name,result)
    port_reset()
    return add_result(testcase_name,result)

def test_enable_one_port():
    # This testcase will Enable PORT-5 of device
    testcase_name = 'Test_enable_one_port'
    result= ''

    info_testcase_executing(testcase_name)

    port_under_test = 'PORT-5'
    port_config(port_under_test, state='enable')

    print(ssh.send_command('port show status'))

    port_under_test_state = port_getstate(port_under_test)

    if port_under_test_state == 'Enabled':
        result= 'PASSED'
    else:
        result= 'FAILED'

    info_testcase_result(testcase_name,result)
    port_reset()
    return add_result(testcase_name,result)

def test_enable_all_port():
    # This testcase will Enable all PORT of device
    testcase_name = 'Test_enable_all_port'
    result= ''

    info_testcase_executing(testcase_name)
    port_reset()
    for i in lport:
        port_config(i, state='Ensable')

    print(ssh.send_command('port show status'))
    port_under_test = lport
    port_under_test_state = []
    for i in range(len(port_under_test)):
        port_under_test_state.append(port_getstate(port_under_test[i]))
        if port_under_test_state[i] =="Enabled":
            pass
        else:
            print('State of PORT-'+ str(i+1) + ' is '+ port_under_test_state[i] )
            result='FAILED'

            info_testcase_result(testcase_name,result)

            return add_result(testcase_name,result)

    result = 'PASSED'

    info_testcase_result(testcase_name,result)
    port_reset()
    return add_result(testcase_name,result)

def test_show_port_statistic():
     # This testcase will show statistics PORT-5 of device (More detail)
     testcase_name = 'test_show_port_statistics'
     result = ''
     port_under_test= 'PORT-5'
     info_testcase_executing(testcase_name)
     if port_get_statistic(port_under_test) != None:
         result= 'PASSED'
     else:
         result = 'FAILED'
     info_testcase_result(testcase_name,result)
     return add_result(testcase_name,result)

def test_show_port_statistics_all_port():
    # This testcase will show statistics all PORT of device (transmitted packets, received packets)
    testcase_name = 'test_show_port_statistics_all_port'
    result = ''
    info_testcase_executing(testcase_name)
    if port_get_statistics_all_port() != None:
        result = 'PASSED'
    else:
        result = 'FAILED'
    info_testcase_result(testcase_name,result)
    return add_result(testcase_name, result)

# Filter test
def test_add_filter():
    # This testcase will add filter with name is FilterVLAN100 and VLAN ID is 100
    testcase_name = 'test_add_filter'
    result = ''
    info_testcase_executing(testcase_name)
    filter_name = 'FilterVLAN100'
    vlan_id = '100'
    filter_add(filter_name,vlan_id)
    filter_list = ssh.send_command('filter show l2')
    print(filter_list)
    check_vlan_id = re.findall(filter_name+'.*---',filter_list)[0][77:83]
    check_vlan_id = check_vlan_id.strip()

    if check_vlan_id == vlan_id:
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name,result)
    return add_result(testcase_name,result)

def test_edit_filter():
    # This testcase will edit filter with name is FilterVLAN100 and VLAN ID from 100 to 200
    testcase_name = 'test_edit_filter'
    result = ''
    info_testcase_executing(testcase_name)
    filter_name = 'FilterVLAN100'
    vlan_id = '200'
    filter_edit(filter_name,vlan_id)
    filter_list = ssh.send_command('filter show l2')
    print(filter_list)
    check_vlan_id = re.findall(filter_name+'.*---',filter_list)[0][77:83]
    check_vlan_id = check_vlan_id.strip()

    if check_vlan_id == vlan_id:
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name,result)
    return add_result(testcase_name,result)

def test_delete_filter():
    # This testcase will delete filter with name is FilterVLAN100
    testcase_name = 'test_detete_filter'
    result = ''
    info_testcase_executing(testcase_name)
    filter_name = 'FilterVLAN100'
    filter_delete(filter_name)
    filter_list = ssh.send_command('filter show l2')
    print(filter_list)

    if re.findall(filter_name,filter_list) == []:
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

# policy test

def test_policy_show_configuration():
    # This testcase will show policy configuration on PORT-10 index is 10
    testcase_name = 'test_policy_show_configuration'
    result = ''
    info_testcase_executing(testcase_name)

    port_under_test = 'PORT-10'
    traffic_under_test = change_port_to_Traffic(port_under_test)
    index = 10
    if re.findall(traffic_under_test,policy_show_configuration(port_under_test,index)):
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

def test_policy_show_statistic():
    # This testcase will show policy statistics on PORT-3 index is 1
    testcase_name = 'test_policy_show_statistic'
    result = ''
    info_testcase_executing(testcase_name)

    port_under_test = 'PORT-3'
    traffic_under_test = change_port_to_Traffic(port_under_test)
    index = 1
    if re.findall(traffic_under_test,policy_show_statistic(port_under_test,index)):
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

def test_policy_edit():
    # This testcase will add policy with configuation: inPort 1, policy index: 5, outPort 8, filter FilterVlan100, action permit, state enable
    testcase_name = 'test_policy_add'
    result = ''
    info_testcase_executing(testcase_name)
    port_under_test = 'PORT-1'
    traffic_under_test = change_port_to_Traffic(port_under_test)
    index= 5
    out_port = 'PORT-8'
    filter_name = 'FilterVlan100'
    vlan_id = 100
    filter= filter_add(filter_name,vlan_id)
    action = 'Permit'
    state = 'Enable'

    policy_edit(port_under_test,index, out_port, filter_name, action,  state)
    policy = policy_show_configuration(port_under_test, index)
    if re.findall(port_under_test,policy)[0] == port_under_test and \
            re.findall('Policy..',policy)[0][7:] == str(index) and \
            re.findall('Out-port.{18}',policy)[0][20:] == out_port and \
            re.findall('Filter name.{22}',policy)[0][20:] == filter_name and \
            re.findall('Action.{20}',policy)[0][20:] == action and \
            re.findall('State.{22}', policy)[0][20:] == state+'d':
        result  = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)


# User test
def test_user_add():
    # This testcase will add User with name is user1
    testcase_name = 'test_user_add'
    result = ''
    info_testcase_executing(testcase_name)
    user_name = 'user1'
    user_add(user_name)

    user_list = ssh.send_command('user show')
    print(user_list)

    if re.findall(user_name,user_list):
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

def test_user_permission():
    # This testcase will update permission for User with name is user1 and Admin permission
    testcase_name = 'test_user_permission'
    result = ''
    info_testcase_executing(testcase_name)
    user_name = 'user1'
    permission = 'Admin'
    user_permission(user_name, permission)

    user_permission_detail = ssh.send_command('user permissions show ' + user_name)
    print(user_permission_detail)

    if re.findall(permission,user_permission_detail):
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

def test_user_edit():
    # This testcase will update email for User with name is user1 and email is abc@gmail.com
    testcase_name = 'test_user_edit'
    result = ''
    info_testcase_executing(testcase_name)
    user_name = 'user1'
    email = 'abc@gmail.com'
    user_edit(user_name, email)

    user_detail = ssh.send_command('user show ' + user_name)
    print(user_detail)

    if re.findall(email,user_detail):
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

def test_user_delete():
    # This testcase will delete User with name is user1
    testcase_name = 'test_user_delete'
    result = ''
    info_testcase_executing(testcase_name)
    user_name = 'user1'

    user_delete(user_name)

    user_detail = ssh.send_command('user show')
    print(user_detail)

    if re.findall(user_name,user_detail) == []:
        result = 'PASSED'
    else:
        result = 'FAILED'

    info_testcase_result(testcase_name, result)
    return add_result(testcase_name, result)

Clipper_LT = {
    "device_type": "accedian",
    "host": '10.232.100.121',
    "username": 'admin',
    "password": 'admin',
    "verbose": True,
}

lport = ['PORT-1', 'PORT-2', 'PORT-3', 'PORT-4',
         'PORT-5', 'PORT-6', 'PORT-7', 'PORT-8',
         'PORT-9', 'PORT-10', 'PORT-11','PORT-12']

final_result = ''



ssh = ConnectHandler(**Clipper_LT)
print('\n-------------------------------------------\n')
print(ssh.send_command('board show info'))

final_result += test_disable_one_port()
final_result += test_disable_all_port()
final_result += test_enable_one_port()
final_result += test_enable_all_port()
final_result += test_show_port_statistics_all_port()
final_result += test_show_port_statistic()

final_result += test_add_filter()
final_result += test_edit_filter()
final_result += test_delete_filter()

final_result += test_policy_show_configuration()
final_result += test_policy_edit()
final_result += test_policy_show_statistic()

final_result += test_user_add()
final_result += test_user_permission()
final_result += test_user_edit()
final_result += test_user_delete()

# p5= port_get_statistics_tx_packet('PORT-5')



print('\n \n \nTest Result!!!')
print('==================================================================')
print(final_result)

