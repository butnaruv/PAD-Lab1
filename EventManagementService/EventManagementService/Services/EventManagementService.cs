using AutoMapper;
using EventManagementService.Entities;
using EventManagementService.Protos;
using EventManagementService.Repositories;
using Grpc.Core;
using System;
using EventManagerService = EventManagementService.Protos.EventManagerService;

namespace EventManagementService.Services
{
    public class EventManagementService : EventManagerService.EventManagerServiceBase
    {
        private readonly IEventManagerService _eventManagerService;
        private readonly IMapper _mapper;

        public EventManagementService(IEventManagerService eventManagerService, IMapper mapper)
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
            var offer = _mapper.Map<Event>(request.Event);

            await _eventManagerService.CreateEventAsync(offer);

            var eventDetails = _mapper.Map<EventDetails>(offer);
            return eventDetails;
        }

        public async override Task<EventDetails> UpdateEventAsync(UpdateEvent request, ServerCallContext context)
        {
            var dbEvent = _mapper.Map<Event>(request.Event);

            await _eventManagerService.UpdateEventAsync(dbEvent);

            var eventDetails = _mapper.Map<EventDetails>(dbEvent);
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
