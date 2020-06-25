import geni.portal as portal
import geni.rspec.igext as IG
import geni.rspec.pg as rspec

# Profile based on https://gitlab.flux.utah.edu/powder-profiles/srslte-docker-sim/


tourDescription = """
TODO: Tour Description here
"""

tourInstructions = """
Follow instructions [here](https://gitlab.eurecom.fr/oai/openairinterface5g/-/blob/develop/doc/L2NFAPI_NOS1.md), starting from Step 6 (Start the eNB). 
"""


class GLOBALS(object):
    HOST_IMG = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
    BS_MOUNT_POINT = "/mydata"
    BS_MOUNT_SIZE = "50GB"
    


pc = portal.Context()
pc.defineParameter("hardware_type", "Node Hardware Type (optional)", portal.ParameterType.STRING,
                   "", longDescription="An optional hardware type for the host node.")

params = pc.bindParameters()
pc.verifyParameters()
request = pc.makeRequestRSpec()


# Set up lan
lan = request.Link()

def configure_node(request, name, script):
    node = request.RawPC(name)
    if params.hardware_type:
        node.hardware_type = params.hardware_type
    node.disk_image = GLOBALS.HOST_IMG
    node.addService(rspec.Execute(shell="bash", command="/local/repository/{}".format(script)))
    node_iface = node.addInterface("eth1")
    lan.addInterface(node_iface)
    bs = node.Blockstore(name + "-bs", GLOBALS.BS_MOUNT_POINT)
    bs.size = GLOBALS.BS_MOUNT_SIZE
    bs.placement = "any"

configure_node(request, "enb", "/local/repository/enb_startup.sh")
configure_node(request, "ue", "/local/repository/ue_startup.sh")


tour = IG.Tour()
tour.Description(IG.Tour.MARKDOWN, tourDescription)
tour.Instructions(IG.Tour.MARKDOWN, tourInstructions)
request.addTour(tour)

pc.printRequestRSpec(request)

