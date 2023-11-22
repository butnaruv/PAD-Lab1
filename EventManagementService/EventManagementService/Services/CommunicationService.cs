using Grpc.Core;
using Grpc.Net.Client;
using System.Threading.Tasks;
namespace EventManagementService.Services
{

    public class CommunicationService : Communication.CommunicationBase
    {
        public override Task<MessageResponse> SendMessage(MessageRequest request, ServerCallContext context)
        {
            return Task.FromResult(new MessageResponse { Message = "I got it, you are task manager" });
        }

        public void StartBackgroundTask()
        {
            var cancellationTokenSource = new CancellationTokenSource();
            var cancellationToken = cancellationTokenSource.Token;

            var delay = TimeSpan.FromMinutes(0.1);

            _ = Task.Run(async () =>
            {
                while (!cancellationToken.IsCancellationRequested)
                {
                    using var channel = GrpcChannel.ForAddress("http://127.0.0.1:5000");

                    var client = new Communication.CommunicationClient(channel);

                    var reply = client.SendMessage(new MessageRequest { Message = "World" });
                    Console.WriteLine("Greeting: " + reply.Message);

                    await Task.Delay(delay);
                }
            }, cancellationToken);
        }
    }

}
