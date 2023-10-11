using Grpc.Core;
using System.Threading.Tasks;
namespace EventManagementService.Services
{

    public class CommunicationService : Communication.CommunicationBase
    {
        public override Task<MessageResponse> SendMessage(MessageRequest request, ServerCallContext context)
        {
            return Task.FromResult(new MessageResponse { Message = "I got it, you are task manager" });
        }
    }

}
