# gr-remotecar



## INSTALL

    mkdir build
    cd build
    make
    sudo make install
    sudo ldconfig


## TRY

refer to examples/

`examples/WheelPulse/Wheel.py` is a simple PySide based controller which you can control your toy car with keyboard direction keys. And it is for [RemoteCarIIBaseBand](#remotecariibaseband)



## Just replay it.

on `examples/tx.sh` and `examples/rx.sh` , I demo how to capture the car's remote signal and just replay it. And it turns out to make the car run.

    cd examples
    ./rx.sh car.iq
    ./tx.sh car.iq

and it means: 

        hackrf_transfer -t car.iq -f 27000000 -s 8000000 -a 1 -l 30 -i 30 -x 40 

27000000 is for 27MHz, you may find the frequency sign on you car's remote.



## Principle

We support two kind of remote car control : 

### RemoteCarBaseBand
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarBaseBand/AMDemod.png)


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


### RemoteCarIIBaseBand
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/0.55ms.png)
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/1.65ms.png)
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/AM_DEMOD.png)

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

![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/grc.png)
it is on `examples/analysis.grc`

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
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/qt_wheel.png)
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/example1.png)
![](https://raw.github.com/scateu/gr-remotecar/master/docs/RemoteCarIIBaseBand/example2.png)
