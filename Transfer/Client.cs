using UnityEngine;
using UnityEngine.UI;
using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

public class UDPVideoStream : MonoBehaviour
{
  UdpClient mySock;
  IPEndPoint myIPEP;
  IPEndPoint otherIPEP;

  RawImage dynamicImage;
  Texture2D texture;
  byte[] data;

  void Start()
  {
    myIPEP = new IPEndPoint(IPAddress.Parse("192.168.1.144"), 5000);
    otherIPEP = new IPEndPoint(IPAddress.Parse("192.168.1.144"), 5001);
    dynamicImage = GameObject.Find("DynamicImage").GetComponent<RawImage>();
    texture = new Texture2D(1,1);

    new Thread (() =>
    {
      mySock = new UdpClient(myIPEP);
      while (true) {
        data = mySock.Receive(ref otherIPEP);
      }
    }).Start();
  }

  void Update()
  {
    if (data != null) {
      texture.LoadImage(data);
      dynamicImage.texture = texture;
    }
  }
}
