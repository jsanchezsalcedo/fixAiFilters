'''
FIX aiFILTERS CONNECTIONS v1.0.1
by Jorge Sanchez Salcedo, 2018

Fix aiFilters connections when, between them,
are free slots.

Checks available slots between aiFilters and
re-connect the filters on these slots.
'''

import maya.cmds as cmds

class FixFilters:
    def __init__(self):

        self.fixFilter()

    def checkConnections(self):

        lightSel = cmds.ls(sl=True, lt = True)

        for light in sorted(lightSel):

            for i in range(10):

                filterNumber = filterNumber = + i

                checkConn = cmds.connectionInfo(light + '.aiFilters[' + str(filterNumber) + ']', id = True)

                if checkConn == True:

                    continue

                else:

                    connectionNumber = (filterNumber) + 1

                    return light, filterNumber, connectionNumber

    def checkNextFilter(self):

        light, filterNumber, connectionNumber = self.checkConnections()

        for i in range(10):

            connectionNumber = + connectionNumber + 1

            nextFilter = cmds.connectionInfo(light + '.aiFilters[' + str(connectionNumber) + ']', ied = True)

            if nextFilter == True:

                checkFilter = cmds.connectionInfo(light + '.aiFilters[' + str(connectionNumber) + ']', sfd = True)

                freeSlot = light + '.aiFilters[' + str(filterNumber) + ']'

                connectedSlot = light + '.aiFilters[' + str(connectionNumber) + ']'

                return checkFilter, freeSlot, connectedSlot

            else:

                continue

    def fixFilter(self):

        print ' '
        print ' > You are running FIX aiFILTERS CONNECTIONS v1.0.0 by JS, 2018.'

        try:
            checkFilter, freeSlot, connectedSlot = self.checkNextFilter()

            cmds.connectAttr(checkFilter, freeSlot)

            cmds.disconnectAttr(checkFilter, connectedSlot)

            print '   > You just connected:'
            print '     ', checkFilter, 'to', freeSlot, 'and disconnected from', connectedSlot

            self.fixFilter()

        except TypeError:

            print '   > You already have fixed all aiFilters connections, successfully.'
            print ' '