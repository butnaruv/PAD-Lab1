using Grpc.Net.Client;

namespace EventManagementService.Services
{
    public class EventManager
    {
        public void SendMessage() {
            var channel = GrpcChannel.ForAddress("https://localhost:7206");
            var client = new Communication.CommunicationClient(channel);
            var response = client.SendMessage(new MessageRequest { Message = "I got it, you are task manager" });
        }
        

    }
}
