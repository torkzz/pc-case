using System;
using System.Threading.Tasks;
using DeviceCommunicationLibrary;

class Program
{
    static void Main(string[] args)
    {
        string port = args.Length > 0 ? args[0] : "/dev/ttyACM0";
        Console.WriteLine("=== DIRECT .NET DLL COMMUNICATOR TEST ===");
        Console.WriteLine("Port: " + port);

        var comm = new DeviceCommunicator();
        Console.WriteLine("Connecting to " + port + " at 115200 baud...");
        
        bool ok = comm.Connect(port, 115200);
        Console.WriteLine("Connect result: " + ok);

        if (ok)
        {
            Console.WriteLine("Sending HandshakeAsync (CMD 0x0080)...");
            try
            {
                var task = comm.HandshakeAsync();
                if (task.Wait(3000))
                {
                    var resp = task.Result;
                    Console.WriteLine(">>> HANDSHAKE SUCCESS! <<<");
                    Console.WriteLine("MaxPackageSize: " + resp.MaxPackageSize);
                }
                else
                {
                    Console.WriteLine("Handshake TIMEOUT after 3.0s.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Handshake EXCEPTION: " + ex.Message);
            }

            comm.Disconnect();
        }
    }
}
