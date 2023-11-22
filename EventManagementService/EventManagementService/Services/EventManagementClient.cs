using Grpc.Core;
using Grpc.Net.Client;
using System.Net;

namespace EventManagementService.Services
{
    public class EventManager
    {
        public static void SendMessage()
        {
            var urls = Environment.GetEnvironmentVariable("ASPNETCORE_URLS").Split(";");
            var currentServerUrl = urls.FirstOrDefault(x => x.Contains("http:"));
            var channel = GrpcChannel.ForAddress("http://127.0.0.1:50051");
            var client = new Communication.CommunicationClient(channel);

            try
            {
                var response = client.SendMessage(new MessageRequest { Sender = "Event manager", Message = currentServerUrl });
                Console.WriteLine(response);
            }
            catch (Exception ex) { }
        }
        private static string GetLocalhost()
        {
            return Dns.GetHostEntry(Dns.GetHostName()).AddressList[0].ToString();
        }
    }
}
