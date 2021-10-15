using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class SendServo : MonoBehaviour
{
    FixedJoystick joystick;
    float pan = 90;
    float tilt = 90;
    float MIN = 0;
    float MAX = 180;
    float NORMALIZER = 0.2f;
    UdpClient mySock;
    byte[] sendBytes = new byte[2];
    // Start is called before the first frame update
    void Start()
    {
        joystick = GameObject.Find("PantiltJoystick").GetComponent<FixedJoystick>();
        new Thread (() =>
        {
          mySock = new UdpClient(6000);
          mySock.Connect("192.168.1.191", 5000);

        }).Start();
    }

    // Update is called once per frame
    void Update()
    {
        pan = Mathf.Max(Mathf.Min(pan - (joystick.Horizontal * NORMALIZER), MAX), MIN);
        tilt = Mathf.Max(Mathf.Min(tilt + (joystick.Vertical * NORMALIZER), MAX), MIN);
        Debug.Log("("+pan+","+tilt+")");
        sendBytes[0] = (byte) (int) pan;
        sendBytes[1] = (byte) (int) tilt;
        mySock.Send(sendBytes, 2);
    }
}
