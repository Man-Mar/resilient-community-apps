# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_grpc_interface"""

from __future__ import print_function
from resilient_circuits.util import *

def codegen_reload_data():
    """Parameters to codegen used to generate the fn_grpc_interface package"""
    reload_params = {"package": u"fn_grpc_interface",
                    "incident_fields": [], 
                    "action_fields": [], 
                    "function_params": [u"grpc_channel", u"grpc_function", u"grpc_function_data"], 
                    "datatables": [], 
                    "message_destinations": [u"fn_grpc"], 
                    "functions": [u"function_grpc"], 
                    "phases": [], 
                    "automatic_tasks": [], 
                    "scripts": [], 
                    "workflows": [u"example_grpc_communication_interface"], 
                    "actions": [u"Example: Call gRPC Service"] 
                    }
    return reload_params


def customization_data(client=None):
    """Produce any customization definitions (types, fields, message destinations, etc)
       that should be installed by `resilient-circuits customize`
    """

    # This import data contains:
    #   Function inputs:
    #     grpc_channel
    #     grpc_function
    #     grpc_function_data
    #   Message Destinations:
    #     fn_grpc
    #   Functions:
    #     function_grpc
    #   Workflows:
    #     example_grpc_communication_interface
    #   Rules:
    #     Example: Call gRPC Service


    yield ImportDefinition(u"""
eyJ0YXNrX29yZGVyIjogW10sICJ3b3JrZmxvd3MiOiBbeyJ1dWlkIjogImI3NjVlMzEyLTU1NGYt
NDNlOC05ZDZiLTM3ZTQ4ZDA0NDc2NSIsICJkZXNjcmlwdGlvbiI6ICJBbiBleGFtcGxlIHdvcmtm
bG93IGhvdyBzaG93aW5nIHRvIGNhbGwgYSBnUlBDIFNlcnZpY2UgZnJvbSBhbiBJQk0gUmVzaWxp
ZW50IFdvcmtmbG93IiwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgImV4cG9ydF9rZXkiOiAi
ZXhhbXBsZV9ncnBjX2NvbW11bmljYXRpb25faW50ZXJmYWNlIiwgIndvcmtmbG93X2lkIjogMSwg
Imxhc3RfbW9kaWZpZWRfYnkiOiAiYWRtaW5AZXhhbXBsZS5jb20iLCAiY29udGVudCI6IHsieG1s
IjogIjw/eG1sIHZlcnNpb249XCIxLjBcIiBlbmNvZGluZz1cIlVURi04XCI/PjxkZWZpbml0aW9u
cyB4bWxucz1cImh0dHA6Ly93d3cub21nLm9yZy9zcGVjL0JQTU4vMjAxMDA1MjQvTU9ERUxcIiB4
bWxuczpicG1uZGk9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9CUE1OLzIwMTAwNTI0L0RJXCIg
eG1sbnM6b21nZGM9XCJodHRwOi8vd3d3Lm9tZy5vcmcvc3BlYy9ERC8yMDEwMDUyNC9EQ1wiIHht
bG5zOm9tZ2RpPVwiaHR0cDovL3d3dy5vbWcub3JnL3NwZWMvREQvMjAxMDA1MjQvRElcIiB4bWxu
czpyZXNpbGllbnQ9XCJodHRwOi8vcmVzaWxpZW50LmlibS5jb20vYnBtblwiIHhtbG5zOnhzZD1c
Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hXCIgeG1sbnM6eHNpPVwiaHR0cDovL3d3
dy53My5vcmcvMjAwMS9YTUxTY2hlbWEtaW5zdGFuY2VcIiB0YXJnZXROYW1lc3BhY2U9XCJodHRw
Oi8vd3d3LmNhbXVuZGEub3JnL3Rlc3RcIj48cHJvY2VzcyBpZD1cImV4YW1wbGVfZ3JwY19jb21t
dW5pY2F0aW9uX2ludGVyZmFjZVwiIGlzRXhlY3V0YWJsZT1cInRydWVcIiBuYW1lPVwiRXhhbXBs
ZTogR1JQQyBDb21tdW5pY2F0aW9uIEludGVyZmFjZVwiPjxkb2N1bWVudGF0aW9uPkFuIGV4YW1w
bGUgd29ya2Zsb3cgaG93IHNob3dpbmcgdG8gY2FsbCBhIGdSUEMgU2VydmljZSBmcm9tIGFuIElC
TSBSZXNpbGllbnQgV29ya2Zsb3c8L2RvY3VtZW50YXRpb24+PHN0YXJ0RXZlbnQgaWQ9XCJTdGFy
dEV2ZW50XzE1NWFzeG1cIj48b3V0Z29pbmc+U2VxdWVuY2VGbG93XzE0a3NrZm08L291dGdvaW5n
Pjwvc3RhcnRFdmVudD48c2VydmljZVRhc2sgaWQ9XCJTZXJ2aWNlVGFza18xbmZjZnRmXCIgbmFt
ZT1cIkdSUENcIiByZXNpbGllbnQ6dHlwZT1cImZ1bmN0aW9uXCI+PGV4dGVuc2lvbkVsZW1lbnRz
PjxyZXNpbGllbnQ6ZnVuY3Rpb24gdXVpZD1cIjBmOTY5NjA4LWYyMmYtNGE2Yi1hNzQzLWFmMDFh
MjFkNjkzY1wiPntcImlucHV0c1wiOnt9LFwicG9zdF9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiXFxu
Z3JwY19yZXNwb25zZV9kYXRhID0gcmVzdWx0c1snY29udGVudCddXFxuZ3JwY19jaGFubmVsID0g
cmVzdWx0c1snY2hhbm5lbCddXFxuXFxucmljaF90ZXh0ID0gaGVscGVyLmNyZWF0ZVJpY2hUZXh0
KHVcXFwiXFxcIlxcXCJBIGdSUEMgUmVzcG9uc2UgaGFzIGJlZW4gcmVjZWl2ZWQgZnJvbSAmbHQ7
YiZndDt7MH0mbHQ7L2ImZ3Q7Jmx0O2JyJmd0O1xcbiAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgJmx0O2ImZ3Q7UmVzcG9uc2U6Jmx0Oy9iJmd0OyB7MX1cXFwiXFxcIlxcXCIu
Zm9ybWF0KGdycGNfY2hhbm5lbCwgZ3JwY19yZXNwb25zZV9kYXRhKSlcXG5cXG5pbmNpZGVudC5h
ZGROb3RlKHJpY2hfdGV4dClcIixcInByZV9wcm9jZXNzaW5nX3NjcmlwdFwiOlwiZGVmIGRpY3Rf
dG9fanNvbl9zdHIoZCk6XFxuICBcXFwiXFxcIlxcXCJGdW5jdGlvbiB0aGF0IGNvbnZlcnRzIGEg
ZGljdGlvbmFyeSBpbnRvIGEgSlNPTiBzdHJpbmcuXFxuICAgICBTdXBwb3J0cyB0eXBlczogYmFz
ZXN0cmluZywgdW5pY29kZSwgYm9vbCwgaW50IGFuZCBuZXN0ZWQgZGljdHMuXFxuICAgICBEb2Vz
IG5vdCBzdXBwb3J0IGxpc3RzLlxcbiAgICAgSWYgdGhlIHZhbHVlIGlzIE5vbmUsIGl0IHNldHMg
aXQgdG8gRmFsc2UuXFxcIlxcXCJcXFwiXFxuXFxuICBqc29uX2VudHJ5ID0gdSdcXFwiezB9XFxc
Ijp7MX0nXFxuICBqc29uX2VudHJ5X3N0ciA9IHUnXFxcInswfVxcXCI6XFxcInsxfVxcXCInXFxu
ICBlbnRyaWVzID0gW11cXG5cXG4gIGZvciBlbnRyeSBpbiBkOlxcbiAgICBrZXkgPSBlbnRyeVxc
biAgICB2YWx1ZSA9IGRbZW50cnldXFxuXFxuICAgIGlmIHZhbHVlIGlzIE5vbmU6XFxuICAgICAg
dmFsdWUgPSBGYWxzZVxcblxcbiAgICBpZiBpc2luc3RhbmNlKHZhbHVlLCBsaXN0KTpcXG4gICAg
ICBoZWxwZXIuZmFpbCgnZGljdF90b19qc29uX3N0ciBkb2VzIG5vdCBzdXBwb3J0IFB5dGhvbiBM
aXN0cycpXFxuXFxuICAgIGlmIGlzaW5zdGFuY2UodmFsdWUsIGJhc2VzdHJpbmcpOlxcbiAgICAg
IHZhbHVlID0gdmFsdWUucmVwbGFjZSh1J1xcXCInLCB1J1xcXFxcXFxcXFxcIicpXFxuICAgICAg
ZW50cmllcy5hcHBlbmQoanNvbl9lbnRyeV9zdHIuZm9ybWF0KHVuaWNvZGUoa2V5KSwgdW5pY29k
ZSh2YWx1ZSkpKVxcblxcbiAgICBlbGlmIGlzaW5zdGFuY2UodmFsdWUsIHVuaWNvZGUpOlxcbiAg
ICAgIGVudHJpZXMuYXBwZW5kKGpzb25fZW50cnkuZm9ybWF0KHVuaWNvZGUoa2V5KSwgdW5pY29k
ZSh2YWx1ZSkpKVxcbiAgICBcXG4gICAgZWxpZiBpc2luc3RhbmNlKHZhbHVlLCBib29sKTpcXG4g
ICAgICB2YWx1ZSA9ICd0cnVlJyBpZiB2YWx1ZSA9PSBUcnVlIGVsc2UgJ2ZhbHNlJ1xcbiAgICAg
IGVudHJpZXMuYXBwZW5kKGpzb25fZW50cnkuZm9ybWF0KGtleSwgdmFsdWUpKVxcblxcbiAgICBl
bGlmIGlzaW5zdGFuY2UodmFsdWUsIGludCk6XFxuICAgICAgZW50cmllcy5hcHBlbmQoanNvbl9l
bnRyeS5mb3JtYXQodW5pY29kZShrZXkpLCB2YWx1ZSkpXFxuXFxuICAgIGVsaWYgaXNpbnN0YW5j
ZSh2YWx1ZSwgZGljdCk6XFxuICAgICAgZW50cmllcy5hcHBlbmQoanNvbl9lbnRyeS5mb3JtYXQo
a2V5LCBkaWN0X3RvX2pzb25fc3RyKHZhbHVlKSkpXFxuXFxuICAgIGVsc2U6XFxuICAgICAgaGVs
cGVyLmZhaWwoJ2RpY3RfdG9fanNvbl9zdHIgZG9lcyBub3Qgc3VwcG9ydCB0aGlzIHR5cGU6IHsw
fScuZm9ybWF0KHR5cGUodmFsdWUpKSlcXG5cXG4gIHJldHVybiB1J3swfSB7MX0gezJ9Jy5mb3Jt
YXQodSd7JywgJywnLmpvaW4oZW50cmllcyksIHUnfScpXFxuXFxuIyBEZWZpbmUgSW5wdXRzXFxu
XFxuIyBUaGUgZ1JQQyBDaGFubmVsIHRvIHVzZVxcbmlucHV0cy5ncnBjX2NoYW5uZWwgPSBcXFwi
bG9jYWxob3N0OjUwMDUxXFxcIlxcblxcbiMgVGhlIGdSUEMgRnVuY3Rpb24gdG8gY2FsbFxcbmlu
cHV0cy5ncnBjX2Z1bmN0aW9uID0gXFxcImhlbGxvd29ybGQ6U2F5SGVsbG8oSGVsbG9SZXF1ZXN0
KVxcXCJcXG5cXG4jIFRoZSBnUlBDIEZ1bmN0aW9uIFJlcXVlc3QgRGF0YVxcbmlucHV0cy5ncnBj
X2Z1bmN0aW9uX2RhdGEgPSBkaWN0X3RvX2pzb25fc3RyKHtcXFwibmFtZVxcXCI6IGFydGlmYWN0
LnZhbHVlfSlcIn08L3Jlc2lsaWVudDpmdW5jdGlvbj48L2V4dGVuc2lvbkVsZW1lbnRzPjxpbmNv
bWluZz5TZXF1ZW5jZUZsb3dfMTRrc2tmbTwvaW5jb21pbmc+PG91dGdvaW5nPlNlcXVlbmNlRmxv
d18wdHV2NnR6PC9vdXRnb2luZz48L3NlcnZpY2VUYXNrPjxzZXF1ZW5jZUZsb3cgaWQ9XCJTZXF1
ZW5jZUZsb3dfMTRrc2tmbVwiIHNvdXJjZVJlZj1cIlN0YXJ0RXZlbnRfMTU1YXN4bVwiIHRhcmdl
dFJlZj1cIlNlcnZpY2VUYXNrXzFuZmNmdGZcIi8+PGVuZEV2ZW50IGlkPVwiRW5kRXZlbnRfMXVr
aHZ4cFwiPjxpbmNvbWluZz5TZXF1ZW5jZUZsb3dfMHR1djZ0ejwvaW5jb21pbmc+PC9lbmRFdmVu
dD48c2VxdWVuY2VGbG93IGlkPVwiU2VxdWVuY2VGbG93XzB0dXY2dHpcIiBzb3VyY2VSZWY9XCJT
ZXJ2aWNlVGFza18xbmZjZnRmXCIgdGFyZ2V0UmVmPVwiRW5kRXZlbnRfMXVraHZ4cFwiLz48dGV4
dEFubm90YXRpb24gaWQ9XCJUZXh0QW5ub3RhdGlvbl8wNm1tZWU2XCI+PHRleHQ+PCFbQ0RBVEFb
QSBnZW5lcmFsIHB1cnBvc2Ugd3JhcHBlciB0byBjYWxsIGEgZ1JQQyBTZXJ2aWNlXG5dXT48L3Rl
eHQ+PC90ZXh0QW5ub3RhdGlvbj48YXNzb2NpYXRpb24gaWQ9XCJBc3NvY2lhdGlvbl8wNXhjZDZh
XCIgc291cmNlUmVmPVwiU2VydmljZVRhc2tfMW5mY2Z0ZlwiIHRhcmdldFJlZj1cIlRleHRBbm5v
dGF0aW9uXzA2bW1lZTZcIi8+PC9wcm9jZXNzPjxicG1uZGk6QlBNTkRpYWdyYW0gaWQ9XCJCUE1O
RGlhZ3JhbV8xXCI+PGJwbW5kaTpCUE1OUGxhbmUgYnBtbkVsZW1lbnQ9XCJ1bmRlZmluZWRcIiBp
ZD1cIkJQTU5QbGFuZV8xXCI+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTdGFydEV2
ZW50XzE1NWFzeG1cIiBpZD1cIlN0YXJ0RXZlbnRfMTU1YXN4bV9kaVwiPjxvbWdkYzpCb3VuZHMg
aGVpZ2h0PVwiMzZcIiB3aWR0aD1cIjM2XCIgeD1cIjE4NVwiIHk9XCIxODhcIi8+PGJwbW5kaTpC
UE1OTGFiZWw+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCIwXCIgd2lkdGg9XCI5MFwiIHg9XCIxODBc
IiB5PVwiMjIzXCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hhcGU+PGJwbW5k
aTpCUE1OU2hhcGUgYnBtbkVsZW1lbnQ9XCJTZXJ2aWNlVGFza18xbmZjZnRmXCIgaWQ9XCJTZXJ2
aWNlVGFza18xbmZjZnRmX2RpXCI+PG9tZ2RjOkJvdW5kcyBoZWlnaHQ9XCI4MFwiIHdpZHRoPVwi
MTAwXCIgeD1cIjMzMVwiIHk9XCIxNjZcIi8+PC9icG1uZGk6QlBNTlNoYXBlPjxicG1uZGk6QlBN
TkVkZ2UgYnBtbkVsZW1lbnQ9XCJTZXF1ZW5jZUZsb3dfMTRrc2tmbVwiIGlkPVwiU2VxdWVuY2VG
bG93XzE0a3NrZm1fZGlcIj48b21nZGk6d2F5cG9pbnQgeD1cIjIyMVwiIHhzaTp0eXBlPVwib21n
ZGM6UG9pbnRcIiB5PVwiMjA2XCIvPjxvbWdkaTp3YXlwb2ludCB4PVwiMzMxXCIgeHNpOnR5cGU9
XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PGJwbW5kaTpCUE1OTGFiZWw+PG9tZ2RjOkJvdW5k
cyBoZWlnaHQ9XCIxMlwiIHdpZHRoPVwiOTBcIiB4PVwiMjMxXCIgeT1cIjE4NVwiLz48L2JwbW5k
aTpCUE1OTGFiZWw+PC9icG1uZGk6QlBNTkVkZ2U+PGJwbW5kaTpCUE1OU2hhcGUgYnBtbkVsZW1l
bnQ9XCJFbmRFdmVudF8xdWtodnhwXCIgaWQ9XCJFbmRFdmVudF8xdWtodnhwX2RpXCI+PG9tZ2Rj
OkJvdW5kcyBoZWlnaHQ9XCIzNlwiIHdpZHRoPVwiMzZcIiB4PVwiNTMxXCIgeT1cIjE4OFwiLz48
YnBtbmRpOkJQTU5MYWJlbD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEyXCIgd2lkdGg9XCI5MFwi
IHg9XCI1MDRcIiB5PVwiMjI4XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1OU2hh
cGU+PGJwbW5kaTpCUE1ORWRnZSBicG1uRWxlbWVudD1cIlNlcXVlbmNlRmxvd18wdHV2NnR6XCIg
aWQ9XCJTZXF1ZW5jZUZsb3dfMHR1djZ0el9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDMxXCIg
eHNpOnR5cGU9XCJvbWdkYzpQb2ludFwiIHk9XCIyMDZcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI1
MzFcIiB4c2k6dHlwZT1cIm9tZ2RjOlBvaW50XCIgeT1cIjIwNlwiLz48YnBtbmRpOkJQTU5MYWJl
bD48b21nZGM6Qm91bmRzIGhlaWdodD1cIjEyXCIgd2lkdGg9XCI5MFwiIHg9XCI0MzZcIiB5PVwi
MTg1XCIvPjwvYnBtbmRpOkJQTU5MYWJlbD48L2JwbW5kaTpCUE1ORWRnZT48YnBtbmRpOkJQTU5T
aGFwZSBicG1uRWxlbWVudD1cIlRleHRBbm5vdGF0aW9uXzA2bW1lZTZcIiBpZD1cIlRleHRBbm5v
dGF0aW9uXzA2bW1lZTZfZGlcIj48b21nZGM6Qm91bmRzIGhlaWdodD1cIjU0XCIgd2lkdGg9XCIx
NzNcIiB4PVwiNDYyXCIgeT1cIjgyXCIvPjwvYnBtbmRpOkJQTU5TaGFwZT48YnBtbmRpOkJQTU5F
ZGdlIGJwbW5FbGVtZW50PVwiQXNzb2NpYXRpb25fMDV4Y2Q2YVwiIGlkPVwiQXNzb2NpYXRpb25f
MDV4Y2Q2YV9kaVwiPjxvbWdkaTp3YXlwb2ludCB4PVwiNDMxXCIgeHNpOnR5cGU9XCJvbWdkYzpQ
b2ludFwiIHk9XCIxNzdcIi8+PG9tZ2RpOndheXBvaW50IHg9XCI1MDNcIiB4c2k6dHlwZT1cIm9t
Z2RjOlBvaW50XCIgeT1cIjEzNlwiLz48L2JwbW5kaTpCUE1ORWRnZT48L2JwbW5kaTpCUE1OUGxh
bmU+PC9icG1uZGk6QlBNTkRpYWdyYW0+PC9kZWZpbml0aW9ucz4iLCAid29ya2Zsb3dfaWQiOiAi
ZXhhbXBsZV9ncnBjX2NvbW11bmljYXRpb25faW50ZXJmYWNlIiwgInZlcnNpb24iOiAyOH0sICJs
YXN0X21vZGlmaWVkX3RpbWUiOiAxNTU0OTczOTMxMTg2LCAiY3JlYXRvcl9pZCI6ICJpbnRlZ3Jh
dGlvbnNAZXhhbXBsZS5jb20iLCAiYWN0aW9ucyI6IFtdLCAicHJvZ3JhbW1hdGljX25hbWUiOiAi
ZXhhbXBsZV9ncnBjX2NvbW11bmljYXRpb25faW50ZXJmYWNlIiwgIm5hbWUiOiAiRXhhbXBsZTog
R1JQQyBDb21tdW5pY2F0aW9uIEludGVyZmFjZSJ9XSwgImFjdGlvbnMiOiBbeyJsb2dpY190eXBl
IjogImFsbCIsICJuYW1lIjogIkV4YW1wbGU6IENhbGwgZ1JQQyBTZXJ2aWNlIiwgInZpZXdfaXRl
bXMiOiBbXSwgInR5cGUiOiAxLCAid29ya2Zsb3dzIjogWyJleGFtcGxlX2dycGNfY29tbXVuaWNh
dGlvbl9pbnRlcmZhY2UiXSwgIm9iamVjdF90eXBlIjogImFydGlmYWN0IiwgInRpbWVvdXRfc2Vj
b25kcyI6IDg2NDAwLCAidXVpZCI6ICJmYjU5MzcyZC0xNzAwLTRkM2ItYjAxOS0wYzY1NGYwZjE3
ZGIiLCAiYXV0b21hdGlvbnMiOiBbXSwgImV4cG9ydF9rZXkiOiAiRXhhbXBsZTogQ2FsbCBnUlBD
IFNlcnZpY2UiLCAiY29uZGl0aW9ucyI6IFtdLCAiaWQiOiAxNCwgIm1lc3NhZ2VfZGVzdGluYXRp
b25zIjogW119XSwgImxheW91dHMiOiBbXSwgImV4cG9ydF9mb3JtYXRfdmVyc2lvbiI6IDIsICJp
ZCI6IDEsICJpbmR1c3RyaWVzIjogbnVsbCwgInBoYXNlcyI6IFtdLCAiYWN0aW9uX29yZGVyIjog
W10sICJnZW9zIjogbnVsbCwgImxvY2FsZSI6IG51bGwsICJzZXJ2ZXJfdmVyc2lvbiI6IHsibWFq
b3IiOiAzMSwgInZlcnNpb24iOiAiMzEuMC40MjU0IiwgImJ1aWxkX251bWJlciI6IDQyNTQsICJt
aW5vciI6IDB9LCAidGltZWZyYW1lcyI6IG51bGwsICJ3b3Jrc3BhY2VzIjogW10sICJhdXRvbWF0
aWNfdGFza3MiOiBbXSwgImZ1bmN0aW9ucyI6IFt7ImRpc3BsYXlfbmFtZSI6ICJHUlBDIiwgImRl
c2NyaXB0aW9uIjogeyJjb250ZW50IjogIkZ1bmN0aW9uIHRoYXQgYWxsb3dzIHlvdSB0byBjYWxs
IGEgZ1JQQyBTZXJ2aWNlIHRoYXQgaXMgYmVpbmcgc2VydmVkIG9uIHlvdXIgSW50ZWdyYXRpb25z
IFNlcnZlciIsICJmb3JtYXQiOiAidGV4dCJ9LCAiY3JlYXRvciI6IHsiZGlzcGxheV9uYW1lIjog
Ik9yY2hlc3RyYXRpb24gRW5naW5lIiwgInR5cGUiOiAidXNlciIsICJpZCI6IDM4LCAibmFtZSI6
ICJpbnRlZ3JhdGlvbnNAZXhhbXBsZS5jb20ifSwgInZpZXdfaXRlbXMiOiBbeyJzaG93X2lmIjog
bnVsbCwgImZpZWxkX3R5cGUiOiAiX19mdW5jdGlvbiIsICJzaG93X2xpbmtfaGVhZGVyIjogZmFs
c2UsICJlbGVtZW50IjogImZpZWxkX3V1aWQiLCAiY29udGVudCI6ICIzM2JmN2M0MS0xZjQ1LTRk
MmMtYjkxNS05MTE0NTNkYjFkNWUiLCAic3RlcF9sYWJlbCI6IG51bGx9LCB7InNob3dfaWYiOiBu
dWxsLCAiZmllbGRfdHlwZSI6ICJfX2Z1bmN0aW9uIiwgInNob3dfbGlua19oZWFkZXIiOiBmYWxz
ZSwgImVsZW1lbnQiOiAiZmllbGRfdXVpZCIsICJjb250ZW50IjogImQwOTg3OGRjLWQxMWYtNGUy
ZS1iMTEyLWQ1M2U1ODgyZTI1ZiIsICJzdGVwX2xhYmVsIjogbnVsbH0sIHsic2hvd19pZiI6IG51
bGwsICJmaWVsZF90eXBlIjogIl9fZnVuY3Rpb24iLCAic2hvd19saW5rX2hlYWRlciI6IGZhbHNl
LCAiZWxlbWVudCI6ICJmaWVsZF91dWlkIiwgImNvbnRlbnQiOiAiOWRkZGRmNjItNjBmNy00NTBh
LWE5YWMtMmZkYjg1ZTNjNGEzIiwgInN0ZXBfbGFiZWwiOiBudWxsfV0sICJleHBvcnRfa2V5Ijog
ImZ1bmN0aW9uX2dycGMiLCAidXVpZCI6ICIwZjk2OTYwOC1mMjJmLTRhNmItYTc0My1hZjAxYTIx
ZDY5M2MiLCAibGFzdF9tb2RpZmllZF9ieSI6IHsiZGlzcGxheV9uYW1lIjogIkFkbWluIFVzZXIi
LCAidHlwZSI6ICJ1c2VyIiwgImlkIjogNzEsICJuYW1lIjogImFkbWluQGV4YW1wbGUuY29tIn0s
ICJ2ZXJzaW9uIjogMiwgIndvcmtmbG93cyI6IFt7ImRlc2NyaXB0aW9uIjogbnVsbCwgIm9iamVj
dF90eXBlIjogImFydGlmYWN0IiwgImFjdGlvbnMiOiBbXSwgIm5hbWUiOiAiRXhhbXBsZTogR1JQ
QyBDb21tdW5pY2F0aW9uIEludGVyZmFjZSIsICJ3b3JrZmxvd19pZCI6IDEsICJwcm9ncmFtbWF0
aWNfbmFtZSI6ICJleGFtcGxlX2dycGNfY29tbXVuaWNhdGlvbl9pbnRlcmZhY2UiLCAidXVpZCI6
IG51bGx9XSwgImxhc3RfbW9kaWZpZWRfdGltZSI6IDE1NTQ5NzI5NDM3OTUsICJkZXN0aW5hdGlv
bl9oYW5kbGUiOiAiZm5fZ3JwYyIsICJpZCI6IDM0LCAibmFtZSI6ICJmdW5jdGlvbl9ncnBjIn1d
LCAibm90aWZpY2F0aW9ucyI6IG51bGwsICJyZWd1bGF0b3JzIjogbnVsbCwgImluY2lkZW50X3R5
cGVzIjogW3siY3JlYXRlX2RhdGUiOiAxNTU0OTc0MTkwNTQ4LCAiZGVzY3JpcHRpb24iOiAiQ3Vz
dG9taXphdGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImV4cG9ydF9rZXkiOiAiQ3VzdG9taXph
dGlvbiBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgImlkIjogMCwgIm5hbWUiOiAiQ3VzdG9taXphdGlv
biBQYWNrYWdlcyAoaW50ZXJuYWwpIiwgInVwZGF0ZV9kYXRlIjogMTU1NDk3NDE5MDU0OCwgInV1
aWQiOiAiYmZlZWMyZDQtMzc3MC0xMWU4LWFkMzktNGEwMDA0MDQ0YWEwIiwgImVuYWJsZWQiOiBm
YWxzZSwgInN5c3RlbSI6IGZhbHNlLCAicGFyZW50X2lkIjogbnVsbCwgImhpZGRlbiI6IGZhbHNl
fV0sICJzY3JpcHRzIjogW10sICJ0eXBlcyI6IFtdLCAibWVzc2FnZV9kZXN0aW5hdGlvbnMiOiBb
eyJ1dWlkIjogImIwODdmMzNhLTIxYzctNGE5Yy1iNjA1LTAyYzcxOTk3NjM5MiIsICJleHBvcnRf
a2V5IjogImZuX2dycGMiLCAibmFtZSI6ICJmbl9ncnBjIiwgImRlc3RpbmF0aW9uX3R5cGUiOiAw
LCAicHJvZ3JhbW1hdGljX25hbWUiOiAiZm5fZ3JwYyIsICJleHBlY3RfYWNrIjogdHJ1ZSwgInVz
ZXJzIjogWyJpbnRlZ3JhdGlvbnNAZXhhbXBsZS5jb20iXX1dLCAiaW5jaWRlbnRfYXJ0aWZhY3Rf
dHlwZXMiOiBbXSwgInJvbGVzIjogW10sICJmaWVsZHMiOiBbeyJvcGVyYXRpb25zIjogW10sICJ0
eXBlX2lkIjogMCwgIm9wZXJhdGlvbl9wZXJtcyI6IHt9LCAidGV4dCI6ICJTaW11bGF0aW9uIiwg
ImJsYW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVl
LCAiaWQiOiAzOCwgInJlYWRfb25seSI6IHRydWUsICJ1dWlkIjogImMzZjBlM2VkLTIxZTEtNGQ1
My1hZmZiLWZlNWNhMzMwOGNjYSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAiYm9v
bGVhbiIsICJ0b29sdGlwIjogIldoZXRoZXIgdGhlIGluY2lkZW50IGlzIGEgc2ltdWxhdGlvbiBv
ciBhIHJlZ3VsYXIgaW5jaWRlbnQuICBUaGlzIGZpZWxkIGlzIHJlYWQtb25seS4iLCAiaW50ZXJu
YWwiOiBmYWxzZSwgInJpY2hfdGV4dCI6IGZhbHNlLCAidGVtcGxhdGVzIjogW10sICJleHBvcnRf
a2V5IjogImluY2lkZW50L2luY190cmFpbmluZyIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNl
LCAibmFtZSI6ICJpbmNfdHJhaW5pbmciLCAiZGVwcmVjYXRlZCI6IGZhbHNlLCAiZGVmYXVsdF9j
aG9zZW5fYnlfc2VydmVyIjogZmFsc2UsICJ2YWx1ZXMiOiBbXX0sIHsib3BlcmF0aW9ucyI6IFtd
LCAidHlwZV9pZCI6IDExLCAib3BlcmF0aW9uX3Blcm1zIjoge30sICJ0ZXh0IjogImdycGNfY2hh
bm5lbCIsICJibGFua19vcHRpb24iOiBmYWxzZSwgInByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxl
IjogdHJ1ZSwgImlkIjogMTczLCAicmVhZF9vbmx5IjogZmFsc2UsICJ1dWlkIjogIjMzYmY3YzQx
LTFmNDUtNGQyYy1iOTE1LTkxMTQ1M2RiMWQ1ZSIsICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5
cGUiOiAidGV4dCIsICJ0b29sdGlwIjogInRoaXMgZmllbGQgY29udGFpbiB0aGUgY2hhbm5lbCBp
bmZvIG9mIHRoZSBHUlBDIFNlcnZlciBSdW5uaW5nIGV4Omhvc3RJUDpQb3J0IiwgImludGVybmFs
IjogZmFsc2UsICJyaWNoX3RleHQiOiBmYWxzZSwgInRlbXBsYXRlcyI6IFtdLCAiZXhwb3J0X2tl
eSI6ICJfX2Z1bmN0aW9uL2dycGNfY2hhbm5lbCIsICJoaWRlX25vdGlmaWNhdGlvbiI6IGZhbHNl
LCAicGxhY2Vob2xkZXIiOiAiIiwgIm5hbWUiOiAiZ3JwY19jaGFubmVsIiwgImRlcHJlY2F0ZWQi
OiBmYWxzZSwgImRlZmF1bHRfY2hvc2VuX2J5X3NlcnZlciI6IGZhbHNlLCAicmVxdWlyZWQiOiAi
YWx3YXlzIiwgInZhbHVlcyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEs
ICJvcGVyYXRpb25fcGVybXMiOiB7fSwgInRleHQiOiAiZ3JwY19mdW5jdGlvbl9kYXRhIiwgImJs
YW5rX29wdGlvbiI6IGZhbHNlLCAicHJlZml4IjogbnVsbCwgImNoYW5nZWFibGUiOiB0cnVlLCAi
aWQiOiAxNzUsICJyZWFkX29ubHkiOiBmYWxzZSwgInV1aWQiOiAiOWRkZGRmNjItNjBmNy00NTBh
LWE5YWMtMmZkYjg1ZTNjNGEzIiwgImNob3NlbiI6IGZhbHNlLCAiaW5wdXRfdHlwZSI6ICJ0ZXh0
IiwgInRvb2x0aXAiOiAiQWRkaXRpb25hbCBkYXRhIEZpZWxkcyB0byBzZW5kIGRhdGEgZnJvbSBj
bGllbnQgdG8gc2VydmVyLiBkYXRhIGZvcm1hdCB3aWxsIGJlIGluIGpzb24gYW5kIGtleSBzaG91
bGQgbWF0Y2ggdGhlIHJlcXVlc3QgZnVuY3Rpb24gcGFyYW1ldGVyLiIsICJpbnRlcm5hbCI6IGZh
bHNlLCAicmljaF90ZXh0IjogZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAi
X19mdW5jdGlvbi9ncnBjX2Z1bmN0aW9uX2RhdGEiLCAiaGlkZV9ub3RpZmljYXRpb24iOiBmYWxz
ZSwgInBsYWNlaG9sZGVyIjogIiIsICJuYW1lIjogImdycGNfZnVuY3Rpb25fZGF0YSIsICJkZXBy
ZWNhdGVkIjogZmFsc2UsICJkZWZhdWx0X2Nob3Nlbl9ieV9zZXJ2ZXIiOiBmYWxzZSwgInZhbHVl
cyI6IFtdfSwgeyJvcGVyYXRpb25zIjogW10sICJ0eXBlX2lkIjogMTEsICJvcGVyYXRpb25fcGVy
bXMiOiB7fSwgInRleHQiOiAiZ3JwY19mdW5jdGlvbiIsICJibGFua19vcHRpb24iOiBmYWxzZSwg
InByZWZpeCI6IG51bGwsICJjaGFuZ2VhYmxlIjogdHJ1ZSwgImlkIjogMTc0LCAicmVhZF9vbmx5
IjogZmFsc2UsICJ1dWlkIjogImQwOTg3OGRjLWQxMWYtNGUyZS1iMTEyLWQ1M2U1ODgyZTI1ZiIs
ICJjaG9zZW4iOiBmYWxzZSwgImlucHV0X3R5cGUiOiAidGV4dCIsICJ0b29sdGlwIjogIlRoaXMg
ZmllbGRzIGNvbnRhaW5zIGRhdGEgZnJvbSAucHJvdG8gZmlsZSBpLmUgcGFja2FnZV9uYW1lIDog
cnBjIGZ1bmN0aW9uIG5hbWUoZ3JwYyByZXF1ZXN0IGZ1bmN0aW9uKSBleDogaGVsbG93b3JkIDog
U2F5SGVsbG8oSGVsbG9SZXF1ZXN0KSIsICJpbnRlcm5hbCI6IGZhbHNlLCAicmljaF90ZXh0Ijog
ZmFsc2UsICJ0ZW1wbGF0ZXMiOiBbXSwgImV4cG9ydF9rZXkiOiAiX19mdW5jdGlvbi9ncnBjX2Z1
bmN0aW9uIiwgImhpZGVfbm90aWZpY2F0aW9uIjogZmFsc2UsICJwbGFjZWhvbGRlciI6ICIiLCAi
bmFtZSI6ICJncnBjX2Z1bmN0aW9uIiwgImRlcHJlY2F0ZWQiOiBmYWxzZSwgImRlZmF1bHRfY2hv
c2VuX2J5X3NlcnZlciI6IGZhbHNlLCAicmVxdWlyZWQiOiAiYWx3YXlzIiwgInZhbHVlcyI6IFtd
fV0sICJvdmVycmlkZXMiOiBbXSwgImV4cG9ydF9kYXRlIjogMTU1NDk3Mzk1NjE5MX0=
"""
    )