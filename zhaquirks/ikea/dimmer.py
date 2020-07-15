"""Device handler for IKEA of Sweden TRADFRI remote control."""
from zigpy.profiles import zha, zll
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.closures import WindowCovering
from zigpy.zcl.clusters.general import (
    Alarms,
    Basic,
    Groups,
    Identify,
    LevelControl,
    OnOff,
    Ota,
    PollControl,
    PowerConfiguration,
)
from zigpy.zcl.clusters.homeautomation import Diagnostic
from zigpy.zcl.clusters.lightlink import LightLink

from . import IKEA, LightLinkCluster
from .. import DoublingPowerConfigurationCluster
from ..const import (
    ARGS,
    CLUSTER_ID,
    COMMAND,
    COMMAND_MOVE,
    COMMAND_MOVE_ON_OFF,
    COMMAND_OFF,
    COMMAND_ON,
    DEVICE_TYPE,
    DIM_DOWN,
    DIM_UP,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    LONG_PRESS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
    SHORT_PRESS,
    TURN_OFF,
    TURN_ON,
)

# {
#   "node_descriptor": "<Optional byte1=2 byte2=64 mac_capability_flags=128 manufacturer_code=4476 maximum_buffer_size=82 maximum_incoming_transfer_size=82 server_mask=10752 maximum_outgoing_transfer_size=82 descriptor_capability_field=0>",
#   "endpoints": {
#     "1": {
#       "profile_id": 49246,
#       "device_type": "0x0810",
#       "in_clusters": [
#         "0x0000",
#         "0x0001",
#         "0x0003",
#         "0x0009",
#         "0x0b05",
#         "0x1000"
#       ],
#       "out_clusters": [
#         "0x0003",
#         "0x0004",
#         "0x0006",
#         "0x0008",
#         "0x0019",
#         "0x1000"
#       ]
#     }
#   },
#   "manufacturer": "IKEA of Sweden",
#   "model": "",
#   "class": "zigpy.device.Device"
# }


class IkeaTradfriDimmer(CustomDevice):
    """Custom device representing IKEA of Sweden TRADFRI remote control."""

    signature = {
        # <SimpleDescriptor endpoint=1 profile=260 device_type=2080
        # device_version=1
        # input_clusters=[0, 1, 3, 9, 32, 4096, 64636]
        # output_clusters=[3, 4, 6, 8, 25, 258, 4096]>
        MODELS_INFO: [(IKEA, "TRADFRI wireless dimmer")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zll.PROFILE_ID,
                DEVICE_TYPE: zll.DeviceType.COLOR_SCENE_CONTROLLER,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Alarms.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    LightLink.cluster_id,
                ],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zll.PROFILE_ID,
                DEVICE_TYPE: zll.DeviceType.COLOR_SCENE_CONTROLLER,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    PowerConfiguration.cluster_id,
                    Identify.cluster_id,
                    Alarms.cluster_id,
                    Diagnostic.cluster_id,
                    LightLink.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                    LightLink.cluster_id,
                ],
            }
        },
    }

    device_automation_triggers = { }
