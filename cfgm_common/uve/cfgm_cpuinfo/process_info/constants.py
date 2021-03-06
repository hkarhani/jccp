#
# Autogenerated by Sandesh Compiler (1.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
# Copyright (c) 2013 Juniper Networks, Inc. All rights reserved.
#

from pysandesh.Thrift import TType, TMessageType, TException
from ttypes import *

ConnectionTypeNames = {
    0 : "Test",
    1 : "IFMap",
    2 : "XMPP",
    3 : "Collector",
    4 : "Database",
    5 : "Redis",
    6 : "Zookeeper",
    7 : "Discovery",
    8 : "ApiServer",
    9 : "ToR",
}
ConnectionStatusNames = {
    0 : "Initializing",
    1 : "Down",
    2 : "Up",
}
ProcessStateNames = {
    0 : "Functional",
    1 : "Non-Functional",
}
