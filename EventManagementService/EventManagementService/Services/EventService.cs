using AutoMapper;
using EventManagementService.Entities;
using EventManagementService.Protos;
using EventManagementService.Repositories;
using Grpc.Core;
using Grpc.Net.Client;
using EventManagerService = EventManagementService.Protos.EventManagerService;

namespace EventManagementService.Services
{
    public class EventService : EventManagerService.EventManagerServiceBase
    {
        private readonly IEventRepository _eventManagerService;
        private readonly IMapper _mapper;

        public EventService(IEventRepository eventManagerService, IMapper mapper)
        {
            _eventManagerService = eventManagerService;
            _mapper = mapper;

        }

        public async override Task<Events> GetEventListAsync(Empty request, ServerCallContext context)
        {
            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                //await Task.Delay(6000);
                Console.WriteLine("GET ALL EVENTS was called");
                var eventsDataTask = _eventManagerService.GetEventListAsync();
                await Task.WhenAny(eventsDataTask, Task.Delay(Timeout.Infinite, cts.Token));
                if (eventsDataTask.IsCompletedSuccessfully)
                {
                    var eventsData = eventsDataTask.Result;
                    Events response = new Events();
                    foreach (Event dbEvent in eventsData)
                    {
                        response.Items.Add(_mapper.Map<EventDetails>(dbEvent));
                    }
                    Console.WriteLine("Success!");
                    return response;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
            }

        }

        public async override Task<EventDetails> GetEventByIdAsync(GetByEventId request, ServerCallContext context)
        {
            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                //await Task.Delay(5000);
                Console.WriteLine("GET EVENT BY ID was called");
                var dbEventTask = _eventManagerService.GetEventByIdAsync(request.Id);
                await Task.WhenAny(dbEventTask, Task.Delay(Timeout.Infinite, cts.Token));
                if (dbEventTask.IsCompletedSuccessfully)
                {
                    var dbEvent = dbEventTask.Result;
                    var eventDetails = _mapper.Map<EventDetails>(dbEvent);
                    Console.WriteLine("Success!");
                    return eventDetails;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));

            }

        }

        public async override Task<EventDetails> CreateEventAsync(CreateNewEvent request, ServerCallContext context)
        {
            Console.WriteLine("CREATE NEW EVENT was called");

            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                var offer = _mapper.Map<Event>(request.Event);
                //await Task.Delay(1000);
                var createEventTask = _eventManagerService.CreateEventAsync(offer);
                await Task.WhenAny(createEventTask, Task.Delay(Timeout.Infinite, cts.Token));

                if (createEventTask.IsCompletedSuccessfully)
                {
                    var eventDetails = _mapper.Map<EventDetails>(offer);
                    Console.WriteLine(eventDetails);
                    Console.WriteLine("Success!");
                    return eventDetails;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
            }
        }


        public async override Task<EventDetails> UpdateEventAsync(UpdateEvent request, ServerCallContext context)
        {
            Console.WriteLine("UPDATE EVENT was called");
            var cts = new CancellationTokenSource(TimeSpan.FromSeconds(3));
            try
            {
                var existingEventTask = _eventManagerService.GetEventByIdAsync(request.Event.Id);
                await Task.WhenAny(existingEventTask, Task.Delay(Timeout.Infinite, cts.Token));
                if (existingEventTask.IsCompletedSuccessfully)
                {
                    //var existingEvent = await _eventManagerService.GetEventByIdAsync(request.Event.Id);
                    var existingEvent = existingEventTask.Result;
                    if (request.Event.DressCode != "")
                    {
                        existingEvent.DressCode = request.Event.DressCode;
                    }
                    if (request.Event.Name != "")
                    {
                        existingEvent.Name = request.Event.Name;
                    }
                    if (request.Event.Date != "")
                    {
                        existingEvent.Date = request.Event.Date;
                    }
                    if (request.Event.Location != "")
                    {
                        existingEvent.Location = request.Event.Location;
                    }
                    var dbEvent = _mapper.Map<Event>(request.Event);

                    await _eventManagerService.UpdateEventAsync(existingEvent);

                    var eventDetails = _mapper.Map<EventDetails>(existingEvent);
                    Console.WriteLine("Success!");
                    return eventDetails;
                }
                else
                {
                    Console.WriteLine("Unsucces!");
                    throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
                }
            }
            catch (OperationCanceledException)
            {
                throw new RpcException(new Status(StatusCode.DeadlineExceeded, "Timeout error"));
            }

        }

        public async override Task<DeleteEventResponse> DeleteEventAsync(DeleteEventRequest request, ServerCallContext context)
        {
            Console.WriteLine("DELETE EVENT was called");
            var isDeleted = await _eventManagerService.DeleteEventAsync(request.Id);
            var response = new DeleteEventResponse
            {
                IsDeleted = isDeleted
            };
            Console.WriteLine("Success!");
            return response;
        }
    }
}
