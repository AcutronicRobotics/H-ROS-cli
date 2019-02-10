import logging
from argparse import ArgumentParser
import argcomplete
import nmap
import netifaces
import requests
import json

def main(args=None):
    logger = logging.getLogger(__name__)
    parser = ArgumentParser(description='hros')

    subparsers = parser.add_subparsers(help='commands')

    # A list command
    component_parser = subparsers.add_parser(
        'module', help='Get and Set module related data')
    component_parser.set_defaults(action='list')

    subparsers2 = component_parser.add_subparsers(help='commands')

    component_subparsers_parser = subparsers2.add_parser(
        'list', help='Print a list of modules available')


    component_subparsers_parser_info = subparsers2.add_parser(
        'info', help='Print information of selected module')

    component_subparsers_parser_info.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )
    component_subparsers_parser_info.set_defaults(action='moduleInfo')

    component_subparsers_parser_start = subparsers2.add_parser(
        'start', help='Start the build-in lifecycle service')
    component_subparsers_parser_start.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )
    component_subparsers_parser_start.set_defaults(action='moduleStart')

    component_subparsers_parser_stop = subparsers2.add_parser(
        'stop', help='Stop the build-in lifecycle service')
    component_subparsers_parser_stop.set_defaults(action='moduleStop')

    component_subparsers_parser_stop.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )

    component_subparsers_parser_reset = subparsers2.add_parser(
        'reset', help='Set default configuration for module')
    component_subparsers_parser_reset.set_defaults(action='moduleReset')

    component_subparsers_parser_reset.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )

    # A create command
    configure_parser = subparsers.add_parser(
        'configure', help='Get and Set module specific configuration data')
    configure_parser.set_defaults(action='configure')

    subparsers3 = configure_parser.add_subparsers(help='commands')
    component_subparsers_parser_rmw = subparsers3.add_parser(
        'rmw_implementation', help='Get or Set rmw_implementation')

    component_subparsers_parser_rmw.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',

    )

    # TODO: get choices from SoM
    component_subparsers_parser_rmw.add_argument(
        '--set',
        help='Desired new RMW_IMPLEMENTATION',
        choices=('rmw_opensplice_cpp', 'rmw_fastrtps_cpp')
    )
    component_subparsers_parser_rmw.set_defaults(action='configureRmw')

    component_subparsers_parser_domain = subparsers3.add_parser(
        'ros_domain_id', help='Get or Set ros_domain_id')
    component_subparsers_parser_domain.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )
    component_subparsers_parser_domain.add_argument(
        '--set',
        help='Desired new ROS_DOMAIN_ID',
        type=int,
    )
    component_subparsers_parser_domain.set_defaults(action='configureDomain')

    component_subparsers_parser_type = subparsers3.add_parser(
        'type', help='Get or Set the type of module this SoM can act as')
    component_subparsers_parser_type.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )
    component_subparsers_parser_type.add_argument(
        '--set',
        help='mnbnmSet permissions to prevent writing to the directory',
        type=str
    )
    component_subparsers_parser_type.set_defaults(action='configureType')

    component_subparsers_parser_zero = subparsers3.add_parser(
        'zero', help='Set the actual servomotor position as zero')
    component_subparsers_parser_zero.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )
    component_subparsers_parser_zero.add_argument(
        '--set',
        help='Set to true to store actual position as zero',
        type=str
    )
    component_subparsers_parser_zero.set_defaults(action='configureZero')

    component_subparsers_security = subparsers3.add_parser(
        'security', help='Security related commands')
    component_subparsers_security.add_argument(
        'targetIp',
        help='The IP where a SoM can be found',
    )
    component_subparsers_security.add_argument(
        '--set',
        help='Set to true to enable security to this H-ROS SoM',
        type=str
    )
    component_subparsers_security.set_defaults(action='configureSecurity')


    args = parser.parse_args()
    try:
        if args.action == "moduleInfo":
            url = "http://" + args.targetIp + ":5012/api/module/info"
            print(requestGet(url))
        elif args.action == "componentReset":
            url = "http://" + args.targetIp + ":5012/api/module/reset"
            print(requestGet(url))
        elif args.action == "moduleStop":
            url = "http://" + args.targetIp + ":5012/api/module/stop"
            print(requestGet(url))
        elif args.action == "configureZero":
            if args.set != None:
                url = "http://" + args.targetIp + ":5012/api/module/zero"
                data = '{"type": "' + str(args.set) + '"}'
                print(requestPost(url, data))
        elif args.action == "moduleStart":
            url = "http://" + args.targetIp + ":5012/api/module/start"
            print(requestGet(url))
        elif args.action == "configureRmw":
            if args.set != None:
                url = "http://"+args.targetIp+":5012/api/ros2/rmw_implementation"
                data = '{"rmw_implementation":"'+args.set+'"}'
                print(requestPost(url, data))
            else:
                url = "http://" + args.targetIp + ":5012/api/ros2/rmw_implementation"
                print(requestGet(url))
        elif args.action == "configureDomain":
            if args.set != None:
                url = "http://" + args.targetIp + ":5012/api/ros2/ros_domain_id"
                data = '{"ros_domain_id": ' + str(args.set) + '}'
                print(requestPost(url, data))

            else:
                url = "http://" + args.targetIp + ":5012/api/ros2/ros_domain_id"
                print(requestGet(url))

        elif args.action == "configureType":
            if args.set != None:
                url = "http://" + args.targetIp + ":5012/api/ros2/type"
                data = '{"type": "' + str(args.set) + '"}'
                print(requestPost(url, data))

            else:
                url = "http://" + args.targetIp + ":5012/api/ros2/type"
                print(requestGet(url))

        elif args.action == "configureSecurity":
            url = "http://" + args.targetIp + ":5012/api/sros2/enable"
            data = '{"type": "' + str(args.set) + '"}'
            print(requestPost(url, data))

    except Exception as e:
        print("No valid parameter...\nUse hros -h for more information")


def check_interfaces():

    print('Select your interface to discover the H-ROS modules:')
    interfaces = netifaces.interfaces()
    nic_array = [ ]
    iterator = 1
    for i in interfaces:
        if i == 'lo' or i == 'lo0':
            continue
        else:
            print(str(iterator) + "- " + i)
            nic_array.append(i)
            iterator += 1

    try:
        nic = int(input('Select one of the list: '))
    except Exception as e:
        print('Not allowed character')
        exit(-1)

    if (nic - 1) < 0 or (nic - 1) > len(nic_array) - 1:
        print('Not a valid interface, please select one of the list')
        exit(1)
    elif netifaces.ifaddresses(nic_array[nic -1 ]).get(netifaces.AF_INET) != None:
        for i in netifaces.ifaddresses(nic_array[nic -1 ]).get(netifaces.AF_INET):
            addr = (i['addr'])
    else:
        print('This interface does not have ip')
    return addr

def hros_module_list(addr):

    nm = nmap.PortScanner()

    nm.scan(hosts='192.168.1.0/24', arguments='-n -p T:5012 --open')

    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    for host, status in hosts_list:
        print(host)

def requestGet(url):
    response = requests.get(url)
    return json.dumps(response.json(), indent=4, sort_keys=True)

def requestPost(url, data):
    response = requests.post(url, data=data, headers={"Content-Type": "application/json"})
    return json.dumps(response.json(), indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
