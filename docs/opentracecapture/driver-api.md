# OpenTraceCapture driver structure
OpenTraceCapture is the core library that provides hardware abstraction and signal acquisition capabilities for the OpenTraceLab ecosystem.

## Architecture

``` mermaid
classDiagram
direction LR

class DriverAPI {
  + init
  + cleanup
  + scan
  + dev_open
  + dev_close
  + config_get
  + config_set
  + acquire_start
  + acquire_stop
  + dev_status
}

class DeviceInstance {
  + id
  + vendor_id
  + product_id
  + serial
  + transport
  + channels
  + samplerate
  + trigger
  + options
  + state
  + private_ctx
}

class Channel {
  + index
  + name
  + kind
  + unit
  + enabled
  + scale
  + offset
}

class Transport {
  + usb_handle
  + serial_handle
  + tcp_handle
  + endpoint_in
  + endpoint_out
  + timeout_ms
}

class Buffering {
  + ring_buffer
  + frame_size
  + watermark
}

class TransferThread {
  + run
  + stop
  + status
  + stats_dropped
  + stats_overflow
}

class TriggerEngine {
  + mode
  + level
  + pattern
}

class DriverTable {
  + name
  + id
  + vendor_list
  + product_list
  + callbacks DriverAPI
}

DriverTable --> DriverAPI : uses
DriverAPI --> DeviceInstance : manages
DeviceInstance --> Channel : has many
DeviceInstance --> Transport : uses
DeviceInstance --> Buffering : owns
DeviceInstance --> TriggerEngine : uses
DeviceInstance --> TransferThread : spawns
```

## Runtime data flow

``` mermaid
flowchart LR
  UI[Session Controller] --> OPEN[dev open]
  OPEN --> CFG[config set]
  CFG --> START[acquire start]
  START --> RX[transfer thread read]
  RX --> BUF[ring buffer push]
  BUF --> DEMUX[demux and channel map]
  DEMUX --> OUT[sample frames to core]
  OUT --> DECODE[decode pipeline]
  OUT --> VIEW[trace view]

  UI --> STOP[acquire stop]
  STOP --> CLOSE[dev close]
```

## struct otc_dev_driver
Every driver must define a struct sr_dev_driver to register it with libsigrok. It is defined as follows:
``` c
struct otc_dev_driver {
   /* Driver-specific */
   char *name;
   char *longname;
   int api_version;
   int (*init) (void);
   int (*cleanup) (void);
   GSList *(*scan) (GSList *options);
   GSList *(*dev_list) (void);
   int (*dev_clear) (void);

   /* Device-specific */
   int (*dev_open) (struct otc_dev_inst *sdi);
   int (*dev_close) (struct otc_dev_inst *sdi);
   int (*config_get) (int info_id, const void **data,
           const struct otc_dev_inst *sdi);
   int (*config_set) (const struct otc_dev_inst *sdi, int hwcap,
           const void *value);
   int (*dev_acquisition_start) (const struct otc_dev_inst *sdi,
           void *cb_data);
   int (*dev_acquisition_stop) (struct otc_dev_inst *sdi,
           void *cb_data);

   /* Dynamic */
   void *priv;
};
```
This structure should be the only symbol imported into the libsigrok namespace. The driver's variables thus cannot conflict with the global libsigrok namespace.

### name
A short string describing this driver. It should contain only lowercase a-z, 0-9 and dashes (-). It will be referenced in saved session files.

### longname
A longer freeform string describing this driver. It will be shown to the user.

### api_version
Currently defined as 1.

- Most of the other members of the structure are pointers to driver callbacks:

### init()
Called when the driver is initially loading into libsigrok, typically at program start.

Returns OTC_OK if successful, OTC_ERR otherwise.

### cleanup()
Called before the driver is unloaded. Any resources the driver holds must be released here, such as memory or connectivity library handles.

Returns SR_OK if successful, SR_ERR otherwise.

### scan(GSList *options)
When a frontend wants a driver to scan for devices on the system that it knows about, this function is called. If a device was found, any initialization it needs must be performed here; for example, uploading firmware should be done here.

A driver for USB-connected devices typically doesn't need any help with this: it will find devices known to it by their VendorID and ProductID (VID:PID).

However other drivers — notably those which use a serial port — need to be pointed at the device. The GSList options contains instances of this struct:

``` c
 struct sr_hwopt {
    int hwopt;
    const void *value;
 };
 ```

There are currently two valid hwopt values: OTC_HWOPT_CONN, where the associated value contains a string pointing the driver at the resource it needs to connect to. Right now that means a serial port of the form /dev/ttyUSB0 or /dev/ttyACM0. The second hwopt is OTC_HWOPT_SERIALCOMM, which defines the serial communication parameters for the given port in the form <baudrate>/<data bits><parity><stop bits>, for example "9600/8n1" or "600/7o2".

For serial port-based drivers, OTC_HWOPT_CONN is always required, and OTC_HWOPT_SERIALCOMM always optional: the driver should know at which bitrate its device(s) can communicate, or probe for it.

Any devices found must have a struct otc_dev_inst created, which is added to the driver's known instances -- a GSList stored in the driver context's instances field.

A copy of the struct sr_dev_inst for every device found in the current invocation of scan() must also be returned in a GSList from the function itself; the frontend is responsible for freeing the list (but will not touch the instances it contains).

The instances thus returned to the frontend are central to the communication between the driver and the OpenmTraceCapture frontend: every other callback function has an instance struct as a parameter.

###  dev_list()
Called whenever the frontend needs a list of device instances the driver knows about. This should just return the instances field in the driver's context struct.

### dev_clear()
Clear the list of device instances the driver knows about. A frontend may call the scan() function multiple times to add to the driver's list of known devices, for example with a different serial port each time. If the frontend then wants to start over, it needs this function to clear the list.

Returns SR_OK if successful, SR_ERR otherwise.

### dev_open(struct sr_dev_inst *sdi)
Open the specified device.

Returns SR_OK if successful, SR_ERR otherwise.

### dev_close(struct sr_dev_inst *sdi)
Close the specified device.

Returns SR_OK if successful, SR_ERR otherwise.

### config_get(int info_id, const void **data, struct sr_dev_inst *sdi)
Returns information about the driver, or, if sdi is provided, that device instance. The type of information is given as info_id, one of a set of defined constants. The return value is always a pointer which refers to information specific to the id. Check libsigrok.h for the definitions (SR_DI_*).

### config_set(const struct sr_dev_inst *sdi, int hwcap, const void *value)
This is used to configure the driver and/or connected device. The hwcap parameter is one of the constants returned from calling info_get() with either SR_DI_HWOPTS (driver options) or SR_DI_HWCAPS (device instance options) as the info_id. The value depends on the parameter to be configured.

### dev_acquisition_start(const struct sr_dev_inst *sdi, void *cb_data)
Start acquisition on the specified device. The cb_data parameter will be passed along with the data feed of this session, as the first parameter to session bus callbacks.

### dev_acquisition_stop(const struct sr_dev_inst *sdi, void *cb_data)
Stop acquisition on the specified device. This causes a DF_END packet to be sent to the session bus.

### priv
This should contain a pointer to a struct drv_context, which is initialized by the init() function.


## What you typically re-implement

### init

One-time driver init, register IDs, allocate global state if needed.

### cleanup

Free any global resources created in init.

### scan

Enumerate devices on the selected transport. For USB scan vendor id and product id, build a list of DeviceInstance with serial and friendly name. For serial or tcp perform a lightweight probe.

### dev_open
Open the chosen DeviceInstance, claim interfaces or set serial port params, allocate buffers, prime endpoints.

### config_get and config_set

Handle standard keys samplerate channels trigger coupling voltage range device options and any driver specific keys.

### acquire_start

Spawn the transfer thread, program samplerate and trigger on hardware, start streaming into the ring buffer.

### acquire_stop

Tell hardware to stop, join the transfer thread, flush buffers.

### dev_status

Report rate dropped frames overflow temperature firmware version or other status fields.

### dev_close

Release handles and memory.

## Minimal data structures you will keep

### DeviceInstance

Driver side state for one physical device
id vendor_id product_id serial transport channels samplerate trigger state private_ctx

### Channel

index name kind logic or analog unit enabled scale offset

### Transport

For usb keep libusb device handle and in out endpoints
For serial keep file descriptor baud parity
For tcp keep socket and host port

### Buffering

Lock free ring buffer or double buffer frame_size watermark

### TransferThread

Thread loop that performs bulk transfers or reads then pushes into the ring buffer and updates stats

### TriggerEngine
Mode edge level pattern any pre post settings mirrored to hardware registers when possible

## Skeleton checklist for your driver file

- Register DriverTable with name id vendor_list product_list and the DriverAPI callbacks

- In scan, build DeviceInstance objects with Channel lists based on model

- In dev_open, open transport claim interface set sample rate default trigger allocate Buffering and start idle state

- In acquire_start, configure hardware start endpoint streaming create TransferThread

- In transfer thread
read into bounce buffer push to ring buffer notify core on watermark handle time stamps and dropped samples

- In config_set
validate and apply samplerate channel enable trigger options update hardware live when safe

- In acquire_stop and dev_close
stop streaming join thread free buffers close handles