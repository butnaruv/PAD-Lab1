using Grpc.Core;
using Grpc.Net.Client;

namespace TaskManagementService.Services
{
    public class TaskManager
    {
        public static void SendMessageToEventService()
        {
            var channel = GrpcChannel.ForAddress("https://localhost:7206");
            var client = new Communication.CommunicationClient(channel);
            var response = client.SendMessage(new MessageRequest { Message = "I am task manager" });

            // Process the response from the EventManagementService
            Console.WriteLine(response.Message);
        }
    }
}
