'''
FIX aiFILTERS CONNECTIONS v0.10
by Jorge Sanchez Salcedo, 2018

Fix aiFilters connections when, between them,
are free slots.

Check available slots between filters and
re-connect the filters on these slots.
'''

import maya.cmds as cmds

class FixFilters:
    def __init__(self):

        self.fixFilter()

    def checkConnections(self):

        lightSel = cmds.ls(sl = True, lt = True)

        for light in sorted(lightSel):

            for i in range(10):

                filterNumber = filterNumber = + i

                checkConn = cmds.connectionInfo(light + '.aiFilters[' + str(filterNumber) + ']', id = True)

                if checkConn == True:

                    print filterNumber, checkConn

                    continue

                else:

                    print filterNumber, checkConn

                    connectionNumber = (filterNumber) + 1

                    print filterNumber, connectionNumber

                    return light, filterNumber, connectionNumber

    def checkNextFilter(self):

        light, filterNumber, connectionNumber = self.checkConnections()

        for i in range(10):

            connectionNumber = + connectionNumber + 1

            nextFilter = cmds.connectionInfo(light + '.aiFilters[' + str(connectionNumber) + ']', ied = True)

            print connectionNumber, nextFilter

            if nextFilter == True:

                checkFilter = cmds.connectionInfo(light + '.aiFilters[' + str(connectionNumber) + ']', sfd = True)

                freeSlot = light + '.aiFilters[' + str(filterNumber) + ']'

                connectedSlot = light + '.aiFilters[' + str(connectionNumber) + ']'

                return checkFilter, freeSlot, connectedSlot

            else:

                continue

    def fixFilter(self):

        checkFilter, freeSlot, connectedSlot = self.checkNextFilter()

        cmds.connectAttr(checkFilter, freeSlot)

        cmds.disconnectAttr(checkFilter, connectedSlot)

        print 'You just connected', checkFilter, 'to', freeSlot, 'and disconnected from', connectedSlot

        self.fixFilter()