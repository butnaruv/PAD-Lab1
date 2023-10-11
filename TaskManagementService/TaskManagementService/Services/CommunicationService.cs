using Grpc.Core;
using System.Threading.Tasks;

namespace TaskManagementService.Services
{
  

    public class CommunicationService : Communication.CommunicationBase
    {
        public override Task<MessageResponse> SendMessage(MessageRequest request, ServerCallContext context)
        {
            return Task.FromResult(new MessageResponse { Message = "I am task manager" });
        }
    }

}
