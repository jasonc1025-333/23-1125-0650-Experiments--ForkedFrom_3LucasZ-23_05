using UnityEngine;
using UnityEngine.UI;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class UDPVideoStream : MonoBehaviour
{
  UdpClient mySock;
  IPEndPoint myIPEP;
  IPEndPoint otherIPEP;

  RawImage dynamicImage;
  Texture2D texture;

  void Start()
  {
    myIPEP = new IPEndPoint(IPAddress.Parse("192.168.1.144"), 5000);
    otherIPEP = new IPEndPoint(IPAddress.Parse("192.168.1.144"), 5001);
    mySock = new UdpClient(myIPEP);

    dynamicImage = GameObject.Find("DynamicImage").GetComponent<RawImage>();
    texture = new Texture2D(1,1);
  }
  void Update()
  {
    texture.LoadImage(mySock.Receive(ref otherIPEP));
    dynamicImage.texture = texture;
  }
}