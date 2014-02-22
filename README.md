gr-remotecar



INSTALL
=======

    mkdir build
    cd build
    make
    sudo make install
    sudo ldconfig


TRY
===

refer to examples/

`examples/WheelPulse/Wheel.py` is a simple PySide based controller which you can control your toy car with keyboard direction keys. And it is for RemoteCarIIBaseBand





Principle
=========

We support two kind of remote car control : 

RemoteCarBaseBand
-----------------


                    -->|TIME3  |<--   TIME4
          --------+    +-------+    +-------+    +--------- ... -------+    +---.....
                  |    |       |    |       |    |                     |    |
                  |    |       |    |       |    |                     |    |
                  |    |       |    |       |    |                     |    |
                  |    |       |    |       |    |                     |    |
                  +----+       +----+       +----+                     +----+
                  TIME0        TIME0        TIME0
               -->|                              TIME2                 |<---


TIME0 = 520us
TIME3 = 300us to 1.3ms
TIME4 = 300us to 1.3ms
TIME2 = 20ms

TIME3 and TIME4 controls car's accelerator and direction.


RemoteCarIIBaseBand
--------------------

    +----------+     +----------+     +----------+     +----------+     +-----+     +-----+                        
    |          |     |          |     |          |     |          |     |     |     |     |                 
    |          |     |          |     |          |     |          |     |     |     |     |                 
    |          |     |          |     |          |     |          |     |     |     |     |                 
    |          |     |          |     |          |     |          |     |     |     |     |                 
    |          |     |          |     |          |     |          |     |     |     |     |                 
    |          |     |          |     |          |     |          |     |     |     |     |                 
    +          +-----+          +-----+          +-----+          +-----+     +-----+     +-...                     

    |<-  3t  ->|  t  |<-  3t  ->|  t  |<-  3t  ->|  t  |<-  3t  ->|  t  |  t  |  t  |  t  |    


and we can simply capture it with HackRF using a AM demode gnuradio-companion workflow.

    Left: n=58
    Right: n=64
    Forward: n=10
    Fast Forward: n=22
    Backward: n=40
    Left Forward: n=28
    Right Forward: n=34
    Left Backward: n=46
    Right Backward: n=52

t = 0.55 ms


and you can try it with `examples/WheelPulse/Wheel.py` 
