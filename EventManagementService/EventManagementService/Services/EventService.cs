using AutoMapper;
using EventManagementService.Entities;
using EventManagementService.Protos;
using EventManagementService.Repositories;
using Grpc.Core;
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
            var eventsData = await _eventManagerService.GetEventListAsync();

            Events response = new Events();
            foreach (Event dbEvent in eventsData)
            {
                response.Items.Add(_mapper.Map<EventDetails>(dbEvent));
            }

            return response;
        }

        public async override Task<EventDetails> GetEventByIdAsync(GetByEventId request, ServerCallContext context)
        {
            var dbEvent = await _eventManagerService.GetEventByIdAsync(request.Id);
            var eventDetails = _mapper.Map<EventDetails>(dbEvent);
            return eventDetails;
        }

        public async override Task<EventDetails> CreateEventAsync(CreateNewEvent request, ServerCallContext context)
        {
            Console.WriteLine("entered the create event async from management service");
            var offer = _mapper.Map<Event>(request.Event);

            await _eventManagerService.CreateEventAsync(offer);

            var eventDetails = _mapper.Map<EventDetails>(offer);
            Console.WriteLine(eventDetails);
            Task.FromResult(eventDetails);
            return eventDetails;
        }

        public async override Task<EventDetails> UpdateEventAsync(UpdateEvent request, ServerCallContext context)
        {
            Console.WriteLine("Event is updated...");
            var existingEvent = await _eventManagerService.GetEventByIdAsync(request.Event.Id);
            Console.WriteLine(request.Event.DressCode);
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
            return eventDetails;
        }

        public async override Task<DeleteEventResponse> DeleteEventAsync(DeleteEventRequest request, ServerCallContext context)
        {
            var isDeleted = await _eventManagerService.DeleteEventAsync(request.Id);
            var response = new DeleteEventResponse
            {
                IsDeleted = isDeleted
            };

            return response;
        }
    }
}
