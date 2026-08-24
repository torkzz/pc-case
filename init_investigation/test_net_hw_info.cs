using System;
using System.Threading.Tasks;
using DeviceCommunicationLibrary;

class Program
{
    static void Main(string[] args)
    {
        string port = args.Length > 0 ? args[0] : "/dev/ttyACM0";
        Console.WriteLine("=== TESTING GetHardwareInfoAsync ===");
        var comm = new DeviceCommunicator();
        comm.ErrorOccurred += (sender, err) => Console.WriteLine("[DLL ERROR] " + err);
        comm.DataReceived += (sender, data) => Console.WriteLine("[DLL DATA] " + BitConverter.ToString(data));

        if (comm.Connect(port, 115200))
        {
            try
            {
                Console.WriteLine("Sending GetHardwareInfoAsync (CMD 0x0072)...");
                var task = comm.GetHardwareInfoAsync();
                if (task.Wait(5000))
                {
                    var resp = task.Result;
                    Console.WriteLine(">>> HW INFO SUCCESS! <<<");
                    Console.WriteLine("DisplayWidth: " + resp.DisplayWidth);
                    Console.WriteLine("DisplayHeight: " + resp.DisplayHeight);
                }
                else
                {
                    Console.WriteLine("GetHardwareInfo TIMEOUT after 5.0s.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception: " + ex.Message);
            }
            comm.Disconnect();
        }
    }
}
